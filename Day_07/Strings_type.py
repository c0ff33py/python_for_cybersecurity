fruit = "Mangosteen"
print(fruit[1:4]) #output: ang

print(fruit[5:])  #output: steen

print(fruit[:5] + fruit[5:]) #output: Mangosteen


message = "A kong with a silly typo"
message[2] = "l" # THis will be an error because strings are immutable in Python
print(message)


pets = "Cats & Dog"
print(pets.index("&"))
