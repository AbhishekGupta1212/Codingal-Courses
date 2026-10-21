# Write a program to create two classes for two different countries that consist of three methods to display the following information of respective country - capital, language and type of country. Then, use Polymorphism to create a common interface for both classes.

# Step 1: Define a class India with three methods: capital(), language(), and type(), each printing a fact about India.

# Step 2: Define a class USA with the exact same three method names, each printing a fact about the USA.

# Step 3: Create one object of each class: obj_ind and obj_usa.

# Step 4: Use a for loop to iterate through (obj_ind, obj_usa).

# Step 5: Inside the loop, call country.capital(), country.language(), and country.type() on each object - Python automatically runs each class's own version, with no inheritance needed.


class India:

    def capital(self):
        print("Delhi is the capital of India.")

    def language(self):
        print("It's a most linguistically diverse nation.")

    def type(self):
        print("India is a developing country.")


class USA:

    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the most spoken language.")

    def type(self):
        print("USA is a developed country.")

obj_india=India()
obj_usa=USA()

for i in (obj_india,obj_usa):
    i.capital()
    i.language()
    i.type()