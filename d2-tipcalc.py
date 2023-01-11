# 1OO Days of Code: Band Name Generator project
#
# This program calculates the amount people have
# to pay along with the tip. The sum is split
# evenly among the people.

print("Welcome to Bill Splitter & Tip Calc.")

total = float(input("What was the total bill? €"))
num_people = int(input ("How many people are splitting the bill? "))
tip_percentage = input("What is your desired tip percentage?\na) 10 %\nb) 12 %\nc) 15 %\nType the letter of the option: ")

if tip_percentage == 'a':
    tip_percentage = 0.1
elif tip_percentage == 'b':
    tip_percentage = 0.12
elif tip_percentage == 'c':
    tip_percentage = 0.15
else:
    print("Incorrect option. Rerun the program.")
    exit(1)

print("Each person should pay €" + str(round(((total + (total * tip_percentage)) / num_people),2)))

