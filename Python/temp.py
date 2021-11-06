import math
import random as ra
import turtle


class TurtleBoy:

    '''
    TurtleBoy is the turtle object with a 'gene sequence' of moves and a color
    Dont change the default values of the arguments taken by the __init__ function, they are used for inheritance
    from parents
    moves: array of moves, the 'genes'
    color: color of turtle to keep track of dominant 'species'
    mutated: boolean to say whether the turtle has a mutated sequence from its parents, if so it is a new 'species'
    '''

    def __init__(self, moves=None, color=None, mutated=False):
        self.mutated = mutated
        self.fitness = 0
        self.turtle = turtle.Turtle()
        self.turtle.speed("fastest")
        self.setp(0, -200)
        if moves is None:
            self.moves = [0] * 200  #on first creation populates moves with random movements
            for i in range(len(self.moves)):
                self.moves[i] = ra.randrange(-80, 80) #includes negative values so it  can go backwards and turn right as well
        else:
            self.moves = moves
        if color is not None and not mutated:   #logic to set color for turtle
            self.turtle.pencolor(color)
        elif color is not None:
            self.randrange = ra.randrange(0, 10)    #makes it so if the turtle is mutated is has a 1/10 chance to take a new color
            ran = self.randrange
            if ran == 0:
                self.turtle.pencolor((float(ra.randrange(0, 100)) / 100, float(ra.randrange(0, 100)) / 100,
                                      float(ra.randrange(0, 100)) / 100))
            else:
                self.turtle.pencolor(color)
        else:   #if no color is passed generate a new random color for turtle
            self.turtle.pencolor((float(ra.randrange(0, 100)) / 100, float(ra.randrange(0, 100)) / 100,
                                  float(ra.randrange(0, 100)) / 100))

    def moveit(self, x, y):
        '''function to move the turtle using its random genome, i hardcorded the obstacles coordinates so
        thats the if statement that stops it from moving if it hits the obstacle, change the coordinates if you change
        the obstacle'''
        move = 1    #check to see if the turtle can move
        hit = 0
        for i in range(0,len(self.moves) - 1,2):    #iterates the move array by 2, because it moves and then turns in the same loop
            self.turtle.forward(self.moves[i] * move)   #multiplicative so if move = 0 the turtle has 'crashed'
            self.turtle.left(self.moves[i + 1] * move)  #^^^
            self.posx, self.posy = self.turtle.position()
            if (self.posy > -20 and self.posy < 100) and (self.posx > -150 and self.posx < 150):
                move = 0    #if the turtle has hit the obstacle set move to 0 so it has 'crashed'
            if (self.posx>x-20 and self.posx<x+20) and (self.posy> y-20 and self.posy<y+20):    #it 'hits' the target
                hit = 1
                move = 0
        self.pos = self.turtle.position()   #sets turtles final position to evaluate fitness
        if move == 1:   #this logic is so if the turtle has crashed its fitness decreases
            self.evaluateFitness(x, y)
        elif move == 0 and hit == 0:
            self.posx+=10000
            self.posy+=10000
            self.evaluateFitness(x, y)    #increasing distance to decrease fitness
        elif hit == 1 and move == 0:    #if it hit then increase the fitness
            self.posx = x + (self.posx-x)/2
            self.poxy = y + (self.posy-y)/2
            self.evaluateFitness(x,y)


    def setp(self, x, y):
        '''this is just an interface between the TurtleBoy object and turtle import'''
        self.turtle.up()
        self.turtle.setpos(x, y)
        self.turtle.down()
        self.pos = (x, y)

    def evaluateFitness(self, x, y):
        '''evaluates fitness as a function of distance from the target'''
        x = math.sqrt((self.posx - x) ** 2 + (self.posy - y) ** 2)
        self.fitness = (1 / x) * 100    #fitness function
        if self.posy>100:   #encourages turtles to get beyond the height of the box
            self.fitness *= 1.05
        elif self.posy<-20: #discourages turtles that spin around and do nothing
            self.fitness *=.95
        elif x < 70: #if the turtle is within 50 pixels of the target
                                                    # its fitness increases by 10%
            self.fitness = self.fitness * 1.1

    def crossover(self, p2):
        '''This is the 'reproduction' it takes genes from 2 partners and has a 50% chance of picking partner 1's dna
        for eadch move, 49% for partner 2, and a 1% chance of mutating each move'''
        mutated = False
        color = None
        newmoves = []
        chance = len(self.moves)    #chance for the new array to be populated with selfs dna vs p2, based off %
        count = 0
        for i in self.moves:
            rand = ra.randrange(0, len(self.moves) * 2)
            if rand < chance:   #if the random value is less than chance the new move will be selfs move
                newmoves += [i]
                color = self.turtle.pencolor()
            elif rand > chance and rand < ((len(self.moves) * 2) - (len(self.moves) //100)):    #threshold for p2 vs mutation
                newmoves += [p2.moves[count]]
                color = p2.turtle.pencolor()
            else:   #if the value is < chance and < 99% of 100%, mutate
                mutated = True
                newmoves += [ra.randrange(-120, 120)]
            count += 1
        return (newmoves, color, mutated)

    def __str__(self):
        return "Turtle fitness:" + str(self.fitness) + "color: " + str(self.turtle.pencolor())


def obs():
    '''just a random definition to set the obstacle visual'''
    obs = turtle.Turtle()
    obs.up()
    obs.setpos(0, -20)
    obs.width(20)
    obs.pencolor('red')
    obs.setpos(-150, -20)
    obs.down()
    obs.fillcolor('red')
    obs.begin_fill()
    obs.setpos(-150,100)
    obs.setpos(150, 100)
    obs.setpos(150,-20)
    obs.setpos(-150, -20)
    obs.end_fill()



class TurtleSpecies:

    '''
    target: where the turtles are heading to
    win: turtle.Screen() uses to adjust the update rate
    pop: population of turtles
    iter: iterations or 'generations' of turtles before it stops
    '''

    def __init__(self, target, win, pop, iter):
        '''Init of the turtle species sim, runs for x iterations, and has a populatiwon of x turtles'''
        self.iter = iter
        self.win = win
        self.targetx, self.targety = target
        self.turtlePop = [0] * pop
        for i in range(len(self.turtlePop)):
            self.turtlePop[i] = TurtleBoy()

    def target(self):
        '''definition to set the target visual and position in the species sim'''
        targett = turtle.Turtle()
        targett.up()
        targett.setpos(self.targetx, self.targety)
        targett.down()
        targett.width(30)
        targett.color('green')
        targett.circle(10)

    def evaluate(self, t, b):
        '''evaluates if a turtle is 'fit enough' to reproduce randomly, if it is returned and breeds, decreases fitness as
        reproducing decreases fitness for more genetic diversity'''
        c = ra.randrange(0, b // 2)
        for i in t:
            if i.fitness * 100 > b:
                i.fitness -= i.fitness/10
                return i

    def breed(self):
        '''function to create the next 'generation' takes the current population and loops through it until a new array
        of the same size is filled, for each loop it evaluates the fittest member using 'best' and each time it loops through the array
        'best' decrements so the threshold for fitness decreases'''
        best = 200
        newPop = []
        self.win.tracer(10000, 1)   #sets window speed to make it faster

        while len(newPop) < len(self.turtlePop):    #runs until the array is the same length at the old population
            partner1 = self.evaluate(self.turtlePop, best)  #picks parter 1 for reproducing
            partner2 = self.evaluate(self.turtlePop, best)  #picks partner2
            if (partner1 and partner2 != None): #makes sure they are actual objects, because sometimes evaluate() returns None
                                                                                    #if no turtles meet the criteria
                moves, color, mutated = partner1.crossover(partner2)    #sexy time
                child = TurtleBoy(moves, color, mutated)    #creates a new turtle object based on the genes in crossover
                newPop += [child]   #adds child to the new population
            else:
                best -= 1   #if nothing is returned, decrement best because the threshold is too high
        self.turtlePop = newPop #set the array to the new population, the old turtles died :(

    def run(self):
        '''main loop for running the sim, sets the obstacle and target then runs the methods for x iterations
        prints max fitness, average, and iteration # for each iteration'''
        obs()
        self.target()
        x = 0
        while x < self.iter:
            for i in self.turtlePop:
                self.win.tracer(1000, 1)
                i.moveit(self.targetx, self.targety)
            max, average = self.maxFitness()
            print("Iteration: " + str(x + 1) + " of " + str(self.iter) + " Max: " + str(
                round(max * 100, 1)) + " Average: " + str(round(average * 100, 1)) + "")
            if x < self.iter - 1:
                self.win.clear()
            self.breed()
            x += 1
            self.win.tracer(10, 1)
            self.target()
            obs()
        self.win.exitonclick()

    def maxFitness(self):
        '''function to get the max fitness and average fitness of each generation'''
        max = 0
        average = 0
        for i in self.turtlePop:
            if i.fitness > max:
                max = i.fitness
                average += i.fitness
        return (max, average / len(self.turtlePop))

    def getTarget(self):
        return self.target()


def main():
    target = (0, 200)
    win = turtle.Screen()
    win.tracer(1000, 1)
    sim = TurtleSpecies(target, win, 100, 200)
    sim.run()


if __name__ == "__main__":
    main()
