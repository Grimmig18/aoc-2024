from pathlib import Path
from typing import Callable


def get_level_sequences() -> list[list[int]]:
    file_path = Path(__file__).resolve().parent.joinpath('input.txt')
    sequences: list[list[int]] = []
    
    with open(file_path, 'r') as input:
        for line in input:
            sequences.append([int(val) for val in line.replace('\n', '').split(' ')])
            
    return sequences


def calculate_distances(sequence: list[int]) -> list[int]:
    distances: list[int] = []
    
    for i, level in enumerate(sequence):
        if i == len(sequence) - 1:
            break
        
        distances.append(level - sequence[i + 1])
        
    return distances


def check_level_sequence(sequence: list[int]) -> bool:
    distances = calculate_distances(sequence)
    
    is_decreasing = any(distance for distance in distances if distance < 0)
    is_increasing = any(distance for distance in distances if distance > 0)
    has_illegal_step = any(True for distance in distances if abs(distance) > 3 or distance == 0)
    
    return (is_decreasing ^ is_increasing) and not has_illegal_step
    

def check_all_sequences(seuqences: list[list[int]], checker: Callable[[list[int]], bool]) -> int:
    correct = 0
    for sequence in seuqences:
        if checker(sequence) == True:
            correct += 1
            
    return correct


def check_level_sequence_damper(sequence: list[int]) -> True:
    # Try removing one value at a time
    for i, _ in enumerate(sequence):
        reduced = sequence.copy()
        reduced.pop(i)
        
        if check_level_sequence(reduced):
            return True
        
    return False
        

print('[PART 1] Correct seuqences: {output}'.format(
    output = check_all_sequences(get_level_sequences(), check_level_sequence)
))

print('[PART 2] Correct sequences: {output}'.format(
    output = check_all_sequences(get_level_sequences(), check_level_sequence_damper)
))