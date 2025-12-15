# animals = ["Lions", "Zebra", "Doplin", "Monkey"]

# chars = 0

# for animal in animals:
# 	chars += len(animal)

# print(f"Total characters: {chars}, Average length: {chars/len(animals)}")


# winners = ["Ashley", "Dylan", "Reese"]

# for index, person in enumerate(winners):
# 	print(f"{index + 1} - {person}")


def full_emails(people):
	result = []
	for email, name in people:
		result.append(f"{name} <{email}>")
	return result
print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))