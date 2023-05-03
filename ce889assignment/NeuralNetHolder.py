import csv
import math

lam=0.4

class Neuron:
    def __init__(self,av,weightlen,weightIndex):
        self.av=av
        self.weightlen=weightlen
        self.weights=[]
        self.weightIndex=weightIndex

        
    def multWeights(self, prevLayer):
        i=0
        r=0
        while i<len(prevLayer):
            r=r+prevLayer[i].av*float(prevLayer[i].weights[self.weightIndex])
            i=i+1
        return r
    def sigmoidFunc(self,r):
        return 1 / (1 + math.exp(-(lam*r)))

minmax=list()
with open('minmax.txt') as f:
    lines = f.readline()
    inputminmax=lines.split(",")
    count=0
    for i in range(4):
        minmaxpart=[]
        for j in range(2):
            
            minmaxpart.append(float(inputminmax[count]))
            count+=1
        minmax.append(minmaxpart)

with open('weights.txt') as f:
    hide=int(f.readline())
    inputLayer=[Neuron(0,hide,0),Neuron(0,hide,1),Neuron(1,hide,2)]

    hiddenLayer=[]
    for i in range(hide):
        hiddenLayer.append(Neuron(0,2,i))
    hiddenLayer.append(Neuron(1,2,i+1))


    outputLayer=[Neuron(0,0,0),Neuron(0,0,1)]

    for i in range(len(inputLayer)):
        lines = f.readline()
        #print(lines)
        inputweights=lines.split(",")
        #print(inputweights)
        inputLayer[i].weights=inputweights[:hide]
        #print(inputLayer[i].weights)
    lines = f.readline()
    lines = f.readline()
    for i in range(len(hiddenLayer)):
        lines = f.readline()
        #print(lines)
        hiddenweights=lines.split(",")
        #print(hiddenweights)
        hiddenLayer[i].weights=hiddenweights[:2]
        #print(hiddenLayer[i].weights)







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




            
        
        

class NeuralNetHolder:

    def __init__(self):
        super().__init__()

    
    def predict(self, input_row):
        # WRITE CODE TO PROCESS INPUT ROW AND PREDICT X_Velocity and Y_Velocity
        # this pass can be removed once you add some code
        print(input_row)
        inputs=input_row.split(",")
        inputs[0]=float(inputs[0])
        inputs[1]=float(inputs[1])
        inputs[0] = (inputs[0] - minmax[0][0]) / (minmax[0][1] - minmax[0][0])
        inputs[1] = (inputs[1] - minmax[1][0]) / (minmax[1][1] - minmax[1][0])

        outputs=feedforward_process(inputs)


        outputs[0]=(outputs[0]*(minmax[2][1] - minmax[2][0]))+minmax[2][0]
        outputs[1]=(outputs[1]*(minmax[3][1] - minmax[3][0]))+minmax[3][0]


        return outputs
