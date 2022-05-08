import math
import turtle

n = input("Introduzca el número de picos de la estrella: ")
while not n.isdigit() or int(n) <= 4:
    n = input("Error. Debe insertar un número mayor de 4: ")
n = int(n)

t = turtle.Turtle()
points = []
a = 360/n

t.penup()
for i in range(n):
    t.forward(100)
    points.append(t.pos())
    t.backward(100)
    t.right(a)

s = turtle.Screen()
ind = 0
t.setposition(points[0][0], points[0][1])
t.pendown()
step = int(n/2) - 1 if n % 2 == 0 else math.floor(n/2)
visited = []
for i in range(n):
    if ind in visited:
        t.penup()
        ind = ind + 1
        t.setposition(points[ind][0], points[ind][1])
        t.pendown()
    visited.append(ind)
    ind = (ind + step) % n
    t.setposition(points[ind][0], points[ind][1])
s.exitonclick()

