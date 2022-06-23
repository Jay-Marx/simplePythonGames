import time as t
import pandas as p
import random as r
class item ():
    #item comes first because everything goes back to it
    def __init__(self, name, is_powerup, speed_mult, speed_boost):
        self.name = name
        self.is_powerup = is_powerup
        self.speed_mult = speed_mult
        self.speed_boost = speed_boost
        self.ready = True
        #ensures items are only used once
    def usedFunc (self):
        if self.ready == True  :
    #checks if it has already been used
            self.ready = False
        return 0
    
class racer():
    #racer is next
    def __init__(self, name, start_pos, speed, speed_mult, speed_boost, Item, prfTerrain):
        self.Item = Item
        self.name = name
        self.start_pos = start_pos
        self.speed = speed
        self.speed_mult = speed_mult
        self.speed_boost = speed_boost
        self.terrian = prfTerrain
    def applyItem(self, Item):
        i= self.Item.usedFunc()
        # the i set here is meaningless. The deed is done
        return self.Item.returnSpecialEffect()
    def use_Item (self, opponent):
        if self.Item.is_powerup == False:
            opponent.speed_boost = self.Item.speed_boost +opponent.speed_boost
            opponent.speed_mult = self.Item.speed_mult + opponent.speed_mult
            # if item isnt a powerup, it uses it on the opponent
        elif self.Item.is_powerup == True:
            self.speed_boost = self.Item.speed_boost +self.speed_boost
            self.speed_mult = self.Item.speed_mult + self.speed_mult
 # if it is, then it adds the bonuses to itself
    def calc_race_time(self, Course_length):
        fspeed = (self.speed*self.speed_boost)*self.speed_mult
        return Course_length/fspeed


class course ():
    def __init__ (self, name, length, racers, terrain):
        self.name = name
        self.length = length
        self.racers = racers
        self.terrian = terrain
    def use_Items(self):
        #for list gets the job done
        for i in range(0, len(self.racers)):
            if i < 7:
                self.racers[i].use_Item( self.racers[i+1])
            else:
                self.racers[i].use_Item( self.racers[i-1])
    def calc_Racer_end_pos(self):
        endTimes =[]
        for i in self.racers:
            endTimes.append(i.calc_race_time(self.length))
        return endTimes
    def applyTerrain(self):
        for i in self.racers:
            i.speed = i.speed + h[i.terrian] [self.terrian] #terrain bonus for each. Use a for loop
        # returns a sorted array of end times.
    def run_race(self):
        print('3') # some anticipation always helps
        t.sleep(.5)
        print('2')
        t.sleep(.5)
        print('1')
        t.sleep(.5)
        self.use_Items() #call funciton
        self.applyTerrain() ## apply terrain bonus/effects
        pop =self.calc_Racer_end_pos() # set it to pop
        arr= []
        print(len(pop))
        print(len(self.racers))
        for i in (range(0, 8 )): # 8 racers, then it pushes them out
            arr.append(str(self.racers[i].name) + " Finished At: " + str(pop[i]))
        print(arr)

        
freedone = item('freedone',True, 1, 25)
freed = racer('freed', 8, 200, 20000, 2, freedone, 'Concrete')
# test game
goathoof = item('goat hoof', True, 14,1)
paul = racer('paul', 7, 100, 200, 1,goathoof, 'Concrete')

ssaints = item('ssaints', False, .115, 1)
yonathon = racer('yonathon', 6, 609000, 30, 10, ssaints, 'Sand')
# test game
Bfalcon = item('Blue Falcon', True, 50, -1)
CFalcon = racer('Captain Falcon', 5, 10.50, 20, 10, Bfalcon, 'Water')
# refrences....
wBomb = item('Waluigi Bomb', False, 1, -20)
walouiji = racer('Waluigi', 4, 40, 400,10, wBomb, 'Water')
# test game
it = item('intensity', False, .00001, 1)
aimagase = racer('Ai Magase', 2, 50, 1.5, 10, it, 'Sand')

tooslow = item('You are too SLOW', True, 1, 10)
SONIC = racer('SONIC', 3, 50000000, 500000, 50000, tooslow, 'Water')

hacks = item('wIn? thE gAme?', True, 100000, 1)
hecker = racer('hecker', 1, 100, 100, 1, hacks, 'Concrete')

rockyrockyrocks = course('sweet destiny', 12000, [hecker, SONIC, aimagase, walouiji, CFalcon, yonathon, paul, freed], r.choice(['Concrete', 'Sand', 'Water']))

data = [[15, -15, 0], [0, 15, -15], [-15, 0, 15]]
h= p.DataFrame(data,columns = ['Concrete', 'Sand', 'Water'], index = ['Concrete', 'Sand', 'Water'])
print(h)
rockyrockyrocks.run_race()

