"""
program:
reverse of words in a string
Input: "how are you"
Output: "you are how"
Input: "welcome to python programming"
Output: "programming python to welcome"
Algorithm:NA
"""
# def reverse_sentence():
#     str = "welcome to python programming"
#     # return (str.split()[::-1])
#     return (" ".join(str.split()[::-1]))
# print(reverse_sentence())

"""
algorithm:
insertionSort(A)
    for j=2 to A.length
        key=A[j]
        i=j-1
        while i>0 and A[i]<key
            A[i+1]=A[i]
            i=i-1
        A[i+1]=key
"""
def insertionSort(A):
    for j in range(1, len(A)):
        key=A[j]
        i=j-1
        while i>-1 and A[i] < key:
            A[i+1]=A[i]
            i=i-1
        A[i+1]=key
    return A
A=[52,2,4,61,7,3,1]
print(f'unsorted array is :{A}')
A = insertionSort(A)
print(f'sorted array is :{A}')
