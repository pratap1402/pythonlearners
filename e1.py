"""
program:
calculator
Algorithm:NA
"""
# def simpleCalculator():
#     operation = input('''
#     Please type:
#     + for addition
#     - for subtraction
#     * for multiplication
#     / for division
#     % for remainder
#     ''')
#
#     n1 = int(input('Enter your first number: '))
#     n2 = int(input('Enter your second number: '))
#
#     if operation == '+':
#         print(f'{n1} + {n2} = {n1 + n2}')
#     elif operation == '-':
#         print(f'{n1} - {n2} = {n1 - n2}')
#     elif operation == '*':
#         print(f'{n1} * {n2} = {n1 * n2}')
#     elif operation == '/':
#         print(f'{n1} / {n2} = {n1 / n2}')
#     elif operation == '%':
#         print(f'{n1} % {n2} = {n1 % n2}')
#     else:
#         print('Invalid operator!')
#
# if __name__ == "__main__":
#     simpleCalculator()

"""
program:
length of a string
Algorithm:
read(str)
counter=0
for char in str
    increment counter
print counter
"""
def lengthOFAString(str):
    # str = input("enter a string: ")
    count = 0
    for i in str:
        count += 1
    # print(count)
    return count
#
if __name__ == "__main__":
    str = input("enter a string: ")
    print(lengthOFAString(str))

'''
program:
Prime number
Algorithm:
read(n)
if n is 1
    print neither prime nor composite
count as 0
for i=1 to n
    if n%i is 0
        increment count
if count is 2
    print prime
not if
    print composite
'''
def is_prime_or_not(n):
    count=0
    if n==1:
        # print("neither prime nor composite")
        return 0
    else:
        for i in range(1,n+1):
            if n%i == 0:
                count= count + 1
        if count==2:
            # return "prime"
            return 1
        else:
            # return "not prime"
            return 0

if __name__ == "__main__":
    n=int(input("enter a number: "))
    print(is_prime_or_not(n))
