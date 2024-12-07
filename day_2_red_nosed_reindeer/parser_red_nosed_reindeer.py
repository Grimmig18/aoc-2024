from parser.file_parser import FileParser

def check(distances: list[int]) -> bool:
    return any(distance for distance in distances if distance < 0) ^ any(distance for distance in distances if distance > 0) and not any(True for distance in distances if abs(distance) > 3 or distance == 0)

def run():
    sequences: list[list[int]] = FileParser(__file__).parse().get()
    
    print('[PART 1] Correct seuqences: {output}'.format(
        output = sum(int(check(distances)) for distances in [[sequence[i] - sequence[i + 1] for i in range(0, len(sequence) - 1)] for sequence in sequences])
    ))
    
    
    # print('[PART 2] Correct sequences: {output}'.format(
    #     output = [test[:i] + test[i+1:] for i, _ in enumerate(test)] # TODO: 
    # ))
    
if __name__ == '__main__':
    run()
