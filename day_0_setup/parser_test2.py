from parser.file_parser_2 import FileParser
from parser.parser import ProblemParser


class Solver(ProblemParser):
    def __init__(self):
        super().__init__()
            

solver = Solver()
FileParser(__file__).parse(solver, 'SAMPLE')
solver.print()