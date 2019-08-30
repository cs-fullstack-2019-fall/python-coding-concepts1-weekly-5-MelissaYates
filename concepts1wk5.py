# # ### Problem 1:
# # Ask a user for the year they were born by calculating their age.
# # Assuming they already had their birthday and it’s 2019 print “You are [AGE] years old”
#
# userInput = int(input("What year were you born?"))
# userAge = 2019 - userInput
# print(f'You are {userAge} years old')
#
# # ### Problem 2:
# # Ask the user for a string. If they enter “Kenn”, “Kevin”, “Erin”, or “Autumn” print “Hello Teacher”. Otherwise print “Hello Student”
#
# userStr = input("Enter a name: ")
# if userStr ==  "Kenn":
#     print("Hello Teacher")
# elif userStr == "Kevin":
#     print("Hello Teacher")
# elif userStr == "Erin":
#     print("Hello Teacher")
# elif userStr == "Autumn":
#     print("Hello Teacher")
# else:
#     print("Hello Student")
# # ### Problem 3:
# # Ask the user for a negative number. Print from 7 down to the user's negative number. You must include the user's number.
#
# userNeg = int(input("Please enter a negative number"))
# for eachElement in range(7, userNeg-1, -1):
#     print(eachElement)

# ### Problem 4:
# Ask the user to enter a number between -10 to -5.
# If their input is not between the two numbers ask them to do it again until they get it right.
# Afterward they print the correct number, print "Good job"
#TODO: correct this code
# userNum = int(input("Enter a number between -10 and -5. Enter 'q' to quit."))
# while userNum != 'q':
#     if userNum < -5 and userNum > -10:
#         print("Good Job")
#     else:
#         ("Please enter another number")
#     userNum = int(input("Enter a number between -10 and -5"))

# ## Problem 5:
# Create the list: squad ### Problem 6:
# Create a function that will have the string firstName as a parameter. In the function ask the user for their last name. Print "Hello [FIRST & LAST NAME]" in the function. Call that function= ["One", "Two", "Three", "Four", "Five"].
# Print the list in reverse without using a list method.
# #todo: correct this problem
# squad = ["One", "Two", "Three", "Four", "Five"]
# for eachElement in squad:
#
### Problem 6:
# Create a function that will have the string firstName as a parameter. In the function ask the user for their last name.
# Print "Hello [FIRST & LAST NAME]" in the function. Call that function

# def name(firstName):
#     lastName = input("What is your last name?")
#     print(firstName, lastName)
# firstName = "Melissa"
# name(firstName)

# ### Problem 7:
# Create the class Books with name, rating, genre, and author properties/attributes. Create a class method that will change the rating of the book.
# Outside of the class, create three objects of the class Book and put them in an array.
# Lastly, USING THE ARRAY print only the names of the books using any method we’ve learned in class.
#
class Books:
    def __init__(self, name, rating, genre, author):
        self.name = name
        self.rating = rating
        self.genre = genre
        self.author = author
    def change_rating(self):
        new_rating = self.rating(userRating)
def problem7():
    book = Books("Hunger Games", "5", "Mystery", "Barbara Streisand")
    book1 = Books("The Great Controversy", "5", "Non-Fiction", "Ellen G. White")
    book2 = Books("The Diary of a Young Girl", "5", "Non-Fiction", "Anne Frank")

    array_of_books = [book, book1, book2]


problem7()
#
# ### Problem 8:
# Create a function that asks the user to enter a number.
# If the number is between and include -50 and 5, return "Funds too low".
# If the number is between 5 and 50, return “You should add more funds.” If the number is more than 50, return “Just enough.”

# def funds():
#     userInput = int(input("Enter a number"))
#     if userInput <=5 and userInput >= -50:
#         return "Funds too low"
#     elif userInput > 5 and userInput <=50:
#         return "You should add more funds"
#     elif userInput > 50:
#         return "Just Enough"
# ret_val = funds()
# print(ret_val)

# ### Problem 9:
# Ask the user for a positive number. Create an empty array and starting from zero, add each number by 1 into the array.
# Print EACH ELEMENT of the array.

# userPos = int(input("Please enter a positive number"))
# array_of_numbers = []
# for eachElement in range(0, userPos):
#     array_of_numbers.append(eachElement)
#     print(array_of_numbers[eachElement])

# ### Problem 10:
# Create a new empty array called pet_list. Create a Pet class with a type and breed attribute/property.
# Include a method that will print each attribute/property.
# Add 3 pet objects to the pet_list array. Print the attributes/properties for each pet.


class Pet:
    def __init__(self, type, breed):
        self.type = type
        self.breed = breed
    def print_all_attributes(self):
        print(f'{self.type}, {self.breed}')

pet_list = []
pet = Pet("Dog", "Husky")
pet1 = Pet("Snake", "Python")
pet2 = Pet("Cat", "Egyptian")
pet_list = [pet, pet1, pet2]

for i in pet_list:
    print(pet_list.print_all_attributes())