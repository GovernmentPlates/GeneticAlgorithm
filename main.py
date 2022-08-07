from GAFunctions import initPopulation, evalFitness, pickParents, genChildren
from GAConfig import populationSize, parseConfig, currentGen, maximumGens
import csv

parseConfig()
population = initPopulation(populationSize)
fitnesses = []

def average(val):
    return sum(val) / len(val)

def findBestCandidate(fitnesses):
    fitnesses.sort(reverse=False)
    currentBest = fitnesses[0][0]
    return currentBest

def calculateScore(currentBest):
    relErrorComponentA = abs(currentBest - 0)
    relErrorComponentB = relErrorComponentA / 1 + abs(currentBest)
    score = 100 - relErrorComponentB
    return score

while (maximumGens >= currentGen):
    with open('GAOutput.csv', 'a+', newline='') as GAOutput:
        csvOutput = csv.writer(GAOutput, delimiter=',')
        for pop in population:
            csvOutput.writerow(pop)
        csvOutput.writerow("")
    currentGenFitnesses = evalFitness(population)
    fitnesses.append(currentGenFitnesses)
    parents = pickParents(population)
    children = genChildren(parents)
    population = children
    print(f"Current Generation: {currentGen} - Population Fitness Average: {average(currentGenFitnesses)} (Score: {calculateScore(findBestCandidate(fitnesses))}%)")
    currentGen += 1

print(f"*** Best Fitness: {findBestCandidate(fitnesses)} -- Score: {calculateScore(findBestCandidate(fitnesses))}% ***")
