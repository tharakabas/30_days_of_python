character = 'P'                
print(character)               
print(len(character))          
greeting = 'Hello, World!'  
print(greeting)             
print(len(greeting))        


# Multiline String
multiline_string = '''Python is a great language.
Using python we can impliment multilinr string variable in a simple way.
It's Cool'''
print(multiline_string)

# String Concatenation
first_name = 'Supun'
last_name = 'Tharaka'
space = ' '
full_name = first_name  +  space + last_name
print(full_name)



# Accessing characters in strings by index
language = 'Python 3'
first_letter = language[0]
print(first_letter)
second_letter = language[1]
print(second_letter)
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)

# Slicing

language = 'Python'
first_three = language[0:3]
print(first_three)
last_three = language[3:6]
print(last_three)



# Escape sequence
print('Frist line\nSecond line ?')
print('Tab1\tTab2\tTab3')

## String Methods

challenge = 'python'
print(challenge.capitalize())

print(challenge.endswith('on'))   # True
print(challenge.endswith('son')) # False

print(challenge.find('y'))  # 1
print(challenge.find('p')) # 0
 
name = 'Supun Tharaka'
print(f'Hello My name is {name}')

print(challenge.find('y'))  # 1
print(challenge.find('p')) # 0
