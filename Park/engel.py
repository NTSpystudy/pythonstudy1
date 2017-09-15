import numpy as np
import matplotlib.pyplot as plt
import csv

def main():
    month = []
    income = []
    food_expenses = []
    new_line = []
    account_book = read_file("./account_book.csv")  # account_book = month income food_expenses
    save_the_new_file(account_book, "./account_book1.csv")  # 파일이 변해버리는 것을 대비해서 파일명을 일부러 다르게 해두었습니다

    account_book = np.array(account_book)

    month = account_book[:, 0]
    income = account_book[:, 1]
    food_expenses = account_book[:, 2]

    engels_coefficient = calculate_engel_coefficient(income, food_expenses)
    #print(engels_coefficient)
    visualize_month_by_engel(month, engels_coefficient, "Month", "Engel's coefficient")


def read_file(file_name):  # 파일을 읽어와서 각 원소를 integer형으로 변환해 list 화하여 반환함 단!! 읽어옴과 동시에 새로운 데이터가 있다면 입력하도록 함
    account_book = []
    with open(file_name) as fp:
        next(fp)
        for line in fp:
            splitted = line.strip().split(',')
            account_book.append([int(splitted[0]), int(splitted[1]), int(splitted[2])])

        account_book = set_new_data(account_book)  # 새로운 가계데이터 입력
    return account_book;


def save_the_new_file(account_book, file_name):  # input이 추가되어 새롭게 만들어진 list로 csv파일 갱신
    fp = open(file_name, 'w')
    csvWriter = csv.writer(fp,delimiter=',',lineterminator ='\n')

    csvWriter.writerow(['month', 'income', 'food_expenses'])
    for row in account_book:
        csvWriter.writerow(row)
    fp.close()


def calculate_engel_coefficient(income, food_expenses):  # 엥겔지수 계산 함수
    return food_expenses / income


def visualize_month_by_engel(x, y, x_label, y_label):
    fig = plt.figure(figsize=(10, 6))
    fig.suptitle("Month by engel's Coefficient",fontsize=20)
    plt.xlabel(x_label, fontsize='15')
    plt.ylabel(y_label, fontsize='15')

    plt.scatter(x, y,s=50,color='red')
    plt.plot(x, y, linestyle="--", linewidth=3.0)
    plt.savefig("result.png")
    plt.show()



def set_new_data(account_book):
    input_line = [ x for x in input("새로운 데이터를 입력하세요~! (ex: 8 1000000 222222) :").strip().split(" ")]
    new_line =[]
    for num in input_line:
        if num.isnumeric():#숫자 세개이면 새로운 정보로 인정한다
            new_line.append(int(num))
        else:# 숫자가 아닌 데이터가 입력되면 새로운 정보로 인정하지 않는다
            print('''invalid data type!!
please enter the three integer number!''')
            new_line.clear()
            return account_book

    print('updating~~!')
    account_book.append(new_line)
    return account_book

if __name__ == '__main__':
    main()
