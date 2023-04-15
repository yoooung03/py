print("환영합니다.")
print("파이썬의 세계로 오신 것을 환영합니다.")
print("파이썬은 강력합니다.")

#%%
print(1+2+3, "을 계산하면",6, "입니다." )

#%%
import turtle
t = turtle.Turtle()
t.shape("turtle")

t.forward(100)
t.left(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

turtle.mainloop()
turtle.bye()

#%%
import turtle
t = turtle.Turtle()

t.width(5)
t.color("blue")
t.shape('square')

t.forward(50)
t.left(90)
t.forward(100)

turtle.mainloop()
turtle.bye()

#%%
runfile('C:/2022!/test3.py', wdir='C:/2022!')
몸무게를 kg 단위로 입력하시오: 85.0
키를 미터 단위로 입력하시오: 1.83
당신의 BMI= 25.381468541909282

#%%
chiken= 2
pig= 3
cow= 4
sum= chiken*2+ pig*4+ cow*4

print("닭의 수:", chiken)
print("돼지의 수:", pig)
print("소의 수:", cow)
print("전체 다리의 수:", sum)