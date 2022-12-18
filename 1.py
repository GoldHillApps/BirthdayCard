import ybc_sticker
import turtle as t
for i in range(9):
    t.penup()
    t.goto(-325.0,-473.4)
    t.pendown()
    t.write('你好，我是绿芽老师',font = ('sgshg',50))
t.penup()
t.goto(-157.0,106.0)
t.pendown()
t.goto(-157.0,106.0)
t.pendown()
t.write('生日邀请卡',font=('sgshg',42))
t.penup()
t.goto(-177.8,-79.6)
t.pendown()
t.write('地址：绿芽家里',font=('sgshg',40))
for i in range(9):
    ybc_sticker.load('宇宙')
