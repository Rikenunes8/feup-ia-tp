import UnequalLengthMazes as ULM
from Algorithms import SearchProblemsAlgorithms, algorithmTypes
import boards

class Analyser:

  def analyse(self, n_heuristics):
    print(n_heuristics)
    f = open("analysis.csv", "w")
    for board in range(len(boards.initBoards)):
      ULM.setInitState(board)
      problem = SearchProblemsAlgorithms(ULM.initState, ULM.isFinalState, ULM.newTransitions)
      for algorithm in algorithmTypes:

        #if (algorithm == "depth_limited"):
          #lowerLimit = self.calculateLowerLimit(boards.initBoards[n])
          #f.write(self.analyseDepthLimit(problem, algorithm, lowerLimit))
        if (algorithm == "greedy" or algorithm == "A*"):
          f.write(self.analyseHeuristics(board, problem, algorithm, n_heuristics))
        elif(algorithm != "depth_limited" and algorithm != "iterative_deepening"):
          problem.run(algorithm)
          f.write(self.getSolutionStatisticsStr(board, problem.getSolution(), algorithm, '-'))

      f.write('\n')
    f.close()
    
  def analyseDepthLimit(self, board, problem, algorithm, lowerLimit):
    resultStr = ""
    for limit in range(lowerLimit, round(lowerLimit*1.5)):
      resultStr += "\n limit " + str(limit) + ": "
      problem.run("depth_limited", limit=limit)
      resultStr += self.getSolutionStatisticsStr(board, problem.getSolution(), algorithm, 0)
    return resultStr

  def analyseHeuristics(self, board, problem, algorithm, n_heuristics):
    resultStr = ""
    for heuristic in range(1, n_heuristics+1):
      problem.run(algorithm, heuristic=heuristic)
      resultStr += self.getSolutionStatisticsStr(board, problem.getSolution(), algorithm, heuristic)
    return resultStr

  def calculateLowerLimit(self, initBoard):
    limit = 0
    for line in range(len(initBoard)):
      limit += initBoard[line].count(0)
    return limit

  def getSolutionStatisticsStr(self, board, solution, algorithm, heuristic):
    (path, depth, nodes, time) = solution
    solutionStatisticsStr = str(board) + "," + algorithm + "," + str(heuristic) + "," + str(time) + "," + str(nodes) + "," + str(depth) + '\n'
    return solutionStatisticsStr


