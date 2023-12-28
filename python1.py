import turtle
import random

letters =('a','b', 'c','d','e','f','g','h','i','j','k','l', 'm','n', 'o','p', 'q','r', 's','t','u','v','w', 'x', 'z')
lts=[]
pos=[]
game_over = False
score = 0
min_speed = 5
max_speed = 30

screen= turtle.Screen()
screen.setup(1000,1000)
screen.title('typing Game - Developed by David Lee')
screen.bgcolor('#F0F0F8')

screen.tracer(0,0)
turtle.hideturtle()
turtle.up()
turtle.color('red')

score_turtle=turtle.Turtle()
score_turtle.color('red')
score_turtle.up()
score_turtle.hideturtle()
turtle.goto(350,400)
turtle.write('score: ', align='center', font=('Courier', 25, 'normal'))

screen.tracer(0)

t = turtle.Turtle()

t.speed(0)
t.hideturtle()

def increase_difficulty():
    global min_speed, max_speed
    min_speed +=1
    max_speed +=1
    screen.ontimer(increase_difficulty, 5000)

def draw_letters():
    for i in range (len(letters)):
        lts[i].clear()
        lts[i].goto(pos(i))
        if pos[i][1]<-500:
            game_over:True

        screen.update()

def draw_score():
    score_turtle.clear()
    score_turtle.goto(420,400)
    score_turtle.write('{}'.format(score), align='center', font=('Courier', 25, 'normal'))
    screen.update()

def f(c): 
    if c in letters:
        score +=1
        k= letters.index(c)
        while True:
            l = chr(ord('a')+random.randrange(26))
            if l not in letters:
                letters.append(l)


def draw_game_over():
    turtle.goto(0,0)
    turtle.color('red')
    turtle.write('GAME OVER', align='center', font=('Courier', '50', 'normal'))

    turtle.goto(0,-150)
    turtle.color('orange')
    turtle.write('Your Score is {}'.format(score),align='center', font=('Courier'40,'normal'))
    screen.update()

screen.onkey(lambda: f('a'),'a')
screen.onkey(lambda: f('b'),'b')
screen.onkey(lambda: f('c'),'c')
screen.onkey(lambda: f('d'),'d')
screen.onkey(lambda: f('e'),'e')
screen.onkey(lambda: f('f'),'f')
screen.onkey(lambda: f('g'),'g')
screen.onkey(lambda: f('h'),'h')
screen.onkey(lambda: f('i'),'i')
screen.onkey(lambda: f('j'),'j')
screen.onkey(lambda: f('k'),'k')
screen.onkey(lambda: f('l'),'l')
screen.onkey(lambda: f('m'),'m')
screen.onkey(lambda: f('n'),'n')
screen.onkey(lambda: f('o'),'o')
screen.onkey(lambda: f('p'),'p')
screen.onkey(lambda: f('q'),'q')
screen.onkey(lambda: f('r'),'r')
screen.onkey(lambda: f('s'),'s')
screen.onkey(lambda: f('t'),'t')
screen.onkey(lambda: f('u'),'u')
screen.onkey(lambda: f('v'),'v')
screen.onkey(lambda: f('w'),'w')
screen.onkey(lambda: f('x'),'x')
screen.onkey(lambda: f('y'),'y')
screen.onkey(lambda: f('z'),'z')