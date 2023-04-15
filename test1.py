#문제 1
print("파이썬에 오신 것을 환영합니다")
print("파이썬은 쉽습니다")
print("파이썬으로 빅데이터, 인공지능 프로그램을 작성할 수 있습니다")

#%%
#문제 2
print('2+3=', 2+3)
print('2-3=', 2-3)
print('2*3=', 2*3)
print('2/3=', 2/3)

#%%
#문제 3
import turtle #turtle 모듈 불러오기
t = turtle.Turtle() #turtle 모듈의 Turtle()함수 실행

t.shape("turtle") #커서 (펜모양)
t.color("red") #펜색

t.forward(100) #앞으로 100 피셀 이동
t.left(90) #왼쪽으로 90도 회전
t.forward(50)

turtle.mainloop() #터틀창이 종료될 때까지 입력대기
turtle.bye() #터틀 그래픽 종료

#빨간색 선을 가진 거북이가 'ㄴ' 반대 모양을 민듦

#%%
#문제 4
import turtle
t = turtle.Turtle()
t.shape("turtle")

t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)

turtle.mainloop()
turtle.bye()
