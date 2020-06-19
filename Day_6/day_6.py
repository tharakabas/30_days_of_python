import argparse

my_arg=argparse.ArgumentParser()
my_arg.add_argument('NewItem','-n', '--new',action='store', type=str)
args=my_arg.parse_args()
print(args.NewItem)
