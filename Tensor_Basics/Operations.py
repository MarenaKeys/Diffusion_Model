#Operations log
import torch
#=============================== initialize tensor################
my_tensor = torch.tensor([[1,2,3], [4,5,6]], dtype=torch.float32, device= "cpu", requires_grad=True) # 2 row by 3 col#
###############
f = open("operations.log",'a')
print(my_tensor, file = f)
print(my_tensor.dtype , file = f)
print(my_tensor.device , file = f)
print(my_tensor.shape , file = f)
print(my_tensor.requires_grad , file = f)

#Transpose of Matrix
x = torch.randn(2,3)
print(x , file = f)
print( torch.t(x), file = f)
#Other Common Methods#

x=torch.empty(size= (3,3))
x= torch.zeros((3,3)) #3x3 matrix with values zero
print( x , file = f)
x = torch.rand((3,3)) #makes 3x3 matrix with values between zero and 1
print(x , file = f)
x = torch.ones((3,3)) #makes 3x3 matrix with all values one
x = torch.eye(4,4) #makes identity matrix
print( x, file = f)
x = torch.arange(start=0, end =5, step=1) #like range function
x = torch.linspace(start=0, end =10 , steps=20) #steps are the # of values inbetween start and end
x = torch.empty(size=(1,5)).normal_(mean=0, std=1)
#print(x)
x = torch.empty(size=(1,5)).uniform_(0,1) #similar to rand function
x = torch.diag(torch.ones(3)) #makes diagonal matrix similar to eye function


# How to convert tensor to other types like integers, floats, doubles#
tensor = torch.arange(4)
print(tensor.bool(), file = f)#boolean true/false
print(tensor.short(), file = f)#int16
print(tensor.long(), file = f) #int64 (IMPORTANT)
print(tensor.half(), file = f) #float 16
print(tensor.float(), file = f) #float 32 (IMPORTANT)
print(tensor.double(), file = f) #float 64

#Array to Tensor Conversion and vice-versa
import numpy as np
np_array = np.zeros((5,5))
tensor = torch.from_numpy(np_array)
np_array_back = tensor.numpy()

