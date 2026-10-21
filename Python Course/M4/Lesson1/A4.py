# Create a list of square values of numbers between specified ranges by the user, and then separate the odd and even values.

values=[]
user_num=int(input("Enter your end point number: "))
odd_values=[]
even_values=[]

for i in range(user_num):
    if((i%2==0) or (i%2!=0)):
        values.append(i)
for i in values:
    if i==0:
        continue
    if i%2==0:
        even_values.append(i)
    else:
        odd_values.append(i)
print("Odd Numbers: ", odd_values)
print("Even Numbers: ", even_values)
