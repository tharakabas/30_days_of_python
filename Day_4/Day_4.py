
with open('text1.txt', 'r') as file_object1:
    file1_cont = set(file_object1.read().split())
    # print(file1_cont)

with open('text2.txt', 'r') as file_object2:
    file2_cont = set(file_object2.read().split())

duplicate = file1_cont.intersection(file2_cont)
unique = file1_cont.difference(file2_cont).union(file2_cont.difference(file1_cont))

print(duplicate)
print(unique)
print(duplicate)
