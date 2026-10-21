# Write a program to create an array with the following elements - [1, 3, 5, 3, 7, 9, 3]. Then find the number of occurrences of number 3 in the array. Also, print the reversed array.

import array as arr

array_num=arr.array('i',[1,3,5,3,7,9,3])
print("Original Array: ", str(array_num))

print("Frequency of number 3 in the array: ", str(array_num.count(3)))

array_num.reverse()
print("Reverse the order of the items: ", str(array_num))
