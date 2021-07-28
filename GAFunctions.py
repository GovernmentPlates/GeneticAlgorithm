import random
import math as mt
from GAConfig import populationSize, minMutationRate, maxMutationRate, minSolutionConstraint, maxSolutionConstraint

def ackleyFitnessFunc(x, y):
    ackleyComponentA = -0.2 * mt.sqrt(0.5 * (x*x + y*y))
    ackleyComponentB = 0.5 * (mt.cos(2 * mt.pi * x) + mt.cos(2 * mt.pi * y))
    fitness = (-20 * mt.exp(ackleyComponentA)) - mt.exp(ackleyComponentB) + mt.exp(1) + 20
    return fitness

def initPopulation(popSize):
    initialPopulation = []
    count = 0
    while count < popSize:
        individual = [0, 0]
        individual[0] = random.uniform(minSolutionConstraint, maxSolutionConstraint)
        individual[1] = random.uniform(minSolutionConstraint, maxSolutionConstraint)
        initialPopulation.append(individual)
        count += 1
    return initialPopulation

def evalFitness(population):
    fitnesses = []
    for i in range(populationSize):
        fitness = ackleyFitnessFunc(population[i][0], population[i][1])
        fitnesses.append(fitness)
    return fitnesses

def pickFirstParent(selection):
    firstParentRandom = random.choice(selection)
    return firstParentRandom

def pickSecondParent(selection):
    secondParentRandom = random.choice(selection)
    return secondParentRandom

def calcParentFit(parent):
    parentFit = abs(ackleyFitnessFunc(float(parent[0]), float(parent[1])))
    return parentFit

def pickParents(population):
    parents = []
    for k in range(populationSize):
        firstParent = pickFirstParent(population)
        secondParent = pickSecondParent(population)
        firstParentFit = calcParentFit(firstParent)
        secondParentFit = calcParentFit(secondParent)
        if secondParentFit < firstParentFit:
            parents.append(secondParent)
        else:
            parents.append(firstParent)
    return parents

def genRandCoors(min, max):
    randCoors = random.uniform(min, max)
    return randCoors

def crossoverFunc(randSelectedFirstParent, randSelectedSecondParent):
    if random.randint(0, 1):
        childXCoors = randSelectedFirstParent[0]
        childXCoors += genRandCoors(minMutationRate, maxMutationRate)
        childYCoors = randSelectedSecondParent[1]
        childYCoors += genRandCoors(minMutationRate, maxMutationRate)
        child = [childXCoors, childYCoors]
    else:
        childXCoors = randSelectedFirstParent[1]
        childXCoors += genRandCoors(minMutationRate, maxMutationRate)
        childYCoors = randSelectedSecondParent[0]
        childYCoors += genRandCoors(minMutationRate, maxMutationRate)
        child = [childXCoors, childYCoors]
    return child

def genChildren(parents):
    children = []
    count = 0
    while count < populationSize:
        randSelectedFirstParent = pickFirstParent(parents)
        randSelectedSecondParent = pickSecondParent(parents)
        child = crossoverFunc(randSelectedFirstParent, randSelectedSecondParent)
        children.append(child)
        count += 1
    return children