class ProblemParser:
    def __init__(self):
        self.lines = []


    def parse_line(self, data: str):
        self.lines.append(data.strip())
    
    
    def print(self):
        for line in self.lines:
            print(line)