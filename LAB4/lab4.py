
users = {}
unique_items = set()
ordered_items = []

num_users = int(input("Enter number of users: "))

for _ in range(num_users):
    username = input("Enter username: ")
    num_items = int(input("How many items? "))

    items = []
    for i in range(1, num_items + 1):
        item = input(f"Item {i}: ")
        items.append(item)

        if item not in unique_items:
            unique_items.add(item)
            ordered_items.append(item)

    users[username] = items

print("USER DATA:")
for user, items in users.items():
    print(f"{user} -> {items}")

item_count = {}

for item in unique_items:
    count = 0
    for items in users.values():
        if item in items:
            count += 1
    item_count[item] = count
print()
print("COMMON ITEMS:")
for item in ordered_items:
    if item_count[item] > 1:
        print(item)
print()
print("UNIQUE ITEMS:")
for item in ordered_items:
    if item_count[item] == 1:
        print(item)

if item_count:
    max_count = max(item_count.values())
    most_popular = []

    for item in ordered_items:
        if item_count[item] == max_count:
            most_popular.append(item)
    print()
    if len(most_popular) == 1:
        print("MOST POPULAR ITEM:")
    else:
        print("MOST POPULAR ITEMS:")

    for item in most_popular:
        print(item)