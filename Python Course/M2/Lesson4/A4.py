# Write a program to convert a decimal number into a binary number?

num=float(input("Enter a decimal number: "))
print("The binary equivalent of", num, "is", bin(int(num)).replace("0b", ""))