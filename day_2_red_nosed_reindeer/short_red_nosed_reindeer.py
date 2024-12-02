from pathlib import Path

def check(distances: list[int]) -> bool:
    return any(distance for distance in distances if distance < 0) ^ any(distance for distance in distances if distance > 0) and not any(True for distance in distances if abs(distance) > 3 or distance == 0)

sequences: list[list[int]] = []
with open(Path(__file__).resolve().parent.joinpath('input.txt'), 'r') as file:
    [sequences.append([int(val) for val in line.replace('\n', '').split(' ')]) for line in file]

total_safe = 0
total_safe_damper = 0

for levels in sequences:
    distances = [levels[i] - levels[i + 1] for i in range(0, len(levels) - 1)]
    if check(distances):
        total_safe += 1
        
    # Try removing singular entries
    for i, _ in enumerate(levels):
        reduced = levels.copy()
        reduced.pop(i) 
        distances = [reduced[i] - reduced[i + 1] for i in range(0, len(reduced) - 1)]
        
        if check(distances):
            total_safe_damper += 1
            break

print('[PART 1] Correct seuqences: {output}'.format(output = total_safe))
print('[PART 2] Correct sequences: {output}'.format(output = total_safe_damper))