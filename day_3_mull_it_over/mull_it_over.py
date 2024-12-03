import re
from parser.file_parser import FileParser

data: list[list[str]] = FileParser(__file__).parse(mode = 'INPUT').get()
as_string: str = ''.join([''.join(line) for line in data])


print('[PART 1] Sum of all multiplications: {output}'.format(
    output = sum(int(match.split(',')[0][4:]) * int(match.split(',')[1][:-1]) for match in re.findall(r'mul\(\d+,\d+\)', as_string))
))

multi_sum = 0
is_enabled = True
for match in re.findall(r'mul\(\d+,\d+\)|don\'t\(\)|do\(\)', as_string):
    if match == 'do()':
        is_enabled = True
        continue
    elif match == 'don\'t()':
        is_enabled = False
        continue
    
    parts = match.split(',')
    multi_sum += int(parts[0][4:]) * int(parts[1][:-1]) if is_enabled else 0
    
print('[PART 2] Sum of filtered multiplications: {output}'.format(
    output = multi_sum
))