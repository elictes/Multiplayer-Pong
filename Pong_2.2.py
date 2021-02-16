#thank you for checking out my code! Jonas :-)
import time
import turtle
import os
import socket
import sys

#some variables..
ai = 0
MultiMode = 0
name1="Example"
name2="Example"
ccolor = 0
#os clear screen
def Clearscreen():
    os.system("clear" if sys.platform == "linux" else "cls")
#Writen Introduction and Player names
Clearscreen()
print("")
print(" ------------------------------------------------------------------")
print(" Hello fellow Player of Jonas's rocket ship incredible Pong game. ")
print(" ------------------------------------------------------------------")
print("")
time.sleep(2)

while True:
    Clearscreen()
    print("\n MENU\n ----------\n")
    print(" │1. Play")
    print(" │2. Help")
    print(" │3. Settings")
    print(" │4. About\n")
    menu_a = input(" > ")
    Clearscreen()

    if menu_a == "1":
        break
    if menu_a == "2":
        print("\n HELP\n ----------\n")
        print(" The Goal of the Game is to Hit the Ball with your Paddle,\n in a way, that it bounces to the side of your opponent.\n When The Ball reaches space behind your Paddle, your opponent gets a point.\n Try to get as many points as possible. :-)")
        print('\n The Buttons W and S move the Player On The Left Up and Down.\n If you are playing SinglePlayer or Online MultiPlayer you will by default be on the Right side\n If you are playing with a frient on the same PC Player 1 Will be on the Left side,\n and Player 2 will be on the Right side.')
        print(" Anyways enjoy!! :-)\n")
        esc=input(" [Press Enter to Exit]\n")
        
    if menu_a == "3":
        print("\n SETTINGS\n ----------\n")
        print("\n Select your Preffered ball Color:")
        print("\n │1. Red")
        print(" │2. Green")
        print(" │3. Blue\n")
        print(" [Press Enter for no Change]\n")
        menu_b = input(" > ")
        Clearscreen()
        if menu_b == "1":
            ccolor = 0
            print(" -------------------\n You selected RED\n -------------------")
            time.sleep(1)
        if menu_b == "2":
            ccolor = 1
            print(" -------------------\n You selected GREEN\n -------------------")
            time.sleep(1)
        if menu_b == "3":
            ccolor = 2
            print(" -------------------\n You selected BLUE\n -------------------")
            time.sleep(1)
    
    if menu_a == "4":
        print("\n About\n ----------\n")
        print(" Version : 2.1\n Created by Jonas Schröder\n This Patch is from the 16th Febuary 2021\n")
        esc=input(" [Press Enter to Exit]\n")

while True:      
    print("\n PLAY\n ----------\n")
    print(" │1. SinglePlayer")
    print(" │2. 2 Players")
    print(" │3. Multiplayer\n")
    menu_c = input(" > ")
    Clearscreen()
    if menu_c == "1":
        print("\n -------------------\n Starting Game..\n -------------------")
        name1="You"
        name2="Bot"
        ai = 1
        break
    if menu_c == "2":
        name1 = input("\n Name of the Player on the Left side: ")
        name2 = input("\n Name of the Player on the Right side: ")
        Clearscreen()
        print("\n -------------------\n Starting Game..\n -------------------")
        break
    if menu_c == "3":
        Clearscreen()
        print("\n PLAY\n ----------\n")
        print(" │1. Host a Game")
        print(" │2. Join a game\n")
        menu_d = input(" > ")
        Clearscreen()
        if menu_d == "1":
            MultiMode = 1
            name1 = input("\n Your Player Name: ")
            port=int(input("\n Wich Port do you want to Play on? "))
            Clearscreen()
            print("\n -------------------\n Starting Game..\n -------------------")
            break
        if menu_d == "2":
            MultiMode = 2
            name1 = input("\n Your Player Name: ")
            host_ip=(input("\n Enter the IP adress of the Host: "))
            port=int(input("\n Enter the Port of the Host: "))
            Clearscreen()
            print("\n -------------------\n Starting Game..\n -------------------")
            break

time.sleep(0.7)
Clearscreen()
print("Game Output:\n")
time.sleep(0.5)

#Server funktions
if MultiMode == 1:
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print("Your Local IP is: ", ip," \n ")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((ip, port))
    except socket.error as e:
        print(str(e))
    print("Waiting for Player 2...\n")
    s.listen(1)
    conn, addr = s.accept()
    print('Connected to', addr,"\n")
if MultiMode == 2:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host_ip, port))

#Name exchange between Host and Client
if MultiMode == 1:
    data = conn.recv(128)
    name2 = data.decode('utf-8')
    conn.send(bytes(name1,"utf-8"))
    time.sleep(0.7)
if MultiMode == 2:
    s.send(str.encode(name1))
    msg = s.recv(128)
    name2=msg.decode("utf-8")
    time.sleep(0.7)

#Defining Screen
win = turtle.Screen()
win.title("Pong / My first Game")
win.bgcolor("white")
win.tracer(10)

#Up and Down Black Border
up_border = turtle.Turtle()
up_border.speed(0)
up_border.shape("square")
up_border.color("black")
up_border.shapesize(stretch_wid=0.2, stretch_len=40)
up_border.penup()
up_border.goto(0, 303)

down_border = turtle.Turtle()
down_border.speed(0)
down_border.shape("square")
down_border.color("black")
down_border.shapesize(stretch_wid=0.2, stretch_len=40)
down_border.penup()
down_border.goto(0, -303)

#Paddle 1
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("black")
paddle_a.penup()
paddle_a.goto(-375, 0)

#Paddle 2
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("black")
paddle_b.penup()
paddle_b.goto(375, 0)
#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
if ccolor == 0:
    ball.color("red")
if ccolor == 1:
    ball.color("green")
if ccolor == 2:
    ball.color("blue")
ball.penup()
ball.goto(0, 0)
if MultiMode == 0:
    ball.dx = 0.1
    ball.dy = -0.1
if MultiMode == 1:
    ball.dx = 3
    ball.dy = -3
if MultiMode == 2:
    ball.dx = -3
    ball.dy = 3

#Score
score_a = 0
score_b = 0
win_a = 0
win_b = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("{}: 0  ! 0 : 0  !  {}: 0".format(name1, name2), align="center", font=("Arial", 20, "bold"))

#Functions for moving paddles
def paddle_a_up():
    y = paddle_a.ycor()
    y +=20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y -=20
    paddle_a.sety(y)
def paddle_b_up():
    if ai == 0:
        y = paddle_b.ycor()
        y +=20
        paddle_b.sety(y)
    else:
        y = paddle_b.ycor()
        y +=1
        paddle_b.sety(y)
def paddle_b_down():
    if ai == 0:
        y = paddle_b.ycor()
        y -=20
        paddle_b.sety(y)
    else:
        y = paddle_b.ycor()
        y -=1
        paddle_b.sety(y)

#Retry Loop
def retry():
    reetry = input("Do you want to play again? Y/n: ")
    print("")
    if reetry == "Y":
        time.sleep(1.5)
    else:
        turtle.Screen().bye()
roundi = 0

#Main Game Loop
while True:
    while True:
        win.update()
        if score_a == 11:
            score_a = 0
            score_b = 0
            win_a +=1
            roundi +=1
            win.update()
            print("Weeee!! "+name1+" won Round " + str(roundi) + " !!!\n ")
            break
    
        elif score_b == 11:
            score_b = 0
            score_a = 0
            win_b +=1
            roundi +=1
            win.update()
            print("Weeee!! "+name2+" won Round " + str(roundi) + " !!!\n ")
            break
        
        #MultiPlayer
        if MultiMode == 1:
            p1y = paddle_a.ycor()
            p1score=score_a

            data = conn.recv(64)
            p2y_bf = data.decode('utf-8')
            p2y=float(p2y_bf)
            conn.send(bytes(str(p1y),"utf-8"))
            p2y*=-1
            paddle_b.sety(p2y)
        
            data = conn.recv(64)
            p2score_bf = data.decode('utf-8')
            p2score=float(p2score_bf)
            conn.send(bytes(str(p1score),"utf-8"))
            if p2score == score_b:
                pass
            else:
                print("Something isn't right with the connection...")
                break


        if MultiMode == 2:
            p1y = paddle_a.ycor()
            p1score=score_a

            s.send(str.encode(str(p1y)))
            msg = s.recv(128)
            p2y_bf=msg.decode("utf-8")
            p2y=float(p2y_bf)
            p2y*=-1
            paddle_b.sety(p2y)

            s.send(str.encode(str(p1score)))
            msg = s.recv(128)
            p2score_bf=msg.decode("utf-8")
            p2score=float(p2score_bf)
            if p2score == score_b:
                pass
            else:
                print("Something isn't right with the connection...")
                break
    
        #Paddle Border
        win.listen()
        if paddle_a.ycor() > 247:
            paddle_a.sety(247)
        if paddle_a.ycor() < -247:
            paddle_a.sety(-247)
        
        if paddle_b.ycor() > 247:
            paddle_b.sety(247)
        if paddle_b.ycor() < -247:
            paddle_b.sety(-247)

        #Keyboard Control
        win.listen()
        win.onkeypress(paddle_a_up, "w")
        win.listen()
        win.onkeypress(paddle_a_down, "s")
        if ai == 0:
            win.listen()
            win.onkeypress(paddle_b_up, "Up")
            win.listen()
            win.onkeypress(paddle_b_down, "Down")

        #AI,, Well not really an AI just basic code, but AI sounds much cooler.. :-)
        if ai == 1:
            if ball.xcor() > -150:
                if ball.ycor() > paddle_b.ycor():
                    paddle_b_up()
                if ball.ycor() < paddle_b.ycor():
                    paddle_b_down()

        # Ball Move
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 390:
            ball.goto(0, 0)
            time.sleep(0.2)
            ball.dx *= -1
            score_a +=1
            pen.clear()
            pen.write("{}: {}  ! {}:{} !  {}: {}".format(name1, score_a, win_a, win_b, name2, score_b), align="center", font=("Arial", 20, "bold"))

        if ball.xcor() < -390:
            ball.goto(0, 0)
            time.sleep(0.2)
            ball.dx *= -1
            score_b +=1
            pen.clear()
            pen.write("{}: {}  ! {}:{} !  {}: {}".format(name1, score_a, win_a, win_b, name2, score_b), align="center", font=("Arial", 20, "bold"))

            
        #Paddle vs Ball... Who's gonna win?
        if (ball.xcor() > 355 and ball.xcor() < 375) and (ball.ycor() < paddle_b.ycor() +50 and ball.ycor() > paddle_b.ycor() -50):
            ball.setx(340)
            ball.dx *= -1

        if (ball.xcor() < -355 and ball.xcor() > -375) and (ball.ycor() < paddle_a.ycor() +50 and ball.ycor() > paddle_a.ycor() -50):
            ball.setx(-340)
            ball.dx *= -1

    #Final Win Announcement
    if win_a == 3:
        score_a = 0
        score_b = 0
        roundi = 0
        print(name1 +" is a true Hero! because She/He just won " + str(win_a) + ":" + str(win_b) + "\n \nCongratulations!!!!")
        win_a = 0
        win_b = 0
        time.sleep(0.3)
        retry()
    elif win_b == 3:
        score_b = 0
        score_a = 0
        roundi = 0
        print(name2 +" is a true Hero! because She/He just won "+ str(win_b) + ":" + str(win_a) +" \n \nCongratulations!!!!")
        win_a = 0
        win_b = 0
        time.sleep(0.3)
        retry()
