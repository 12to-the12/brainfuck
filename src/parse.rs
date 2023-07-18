use std::{thread, time};

const SLOWDOWN: u64 = 200; // milliseconds stopped for every operation
const MEMORY_SIZE: usize = 16; // number of memory locations

pub fn parse(program: String, slow: bool, draw: bool) {
    // let ctrl_count = &program.matches('[').count();
    let mut open_stack: Vec<usize> = Vec::new();
    let mut close_stack: Vec<usize> = Vec::new();

    let instructions = program.clone().into_bytes();

    for (index, instr) in instructions.iter().enumerate().rev() {
        let instr: char = *instr as char;
        match instr {
            // '[' => open_stack.push(index),
            ']' => close_stack.push(index),
            _ => (),
        }
    }

    // let mut position: isize;

    let mut memory: [u8; MEMORY_SIZE] = [0; MEMORY_SIZE];
    let mut memory_pointer: usize = 0;

    let mut program_pointer: usize = 0;

    let mut closing_pointer: usize = close_stack[0];

    // if non zero: ()
    // if zero: GOTO closing bracket & point next opener
    // if
    // if ending non zero: GOTO opening bracket
    // if ending on zero: ()
    // +++[++[++]-<>]++
    // @4 if 0 GOTO 14
    // @7 if 0 GOTO 10
    // @10 if nonzero GOTO 7
    // @14 if nonzero GOTO 4
    //
    loop {
        let instr: &u8 = &instructions[program_pointer];
        let instr: char = *instr as char;
        match instr {
            '+' => memory[memory_pointer] += 1,
            '-' => memory[memory_pointer] -= 1,
            '>' => memory_pointer += 1,
            '<' => {
                if memory_pointer == 0 {
                    panic!();
                }
                memory_pointer -= 1
            }
            '[' => {
                if memory[memory_pointer] == 0 {
                    // GOTO closing bracket
                    // only occurs on first encounter

                    program_pointer = closing_pointer;
                    closing_pointer = close_stack[open_stack.len() - 1];
                } else {
                    open_stack.push(program_pointer)
                }
            }
            ']' => {
                if memory[memory_pointer] != 0 {
                    program_pointer = open_stack[open_stack.len() - 1];
                } else {
                    open_stack.pop();
                }
            }
            '.' => print!("{}", memory[memory_pointer] as char),
            _ => (), // bf programs can include any character
        }
        program_pointer += 1;
        if program_pointer == instructions.len() {
            break;
        }

        if slow {
            let x = time::Duration::from_millis(SLOWDOWN);
            thread::sleep(x);
        }
        if draw {
            print!("{esc}[2J{esc}[1;1H", esc = 27 as char);
            println!("{:?}", memory);
            println!(" {}^", " ".repeat(memory_pointer * 3));
            println!("");
            println!("{:?}", &program);
            println!(" {}^", " ".repeat(program_pointer));
            println!(
                "\nopen_stack:{:?}\nclose_stack:{:?}\n{program_pointer}",
                &open_stack, &close_stack
            );
            println!("{}", closing_pointer);
        }
    }
    print!("{esc}[2J{esc}[1;1H", esc = 27 as char);
    println!("{:?}", memory);
}
