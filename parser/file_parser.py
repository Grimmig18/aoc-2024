from pathlib import Path
from typing import Callable, Literal, Self

InputMode = Literal['INPUT', 'SAMPLE']

class FileParser[Item]:
    
    def __init__(
        self, 
        source_script: str, 
        source_folder: str = '', 
        input_file: str = 'input.txt', 
        sample_file: str = 'sample.txt'
    ) -> None:
        self.input_file_path: Path
        self.sample_file_path: Path
        
        self.last_parsed: list[list[Item]] = []
        
        if source_folder:
            # Explicit data source defined
            self.input_file_path = Path(source_folder).resolve().joinpath(input_file)
            self.sample_file_path = Path(source_folder).resolve().joinpath(sample_file)
        else:
            # In same folder as calling script
            self.input_file_path = Path(source_script).resolve().parent.joinpath(input_file)
            self.sample_file_path = Path(source_script).resolve().parent.joinpath(sample_file)
    
    
    def parse(self, parser_function: Callable[[str], list[Item]] = None, mode: InputMode = 'INPUT') -> Self:
        if parser_function is None:
            # Enables default behavior if nothing is passed to parser_function
            # Cannot be provided as "normal" default argument, since it is an object attribute
            parser_function = self.__default_parser
        
        self.last_parsed = self.__parse_lines(parser_function, mode)
        return self
    
    
    def print(self) -> None:
        for item_list in self.last_parsed:
            print(item_list)
            
                
    def get(self) -> list[list[Item]]:
        return self.last_parsed
    
    
    def __parse_lines(self, parser_function: Callable[[str], list[Item]], mode: InputMode) -> list[list[Item]]:
        file_path = self.input_file_path if mode == 'INPUT' else self.sample_file_path
        
        collection: list[list[Item]] = []
        with open(file_path, 'r') as file:
            for line in file:
                # Pass each line into parser function 
                collection.append(parser_function(line))
                
        return collection
                
    
    def __default_parser(self, line: str) -> list[int]:
        # Split at white spaces, return elements as integers
        return [int(element) for element in line.replace('\n', '').split()]
    
    
