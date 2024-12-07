from copy import deepcopy
from typing import Literal, Self
from parser.file_parser import FileParser
  
type Position = tuple[int, int]
type TileType = Literal['empty', 'guard', 'obstacle']
type TileMap = list[list[TileType]]
type Direction = tuple[int, int]

class MapParser:
    def __init__(self) -> None:
        self.guard_position = (-1, -1)
        self.initial_guard_position = self.guard_position
        self.line_index = -1
        
        self.next_step_direction = 0
        self.step_directions: list[Direction] = [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1)
        ]
        
        self.map: TileMap = []
        self.unique_positions: dict[Position, bool] = {}
        self.path: list[tuple[Position, Direction]] = []
        self.original_path: list[tuple[Position, Direction]] = None
        
        self.tile_mapping: dict[str, TileType] = {
            '.': 'empty',
            '#': 'obstacle',
            '^': 'guard',
            'O': 'custom_obstacle'
        }
    
    
    def parse_map(self, line: str) -> list[TileType]:
        self.line_index += 1
        output = []
        for i, tile in enumerate(list(line.replace('\n', ''))):
            output.append(self.tile_mapping[tile])
            
            if self.tile_mapping[tile] == 'guard':
                self.guard_position = (self.line_index, i)
                self.initial_guard_position = self.guard_position
                
        return output
    
    
    def set_map(self, map: TileMap) -> Self:
        self.map = map
        self.save_initial_state()
        return self
    
    
    def walk(self) -> tuple[int, bool]:
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
                if (self.guard_position, self.step_directions[self.next_step_direction]) in self.path:
                    return len(self.unique_positions), True
                
                self.unique_positions[self.guard_position] = True
                self.path.append((self.guard_position, self.step_directions[self.next_step_direction]))
        
        return len(self.unique_positions), False
    
    
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
        if next_map_tile not in ['empty', 'guard']:
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
                
                line_str += next(key for key, type in self.tile_mapping.items() if type == tile)
            
            print(line_str)
    
            
    def obstacle_positions(self) -> list[Position]:
        # Original complete path
        obstacle_positions: list[Position] = []
        
        # At any one point on the path:
        # If placing an obstacle in front of the guard leads to the guard
        # re-visiting the current tile at a later point in time walking in the same direction, a loop exists
        for i, row in enumerate(self.map):
            for j, tile in enumerate(row):
                self.reset()
                # Try placing obstacle on each empty tile
                if tile != 'empty':
                    continue
                
                relevant_tiles: list[Position] = [(i, j)]
                relevant_tiles.extend([(i + direction[0], j + direction[1]) for direction in self.step_directions])
                
                if len([tile for tile in relevant_tiles if tile in [node[0] for node in self.original_path]]) == 0:
                    continue
                
                print('Placing obstacle at position: {i}, {j}'.format(i = i, j = j))
                self.map[i][j] = 'custom_obstacle'
                
                _, is_loop = self.walk()
                if is_loop:
                    print('Obstacle looped!')
                    obstacle_positions.append((i, j))
        
        self.reset()
        return obstacle_positions
    
    
    
    def draw_obstacles(self, obstacle_positions: list[Position]):
        for i, tile_row in enumerate(self.map):
            line_str = ''
            for j, tile in enumerate(tile_row):
                if (i, j) in obstacle_positions:
                    line_str += 'O'
                    continue
                
                # if (i, j) in self.unique_positions:
                #     line_str += 'X'
                #     continue
                
                line_str += next(key for key, type in self.tile_mapping.items() if type == tile)
            
            print(line_str)


    def save_initial_state(self):
        self.original_map = deepcopy(self.map)
        self.initial_guard_position = self.guard_position


    def reset(self):
        self.map = deepcopy(self.original_map)
        self.guard_position = deepcopy(self.initial_guard_position)
        self.unique_positions = {}
        self.unique_positions[self.guard_position] = True
        self.next_step_direction = 0
        
        if self.original_path is None:
            # Save first complete path
            self.original_path = self.path
        self.path = []
        
        
        
map_parser = MapParser()
lab_map = FileParser(__file__).parse(parser_function = map_parser.parse_map, mode = 'INPUT').get()

steps, _ = map_parser.set_map(lab_map).walk()	
map_parser.draw_path()
print('[PART 1] Distincts guard postitions: {output}'.format(output = steps))

obstacle_positions = map_parser.obstacle_positions()
map_parser.draw_obstacles(obstacle_positions)
print('[PART 2] Possible obstacle positions: {output}'.format(output = len(obstacle_positions)))