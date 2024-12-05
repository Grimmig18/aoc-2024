from pathlib import Path

class PrintQueue:
    def __init__(self) -> None:
        self.page_prereq: dict[int, list[int]] = {}
        self.second_part = False
        self.correct_sequences: list[list[int]] = []
        self.fixed_sequences: list[list[int]] = []

    def check_sequences(self) -> tuple[list[list[int]], list[list[int]]]:
        with open(Path(__file__).resolve().parent.joinpath('input.txt'), 'r') as file:
            for line in file:
                if line == '\n' and self.second_part == False:
                    self.second_part = True
                    continue
                
                if self.second_part == False:
                    numbers = [int(number) for number in line.replace('\n', '').split('|')]
                    if numbers[1] not in self.page_prereq:
                        self.page_prereq[numbers[1]] = []
                        
                    self.page_prereq[numbers[1]].append(numbers[0])
                    
                    
                if self.second_part == True and line != '\n':
                    pages = [int(page) for page in line.split(',')]
                    
                    if self.check_sequence(pages)[0] == True: 
                        self.correct_sequences.append(pages)
                    else:
                        is_fixed, fixed_seq = self.try_fix(pages)
                        if is_fixed:
                            self.fixed_sequences.append(fixed_seq)
                            
                        
        return self.correct_sequences, self.fixed_sequences


    def check_sequence(self, pages) -> tuple[bool, tuple[int, int]]:
        correct_pages: list[int] = []
        failed_condition: tuple[int, int] = (-1, -1)
        
        for page in pages:
            pre_req_satisfied = True
            
            if page in self.page_prereq:
                relevant_prereq = [req for req in self.page_prereq[page] if req in pages]
                            
                for pre_req in relevant_prereq:
                    if pre_req not in correct_pages:
                        failed_condition = (page, pre_req)
                        pre_req_satisfied = False

            if pre_req_satisfied == True:
                correct_pages.append(page)
            else:
                break
                            
        return len(correct_pages) == len(pages), failed_condition
    
    
    def try_fix(self, pages: list[int]) -> tuple[bool, list[int]]:
        is_valid: bool = False
        mutated_pages: list[int] = pages.copy()
        tried_mutated_pages: list[list[int]] = []
        failed_condition: tuple[int, int] = None
        
        while not is_valid:
            # Mutate
            if failed_condition is not None:
                # Swap pages that failed condition
                index1 = mutated_pages.index(failed_condition[0])
                index2 = mutated_pages.index(failed_condition[1])
                mutated_pages[index1], mutated_pages[index2] = mutated_pages[index2], mutated_pages[index1]
            
            if mutated_pages in tried_mutated_pages:
                break
            
            is_valid, failed_condition = self.check_sequence(mutated_pages)
            tried_mutated_pages.append(mutated_pages.copy())
            
        if is_valid:
            return True, mutated_pages
        
        return False, None
        
        
correct, fixed = PrintQueue().check_sequences()
      
print('[PART 1] Sum of middle elements of correct instructions {output}'.format(
    output = sum(seq[int(len(seq) / 2)] for seq in correct))
)

print('[PART 2] Sum of middle elements of fixed intrusctions {output}'.format(
    output = sum(seq[int(len(seq) / 2)] for seq in fixed))
)