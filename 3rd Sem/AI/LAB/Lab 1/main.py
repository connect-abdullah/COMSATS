# LAB Task 1

# numbers = []
# while True:
#     x = input("Enter Number (or press Enter to finish): ")
#     if x == "":
#         break
#     numbers.append(x)

# num_str = "".join( numbers)
# reversed_num = num_str[::-1]
# if reversed_num:
#     print(int(reversed_num))


# # LAB Task 2

# integers = [1,2,3,4,5,6,7,8,9,10]
# even = 0
# odd = 0

# for num in integers:
#     if(num % 2 == 0):
#         even += num
#     else:
#         odd += num
        
# print("Sum of Even Numbers: ", even)
# print("Sum of Odd Numbers: ", odd)


# LAB Task 3

# term = int(input("Input the number of terms: "))
# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)

# for i in range(term):
#         print(fib(i), end=" ")    


# # LAB Task 4

# marks = int(input("Enter marks (1-100): "))
# try:
#     if marks < 1 or marks > 100:
#         print("Invalid marks. Please enter a value between 1 and 100.")
#     elif marks < 50:
#         print("Grade F")
#     elif 50 <= marks <= 60:
#         print("Grade E")
#     elif 61 <= marks <= 70:
#         print("Grade D")
#     elif 71 <= marks <= 80:
#         print("Grade C")
#     elif 81 <= marks <= 90:
#         print("Grade B")
#     elif 91 <= marks <= 100:
#         print("Grade A")
# except ValueError:
#     print("Invalid input. Please enter a numeric value.")


# LAB Task 5

number = int(input("Number for factorial: "))
def factorial(n):
    if(n<=1):
        return 1
    
    return n * factorial(n-1)

print(factorial(number))