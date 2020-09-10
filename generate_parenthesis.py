    def generateParenthesis(self, n: int) -> List[str]:
        solution = []
   
        def backtrack(combination, left, right):
            if len(combination) == 2*n:
                solution.append(combination)
                return
            else:
                if left < right:
                    backtrack(combination + ")", left, right-1)
                if left > 0:
                    backtrack(combination+ "(", left-1, right)
             

        backtrack("", n, n)
        return solution
