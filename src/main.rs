

// instruction set
// set0  val
// set1  val
// clr reg#
// swap
// dupl reg1/reg2 (->reg2/reg1)
// add  -> reg0
// subt -reg1/reg2 (->reg0/reg1) # specified is what is subtracted from
// mult -> reg0
// pow reg1 * reg0
// div  -> reg0
// write (reg0@->  RAM@reg1)
// read (->reg0   RAM@reg1)
// 
// 
// 
extern crate brainfuck;
use brainfuck::parse;
// use brainfuck_rust::assembler;

use std::time::Instant;


fn main(){
    // assembler::read_file_string("assembly.txt")
    let program: String = String::from("+ >>>++<<< [->+<]>[->> [->+>+<<]>>[-<<+>>]< [-<<<<+>>>>]<<<]<[->+<]>[->> [->+>+<<]>>[-<<+>>]< [-<<<<+>>>>]<<<]<[->+<]>[->> [->+>+<<]>>[-<<+>>]< [-<<<<+>>>>]<<<]<[->+<]>[->> [->+>+<<]>>[-<<+>>]< [-<<<<+>>>>]<<<]<[->+<]>[->> [->+>+<<]>>[-<<+>>]< [-<<<<+>>>>]<<<]<[->+<]>[->> [->+>+<<]>>[-<<+>>]< [-<<<<+>>>>]<<<]<");
    println!("<start>");
    let start = Instant::now();
    parse::parse(program.clone(), true);

    let duration = start.elapsed();
    println!("Time elapsed is: {:?}", duration);
    println!("Time elapsed per op is: {:?}", duration);
    println!("Operations per second is: {:?} per op", duration);
}
// fn main() {
    
    
//     let program: String = String::from("+ >>>++<<< [->+<]>[->> [->+>+<<]>>[-<<+>>]< [-<<<<+>>>>]<<<]<[->+<]>[->> [->+>+<<]>>[-<<+>>]< [-<<<<+>>>>]<<<]<[->+<]>[->> [->+>+<<]>>[-<<+>>]< [-<<<<+>>>>]<<<]<[->+<]>[->> [->+>+<<]>>[-<<+>>]< [-<<<<+>>>>]<<<]<[->+<]>[->> [->+>+<<]>>[-<<+>>]< [-<<<<+>>>>]<<<]<[->+<]>[->> [->+>+<<]>>[-<<+>>]< [-<<<<+>>>>]<<<]<");
//     println!("<start>");
//     let start = Instant::now();
//     let  reps: u32 = 1;
//     let mut count: u32 = reps;
//     loop{

//         if count > 0 {
//             parse::parse(program.clone(), true);
//             count-=1}
//         else {
//             parse::parse(program.clone(), true);
//             break;}
        
//     }
//     let duration = start.elapsed();
    
//     println!("Time elapsed is: {:?}", duration);
//     println!("Time elapsed per op is: {:?}", duration/reps);
//     println!("Operations per second is: {:?} per op", duration);
    
// }
