# function without parameter


def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)


add_two_numbers()


# function that return values


def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total


tot = add_two_numbers()
print(tot)


# function with parameters


def sum_of_numbers(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total


tot1 = sum_of_numbers(10)
print(tot1)
