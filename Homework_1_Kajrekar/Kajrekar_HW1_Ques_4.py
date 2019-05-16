# Name: Nikhil Kajrekar
# UTA ID: 1001552488

color1 = input("Enter first of the two primary colors to mix: ")
color2 = input("Enter second of the two primary colors to mix: ")
if color1 == color2:
    print("Error: Please enter two different colors to mix")
elif (color1 == "red" and color2 == "blue") or (color2 == "red" and color1 == "blue"):
    print("The resulting secondary color after mixing is purple")
elif (color1 == "red" and color2 == "yellow") or (color2 == "red" and color1 == "yellow"):
    print("The resulting secondary color after mixing is orange")
elif (color1 == "blue" and color2 == "yellow") or (color2 == "blue" and color1 == "yellow"):
    print("The resulting secondary color after mixing is green")
else:
    print('Error: Primary colors can only be "red" , "blue" or "yellow"')