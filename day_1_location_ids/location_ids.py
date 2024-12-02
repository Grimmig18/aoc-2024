from pathlib import Path


def get_ids() -> tuple[list[int], list[int]]:
    file_path = Path(__file__).resolve().parent.joinpath('input.txt')
    
    ids1 = []
    ids2 = []

    with open(file_path, 'r') as input:
        for line in input:
            # 1234  4321\n -> [1234, 4321]
            ids = line.replace('\n', '').split('  ')

            ids1.append(int(ids[0]))
            ids2.append(int(ids[1]))

    return (ids1, ids2)


def calculate_distances(numbers1: list[int], numbers2: list[int]) -> int:
    diff_sum = 0
    
    for i, number1 in enumerate(numbers1):
        number2 = numbers2[i]
        diff_sum += abs(number1 - number2)

    return diff_sum


def get_number_frequency(numbers: list[int]) -> dict[int, int]:
    frequency: dict[int, int] = {}
    
    for number in numbers:
        if number not in frequency.keys():
            # Create new
            frequency[number] = 1
        else:
            # Increase existing by one
            frequency[number] += 1 

    return frequency


def calculate_similarity(numbers: list[int], frequency: dict[int, int]) -> int:
    similarity_sum = 0
    
    for number in numbers:
        if number in frequency.keys():
            similarity_sum += number * frequency[number]

    return similarity_sum


numbers1, numbers2 = get_ids()
numbers1.sort()
numbers2.sort()
print('[PART 1] Total distance: {output}'.format(output = calculate_distances(numbers1, numbers2)))

numbers2_frequency = get_number_frequency(numbers2)
print('[PART 2] Total similarity: {output}'.format(output = calculate_similarity(numbers1, numbers2_frequency)))