#%%
def print_msg(name):
    print("안녕하세요?")
    print(f"{name}님의 생일을 축하드립니다.")
    print()
name_List=["손흥민","이강인","조규성","김영권","황인범범"]
for i in name_List:
    print_msg(i)

#%%
def get_area(radius):
    area=3.14*radius*2
    return area
    print(get_area(5))
    r=int(input("반지름"))
    print(f"반지름={r} 원의 넓이={get_area(r)}")
# %%
def get_input():
    return 2,3

x,y= get_input()
# %%
def main():
    result=get_area(3)
    print("반지름이 3인 원의 면적=", result)

def get_area(radius):
    area=3.14*radius**2
    return area

main()
# %%
def main():
    print(f"20cm 피자 2개의 면적:{get_area(20)+get_area(20)} ")
    print(f"30cm 피자 1개의 면적:{get_area(30)}")

def get_area(radius):
    if radius>0:
        area=3.14*radius**2
    else:
        area=0
    return area
main()
#원의 면적 계산
#radius 원의 반지름
#return 원의 면적

#%%
def get_area(radius):
    if radius>0:
        area=3.14*radius**2
    else:
        area=0
    return area

result_1=get_area(20)
result_2=get_area(30)

print(f"20cm 피자 2개의 면적:{result_1*2}")
print(f"30cm 피자 1개의 면적: {result_2}")


# %%
def get_sum(start,end):
    sum=0
    for i in range(start,end+1):
        sum+=i
    return sum
result = get_sum(1,10)
print(f"1~10까지의 합={result}")

# %%
def get_sum(start,end):
    sum=0
    for i in range(start,end+1):
        sum+=i
    return sum

x=get_sum(1,10)
print('1~20d의 합')
y=get_sum(1,10)
result = get_sum
print(f"1~10까지의 합={result}")

#%%
def set_radius(radius):
    radius=100
    return
r= 20
set_radius(r)
print(r)
# %%
def greet(name,msg):
    print(f"안녕 {name},{msg}")
greet("철수","좋은 아침!")
# %%
def print_nums(a,b,c):
    print(a,b,c)
print()
# %%
def personal_info(name,age,adress):
    print('이름:', name)
    print('나이:', age)
    print('주소:', adress)
personal_info(age=30, adress='ChunCheon',name='son')
# %%
