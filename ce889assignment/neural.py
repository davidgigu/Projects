import csv
import random
import math

import matplotlib.pyplot as plt


lam=0.4
lr=0.01
mt=0.9





class Neuron:
    def __init__(self,av,weightlen,weightIndex):
        self.av=av
        li=[]
        for j in range (weightlen):
            li.append(random.random())
        self.weights=li
        self.weightIndex=weightIndex
        self.grad_val=0
        self.delta_weights=[]
        for k in range(weightlen):
            self.delta_weights.append(0)
        
    def multWeights(self, prevLayer):
        i=0
        r=0
        while i<len(prevLayer):
            r=r+prevLayer[i].av*prevLayer[i].weights[self.weightIndex]
            i=i+1
        return r
    def sigmoidFunc(self,r):
        return 1 / (1 + math.exp(-(lam*r)))






hide=int(input("Enter the number of hidden neurons:"))

inputLayer=[Neuron(0,hide,0),Neuron(0,hide,1),Neuron(1,hide,2)]

hiddenLayer=[]
for i in range(hide):
    hiddenLayer.append(Neuron(0,2,i))
hiddenLayer.append(Neuron(1,2,i+1))


outputLayer=[Neuron(0,0,0),Neuron(0,0,1)]


def feedforward_process(inputs):
    inputLayer[0].av=inputs[0]
    inputLayer[1].av=inputs[1]
    for i in range(len(hiddenLayer)-1):
        hiddenLayer[i].av=hiddenLayer[i].sigmoidFunc(hiddenLayer[i].multWeights(inputLayer))
    for i in range(len(outputLayer)):
        outputLayer[i].av=outputLayer[i].sigmoidFunc(outputLayer[i].multWeights(hiddenLayer))
    outputs=[]
    for i in range(len(outputLayer)):
        outputs.append(outputLayer[i].av)
    return outputs


def backprop_process(outputs):
    error=[0,0]

    for i in range(len(outputLayer)):
        error[i]=outputs[i]-outputLayer[i].av
        
    for i in range(len(outputLayer)):
        outputLayer[i].grad_val=lam*outputLayer[i].av*(1-outputLayer[i].av)*error[i]
    for i in range(len(hiddenLayer)):
        sumterm=0
        for j in range(len(outputLayer)):
            sumterm+=outputLayer[j].grad_val*hiddenLayer[i].weights[j]
        hiddenLayer[i].grad_val=lam*hiddenLayer[i].av*(1-hiddenLayer[i].av)*sumterm
    for i in range(len(hiddenLayer)):
        for j in range(len(outputLayer)):
            hiddenLayer[i].delta_weights[j]=lr*outputLayer[j].grad_val*hiddenLayer[i].av+mt*hiddenLayer[i].delta_weights[j]
    for i in range(len(inputLayer)):
        for j in range(len(hiddenLayer)-1):
            inputLayer[i].delta_weights[j]=lr*hiddenLayer[j].grad_val*inputLayer[i].av+mt*inputLayer[i].delta_weights[j]
    for i in range(len(hiddenLayer)):
        for j in range(len(outputLayer)):
            hiddenLayer[i].weights[j]+=hiddenLayer[i].delta_weights[j]
    for i in range(len(inputLayer)):
        for j in range(len(hiddenLayer)-1):
            inputLayer[i].weights[j]+=inputLayer[i].delta_weights[j]
            

def training():
    flag=0
    patcount=0
    patience=15
    prevvalerr=0
    weightqueue=[]
    valqueue=[]
    epochqueue=[]
    for epoch in range(1000):
        if(epoch!=0):
            prevvalerr=val_error
            
        with open('train.csv', 'r') as df:
            reader = csv.reader(df)
            i=0
            for row in reader:
               i=i+1
               inputs=[]
               reqoutputs=[]
               inputs.append(float(row[0]))
               inputs.append(float(row[1]))
               reqoutputs.append(float(row[2]))
               reqoutputs.append(float(row[3]))
               outputs=feedforward_process(inputs)
               backprop_process(reqoutputs)
            print("Epoch:"+str(epoch+1))
        with open('train.csv', 'r') as df:
            reader = csv.reader(df)
            train_error=0
            i=0
            for row in reader:
                i=i+1
                inputs=[]
                reqoutputs=[]
                inputs.append(float(row[0]))
                inputs.append(float(row[1]))
                reqoutputs.append(float(row[2]))
                reqoutputs.append(float(row[3]))
                outputs=feedforward_process(inputs)
                train_error+=(((outputs[0]-reqoutputs[0])**2)+((outputs[1]-reqoutputs[1])**2))/2
            train_error=math.sqrt(train_error/i)
        with open('val.csv', 'r') as dfval:
            readerval = csv.reader(dfval)
            val_error=0
            i=0
            for row in readerval:
                i=i+1
                inputsval=[]
                reqoutputsval=[]
                inputsval.append(float(row[0]))
                inputsval.append(float(row[1]))
                reqoutputsval.append(float(row[2]))
                reqoutputsval.append(float(row[3]))
                outputsval=feedforward_process(inputsval)
                val_error+=(((outputsval[0]-reqoutputsval[0])**2)+((outputsval[1]-reqoutputsval[1])**2))/2
            val_error=math.sqrt(val_error/i)
        print("Training error: "+str(train_error))
        print("Previous validation error: "+str(prevvalerr))
        print("Validation error: "+str(val_error))
        valqueue.append(val_error)
        epochqueue.append(epoch+1)
        queuemember=[val_error]

        for inputNeuron in inputLayer:
            for i in range(len(inputNeuron.weights)):
               queuemember.append(inputNeuron.weights[i])
       
        for hiddenNeuron in hiddenLayer:
            for i in range(len(hiddenNeuron.weights)):
                queuemember.append(hiddenNeuron.weights[i])
        if(epoch<patience):
            weightqueue.append(queuemember)
        else:
            weightqueue.pop(0)
            weightqueue.append(queuemember)
        #print (weightqueue)    
        if(epoch!=0):
            if(epoch+1>=100):
                print("\nMax number of epochs reached!\nThe latest weights are saved!")
                break
                

            elif(abs(prevvalerr-val_error)<0.00001):
                print("\nEarly stopping criteria(difference in validation error is less than 0.00001)is satisfied!\n The latest weights are saved!")
                break
                


            elif(prevvalerr<val_error):
                flag=1

            if(flag==1):
                patcount+=1
                if(patcount==patience):
                    val_err_req=weightqueue[0][0]
                    req_weight_index=0
                    for i in range(patience):
                        if(weightqueue[i][0]<val_err_req):
                            val_err_req=weightqueue[i][0]
                            req_weight_index=i

                    
                    for inputNeuron in inputLayer:
                        for i in range(len(inputNeuron.weights)):
                            inputNeuron.weights[i]=weightqueue[req_weight_index][i+1]
                   
       
                    for hiddenNeuron in hiddenLayer:
                        for i in range(len(hiddenNeuron.weights)):
                            hiddenNeuron.weights[i]=weightqueue[req_weight_index][i+len(inputNeuron.weights)+1]
                    print("\nEarly stopping criteria satisfied! \nThe best weights are saved!")
                    print("\nThe best validation error: "+str(weightqueue[req_weight_index][0]))
                    break
    

    plt.plot(epochqueue , valqueue)
 
   
    plt.xlabel('Epochs')
   
    plt.ylabel('RMSE Error')
 
   
    plt.title('Epochs vs RMSE')
 
    
    plt.show()
                    
training()    

with open('weights.txt', 'w') as f:
    f.writelines(str(hide))
    f.write("\n")
    for inputNeuron in inputLayer:
        for i in range(len(inputNeuron.weights)):
            f.writelines(str(inputNeuron.weights[i]))
            f.writelines(",")
        f.write("\n")
    f.write("\n")
    f.write("\n")
    for hiddenNeuron in hiddenLayer:
        for i in range(len(hiddenNeuron.weights)):
            f.writelines(str(hiddenNeuron.weights[i]))
            f.writelines(",")
        f.write("\n")



