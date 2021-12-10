## Malit, Lexter R. ##
## CS - 302 ##
## THIS PROJECT USED A LIBRARY CALLED PYTHON TURTLE FOR THE IMPLEMENTATION OF THE DIGITS IN A DIGITAL CLOCK ##
## TO INSTALL TYPE "pip install PythonTurtle" on your terminal/cmd ##
## P.s if you want to see the individual digits being drawn, remove turtle.tracer(0,0) on line 274 ##

#importing libraries
import turtle
import time
import datetime

#use the library through the use of a variable
lex = turtle.Turtle()

# functions zero,one,two,three,four,five,six,seven,eight,and nine
# will be responsible for drawing the digits.
def zero():
    lex.forward(25)
    lex.pendown()
    lex.left(90)                             
    lex.forward(25)
    lex.left(90)
    lex.forward(25)
    lex.left(90)
    lex.forward(25)
    lex.forward(25)
    lex.left(90)
    lex.forward(25)
    lex.left(90)
    lex.forward(25)
    lex.right(90)
    lex.penup()
    
def one():
    lex.forward(25)
    lex.pendown()
    lex.left(90)
    lex.forward(25)
    lex.penup()
    lex.left(90)
    lex.forward(25)
    lex.left(90)
    lex.forward(25)
    lex.forward(25)
    lex.left(90)
    lex.forward(25)
    lex.left(90)
    lex.pendown()
    lex.forward(25)
    lex.right(90)
    lex.penup()
    
def two():
    lex.pendown()
    lex.forward(25)
    lex.left(90)
    lex.forward(25)
    lex.left(90)
    lex.forward(25)
    lex.left(90)
    lex.penup()
    lex.forward(25)
    lex.pendown()
    lex.forward(25)
    lex.left(90)
    lex.forward(25)
    lex.left(90)
    lex.penup()
    lex.forward(25)
    lex.right(90)
    lex.penup()
    
def three():
    lex.pendown()
    lex.forward(25)
    lex.left(90)
    lex.forward(25)
    lex.left(90)
    lex.forward(25)
    lex.left(90)
    lex.penup()
    lex.forward(25)
    lex.forward(25)
    lex.pendown()
    lex.left(90)
    lex.forward(25)
    lex.left(90)
    lex.forward(25)
    lex.right(90)
    lex.penup()
    
def four():
    lex.pendown()
    lex.forward(25)
    lex.left(90)
    lex.forward(25)
    lex.left(90)
    lex.penup()
    lex.forward(25)
    lex.pendown()
    lex.left(90)
    lex.forward(25)
    lex.penup()
    lex.forward(25)
    lex.left(90)
    lex.forward(25)
    lex.pendown()
    lex.left(90)
    lex.forward(25)
    lex.right(90)
    lex.penup()
    
def five():
    lex.pendown()
    lex.forward(25)
    lex.left(90)
    lex.penup()
    lex.forward(25)
    lex.pendown()
    lex.left(90)
    lex.forward(25)
    lex.left(90)
    lex.forward(25)
    lex.penup()
    lex.forward(25)
    lex.pendown()
    lex.left(90)
    lex.forward(25)
    lex.left(90)
    lex.forward(25)
    lex.right(90)
    lex.penup()
    
def six():
    lex.pendown()
    lex.forward(25)
    lex.left(90)
    lex.penup()
    lex.forward(25)
    lex.pendown()
    lex.left(90)
    lex.forward(25)
    lex.left(90)
    lex.forward(25)
    lex.forward(25)
    lex.left(90)
    lex.forward(25)
    lex.left(90)
    lex.forward(25)
    lex.right(90)
    lex.penup()
    
def seven():
    lex.forward(25)
    lex.pendown()
    lex.left(90)
    lex.forward(25)
    lex.left(90)
    lex.forward(25)
    lex.penup()
    lex.left(90)
    lex.forward(25)
    lex.forward(25)
    lex.left(90)
    lex.forward(25)
    lex.left(90)
    lex.pendown()
    lex.forward(25)
    lex.right(90)
    lex.penup()
    
def eight():
    lex.pendown()
    lex.forward(25)
    lex.left(90)
    lex.forward(25)
    lex.left(90)
    lex.forward(25)
    lex.left(90)
    lex.forward(25)
    lex.forward(25)
    lex.left(90)
    lex.forward(25)
    lex.left(90)
    lex.forward(25)
    lex.right(90)
    lex.penup()
    
def nine():
    lex.pendown()
    lex.forward(25)
    lex.left(90)
    lex.forward(25)
    lex.left(90)
    lex.forward(25)
    lex.left(90)
    lex.forward(25)
    lex.penup()
    lex.forward(25)
    lex.pendown()
    lex.left(90)
    lex.forward(25)
    lex.left(90)
    lex.forward(25)
    lex.right(90)
    lex.penup()


#since the functions zero to nine. doesnt have a integer value in the back end of the program.
#function numbers() will be responsible on assigning the digits on their respective number
def numbers(num):
    if num == '0':
        zero()
    if num == '1':
        one()
    if num == '2':
        two()
    if num == '3':
        three()
    if num == '4':
        four()
    if num == '5':
        five()
    if num == '6':
        six()
    if num == '7':
        seven()
    if num == '8':
        eight()
    if num == '9':
        nine()


#this is the main fucntion of the program, which is responsible on handling the back end of the program.
def clockFunction():
    # calling the datetime library and getting the individual values of a realtime clock
    #all these values are static
    dateTime = datetime.datetime.now()
    year = dateTime.year #returns the value current year as int
    month = dateTime.month #returns the value current month as int 01-12
    day = dateTime.day #returns the value of current day as int(1-30, 1-31, 1-28, 1-29)
    hours = dateTime.hour #returns the value of hour as int 01-24
    minutes = dateTime.minute #value of minute in int 1-60
    seconds = dateTime.second #value of seconds in int 1-60
    dayOfWeek = dateTime.today().weekday()

    #list for displaying daysOfWeek as a string
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


    lex.pencolor("#00D700")
    # this is responsible on creating the window for the program
    screen = turtle.Screen()
    screen.setup(900,500)
    screen.bgcolor("black")
    #lex.speed will have the draw speed of the objects. having it to 0 means its the fastest speed
    lex.speed(0)
    #pensize will determine the thickness of the objects
    lex.pensize(10)
    #hideturtle will hide the arrow following each drawings
    lex.hideturtle()








    
    #main code for computing time
    while True:
        #tracer(0,0) will be repsonsible on making sure that the speed of draw is instant.
        turtle.tracer(0,0)


        #since I use millitary clock. I got to have consistent 2 digit numbers
        #if len(x) < 2. will be responsible on making sure that all my values has 2 digits.
        # ex: instead of having just 2. i will have 02
        seconds = str(seconds)
        if len(seconds) < 2:
            seconds = '0' + seconds
        secondsTens = seconds[0]
        secondsOnes = seconds[1]


        minutes = str(minutes)
        if len(minutes) < 2:
            minutes = '0' + minutes
        minutesTens = minutes[0]
        minutesOnes = minutes[1]

        
        hours = str(hours)
        if len(hours) < 2:
            hours = '0' + hours
        hoursTens = hours[0]
        hoursOnes = hours[1]


        #turtle.update() and lex.clear() will clear the screen on every iteration
        turtle.update()
        lex.penup()
        lex.clear()
 

        #converting objects to int. so it can be used on conditional statements
        seconds = int(seconds)
        minutes = int(minutes)
        hours = int(hours)
        year = int(year)
        month = int(month)
        day = int(day)
        dayOfWeek = int(dayOfWeek)


        #if seconds reaches 60 it will add 1 to minutes, and secondsTens,SecondsOnes == 00 thus letting me go back to 00 on seconds
        #almost same rules were applied on the rest of the conditional statements
        if seconds == 60:
            minutes = minutes + 1
            secondsTens = '0'
            secondsOnes = '0'
            seconds = 0
            
        if minutes == 60:
            minutesTens = '0'
            minutesOnes = '0'
            hours = hours + 1
            minutes = 0

        # if hours reaches 24, it will go back to 00, since that is the end of day or 12:00AM
        # this also handles the main computation for date and day of week
        if hours == 24:
            hours = 0
            day = day + 1
            dayOfWeek = dayOfWeek + 1

        #if dayOfWeek > 6. Then it will return the value of 0 resulting a value of Monday on days[x].
        if dayOfWeek > 6:
            dayOfWeek = 0
            
        #computation for months that has 31 days on them, except december
        if  day == 32  and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10):
            day = 1
            month = month + 1
            
        #computation for months that has 30 days on them
        if  day == 31 and (month == 4 or month == 6 or month == 9 or month == 11) :
            month = month + 1
            day = 1

        # coomputation of the month of february during leap year
        if day == 30 and month == 2 and (year % 400 == 0 or year % 4 == 0):
            day = 1
            month = month + 1

        #computation of month of february(non leap-year)
        if day == 29 and month == 2 and year % 4 != 0:
            day = 1
            month = month + 1

        #computation of month of december. if day > 31, it means it will come back to month 1(january) and add +1 to year.
        if day == 32 and month == 12:
            day = 1
            month = 1
            year = year + 1


        # this will print everything that is happening inside the window
        lex.goto(-200,0)
        numbers(hoursTens)        
        lex.goto(-150,0)
        numbers(hoursOnes)
        
        lex.goto(-103,-50)
        lex.write(":".zfill(1),font=("Arial", 75, "bold"))

        lex.goto(-50,0)
        numbers(minutesTens)
        lex.goto(0,0)
        numbers(minutesOnes)
        
        lex.goto(47,-50)
        lex.write(":".zfill(1),font=("Arial", 75, "bold"))

        lex.goto(100,0)
        numbers(secondsTens)
        lex.goto(150,0)
        numbers(secondsOnes)

        lex.goto(-180,-75)
        lex.write(str(month).zfill(2) + " - " + str(day).zfill(2) + " - " + str(year).zfill(2), font=("Arial", 20, "bold"))

        lex.goto(25,-75)
        lex.write(str(days[dayOfWeek]).zfill(len(days[dayOfWeek])),font=("Arial", 20, "bold"))
        #time.sleep will be responsible on updating everything every 1 second. time.sleep(seconds)
        #seconds+=1 so that the value of the seconds keep iterating every 1 second thus making the flow of time possible
        time.sleep(1)
        seconds +=1
        


#calling the clockFunction() and turtle.done() means that you are done using the library.
clockFunction()
turtle.done()







