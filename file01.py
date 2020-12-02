# 명령 조건(함수, 상수, 변수 등 but true(참) 와 false(거짓)로 구분할 것임. ) : 
#     명령1 (명령이 참일 경우 실행되는 명령)
#     명령2
#     명령3
# 외부명령(명령이 거짓일 때 실행하는 명령)
#     명령1
#     명령2
#     명령3

# fNum = 10
# sNum = 5

# if fNum > sNum : 
#     print("fNum이 sNum 보다 크다")

# if fNum < sNum :
#     print("sNum이 fNum 보다 크다")

# inVal = int(input("정수 입력 : "))

# if inVal%2==0 :
#     print("입력값 {}은(는) 짝수 입니다.".format(inVal))
# if inVal%2 != 0:
#     print("입력값 {}은(는) 홀수 입니다.".format(inVal))

# print("1.Easy game")
# print("2.Hard game")
# print("3.Exit")
# selMenu = input("레벨 선택 : ")

# if selMenu == '1' : 
#     print("Easy Game Start")
# if selMenu == '2' : 
#     print("Hard Game Start")
# if not(selMenu == '1' or selMenu == '2') : 
#     print("Exit Game")

# # 날짜를 입력 받기 무슨 요일인지출력 해보기

# # 1~31일까지 존재
# # 무조건 1일은 월요일
# # 입력한 날짜가 무슨 요일인지 계산해보기

# # dateVal = int(input("날짜 입력 : "))

# # dayVal = dateVal % 7 

# # if dayVal == 1 : 
# #     print('{}일 : 월요일'.format(dateVal))
# # if dayVal == 2 : 
# #     print('{}일 : 화요일'.format(dateVal))
# # if dayVal == 3 : 
# #     print('{}일 : 수요일'.format(dateVal))
# # if dayVal == 4 : 
# #     print('{}일 : 목요일'.format(dateVal))
# # if dayVal == 5 : 
# #     print('{}일 : 금요일'.format(dateVal))
# # if dayVal == 6 : 
# #     print('{}일 : 토요일'.format(dateVal))
# # if dayVal == 0 : 
# #     print('{}일 : 일요일'.format(dateVal))

# # Q1. 입력한 데이터가 3의 배수인 경우에 출력해주세요
# # Q5. 세 수를 입력 받아 큰 수를 출력해 보세요.
# # Q6. 두 수를 입력 받아 큰 수가 짝수이면 출력해 보세요.
# # Q7. 두 수를 입력 받아 큰 수가 짝수이면서 3의 배수 이면 출력해 주세요.
# # ranVal = int(input('숫자를 입력해보세요 : '))
# # if not ranVal % 3 = 1 or 2
# #     print('{}'.format(ranVal))

# # ranVal = int(input('숫자를 입력하세요'))
# # if not ( (ranVal%3 == 1) or (ranVal%3 == 2) ) :
# #     print('{}'.format(ranVal))
    
# #if inVal%2 != 0:
# #     print("입력값 {}은(는) 홀수 입니다.".format(inVal))

# # ultiNum = float(input('숫자를 입력하세요: '))
# # if ultiNum > 0 :
# #     print("{}".format(ultiNum))
# # if ultiNum < 0 :
# #     print('{}'.format(ultiNum*-1))



# # happyNum = int(input("숫자를 입력하세요 : "))
# # if happyNum % 2 == 0 :
# #     print('{}'.format('짝수'))
# # if happyNum % 2 == 1 :
# #     print("{}".format('홀수'))

# # fstWord = int(input('첫 번째 숫자를 입력하세요.'))
# # secWord = int(input("두 번째 숫자를 입력하세요."))

# # if fstWord < secWord : 
# #     print('{}'.format(secWord))
# # if fstWord > secWord : 
# #     print('{}'.format(fstWord))


# # 강사님 해법
# # kksVal = int(input("정수 입력 : "))
# # if kksVal%3 == 0: 
# # print("{}은 3배의 배수입니다."format(kksVal))

# # # Q2. 입력 받은 값의 절대값을 구해보세요
# # kksVal = int(input("정수 입력 : "))
# # absVal = kksVal
# #     print("{}은(는)의 절대값은 {}입니다.".format(kksVal, absVal))

# # if kksVal <0 :
# #     absVal = kksVal * -1
# #     print("{}은(는)의 절대값은 {}입니다.".format(kksVal,absVal))


# # #   Q3. 입력 받은 수의 홀수,짝수를 구분해 보세요.
# # kksVal = int(input('정수입력 : '))

# # if kksVal%2 ==0 :
# #     print("{}은 짝수 입니다.".format(kksVal))

# # if kksVal%2 !==0 :
# #     print("{}은 짝수 입니다.".format(kksVal))
    
# # # Q4. 두 수를 입력 받아 큰 수를 출력해 보세요.
# # fNum = int(input("정수 입력 : "))
# # sNum = int(input('정수 입력 : '))
# # maxNum = 0
# # if fNum > sNum :
# #     maxNum = fNum 
# # if fNum < sNum : 
# #     maxNum =sNum
# # print("{}와 {}wnd 큰 수는 {}입니다".format(fNum, sNum, maxNum))

# fNum = int(input('정수 입력: '))
# sNum = int(input('정수 입력: '))
# tNum = int(input('정수 입력: '))

# maxNum = 0
# if fNum>sNum and fNum > tNum
# maxNum = fNum
# if sNum>fNum and fNum > tNum
# maxNum = sNum
# if tNum>fNum and fNum > sNum
# maxNum = tNum
# print("{},{}, 그리고 {}중 큰 수는 {}입니다."\
#     .format(fNum,sNum,Tnum,maxNum))

# fNum = int(input('정수 입력 : '))
# sNum = int(input('정수 입력 : '))
# maxNum = 0

# if fNum > sNum :
#     maxNum = fNum
# if sNum > fNum :
#     maxNum = sNum

# if maxNum%2 == 0 :
#     print("{}와 {}중 큰 수는 {}이면서, 짝수 입니다."\
#         .format(fNum, sNum, maxNum))

# fNum = int(input('정수 입력 : '))
# sNum = int(input('정수 입력 : '))
# sumNum = fNum + sNum
# if (sumNum% 2== 0) and (sumNum%3 == 0) :
#     print("{}와 {}의 합은 {}이면서 3의 배수 입니다.".format(fNum, sNum, sumNum))


# Q1. 입력한 데이터가 3의 배수인 경우에 출력해주세요
# Q2. 입력 받은 값의 절대값을 구해보세요
# Q5. 세 수를 입력 받아 큰 수를 출력해 보세요.
# Q6. 두 수를 입력 받아 큰 수가 짝수이면 출력해 보세요.
# Q7. 두 수를 입력 받아 합이 짝수이면서 3의 배수 이면 출력해 주세요.
# Q4. 두 수를 입력 받아 큰 수를 출력해 보세요.
#    Q3. 입력 받은 수의 홀수,짝수를 구분해 보세요.