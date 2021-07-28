# (Simple) Genetic Algorithm
Simple genetic algorithm with Ackley's function optimization.

**Author:** Dominic Hollis (GovernmentPlates) -- Uni Coursework
***

## Running the GA
Make sure that all the files `main.py`, `GAFunctions.py` and `GAConfig.py` are in the same
directory.

Then run `main.py` from your Python CLI -- after a few seconds (depending on your parameters), you should see a GAOutput.csv generated.
The CSV contains the population coordinates, which can then be fed into a program like Excel to produce a graph.

![GAOutput.csv scatter graph](https://github.com/GovernmentPlates/GeneticAlgorithm/blob/main/GAGraph.png)

**IMPORTANT:** Make sure that you are reading the output of the console for any messages.

## Adjusting the parameters of the GA
The script will read from the configuration file called `ga.config`. You can open this file up
in a text editor of your choice and change around the parameters on there.

If this is the first time you are running the script, it will generate a configuration file with default parameters for you. Once it does this, re-run `main.py`.

Example `ga.config` file:
```
populationSize:100
maximumGens:1000
minBoundsSolutionConstraint:-5
maxBoundsSolutionConstraint:5
```

**populationSize** Set's the size of the population (used in generating the population for the first time).

**maximumGens** Set's the maximum number of generations that the GA will go through.

**minBoundsSolutionConstraint** A minimum boundary value (used in generating random numbers).

**maxBoundsSolutionConstraint** A maximum boundary value (used in generating random numbers).

**NOTE:** As per the [university assignment] requirements, the **minBoundsSolutionConstraint** and **maxBoundsSolutionConstraint** must be set at **-5** and **5** (constraints).


## Features Implemented
* Population generation
* Genetic crossover + Mutation
* Child generation
* Ackley function optimization (used in the fitness function)
* Configuration system (innovation?)