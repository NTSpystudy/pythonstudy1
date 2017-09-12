import numpy as np


def main():
    account_book  = read_file("./account_book.csv")
    print(account_book)

def read_file(file_name):
    account_book = []
    with open(file_name) as fp:
        next(fp)
        for line in fp:
            splitted = line.strip().split(',')
            account_book.append(splitted)
            print(splitted[0])

    return np.array(account_book);
if __name__ == '__main__':
    main()