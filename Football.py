# John Schindler's Final Project
# This is a Football game
import random
import numpy

def callPlay(a,ty):
    print('')
    play = input('Would you like to run or pass? ') # Asks user to call a play
    if a==1: # If user selects run based team
        if play == 'run':
            Yards = int(random.lognormvariate(1.5,1.5))-1 # Generates run yards. Distribution favors longer runs
            if Yards>=80-ty:
                Yards=80-ty
            print(Yards,'yard gain')
            return Yards
        else:
            comp=numpy.random.binomial(1,.4) # Used to determine whether pass is completed
            if comp==1:
                Yards = int(random.lognormvariate(1,1)) # Generates pass yards. Distribution less favorable to pass
                if Yards>=80-ty:
                    Yards=80-ty
                print(Yards,'yard gain')
            else:
                print('Incomplete pass.')
                Yards=0
            return Yards
    if a==2: # If user selects pass based team
        if play == 'run':
            Yards = int(random.lognormvariate(0.5,2))-1 # Generates run yards. Distribution is less favorable to run.
            if Yards>=80-ty:
                Yards=80-ty
            print(Yards,'yard gain')
            return Yards
        else:
            comp=numpy.random.binomial(1,.6) # Used to determine whether pass is completed. Greater chance of completion
            if comp==1:
                Yards = int(random.lognormvariate(2,1)) # Generates pass yards. Distribution favors longer passes
                if Yards>=80-ty:
                    Yards=80-ty
                print(Yards,'yard gain')
            else:
                print('Incomplete pass.')
                Yards=0
            return Yards
    if a==3: # If user selects balanced team
        if play == 'run':
            Yards = int(random.lognormvariate(1,1.7))-1 # Run yards distribution is between run and pass based team
            if Yards>=80-ty:
                Yards=80-ty
            print(Yards,'yard gain')
            return Yards
        else:
            comp=numpy.random.binomial(1,.5) # Chance of completion is between run and pass based teams
            if comp==1:
                Yards = int(random.lognormvariate(1.5,1)) # Pass yards distribution is between run and pass based teams
                if Yards>=80-ty:
                    Yards=80-ty
                print(Yards,'yard gain')
            else:
                print('Incomplete pass.')
                Yards=0
            return Yards
        
def football(ty,d,yardline,tg):
    Yards=callPlay(a,ty) # Calls a play
    tg -= Yards # Calculates yards to go
    if tg <= 0: # In case of first down
        ty += Yards
        yardline=20+ty
        if yardline<=50: # for yardline on your side of field
            print('Congratulations, you got a 1st down. It is now first down with 10 yards to go.')
            print('You are now on your',yardline, 'yard line.')
        else: # for yardline on opponents side of field
            if yardline>=100: # In case of touchdown
                print('Congratulations!')
            elif yardline>=90: # In case of goal to go
                displayline=100-yardline
                print('First down. Goal to go from the',displayline,'.')
            else:
                displayline=100-yardline
                print('Congratulations, you got a 1st down. It is now first down with 10 yards to go.')
                print('You are now on the opponents',displayline, 'yard line.')
        d=1 # resets down to 1
        tg=10 # resets yards to go to 10
    else: # If not a first down
        ty += Yards # calculates total yards
        yardline=20+ty # calculates yard line
        if yardline<=50:
            print('You are now on your',yardline, 'yard line.')
        else:
            if yardline>=100:
                print('')
            else:
                displayline=100-yardline
                print('You are now on the opponents',displayline, 'yard line.')
        d +=1 # adds to down counter
        if d==2:
            print('Its second down and',tg,'yards to go.')
        if d==3:
            print('Its third down and',tg,'yards to go.')
        if d==4:
            print('Its fourth down and',tg,'yards to go.')
            print('Choose your next play wisely.  If you do not get a first down, you will lose the game.')
    if ty<80 and d<5: # If not first down or touchdown
        football(ty,d,yardline,tg) # calls another play
    if ty<80 and d==5: # If turnover on downs
        print('Sorry. You lost.')
        again=input('Do you want to try again? ') # Asks user if they want to play again
        if again=='yes':
            football(0,1,20,10)
        else: # ends game
            print('Thanks for playing.  Hope you enjoyed the game.  Redskins rule!')
    if ty>=80: # If touchdown
        print('You scored a touchdown! You won the game!')
        again=input('Do you want to try again? ')
        if again=='yes':
            football(0,1,20,10)
        else:
            print('Thanks for playing.  Hope you enjoyed the game.  Redskins rule!')
    
print('This program simulates a sudden death overtime situation in a football game.')
print('You start the game on your own 20 yard line with the ball.')
print('You have to select whether to run or pass on each play.')
print('If you can gain 80 yards without turning the ball over on downs, you score a touchdown and win the game.')
print('Good Luck!')      
print('')
print('You get to select what kind of team you are.') # User can choose what playstyle they want to have
team=input('Do you want to be a run first team, a pass first team, or a balanced team? (Enter "run" ,"pass" ,or "balanced")')
if team=='run':
    a=1
elif team=='pass':
    a=2
elif team=='balanced':
    a=3
else: # If user enters something besides options given
    a=3
    print('You made a selection I did not understand. I will assume you want to be a balanced team.')
d = 1
ty = 0
tg=10
yardline=20
print('First down and 10 yards to go')
football(ty,d,yardline,tg) # Runs the game