"""
program:
patterns
Algorithm:
read(n)
for i=1 to n
    for j=1 to i
        print(i)
"""
# def patterns():
#     n = int(input("enter no of rows: "))
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(i,end="")
#         print(end="\n")
# patterns()
#
# def patterns():
#     n = int(input("enter no of rows: "))
#     for i in range(1,n+1):
#         print(str(i)*i)
# patterns()
#
# def patterns():
#     n = int(input("enter no of rows: "))
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(j,end="")
#         print(end="\n")
# patterns()

"""
program:
reverse of a string
Algorithm:
read(str)
reverse_str=""
for i=1 to str.length
    reverse_str = str[char] + reverse_str
print reverse_str
"""
def reverse_str(str):
    reverse_str = ""
    for i in range(len(str)):
        # print(f"i: {i}, str[i]:{str[i]}")
        reverse_str = str[i] + reverse_str
    return reverse_str

if __name__ == "__main__":
    str = input("enter a string: ")
    print(reverse_str(str))
#
# def reverse_str(str):
#     reverse_str = ""
#     for i in range(1,len(str)+1):
#         reverse_str=reverse_str+str[-i]
#     return reverse_str
# print(reverse_str("python"))
#
# def reverseString(str):
#     return (str[::-1])
# print(reverseString("pratap"))

'''
program:
fibinocci series
Algorithm:NA
'''
# def fibinocci():
#     a,b = 0,1
#     while a < 50:
#         print(a)
#         a, b = b, a+b
# fibinocci()
