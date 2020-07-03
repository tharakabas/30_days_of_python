import argparse
import os

my_parser = argparse.ArgumentParser(description='List the content of folder')
my_parser.add_argument('Path', metavar='path', type=str, help='The path to list')
args = my_parser.parse_args()
input_path = args.Path

if not os.path.isdir(input_path):
    print('The path specified is not exist')
    exit(3)

for item in os.listdir(input_path):
    print(item)