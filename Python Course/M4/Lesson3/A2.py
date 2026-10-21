# Initialize dictionary
test_dict = {'Go' : 1, 'Goa' : 2, 'Gone' : 3, 'for' : 2, 'Good' : 5}
  
# printing original dictionary
print("The original dictionary : " +  str(test_dict))
  
# Initialize value 
K = 2
  
# Using loop
# Selective key values in dictionary
res = 0
for key in test_dict:
    if test_dict[key] == K:
        res = res + 1
      
# printing result 
print("Frequency of K is : " + str(res))

