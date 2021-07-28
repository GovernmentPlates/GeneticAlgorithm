import os.path

def checkConfig():
    if os.path.isfile('ga.config'):
        return True
    else:
        return False

def genConfig():
    configFile = open('ga.config', 'w+')
    configFile.write("populationSize:100\rmaximumGens:1000\rminBoundsSolutionConstraint:-5\rmaxBoundsSolutionConstraint:5")
    configFile.close()
    print('Generated default config file - please re-run this script')
    exit(0)

def parseConfig():
    if checkConfig() is True:
        configuration = {}
        with open('ga.config', 'r') as configFile:
            for line in configFile:
                fields = line.split(':')
                if len(fields) == 2:
                    configuration[fields[0].strip()] = int(fields[1])
        print('Config file found - values loaded: ' + str(configuration))
        return configuration
    elif checkConfig() is False:
        print('Config file was not found - Generating...')
        genConfig()

config = parseConfig()

populationSize = config['populationSize']
maximumGens = config['maximumGens']
minSolutionConstraint = config['minBoundsSolutionConstraint']
maxSolutionConstraint = config['maxBoundsSolutionConstraint']
minMutationRate = config['minBoundsSolutionConstraint'] / config['maximumGens']
maxMutationRate = config['maxBoundsSolutionConstraint'] / config['maximumGens']

currentGen = 0