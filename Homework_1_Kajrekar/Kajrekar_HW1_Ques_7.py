# Name: Nikhil Kajrekar
# UTA ID: 1001552488

vegetarian = "No"
vegan = "No"
gluten_free = "No"

vegetarian_ques = input("Is anyone in your party a vegetarian? ")
vegan_ques = input("Is anyone in your party a vegan? ")
gluten_free_ques = input("Is anyone in your party gluten free? ")

if vegetarian_ques == "Yes" or vegetarian_ques == "yes":
    vegetarian = "Yes"

if vegan_ques == "Yes" or vegan_ques == "yes":
    vegan = "Yes"

if gluten_free_ques == "Yes" or gluten_free_ques == "yes":
    gluten_free = "Yes"

print("Here are your restaurant choices: ")

if vegetarian == "No" and vegan == "No" and gluten_free == "No":
    print("Joe's Gourmet Burgers")

if vegan == "No" and gluten_free == "No":
    print("Mama's Fine Italian")

if vegan == "No":
    print("Main Street Pizza Company")

print("Corner Cafe")
print("The Chef's Kitchen")

