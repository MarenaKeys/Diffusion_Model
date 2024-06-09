#Math.log
import torch

w = open("math.log", 'a')
x = torch.tensor([1,2,3])
y = torch.tensor([9,8,7])
print(x,file=w)
print(y,file=w)
#Addition
z1 = torch.empty(3)
torch.add(x,y, out=z1)
#print(z1)

z2 = torch.add(x,y)

z3= x + y  #best way
print("Addition:",file=w)
print(z3,file=w)

#Subtraction

z = x - y
print("Subtraction:",file=w)
print(z,file=w)
#Division
z = torch.true_divide(x,y) #divides x by y
print("Division: ",file=w)
print(z,file=w)
#inplace operations
t = torch.zeros(3)
t.add_(x)
t += x #t = t+x
print("Inplace:",file=w)
print(t,file=w)
# Exponential
z = x.pow(2)
#or
z = x ** 2
print("Exponents:",file=w)
print(z,file=w)
#Comparison
z = x > 0
z = x < 0
print("Are the values of x less than zero?: ",file=w)
print(z,file=w)
#Matrix Multiplication
x1= torch.rand((2,5))
x2 = torch.rand((5,3))
x3 = torch.mm(x1,x2)
x3= x1.mm(x2)
print("Random matrix multiplication",file=w)
print(x1,file=w)
print(x2,file=w)
print(x3,file=w)
#Matrix exponents
matrix_exp = torch.rand(5,5)

#element wise mult.
z = x * y

# Dot product
z = torch.dot(x,y)
print("Dot Product:",file=w)
print(z,file=w)
#Batch Multiplication

batch = 32
n = 10
m = 20
p = 30

tensor1=torch.rand((batch,n,m))
tensor2 = torch.rand((batch,m , p))
out_bmm = torch.bmm(tensor1, tensor2) # batch,n,p

#Broadcasting
x1 = torch.rand((5,5))
x2 = torch.rand((1,5))

z = x1-x2
z = x1 ** x2  #dont make sense mathematically

#Other operations
sum_x = torch.sum(x, dim=0)

values, indices = torch.max(x,dim=0) #can do max or min   can write as x.max(dim=0)
abs_x = torch.abs(x)
z = torch.argmax(x,dim=0) #returns index of one that is max or min
mean_x = torch.mean(x.float(), dim=0)
z = torch.eq(x,y) #checks which elem are equals
print("Are the elements of x and y equal?",file=w)
print(z,file=w)
sorted_y, indices = torch.sort(y, dim=0, descending=False)

z = torch.clamp(x,min=0)

x = torch.tensor([1,0,1,1,1], dtype=torch.bool)