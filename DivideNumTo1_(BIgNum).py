# 3번. 1이 될때까지 (n이 큰수 인 경우)

# <sol>
# n을 k로 많이 나눌수록 n이 많이 줄어들어서 1로 만들 때 필요한 연산 횟수가 줄어드니까 최대한 많이 나눠 !

n, k = map(int, input().split())
cnt = 0

while n>=k: # 무한 반복문 -> 탈출 조건 : n<k 일 때!
  # n이 k로 나누어 떨어지는 수가 될 때 까지 -1을 해준다. 그 횟수를 먼저 계산해주기
  target = (n // k) * k
  cnt += (n-target) # n-target 만큼 -1을 반복해줘야 하니까
  n = target

  # k로 나누어 떨어지지 않는다면 break
  n //= k
  cnt += 1

# 마지막으로 남은 수에 대하여 1씩 빼주기
cnt += (n-1)
print(cnt)