# 그리디 알고리즘 실전문제 1번 (큰수의 법칙)
import time

# n개의 수를 입력받아서 배열 생성. 숫자는 1~ 10000 . 더하는건 m번. 연속으로 최대k번 가능
start_time = time.time()
# map 함수를 이용해서 여러개의 정수 한줄로 입력받기 (and 입력 받은거 공백으로 구분 -> split으로 자른다)
result=0;
arr=[];
n,m,k = map(int, input("입력:").split())

# 시작시간
start_time = time.time()

# n개의 수 입력받아 list에 넣기 -> 위와의 차이점은 앞에 list 써주는거
inputNum = list(map(int, input("숫자 목록: ").split()))

# 내림차순 정렬
inputNum.sort(reverse=True)

first = inputNum[0]
second = inputNum[1]

if first == second:
    result = first * m
else:
    result = first *(m // k) * k + second * (m%k) # /은 나눗셈 시 몫과 나머지 그대로 나오고, //은 몫만 나온다.(띄어쓰기 주의) %는 나머지!
print(result)

# 종료시간
end_time = time.time()
print(end_time - start_time)