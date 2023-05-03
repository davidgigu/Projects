import csv
import math



def load_dataset():
    file = open('ce889_dataCollection.csv', "r")
    dataset = list(csv.reader(file))
    return dataset

def string_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())

 

def minmax(dataset):
    min_max = list()
    for i in range(4):
        col_values=[]
        for row in dataset:
            col_values.append(row[i])
        value_min=col_values[0]
        for i in col_values:
            if(i<value_min):
                value_min=i
        value_max=col_values[0]
        for i in col_values:
            if(i>value_max):
                value_max=i
        min_max.append([value_min, value_max])

    return min_max
 

def normalize(dataset, min_max):
    for row in dataset:
        for i in range(4):
            row[i] = (row[i] - min_max[i][0]) / (min_max[i][1] - min_max[i][0])
 

dataset=load_dataset()


for i in range(4):
    string_to_float(dataset, i)

min_max = minmax(dataset)
normalize(dataset, min_max)



trainvalmiddle=math.floor(len(dataset)*0.70)

datasettrain=dataset[:trainvalmiddle-1]
datasetval=dataset[trainvalmiddle:]






with open('train.csv', 'w+', newline='') as csvtrain: 
   
    trainwriter = csv.writer(csvtrain) 
    trainwriter.writerows(datasettrain)

with open('val.csv', 'w+', newline='') as csvval: 
   
    valwriter = csv.writer(csvval) 
    valwriter.writerows(datasetval)




with open('minmax.txt', 'w') as f:
    for i in range(4):
        for j in range(2):
            f.writelines(str(min_max[i][j]))
            f.writelines(",")

