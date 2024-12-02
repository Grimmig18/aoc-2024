from pathlib import Path
from typing import Callable


with open(Path(__file__).resolve().parent.joinpath('input.txt'), 'r') as file:
    numbers1, numbers2 = [], []
    split_line: Callable[[str], str] = lambda line : line.replace('\n', '').split('  ')
    [(
        numbers1.append(int(split_line(line)[0])), 
        numbers2.append(int(split_line(line)[1]))
    ) for line in file]

numbers1.sort()
numbers2.sort()

print('[PART 1] Total distance: {output}'.format(
    output = sum(abs(number1 - numbers2[i]) for i, number1 in enumerate(numbers1))
))

print('[PART 2] Total similarity: {output}'.format(
    output = sum(number1 * numbers2.count(number1) for number1 in numbers1)
))