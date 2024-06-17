#Indexing Log
import torch

batch_size= 10
features = 25
x = torch.rand((batch_size, features))
g = open("Indexing.log", 'a')
print(x[0].shape, file = g) #gives all features # x[0,:]
print(x[:,0].shape, file =g )#1 exa
print(x[2,0:10], file =g ) #0:10 makes list from 0 to 9 from 3rd row