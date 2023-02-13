from intepreter import interpret


# reg1 reg2
# setadd subt mult div push to mem @ reg 2
"""instruction set
set0  val
set1  val
clr reg#
swap
dupl reg1/reg2 (->reg2/reg1)
add  -> reg0
subt -reg1/reg2 (->reg0/reg1) # specified is what is subtracted from
mult -> reg0
pow reg1 * reg0
div  -> reg0
write (reg0@->  RAM@reg1)
read (->reg0   RAM@reg1)"""
instruction_set = 'set0 set1 clr swap dupl add subt mult pow div write read'
instruction_set = instruction_set.split()
assembly_program = """\
set0 1
set1 2
pow 6"""

assembly_program = assembly_program.split('\n')

brainfuck = ''
for instruction in assembly_program:
    inst, value = instruction.split()
    value = int(value)
    print(inst, value)
    if not inst in instruction_set: raise Exception(f'invalid instruction \'{inst}\'')
    match inst:
        case 'set0': brainfuck += value * '+'
        case 'set1': brainfuck += '>>>' + value * '+' + '<<<'
        case 'clr':
            if value == 0:   brainfuck += '[-]'
            elif value == 1: brainfuck += '>>>' + '[-]' + '<<<'
            else: raise Exception(f'invalid clr address \'{value}\'')
        case 'swap':
            brainfuck +=  '[- >>> >>> + <<< <<<]' # move reg1 to workspace
            brainfuck +=  '>>>[- <<< + >>>]' # move reg2 to reg0
            brainfuck +=  '>>> [- <<< + >>>] <<< <<<' # move workspace to reg1
        case 'dupl':
            if value == 0:
                brainfuck += '[->+>>+<<<]>[-<+>]<' # duplicate value in reg0 & rewrite
            elif value == 1:
                brainfuck += '>>>[-<+<<+>>>]<[->+<]<<'
            else: raise Exception(f'invalid dupl address \'{value}\'')
        case 'add':
            if value == 0: brainfuck += '>>>[-<<<+>>>]<<<'
            if value == 1: brainfuck += '[->>>+<<<]'
        case 'subt':
            if value == 0: brainfuck += '>>>[-<<<->>>]<<<'
            if value == 1: brainfuck += '[->>>-<<<]'
        case 'mult': # moves controller to reg+1, hash dupl of reg2 along reg+1
            if value == 0:
                brainfuck += '[->+<]>[->>'
                brainfuck += '[->+>+<<]>>[-<<+>>]<' # duplicates and returns farthest
                brainfuck += '[-<<<<+>>>>]<<<]<'
            if value == 1: raise Exception(f'not implemented')
        case 'pow': 
                brainfuck += value * '[->+<]>[->> [->+>+<<]>>[-<<+>>]< [-<<<<+>>>>]<<<]<'

    brainfuck += ' '
print(brainfuck)
interpret(brainfuck)