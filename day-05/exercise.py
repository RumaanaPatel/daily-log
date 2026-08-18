# first, last, and total count
food = ["Alfredo", "Biryani", "Qasadia", "Pasta", "chillie chicken"]
print("first: ", food[0])
print("last: ", food[4])
print("number of food: ", len(food))

# max, min, and sum
numbers = []
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

largest = max(numbers)
smallest = min(numbers)
average = sum(numbers) / len(numbers)

print(f"Largets: {largest}")
print(f"Smallest: {smallest}")
print(f"Average: {average}")

# Ascending, descending, and reversed
given_num = [3, 7, 2, 9, 4, 1, 8]
given_num.sort()
print("Ascending: ", given_num)
given_num.sort(reverse=True)
print("Descending:", given_num)
given_num.reverse()
print("Reverse: ", given_num)

# remove the dupelicate usind 2 different methords
dupe = {1, 2, 2, 3, 3, 3}
print(dupe)
unique = list(set(dupe))
print(unique)

# Print every key and value using .items()
student = {
    "Rumaana": {
    "age": 19,
    "major": "software Engineering",
    "year": 3,
    "university": "Utah Valley University"
    }
}
for key, value in student.items():
    print(f"{key}: {value}")

# print the students grade
names = {
    "Rumaana": "A",
    "Alice": "B",
    "Bob": "c",
    "Amber": "C",
    "David": "B"
}

search = input("Student name: ")
if search in names:
    print(f"{search}'s grade is {names[search]}")
else:
    print(f"student {search} not found.")

# print word counts
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_counts = {}
for word in words:
    word = word.lower()
    if word in word_counts:
        word_counts[word] +=1
    else:
        word_counts[word] = 1
print(word_counts)

# print the names in both and combine them without printing the suplicate
name_one = {"Aclice", "Bob", "Emma"}
name_two = {"Bob", "Luke", "Daisy"}
print(name_one)
print(name_two)
print(name_one | name_two)

# contact menu
contacts = {
    "Alice": "324-567-6789",
    "Bob": "453-764-7689"
}
while True:
    print("\n---Contacts Menue---")
    print("1. Add contact")
    print("2. Look up contact")
    print("3. List of contacts")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")
    if choice == "1":
        name = input("name: ")
        phone = input("phone number: ")
        contacts[name] = phone
        print(f"Contact {name} added.")
    elif choice == "2":
        name = input("Enter name to look up: ")
        print(f"Phone: {contacts.get(name, 'Not found')}")
    elif choice == "3":
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    elif choice == "4":
        print("Goodbye")
        break
    else:
        print("Invalid choice. Try again")

# list comprehension to produce a new list containing only the numbers greater than 10, doubled
num = [2, 5, 12, 7, 20, 10, 15]
result = [num * 2 for num in num if num > 10]
print(result)