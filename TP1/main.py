from SearchProblem import SearchProblemsAlgorithms
import UnequalLengthMazes as ULM

if __name__=='__main__':
  problem = SearchProblemsAlgorithms(ULM.initState, ULM.isFinalState, ULM.newTransitions)
  # problem.run("iterative_deepening")
  # problem.run("depth")
  problem.run("breadth")