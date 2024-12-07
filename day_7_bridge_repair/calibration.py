from dataclasses import dataclass, field
from typing import Callable, Literal

from parser.file_parser_2 import FileParser
from parser.parser import ParserInterface


type OperationSign = Literal['+', '*']
type OperationFunction = Callable[[int, int], int]


@dataclass
class Operation:
    sign: OperationSign
    operator: OperationFunction

@dataclass
class Problem:
    result: int = 0
    numbers: list[int] = field(default_factory=list)
    
    
@dataclass
class Solution:
    problem: Problem = None
    result: int = None
    operations: list[Operation] = field(default_factory=list)
    
    
class Solver(ParserInterface):
    def __init__(self):
        self.operations: list[Operation] = [
            Operation(sign = '+', operator = self.add),
            Operation(sign = '*', operator = self.multiply),
        ]
        self.base = len(self.operations)
        
        self.problems: list[Problem] = []
    
    def parse_line(self, line: str):
        result_str, numbers_str = line.split(':')
        number_str_list = numbers_str.strip().split(' ')
        
        self.problems.append(Problem(
            result = int(result_str),
            numbers = [int(number) for number in number_str_list]
        ))
    
    
    def add_operation(self, operation: Operation):
        self.operations.append(operation)
        self.base = len(self.operations)
        
        
    def multiply(self, a: int, b: int) -> int:
        return a * b
    
    
    def add(self, a: int, b: int) -> int:
        return a + b
    
    def concatenate(sel, a: int, b: int) -> int:
        return int(str(a) + str(b))
    
    
    def try_solve(self) -> list[Solution]:
        solutions: list[Solution] = []
        
        for problem in self.problems:
            solution_found = False
            
            for i in range(self.base ** (len(problem.numbers) - 1)):
                i_base = self.number_to_base(i, self.base, len(problem.numbers) - 1)
                operations = self.based_to_operations(i_base)
                solution = self.solve(problem, operations)
                
                if solution.result == problem.result:
                    self.print([solution])
                    solutions.append(solution)
                    solution_found = True
                    break
                
            if solution_found:
                continue
                    
        return solutions
    
    
    def based_to_operations(self, based: list[int]) -> list[Operation]:
        return [self.operations[i] for i in based]
    
    
    def solve(self, problem: Problem, operations: list[Operation]) -> Solution:
        result = problem.numbers[0]
        ops = iter(operations)
        
        for i, number in enumerate(problem.numbers):
            if i == 0:
                continue
            
            if result > problem.result:
                break
            
            op = next(ops)
            result = op.operator(result, number)
            
        return Solution(
            problem = problem,
            result = result,
            operations = operations
        )       
    
    
    # https://stackoverflow.com/questions/2267362/how-to-convert-an-integer-to-a-string-in-any-base
    def number_to_base(self, number: int, base: int, places: int) -> list[int]:
        padding: list[int] = [0] * places
        
        if number == 0:
            return padding[:places - 1] + [0]
        digits = []
        while number:
            digits.append(int(number % base))
            number //= base
        
        result = digits[::-1]
        padding_places = places - len(result) if places - len(result) > 0 else 0
        
        return padding[:padding_places] + result
    
    
    def print(self, solutions: list[Solution]):
        for solution in solutions:
            solution_str = str(solution.problem.numbers[0])
            for i in range(len(solution.operations)):
                solution_str += ' {sign} {number}'.format(
                    sign = solution.operations[i].sign, 
                    number = solution.problem.numbers[i + 1]
                )
            
            print('Found solution for problem {result}: {solution_str}'.format(
                result = solution.result, 
                solution_str = solution_str)
            )
            
solver = Solver()
file_parser = FileParser(__file__).parse(solver, mode = 'INPUT')
solutions = solver.try_solve()

# Add new operator for part 2
solver.add_operation(Operation(sign = '||', operator = solver.concatenate))
solutions2 = solver.try_solve()

print('[PART 1] Sum of solvable problem results: {output}'.format(output = sum([s.result for s in solutions])))
print('[PART 2] Sum of all solvable problem results (using || operator): {output}'.format(output =  sum([s.result for s in solutions2])))