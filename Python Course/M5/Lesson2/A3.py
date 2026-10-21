# 1) Create a class named `pair_elements`.

# 2) Inside the class, define a method `twoSum(self, nums, target)`:
#    (This method finds two numbers in `nums` whose sum equals `target`
#     and returns their index positions.)

# 3) Create an empty dictionary `lookup = {}`.
#    (This will store numbers as keys and their indexes as values for quick searching.)

# 4) Use a loop with `enumerate(nums)` to iterate through `nums`:
#    a) `i` gives the index of the current element.
#    b) `num` gives the value at that index.

# 5) For each number, check if the required pair exists:
#    a) Compute `target - num`.
#    b) If `target - num` is already present in `lookup`,
#       return a tuple containing:
#       - the index of the matching number from `lookup`
#       - the current index `i`

# 6) If the pair is not found yet, store the current number and its index:
#    a) `lookup[num] = i`

# 7) Take an integer input from the user and store it in `value`.
#    (This is the target sum to search for.)

# 8) Call the method `twoSum()` using:
#    a) the tuple `(10, 20, 30, 40, 50, 60, 70)` as `nums`
#    b) `value` as the `target`

# 9) Print the two indexes returned by `twoSum()` in the format:
#    "index1=..., index2=..."

class pair_elements:
    def twoSum(self,nums,target):
        lookup={}

        for i,num in enumerate(nums):
            if target-num in lookup:
                return (lookup[target-num],i)
            lookup[num]=i

value=int(input("Enter sum for which you want to search: "))
a=pair_elements()
print(a.twoSum((10, 20, 30, 40, 50, 60, 70),value))
