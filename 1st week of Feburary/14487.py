# 주어진 데이터들은 지금 현재 위치로 부터 각각의 마을까지 도달하는데 드는 비용을 의미한다. 

# 그렇다면 최대 비용이 드는 지역만 빼고 모두 더하면 된다. (최대 비용이 드는 길만 제외하고 한바퀴 돌면 된다.)


n = int(input())

data = list(map(int,input().split()))

min_distance = 0

max_money = 0

for i in data:
  min_distance += i

for i in data:
  if i>max_money:
    max_money = i

print(min_distance - max_money)
