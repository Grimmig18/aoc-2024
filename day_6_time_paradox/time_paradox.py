from typing import Literal
from parser.file_parser import FileParser
  
type Position = tuple[int, int]
type TileType = Literal['empty', 'guard', 'obstacle']
type TileMap = list[list[TileType]]

class MapParser:
    def __init__(self) -> None:
        self.guard_position = (-1, -1)
        self.line_index = -1
        
        self.next_step_direction = 0
        self.step_directions = [
            [-1, 0],
            [0, 1],
            [1, 0],
            [0, -1]
        ]
        
        self.map: TileMap = []
        self.unique_positions: dict[Position, bool] = {}
        
        self.tile_mapping: dict[str, TileType] = {
            '.': 'empty',
            '#': 'obstacle',
            '^': 'guard'
        }
        
    def parse_map(self, line: str) -> list[TileType]:
        self.line_index += 1
        output = []
        for i, tile in enumerate(list(line.replace('\n', ''))):
            output.append(self.tile_mapping[tile])
            
            if self.tile_mapping[tile] == 'guard':
                self.guard_position = (self.line_index, i)
                
        return output
    
    def walk(self, map: TileMap) -> int:
        self.map = map
        self.unique_positions[self.guard_position] = True
        
        while True:
            move = self.step(self.step_directions[self.next_step_direction])
            
            if move[0] == -1 and move[1] == -1 and move[2] == False:
                # Off the map
                break
            
            if move[2] == False:
                # Colide with obstacle, get next direction
                self.next_direction()
                
            if move[2] == True:
                # Continue moving
                self.guard_position = (move[0], move[1])
                self.unique_positions[self.guard_position] = True
        
        return len(self.unique_positions)
    
    
    def step(self, direction: tuple[int, int]) -> tuple[int, int, bool]:
        next_guard_position = (self.guard_position[0] + direction[0], self.guard_position[1] + direction[1])
        
        # Check if next move would be on map
        if next_guard_position[0] > len(self.map) - 1 \
            or next_guard_position[1] > len(self.map[0]) - 1 \
            or next_guard_position[0] < 0 \
            or next_guard_position[1] < 0:
                
            return (-1, -1, False)
        
        # Check if next move would collide
        next_map_tile: TileType = self.map[next_guard_position[0]][next_guard_position[1]]
        if next_map_tile != 'empty' and next_map_tile != 'guard':
            return (self.guard_position[0], self.guard_position[1], False)
    
        return (next_guard_position[0], next_guard_position[1], True)
    
    
    def next_direction(self) -> tuple[int, int]:
        index = self.next_step_direction
        self.next_step_direction = self.next_step_direction + 1 if self.next_step_direction < len(self.step_directions) -1 else 0
        
        return self.step_directions[index]
    
    
    def draw_path(self):
        for i, tile_row in enumerate(self.map):
            line_str = ''
            for j, tile in enumerate(tile_row):
                if (i, j) in self.unique_positions:
                    line_str += 'X'
                    continue
                
                line_str += next(key for key, type in self.tile_mapping.items() if type == self.map[i][j])
            
            print(line_str)


map_parser = MapParser()
lab_map = FileParser(__file__).parse(parser_function = map_parser.parse_map, mode = 'SAMPLE').get()

steps = map_parser.walk(lab_map)	
map_parser.draw_path()
print('[PART 1] Distincts guard postitions: {output}'.format(output = steps))