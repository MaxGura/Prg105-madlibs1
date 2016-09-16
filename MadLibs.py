# Variables
print "Any input can be fictitious or non-fictitious "

print "Enter a character."
character = raw_input()
if character == "":
    name = "Jack Sparrow"

print "Name an animal."
animal = raw_input()
if animal == "":
    animal = "Python"

print "Give an action."
action = raw_input()
if action == "":
    action = "slithers"

print "Name a color."
color = raw_input()
if color == "":
    color = "red"

print "Name a place/location."
place = raw_input()
if place == "":
    place = "flames"

print "Name an organization."
group = raw_input()
if group == "":
    group = "InGen"

print "Provide another character."
person2 = raw_input()
if person2 == "":
    person2 = "Finn"

print "Provide an object"
example = raw_input()
if example == "":
    example = "fur"

print "Provide any weather."
weather = raw_input()
if weather == "":
    weather = "Flaming Hail"

# poem
print(character + ", " "the magic " + animal + " lived by the sea")
print("And " + action + " in the " + color + " " + place)
print("in a land called Honnah Lee ")
print(group + " loved that rascal " + person2)
print("And brought him " + animal + " " + example + " and sealing wax and other fancy stuff, oh! ")
print(character + "," "the magic " + animal + " lived by the sea")
print("And frolicked in the autumn " + weather + " in a land called Honalee,")
print(character + ", the magic " + animal + " lived by the sea")
print("And frolicked in the autumn " + weather + " in a land called Honalee")
