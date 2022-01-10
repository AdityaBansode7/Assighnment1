#Write a program to manipulate List data

A=['Viresh','Aditya','Vitthal','Aniruddh','Shubham','abc',64,44,29,66,00]

print("\n\nList A :",A[:])

print("List A : 2 to 5",A[2:6])

print("List A In Reverse:",A[::-1])

A.append('Aditya')

print("List A After Appending  :",A[:])

A.insert(4,'Suyash')

print("List A After Inserting  :",A[:])

A.pop(4)

print("List A After Poping :",A[:])

A.remove('abc')

print("List A After Removing :",A[:])

del A[0]

print("List A After Deleteing :",A[:])

A.clear()

print("List A After Clearing :",A[:])

#Write a program to manipulate Tuple data

B=("Tukaram","Aditya","Vitthal","Aniruddh","Shubham","abc","Amit",64,44,29,0)

print("\n\nTuple B:",B)

print("Tuple B: 2 to 5",B[2:6])

print("Tuple B in Reverse:",B[::-1])

print("Count of Aditya is :",B.count('Aditya'))

print("Index of Aditya",B.index('Aditya'))
