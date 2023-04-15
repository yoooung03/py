import turtle #turtle 모듈 불러오기
t = turtle.Turtle() #turtle 모듈의 Turtle()함수 실행

t.shape("turtle") #커서 (펜모양)
t.color("red") #펜색

t.forward(566) #앞으로 100 피셀 이동
t.left(90) #왼쪽으로 90도 회전
t.forward(110)
t.left(90)
t.forward(566)
t.right(135)
t.forward(400)
t.right(90)
t.forward(400)
t.right(135)
t.forward(142)
t.right(90)
t.forward(142)
t.left(90)
t.forward(283)
t.left(90)
t.forward(142)
t.right(90)
t.forward(142)
t.left(90)
t.forward(110)
t.circle(60)
t.left(90)
t.forward(566)
t.left(90)
t.circle(60)


turtle.mainloop() #터틀창이 종료될 때까지 입력대기