from parser.file_parser import FileParser

class Xmas:
    def __init__(self, file_input: list[list[str]]) -> None:
        self.xmas = 'XMAS'
        self.file_input = file_input
        
        self.search_directions = [
            [0, 1],
            [1, 1],
            [1, 0],
            [1, -1],
            [0, -1],
            [-1, -1],
            [-1, 1],
            [-1, 0],
        ]
        
    
    def search_xmas(self, col_idx, row_idx) -> tuple[int]:
        xmas_found = 0
        
        for search_direction in self.search_directions:
            xmas_found += 1 if self.check_direction(col_idx, row_idx, search_direction) else 0
            
        return xmas_found


    def check_direction(self, col_idx, row_idx, search_direction) -> bool:
        steps = len(self.xmas)
        sequence = data[col_idx][row_idx]
        
        next_col_idx = col_idx
        next_row_idx = row_idx
            
        for _ in range(steps - 1):
            next_col_idx += search_direction[0] if abs(search_direction[0]) > 0 else 0
            next_row_idx += search_direction[1] if abs(search_direction[1]) > 0 else 0
            
            if next_col_idx < 0 or next_row_idx < 0 or next_col_idx > len(self.file_input) - 1 or next_row_idx > len(self.file_input[next_col_idx]) - 1:
                break
            
            sequence += self.file_input[next_col_idx][next_row_idx]
            
        return sequence == self.xmas


class CrossMas(Xmas):
    def __init__(self, file_input: list[list[str]]) -> None:
        super().__init__(file_input)
        
        self.search_directions = [
            [1, 1], # Bottom right
            [1, -1], # Bottom left
            [-1, -1], # Top left
            [-1, 1], # Top right
        ]
        
        
    def search_cross_mas(self, col_idx, row_idx) -> bool:
        bottom_right = ''
        bottom_left = ''
        top_left = ''
        top_right = ''
        
        
        for i, direction in enumerate(self.search_directions):
            next_col_idx = col_idx + direction[0]
            next_row_idx = row_idx + direction[1]
            
            if next_col_idx < 0 or next_row_idx < 0 or next_col_idx > len(self.file_input) - 1 or next_row_idx > len(self.file_input[next_col_idx]) - 1:
                break
            
            match i:
                case 0: bottom_right = self.file_input[next_col_idx][next_row_idx]
                case 1: bottom_left = self.file_input[next_col_idx][next_row_idx]
                case 2: top_left = self.file_input[next_col_idx][next_row_idx]
                case 3: top_right = self.file_input[next_col_idx][next_row_idx]
        
        tl_to_br = (top_left == 'S' and bottom_right == 'M') or (top_left == 'M' and bottom_right == 'S')
        bl_to_tr = (top_right == 'S' and bottom_left == 'M') or (top_right == 'M' and bottom_left == 'S')
        
        return tl_to_br and bl_to_tr
             

if __name__ == '__main__':
    data: list[list[str]] = FileParser(__file__).parse(
        parser_function = lambda line : [str(element) for element in list(line.replace('\n', ''))], 
        mode = 'INPUT'
    ).get()

    xmas_search = Xmas(data)
    cross_mas_search = CrossMas(data)
    
    all_found_xmas = 0
    all_found_cross_mas = 0
    
    for i, line in enumerate(data):
        for j, start_char in enumerate(line):
            
            if start_char == 'X':
                all_found_xmas += xmas_search.search_xmas(i, j)
            elif start_char == 'A':
                all_found_cross_mas += 1 if cross_mas_search.search_cross_mas(i, j) else 0
            
    print('[PART 1] XMAS strings found: {output}'.format(output = all_found_xmas)) 
    print('[PART 2] Cross-MAS strings found: {output}'.format(output = all_found_cross_mas))