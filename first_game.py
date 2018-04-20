import sys
import os
import cmd
import pygame,textwrap,random,time
import osinterface
from datetime import datetime, timedelta
#get new date code
"""from datetime import datetime, timedelta
s = '2017/1/20'
date = datetime.strptime(s, "%Y/%m/%d")
modified_date = date + timedelta(days=7)
datetime.strftime(modified_date,"%Y/%m/%d")
print(modified_date)
"""
#demo election class info + datetime code
"""

from datetime import datetime, timedelta
class election:

    def __init__(self,resistcandidate,antiresistcandidate,place,date):
        self.resistcandidate = resistcandidate
        self.antiresistcandidate = antiresistcandidate
        self.place = place
        self.date = date

    def electioninfo(self):
        return '{} {} {} {}'.format(self.resistcandidate,self.antiresistcandidate,self.place,self.date)
#election_1 = election('Conor Lamb','Rick Saccone','PA-18 CD','3.13.2018')
#print(election_1.electioninfo())



s = '2017/1/27'
x = '2017/1/20'
date = datetime.strptime(s, "%Y/%m/%d")
date2 = datetime.strptime(x, "%Y/%m/%d")

for i in range(0,7):
    modified_date = date + timedelta(days=-1)

    if (modified_date == date):
        break

    datetime.strftime(modified_date,"%Y/%m/%d")
    print(modified_date)
    modified_date = modified_date
    date = modified_date


"""
#intro quotes
"""class specialelection():
    pass"""
quotes = ['It is easier to resist at the beginning than at the end. - Leonardo Da Vinci','People get used to anything. The less you think about your oppression, the more your tolerance for it grows. After a while, people just think oppression is the normal state of things. But to become free, you have to be acutely aware of being a slave. - Assata Shakur','I believe in the resistance as I believe there can be no light without shadow; or rather, no shadow unless there is also light. - Margaret Akwood','[I]f you do not resist the apparently inevitable, you will never know how inevitable the inevitable was. - Terry Eagleton']
osinterface.clear()

pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()

class election:

    def __init__(self,resistcandidate,antiresistcandidate,place,date):
        self.resistcandidate = resistcandidate
        self.antiresistcandidate = antiresistcandidate
        self.place = place
        self.date = date

    def electioninfo(self):
        return '{} {} {} {}'.format(self.resistcandidate,self.antiresistcandidate,self.place,self.date)

election1 = election("Grace Meng","Daniel Maio","NY-6","11.8.2016")
election1 = election1.electioninfo()
election2 = election("Conor Lamb","Rick Saccone","PA-18","2.13.2018")
election2 = election2.electioninfo()
electionhold = [election1,election2]
"""def endthemusic():
    pygame.mixer.music.stop()
global endit = endthemusic()
"""
class actuallyresist(cmd.Cmd):
    prompt = '\n> '

    # The default() method is called when none of the other do_*() command methods match.
    def default(self, arg):
        print('That is an invalid resistance action. Type "help" for a list of commands.')

    # A very simple "quit" command to terminate the program:
    def do_quit(self, arg):
        """Quit the game."""
        return True # this exits the Cmd application loop in cmdloop()
    def do_viewelection(self,arg):
        print(electionhold)
    def help_viewelection(self):
        print("This method allows you to view upcoming elections in which you can deliver aid to the candidate of your choice")
    def help_endmusic(self):
        print("The developer ran into issues trying to implement this method please try again later")
    def do_endmusic(self):
        pass



x= 100
number = random.randint(1,4)
if number == 1:
    for line in textwrap.wrap(quotes[0],x):
        print(line)
elif number == 2:
    for line in textwrap.wrap(quotes[1],x):
        print(line)
elif number == 3:
    for line in textwrap.wrap(quotes[2],x):
        print(line)
elif number == 4:
    for line in textwrap.wrap(quotes[3],x):
        print(line)
time.sleep(10)
osinterface.pause()
#intro and tutorial
try:
    pygame.mixer.music.load('trump_swear_in.wav')
    pygame.mixer.music.play(1)
except:
    sys.exit(1)
time.sleep(46)
try:
    pygame.mixer.music.load('new_direction.wav')
    pygame.mixer.music.play(-1)
except:
    sys.exit(1)
name = input("Please enter your name:")
intro1 = "Hello you "
intro2 = " have been selected to head the anti-Trump resistance campaign, in your capacity as head of the resistance you will control how we respond to measures by the evil president who conspired with the Russians against America to win the election.We wish you luck.Remember Resist till your last breath"
realintro = intro1 + name + intro2
for line in textwrap.wrap(realintro,x):
    print(line)
actuallyresist().cmdloop()