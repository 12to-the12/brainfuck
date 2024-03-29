
import numpy as np




import os
clear = lambda : os.system("clear")
import time



def interpret(program, verbose=True):
    program_length = len(program)
    memory = np.zeros( (8), dtype='uint8')
    data_pointer = 0
    program_pointer = 0
    block_stack = []

    executing = True

    while executing:
        if data_pointer < 0: raise Exception(f'data_pointer out of bounds {data_pointer}')
        if verbose:
            #time.sleep(0.1)
            os.system('cls')
            print(program)
            print(program_pointer * ' ' + '^')
            print()

        match program[program_pointer]:
            case ' ': pass
            case '+': memory[data_pointer] += 1
            case '-': memory[data_pointer] -= 1
            case '>': data_pointer += 1
            case '<': data_pointer -= 1
            case '[':
                if memory[data_pointer] != 0:
                    block_stack.append(program_pointer)
            case ']':
                if memory[data_pointer] != 0:

                    program_pointer = block_stack[-1]
                else: block_stack.pop()

        if verbose:
            print(memory)
            print( ' ' + data_pointer * 2 * ' ' + '^')

        program_pointer += 1



        if program_pointer == program_length: executing = False
    
    if not verbose: print(memory)

if __name__ == '__main__':
    with open('code.txt', 'r') as f:
        program = f.read()
    clear()
    # program = '+>>>++<<<[->+<]>[->> [->+>+<<]>>[-<<+>>]< [-<<<<+>>>>]<<<]<[->+<]>[->> [->+>+<<]>>[-<<+>>]< [-<<<<+>>>>]<<<]<[->+<]>[->> [->+>+<<]>>[-<<+>>]< [-<<<<+>>>>]<<<]<[->+<]>[->> [->+>+<<]>>[-<<+>>]< [-<<<<+>>>>]<<<]<[->+<]>[->> [->+>+<<]>>[-<<+>>]< [-<<<<+>>>>]<<<]<[->+<]>[->> [->+>+<<]>>[-<<+>>]< [-<<<<+>>>>]<<<]<[->+<]>[->> [->+>+<<]>>[-<<+>>]< [-<<<<+>>>>]<<<]< '
    start = time.time()
    interpret(program, verbose=False)
    end = time.time()
    print(f"Time elapsed is: {(end-start)*1_000_000:.3f}µs")#
    