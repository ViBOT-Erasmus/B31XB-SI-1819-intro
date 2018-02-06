import sys

def print_int_lists(*args):
    """printing the list of integerts"""
    a = [i for i in range(int(args[0]))]
    print(a)
    return a


if __name__ == '__main__':

    print_int_lists(sys.argv[1])
