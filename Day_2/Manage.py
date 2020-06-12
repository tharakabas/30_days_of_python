

with open('some1.txt', 'r') as file_object1:
    file1_cont = set(file_object1.read().split())
    # print(file1_cont)

with open('some2.txt', 'r') as file_object2:
    file2_cont = set(file_object2.read().split())

duplicate = file1_cont.intersection(file2_cont)
unique = file1_cont.difference(file2_cont)

print(duplicate)
print(unique)
