## 숫자 카드게임. n x m 형태로 카드가 놓여있음. n은 행의개수, m은 열의 개수
## 뽑고자 하는 카드가 포함된 행을 선택 후, 그 행의 가장 숫자가 낮은 카드를 뽑아야 한다.
## 처음에 카드를 골라낼 행을 선택할 때 , 이후 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있게 전략 세우기

# 행의개수 n, 열의개수 m 을 공백을 기준으로 입력받기 (1 ~ 100)
n,m = map(int,input().split())

num_list = []
# # 각 카드에 적힌 숫자 입력받기 (1 ~ 10,000). 행의 개수만큼 반복해서 입력받아서 배열에 넣기
for _ in range(n):
  num_list.append(list(map(int,input().split())))

result = 0
for i in range(n):
  max_num = min(num_list[i])
  if result < max_num:
    result = max_num
print(result)

## 풀이
n,m = map(int,input().split())
result = 0

for i in range(n):
  data = list(map(int,input().split()))
  min_num = min(data) # 현재 줄에서 가장 작은 수
  result = max(result, min_num)
print(result)

#### 참고
# input()대신 readline()사용하기
# import sys

# n,m = map(int,input().split())
# num_list = []
# for _ in range(n):
#   read_num = list(map(int,sys.stdin.readline().split()))
#   num_list.append(read_num)
# print(num_list)