# Check the frequency of a value in the given test dictionary.
dict={'Codingal' : 3, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}

K=2

res = 0
for key in dict:
    if dict[key] == K:
        res = res + 1
      
print("Frequency of K is : " + str(res))