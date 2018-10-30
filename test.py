"""
n=int(input("enter the number: "))
d=dict()
for i in range(1,n+1):
	d[i]=i*i
print(d)
"""
"""
def Sum(number1, number2):
	return number1+number2
print(Sum(10,2))
"""
def fact(x):
	if x==0 or x==1:
		return 1
	return x * fact(x-1)
x=int(input("input: "))
print(fact(x))