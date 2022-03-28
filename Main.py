print("Welcome to Python Pizza delivery!!")
bill = 0
size= input("Enter pizza size S,M,L\n")
if size=="S":
	bill += 500
elif size=="M":
	bill+=1000
else:
	bill+=1500
add_pepperoni = input("Add pepperoni Y or N:\n")
if add_pepperoni=="Y":
	if size =="S":
		bill+=100
	elif size=="M":
		bill+=150
	else:
		bill+=200
else:
	bill==bill
extra_cheese = input("Extra cheese Y or N:\n")
if extra_cheese=="Y":
	bill+=50
	print(f"Total bill is KES {bill}. Thank you!!")
	
print("Welcome to the python love calculator")
name_one=input("Enter your name:\n")
name_two=input("Enter lover's name:\n")
combined_name=name_one+name_two
low_caps =combined_name.lower()
t= combined_name.count("t")
r= combined_name.count("r")
u= combined_name.count("u")
e=combined_name.count("e")
true= t+r+u+e
l=combined_name.count("l")
o=combined_name.count("o")
v=combined_name.count("v")
e=combined_name.count("e")
love=l+o+v+e
love_score =int(str(true)+str(love))
print(love_score)
if love_score <=10 or love_score >=90:
	print(f"Your love score is {love_score}, you go together liKe coke and menthos")
elif love_score >=40 and love_score<=50:
	print(f"Your love_score is {love_score},you are alright together")
else:
	print(f"Your love_score is {love_score}")
