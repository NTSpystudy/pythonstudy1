
import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd

def main():

    # x축과 y축 정의
    x=[]
    y=[]

    # account_book.csv 생성
    jisoo = open("account_book.csv")

    cnt = 0
    for row in csv.reader(jisoo):
        if(cnt==0):
            cnt = cnt + 1
            continue

        month = row[0]
        income = row[1]
        food_expense = row[2]

        # x,y 에 넣기
        x.append(month)
        y.append(int(food_expense)/int(income))

    jisoo.close()

    # 8월 입력값 받기
    income8 = input("8월 수입을 입력해 주세요. \n")
    food_expense8 = input("8월 음식지출비를 입력해 주세요. \n")

    # 8월 입력값 x,y 에 넣기
    x.append(8)
    y.append(int(food_expense8)/int(income8))

    # 입력값 받기 후
    print(x)
    print(y)

    # jisoo = open("account_book.csv", "a")
    #
    # wr = csv.writer(jisoo)
    # wr.writerow(['\n8', income8, food_expense8])
    #
    # jisoo.close()

    # 그래프 그리기
    plt.plot(x,y, label="Engel's Coefficient")
    plt.xlabel("month")
    plt.ylabel("Engel's Coefficient")
    plt.title("Engel's Coefficient of jisoo")
    plt.legend()
    plt.show()


    # jisoo = pd.read_csv("account_book.csv")
    # print(jisoo.head(5))


if __name__ == '__main__':
    main()