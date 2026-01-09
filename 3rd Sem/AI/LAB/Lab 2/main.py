# Lab Task 1
# list1 = list(map(int, input("Enter first list (space-separated): ").split()))
# list2 = list(map(int, input("Enter second list (space-separated): ").split()))

# merged_list = sorted(list1 + list2)
# print("Merged & Sorted List:", merged_list)


# Lab Task 2

# print("Smallest:", min(merged_list))
# print("Largest:", max(merged_list))


# Lab Task 3 
# from math import sin, cos, pi

# h = 0.001  # step size
# x = -pi

# while x <= pi:
#     derivative = (sin(x + h) - sin(x)) / h  # numerical derivative
#     print(f"x={x:.3f}, Approx={derivative:.6f}, cos(x)={cos(x):.6f}")
#     x += 0.001


# # Lab Task 4
# birthdays = {
#     "Abu Bakr": "03/14/2005",
#     "Abbas": "01/17/2009",
#     "Abdul Wali": "12/10/1996"
# }

# print("Welcome to the birthday dictionary. We know the birthdays of:")
# for name in birthdays:
#     print(name)

# person = input("Who's birthday do you want to look up? ")
# if person in birthdays:
#     print(f"{person}'s birthday is {birthdays[person]}.")
# else:
#     print("Sorry, we don't have that birthday.")


# Lab Task 5
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
keys = ["name", "salary"]

new_dict = {k: sample_dict[k] for k in keys}
print(new_dict)
