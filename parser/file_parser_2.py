from pathlib import Path
from typing import Literal
from parser.parser import ProblemParser

InputMode = Literal['INPUT', 'SAMPLE']

class FileParser:
    def __init__(
        self, 
        source_script: str, 
        input_file: str = 'input.txt', 
        sample_file: str = 'sample.txt'
    ) -> None:
        self.input_file_path: Path
        self.sample_file_path: Path
        
        # In same folder as calling script
        self.input_file_path = Path(source_script).resolve().parent.joinpath(input_file)
        self.sample_file_path = Path(source_script).resolve().parent.joinpath(sample_file)
        
        self.data: list[str] = []
    
    
    def parse(self, parser: ProblemParser, mode: InputMode = 'SAMPLE') -> ProblemParser:
        file_path = self.input_file_path if mode == 'INPUT' else self.sample_file_path
                
        with open(file_path, 'r') as file:
            for line in file:
                # Pass each line into parser function 
                self.data.append(line)
                parser.parse_line(line)
                
                
    def print(self):
        for line in self.data:
            print(line)
    