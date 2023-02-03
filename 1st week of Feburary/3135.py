# 첫번째 버튼은 주파수를 1 증가시킴
# 두번째 버튼은 주파수를 1 감소시킨다. 
# 나머지 N개의 버튼은 즐겨찾기 기능으로, 미리 지정된 주파수로 이동한다. 

#최소한의 클릭을 해야한다.

#듣고싶은 주파수 A와 B가 주어질 때

A, B = map(int, input().split())

n = int(input())

arr = []

for i in range(n):
    new = int(input())
    arr.append(new)


count = 0

min_menu = arr[0]

option = 0 
# 주파수 A에서 B로 갈 때 눌러야 하는 가장 적은 버튼수를 구해보자.

#전략

# 즐겨찾기 메뉴와 B사이의 차이가 최솟값일 때 그때의 즐겨찾기 메뉴를 클릭한다.
# 

# 경우 1 : 메뉴를 경유하여 B에 도달할 때 
# 즐겨착기 메뉴의 주파수 - B의 주파수 가 음수이면 두번째 버튼(1씩 증가하는 버튼)을 반복적으로 클릭하여 B에 도달하도록 한다.
# 즐겨찾기 메뉴의 주파수 - B의 주파수가 양수이면 첫번째 버튼(1씩 감소하는 버튼)을 반복적으로 클릭하여 B에 도달하도록 한다.
# 


#경우 2 : 메뉴를 경유하지 않고 B에 도달 할때 
# |A-B|가 |즐겨찾기 - B|보다 작은 경우 첫번째 혹은 두번째 버튼을 통해 직접적으로 바로 이동한다. 

for i in range(n):
    #메뉴 B와 최소거리인 즐겨찾기 탐색
    if abs(arr[i]-B)<abs(min_menu-B):
        min_menu = arr[i]


for i in range(n):
    # A에서 B로 바로 갈지, 즐겨찾기를 경유해서 갈지 파악
    if abs(A-B)<=abs(arr[i]-B):
        option = 0
    else:
        option = 1
        break
       
    
if option ==0:
    count = abs(A-B)
else:
    count = abs(min_menu - B)+1
### 내가 처음에 계속 틀렸던 이유 : for문을 한번에 처리하고 싶어서 두번째 for문을 첫번째 for문에 같이 썻었는데 그럴 경우 option값이 1이 선택되더라도 다음 반복에서 
# option 값이 0으로 변할 수 있다. 때문에 option이 1이 되는 순간 break를 걸어줘야 하는데 이때 for문을 두개를 같이 쓰면 첫번째 for문에서 모든 탐색이 불가능하다.
# 때문에 for문을 두개로 분리하고 두번째 for문에 break를 넣어준다. 



print(count)


