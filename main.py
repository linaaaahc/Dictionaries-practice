phone = input("Phone = ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output= ""
for number in phone:
    output += digits_mapping.get(number, "Not a number") + " "
print(output)