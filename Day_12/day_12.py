# decimal to binary, octal, hexadecimal calculator

num = input("Enter thr decimal number : ")
abs_num = int(num)
print("The decimal value of", abs_num, "is:")
print(bin(abs_num), "in binary.")
print(oct(abs_num), "in octal.")
print(hex(abs_num), "in hexadecimal.")