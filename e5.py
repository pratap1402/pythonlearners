import re
from exercises.e1 import is_prime_or_not

# 0.0.0.0 to 999.999.999.999
# def validateIPAddress(hostip):
#     validate = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
#     test = validate.match(hostIP)
#     if test:
#         print("Valid")
#     else:
#         print("Invalid")
#
# hostIP = input("enter ip: ")
# validateIPAddress(hostIP)

# def twoSum(nums,target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return i, j
#
# print(twoSum([2, 7, 11, 15],9))#output: [0,1]
# print(twoSum([3,3],6))#output: [0,1]

# Generate Prime numbers()
# def generatePrime():
#     """
#     generate prime numbers
#     :return:
#     """
#     prime_list = []
#     for i in range(1,51):
#         flag = is_prime_or_not(i)
#         if flag:
#             prime_list.append(i)
#     print(prime_list)
# generatePrime()
# print(generatePrime.__doc__)
