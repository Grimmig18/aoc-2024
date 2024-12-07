from abc import ABC, abstractmethod

class ParserInterface(ABC):
    @abstractmethod
    def parse_line(self, data: str):
        pass