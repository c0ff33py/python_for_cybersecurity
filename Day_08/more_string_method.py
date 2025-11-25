name = "Mountains".upper()
print(name)  # Output: MOUNTAINS

answer = "YES"
if answer.lower() == "yes":
    print("User said yes")

word = " yes ".strip()
print(f"'{word}'") # Output: 'yes'

word1= " yes ".lstrip()
print(f"'{word1}'") # Output: 'yes '

word2 = " yes ".rstrip()
print(f"'{word2}'") # Output: ' yes'

words = "The number of times e occurs in this string is 4".count("e")
print(words) # Output: 4

phrase = " ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"])
print(phrase) # Output: This is a phrase joined by spaces

phrase1 = "...".join(["This", "is", "a", "phrase", "joined", "by", "three", "dots"])
print(phrase1) # Output: This...is...a...phrase...joined...by...three...dots