from dataclasses import dataclass
from parser.file_parser_2 import FileParser
from parser.parser import ParserInterface

@dataclass
class Point:
    col_index: int = -1
    row_index: int = -1
    
    def __eq__(self, value) -> bool:
        if isinstance(value, Point):
            return self.col_index == value.col_index and self.row_index == value.row_index
        return False

@dataclass
class Node:
    type: str
    position: Point
    
    
@dataclass
class Antenna(Node):
    pass


class ResonanceSolver(ParserInterface):
    def __init__(self):
        self.grid_cols: int = 0
        self.grid_rows: int = 0
        self.antenna_positions: dict[str, list[Antenna]] = {}
        self.all_antennas: list[Antenna] = []
        self.tiles_to_skip: list[str] = ['.']

    
    def parse_line(self, line: str):
        tiles = list(line.strip())
        
        if self.grid_cols == 0:
            self.grid_cols = len(tiles)
        
        for i, tile in enumerate(tiles):
            if tile in self.tiles_to_skip:
                continue
            
            if tile not in self.antenna_positions:
                self.antenna_positions[tile] = []
                
            antenna = Antenna(tile, Point(i, self.grid_rows))
            self.antenna_positions[tile].append(antenna)
            self.all_antennas.append(antenna)
        
        self.grid_rows += 1
        
    
    def find_antinodes(self) -> list[Node]:
        antinodes: list[Node] = []
        
        for type, antennas in self.antenna_positions.items():
            type_antinodes = self.find_antinode_for_type(antennas)
            antinodes.extend(type_antinodes)
            print('Found {n} antinodes for type {type}'.format(n = len(type_antinodes), type = type))
        
        return antinodes
    
    
    def find_antinode_for_type(self, antennas: list[Antenna]) -> list[Node]:
        antinodes: list[Node] = []
        
        for antenna1 in antennas:
            for antenna2 in antennas:
                if antenna1.position == antenna2.position:
                    continue
                
                antinode_points = []
                antinode_points.extend(self.calculate_antinodes(antenna1.position, antenna2.position))
                antinode_points.extend(self.calculate_antinodes(antenna2.position, antenna1.position))
                
                antinodes.extend([Node(antenna1.type, p) for p in antinode_points])
    
        return antinodes
    
    
    def calculate_antinodes(self, point1: Point, point2: Point) -> list[Point]:
        col_dist = point2.col_index - point1.col_index
        row_dist = point2.row_index - point1.row_index
        
        antinode = Point(
            col_index = point2.col_index + col_dist,
            row_index = point2.row_index + row_dist
        )
        
        if self.is_point_on_map(antinode):
            return [antinode]
        
        return []


    def print(self, antinodes: list[Node]):
        for row in range(self.grid_rows):
            row_str = ''
            for col in range(self.grid_cols):
                antenna = next((a for a in self.all_antennas if a.position.col_index == col and a.position.row_index == row), None)
                antinode = next((a for a in antinodes if a.position.col_index == col and a.position.row_index == row), None)
                
                if antenna is not None:
                    row_str += antenna.type
                    continue
                
                if antinode is not None:                  
                    row_str += '#'
                    continue
                
                row_str += '.'
                
            print(row_str)
        
        print('Rows x Cols: {rows}x{cols}: {n_a} antennas, {n_b} antinodes, {n_c} hidden, {n_d} unique positions'.format(
            rows = self.grid_rows,
            cols = self.grid_cols,
            n_a = len(self.all_antennas),
            n_b = len(antinodes),
            n_c = len(self.get_hidden_nodes(antinodes)),
            n_d = len(set([(a.position.col_index, a.position.row_index) for a in antinodes]))
        ))
        
        
    def get_hidden_nodes(self, antinodes: list[Node]) -> list[Node]:
        hidden_nodes: list[Node] = []
        all_antenna_positions = [Point(a.position.col_index, a.position.row_index) for a in self.all_antennas]
        
        for antinode in antinodes:
            if antinode.position in all_antenna_positions:
                hidden_nodes.append(antinode)
                
        return hidden_nodes
    
    
    def is_point_on_map(self, point: Point) -> bool:
        return point.col_index < self.grid_cols \
            and point.row_index < self.grid_rows \
            and point.col_index >= 0 \
            and point.row_index >= 0
    
    
class ResonanceSolver2(ResonanceSolver):
    def __init__(self, part1_solver: ResonanceSolver):
        super().__init__()
        self.part1_solver = part1_solver
        
        self.grid_cols = part1_solver.grid_cols
        self.grid_rows = part1_solver.grid_rows
        self.antenna_positions = part1_solver.antenna_positions
        self.all_antennas = part1_solver.all_antennas
        self.tiles_to_skip = part1_solver.tiles_to_skip
    
    
    def calculate_antinodes(self, point1: Point, point2: Point) -> list[Point]:
        col_dist = point2.col_index - point1.col_index
        row_dist = point2.row_index - point1.row_index
        
        antinodes: list[Point] = [point1]
        for direction in [1, -1]:
            next_point = Point(point1.col_index + (direction * col_dist), point1.row_index + (direction * row_dist))
            
            while self.is_point_on_map(next_point):
                antinodes.append(next_point)
                next_point = Point(next_point.col_index + (direction * col_dist), next_point.row_index + (direction * row_dist))
        
        return antinodes
    
    
solver = ResonanceSolver()
FileParser(__file__).parse(solver, mode = 'INPUT')

antinodes = solver.find_antinodes()
solver.print(antinodes)

solver2 = ResonanceSolver2(solver)
antinodes2 = solver2.find_antinodes()
solver2.print(antinodes2)
