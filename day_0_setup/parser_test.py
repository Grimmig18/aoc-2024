from parser.file_parser import FileParser

def line_to_strings(line: str) -> list[str]:
    return [str(element) for element in line.replace('\n', '').split()]

if __name__ == '__main__':
    parser = FileParser(__file__)
    
    # Just print the lines in file using default parser
    print('Print lines using default parser: input.txt')
    parser.parse().print()
    
    print('\nPrint lines using default parser: sample.txt')
    parser.parse(mode = 'SAMPLE').print()
    
    # Print lines using to string parser
    print('\nPrint lines using string parser: input.txt')
    parser.parse(parser_function = line_to_strings).print()
    
    print('\nPrint lines using string parser: sample.txt')
    parser.parse(parser_function = line_to_strings, mode = 'SAMPLE').print()
    
    
    # ... or get lines for processing
    lines: list[list[int]] = parser.parse().get()
    print('\n{lines} lines in file'.format(lines = len(lines)))