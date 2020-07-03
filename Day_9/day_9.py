import os
import time
import argparse
import shutil

my_parser = argparse.ArgumentParser(description='Move x months old files in a directory to archive directory')
my_parser.add_argument('Path', metavar='path', type=str, help='The path to directory')
my_parser.add_argument('Months', metavar='months', type=int, help='Number of months')
args = my_parser.parse_args()
input_path = args.Path
input_months = args.Months
old_age = input_months * 30 * 24 * 3600
archive_directory_path = ''

for item in os.listdir(input_path):
    created_date = os.path.getctime(os.path(item))
    if created_date > old_age:
        shutil.move(os.path(item), archive_directory_path)
    else:
        pass
