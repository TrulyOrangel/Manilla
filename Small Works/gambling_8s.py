""" rules for monte carlo
there are 2 reels that look like this:
- - - - - - - - 8 (1 in 9)
- - - - - - - - - 8 (1 in 10)
If you get an 8, you fill a progress bar for that reel
each progress bar has 8 'slots'
when you get both progress bars full, you win 50 credits
if you overflow a progress bar, you get 10 credits
you can't earn 60 credits in one spin
every spin costs 1 credit
"""
from random import randint
from colorama import Fore, Back, Style

def spin():
    net = 0
    win = False
    reel1 = 0
    reel2 = 0

    while win != True:
        net -= 1
        fillFlag = False

        if randint(1,9) == 8: # upper reel
            reel1 += 1
            if reel1 == 9:
                reel1 = 8
                net += 10
                fillFlag = True
        
        if randint(1,10) == 8: # lower reel
            reel2 += 1
            if reel2 == 9:
                reel2 = 8
                net += 1
                fillFlag = True
        
        if reel1 == 8 and reel2 == 8: # win condition
            if fillFlag == True:
                net -= 10 # cancelling out the overflow bonus
            net += 50
            win = True
    
    return net


## MAIN CODE ##

nets = []

n = int(input("How many games would you like to play? >> "))
print("{:^5} {:^5} {:^5}".format("n", "net", "avg"))
for i in range(n):
    nets.append(spin())

    if nets[i] < 0:
        print("{:^5}".format(i+1),\
             Back.RED+"{:^5}".format(nets[i])+Style.RESET_ALL,\
                 "{:^5.2f}".format(sum(nets)/(i+1)))
    elif nets[i] > 0:
        print("{:^5}".format(i+1),\
             Back.GREEN+"{:^5}".format(nets[i])+Style.RESET_ALL,\
                 "{:^5.2f}".format(sum(nets)/(i+1)))
    else:
        print("{:^5}".format(i+1),\
             Back.WHITE+"{:^5}".format(nets[i])+Style.RESET_ALL,\
                 "{:^5.2f}".format(sum(nets)/(i+1)))

print(Fore.YELLOW+"Average net after "+str(n)+" games was "+str(round(sum(nets)/len(nets),2))+Style.RESET_ALL)
