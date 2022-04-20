import re
import UnequalLengthMazes as ULM
from Algorithms import SearchProblemsAlgorithms, algorithmTypes
import boards

class Analyser:

    def analyse(self, n_heuristics):
        f = open("analysis.txt", "w")
        for n in range(len(boards.initBoards)):
            f.write("BOARD %s\n" % n)
            ULM.setInitState(n)
            problem = SearchProblemsAlgorithms(ULM.initState, ULM.isFinalState, ULM.newTransitions)
            for algorithm in algorithmTypes:
                f.write(algorithm + ": ")
                if (algorithm == "depth_limited"):
                    lowerLimit = self.calculateLowerLimit(boards.initBoards[n])
                    for limit in range(lowerLimit, lowerLimit*2):
                        problem.run(algorithm, limit=limit)
                if (algorithm == "greedy" or algorithm == "A*"):
                    for heuristic in range(n_heuristics):
                        problem.run(algorithm, heuristic=heuristic)
                problem.run(algorithm)
                (path, depth, nodes, time) = problem.getSolution() 
                f.write("%s, %s, %s\n" % (time, nodes, depth)) 
            f.write('\n')
        f.close()

    def calculateLowerLimit(self, initBoard):
        limit = 0
        for line in range(len(initBoard)):
            limit += initBoard[line].count(0)
        return limit

