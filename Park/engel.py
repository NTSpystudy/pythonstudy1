import numpy as np
import matplotlib.pyplot as plt
import csv

def main():
    month = []
    income = []
    food_expenses = []
    new_line = []
    account_book  = read_file("./account_book.csv") #account_book = month income food_expenses
    save_the_new_file(account_book,"./account_book1.csv")#파일이 변해버리는 것을 대비해서 파일명을 일부러 다르게 해두었습니다
    
    print(account_book)
    account_book = np.array(account_book)
    
    month = account_book[: ,0]
    income = account_book[: ,1]
    food_expenses = account_book[: ,2]
    
    engels_coefficient = calculate_engel_coefficient(income,food_expenses)
    
    visualize_month_by_engel(month,engels_coefficient)
    
def read_file(file_name):#파일을 읽어와서 각 원소를 integer형으로 변환해 list 화하여 반환함 단!! 읽어옴과 동시에 새로운 데이터가 있다면 입력하도록 함
    account_book = []
    with open(file_name) as fp:
        next(fp)
        for line in fp:
            splitted = line.strip().split(',')
            account_book.append([int(splitted[0]), int(splitted[1]), int(splitted[2])])
            
        account_book = set_new_data(account_book)  # 새로운 가계데이터 입력
    return account_book;


def save_the_new_file(account_book,file_name):#input이 추가되어 새롭게 만들어진 list로 csv파일 갱신
	fp = open(file_name,'w')
	csvWriter = csv.writer(fp)
	
	csvWriter.writerow(['month','income','food_expenses'])
	for row in account_book:
		csvWriter.writerow(row)
	fp.close()
	
def calculate_engel_coefficient(income,food_expenses):#엥겔지수 계산 함수
    return food_expenses/income

def visualize_month_by_engel(x,y):
    fig =plt.figure(figsize=(10,6))
    fig.suptitle("Month by engel's Coefficient")
    
    plt.scatter(x,y)
    plt.plot(x,y,linestyle = "--",linewidth = 3.0)
    plt.savefig("result.png")
    
def set_new_data(account_book):#int가 아닌 데이터가 입력되는 경우를 대비해서 코드수정 필요
	new_line = [int(x) for x in input("New Data(ex: 9 1000000 222222) :").strip().split(" ")]
	print(type(new_line[0]))
	if (type(new_line[0])==int) and (type(new_line[1])==int) and (type(new_line[2])==int):
		print("update~~")
		account_book.append(new_line)
	else:
		print('invalid data!!!')
	return account_book

if __name__ == '__main__':
    main()