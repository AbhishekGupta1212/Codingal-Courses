# Write a program to calculate how many total digits are in a number entered by the user?

num=int(input("Enter a number: "))
count=0

while(num>0):
    num//=10
    count+=1
print(count)