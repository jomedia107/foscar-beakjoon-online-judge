# 변수들을 입력받는다. 
# A : 쌓이는 피로
# C : 회복되는 피로
# B : 일의 양
# M : 최대 허용 피로도도 

A,B,C,M = map(int, input().split())

curr_tired = 0

time = 0
curr_work = 0
# 만약 한시간 일했을때 현재 피로도가가 최대 허용 피로수치에 도달하지 않았다면
# 한시간 더 일해본다. 
#이과정을 반복하다가 만약 최대 피로도 한계보다 커지면 그때 휴식을 취해준다.

while(True):
  if curr_tired + A <=M:    
    curr_tired += A
    time += 1
    curr_work += B

  else:
    curr_tired -= C
    time += 1
    if curr_tired<0:
      curr_tired = 0
  if time ==24:
    break

print(curr_work)

