animals = ["cat", "dog", "panda", "newt", "ostrich", "raccoon"]
print(animals)
message = f"The first two items in the list are: {animals[0:2]}."
print(message)
print(f"The middle two items in the list are: {animals[2:4]}")
print(f"The first and last items in the list are: {animals[0]}, {animals[-1]}")
# print(f"The first two items in the list are: {", ".join(animals[0:2])}") for no brackets in answer
# print(animals[0].title()) to capitalize it
foods = ("spaghetti", "hotdog", "nachos", "chips", "tacos")
print("\nMy restaurant menu:")
for food in foods:
    print(food.title())
foods = ("spaghetti", "hotdog", "nachos", "salad", "barbeque")
print("\nMy updated restaurant menu:")
for food in foods:
    print(food.title())