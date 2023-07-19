from intepreter import interpret


# reg1 reg2
# setadd subt mult div push to mem @ reg 2
"""\
instruction set
set0  (val)
set1  (val)
clr (): reg#
swap
dupl reg1/reg2 (->reg2/reg1)
add  -> reg0
subt -reg1/reg2 (->reg0/reg1) # specified is what is subtracted from
mult  () :reg0 A*B ->
pow reg1 * reg0
div  -> reg0
write (reg0@->  RAM@reg1)
read (->reg0   RAM@reg1)\
print : prints with ASCII
"""

assembly_program = """\
set0 72
print
set0 101
print
set0 108
print
print
set0 111
print
set0 33
print
"""


position_register_A = 0
position_register_B = 3


# assuming 1 is always right of 0

# this function moves from reg A to reg B on the tape
up = (position_register_B-position_register_A) * '>'

# this function moves from reg B back to reg A on the tape
down = (position_register_B-position_register_A) * '<'

inc = 'x'

zero = '[-]'

zero_A = zero
zero_B = up + zero + down


def assemble(assembly_program):
    instruction_set = 'set0 set1 clr swap dupl add subt mult pow div write read print'
    instruction_set = instruction_set.split()

    assembly_program = assembly_program.strip()
    assembly_program = assembly_program.split('\n')
    # assembly_program = list(filter(None , assembly_program) ) # to eliminate empty lines

    bf = ''
    for instruction in assembly_program:
        # print()
        try: instruction, value = instruction.split()
        except: pass
        # print(f"instruction: {instruction}, {value}")
        value = int(value)
        if not instruction in instruction_set:
            raise Exception(f'invalid instruction \'{instruction}\'')
        match instruction:
            case 'set0':
                bf += zero
                bf += value * '+'

            case 'set1':
                bf += up
                bf += zero
                bf += value * '+'
                bf += down

            case 'clr':
                if value == 0:
                    bf += zero_A
                elif value == 1:
                    bf += zero_B
                else:
                    raise Exception(f'invalid clr address \'{value}\'')
            
            case 'swap':
                bf += '[- >>> >>> + <<< <<<]'  # move reg1 to workspace
                bf += '>>>[- <<< + >>>]'  # move reg2 to reg0
                # move workspace to reg1
                bf += '>>> [- <<< + >>>] <<< <<<'
            
            case 'dupl':
                if value == 0:
                    # duplicate value in reg0 & rewrite
                    bf += '[->+>>+<<<]>[-<+>]<'
                elif value == 1:
                    bf += '>>>[-<+<<+>>>]<[->+<]<<'
                else:
                    raise Exception(f'invalid dupl address \'{value}\'')
            
            case 'add':
                if value == 0:
                    bf += '>>>[-<<<+>>>]<<<'
                if value == 1:
                    bf += '[->>>+<<<]'
            
            case 'subt':
                if value == 0:
                    bf += '>>>[-<<<->>>]<<<'
                if value == 1:
                    bf += '[->>>-<<<]'
            
            case 'mult':  # moves controller to reg+1, hash dupl of reg2 along reg+1
                bf += '[->+<]' # reg A shift one left
                bf += '>'
                bf += '[->>' # for A+1 @B
                bf +=    '[->+>+<<]>>[-<<+>>]<' # hash reg B -> B__ & bring B+2 to B, end on B+1
                bf +=    '[-<<<<+>>>>]<<<' # move B+1 to A
                bf += ']'
                bf += '<' # back to A
            
            case 'pow':

                # this is ann inefficient implementation, I'm not sure where to put the decrement register though
                bf += value * \
                    '[->+<]>[->> [->+>+<<]>>[-<<+>>]< [-<<<<+>>>>]<<<]<'
            
            case 'print':
                bf += '.'

            case _:
                raise Exception(f"invalid instruction {instruction}")

        bf += '\n'

    bf += ' '
    return bf


if __name__ == "__main__":
    bf = assemble(assembly_program)
    print(f"output:\n{bf}")
    with open('code.txt', 'w') as f:
        f.write(bf)
    # interpret(bf, verbose=False)
