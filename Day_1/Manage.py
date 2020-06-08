fname = 'hello world.txt'
# file_object = open(fname, 'w')
# file_object.write("Hey tharakabas")
# file_object.write("\nHey this is second line")
# file_object.close()
with open(fname, 'w') as file_object:
    file_object.write('\nhey this is third line')
    file_object.write("\nhey i want to add another line.")