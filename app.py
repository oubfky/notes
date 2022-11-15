print("Hello World")
print("     /|")
print("    / |")
print("   /  |")
print("  /___|")

character_name = "Mike"
character_age = "30"
is_male = False
print("There once was a man named " + character_name)
print("He was " + character_age + " years old.")
print("He really liked the name " + character_name)
print("but didn't like being " + character_age + ".")

print("Giraffe Academy")
print("Giraffe\nAcademy")
print("Giraffe\“Academy")
print("Giraffe\Academy")

phrase = "Giraffe Academy"
print(phrase + " is cool")
print(phrase.lower())  # lower case
print(phrase.upper())  # upper case
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))  # length of the string
print(phrase[0])  # the first character
print(phrase[3])  # a
print(phrase.index("G"))  # 0, the index of G
print(phrase.index("Acad"))
print(phrase.replace("Giraffe", "Elephant"))

print(3+4.5)
print(-2.4)
print(3/2)
print(3*5)
print(3*(4+5))
print(10%3) #mod 1

my_num = 5
print(my_num)
print(str(my_num))#convert a number to a string
print(str(my_num) + " my favorite number")

my_num = -5
print(abs(my_num))
print(pow(3,2)) # 3*3
print(max(4,6))
print(min(4,6))
print(round(5.3))

from math import *
print(floor(5.1))
print(ceil(3.7))
print(sqrt(36))

# name = input("Enter your name:")
# print("Hello "+ name + "!" )

# num1 = input("Enter a number:")
# num2 = input("Enter another number:")
# result = num1+num2 # string
# result = int(num1)+int(num2)
# result = float(num1) + float(num2)
# print(result)

# color = input("Enter a color:")
# plural_noun = input("Enter a Plural Noun:")
# celebrity = input("Enter a celebrity")
# print("Roses are " + color)
# print(plural_noun + " are blue")
# print("I love " + celebrity)

# list
friends = ["Kevin","Karen","Jim"]
friends = ["Kevin",2,"Jim","Kitty","Opera"]
print(friends)
print(friends[2])
print(friends[0])
print(friends[-1])
print(friends)
friends[0] = "Mark"
print(friends)
friends[0] = "Kevin"
print(friends)

lucky_numbers = [1, 4, 5, 6, 1, 3, 1]
print(lucky_numbers)
friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1,"apple") # insert one element, all the other elements pushed to the right
#friends.clear() # clear the list
print(friends)
friends.pop()
print(friends)