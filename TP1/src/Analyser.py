import re
import UnequalLengthMazes as ULM
from Algorithms import SearchProblemsAlgorithms, algorithmTypes
import boards

class Analyser:

    def analyse(self, n_heuristics):
        f = open("analysis.txt", "w")
        for n in range(len(boards.initBoards)):
            f.write("BOARD %s" % n)
            ULM.setInitState(n)
            problem = SearchProblemsAlgorithms(ULM.initState, ULM.isFinalState, ULM.newTransitions)
            for algorithm in algorithmTypes:
                f.write('\n' + algorithm + ": ")

                if (algorithm == "depth_limited"):
                    lowerLimit = self.calculateLowerLimit(boards.initBoards[n])
                    f.write(self.analyseDepthLimit(problem, lowerLimit))
                elif (algorithm == "greedy" or algorithm == "A*"):
                    f.write(self.analyseHeuristics(problem, algorithm, n_heuristics))
                else:
                    problem.run(algorithm)
                    f.write(self.getSolutionStatisticsStr(problem.getSolution()))

            f.write('\n')
        f.close()
    
    def analyseDepthLimit(self, problem, lowerLimit):
        resultStr = ""
        # for limit in range(lowerLimit, lowerLimit+2):
        for limit in range(lowerLimit, round(lowerLimit*1.5)):
            resultStr += "\n limit " + str(limit) + ": "
            problem.run("depth_limited", limit=limit)
            resultStr += self.getSolutionStatisticsStr(problem.getSolution())
        return resultStr

    def analyseHeuristics(self, problem, algorithm, n_heuristics):
        resultStr = ""
        for heuristic in range(n_heuristics):
            resultStr += "\n heuristic " + str(heuristic) + ": "
            problem.run(algorithm, heuristic=heuristic)
            resultStr += self.getSolutionStatisticsStr(problem.getSolution())
        return resultStr

    def calculateLowerLimit(self, initBoard):
        limit = 0
        for line in range(len(initBoard)):
            limit += initBoard[line].count(0)
        return limit

    def getSolutionStatisticsStr(self, solution):
            (path, depth, nodes, time) = solution
            solutionStatisticsStr = str(time) + ", " + str(nodes) + ", " + str(depth)
            return solutionStatisticsStr


