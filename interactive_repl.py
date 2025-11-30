import sys
import os
from src.parser import Parser
from src.semantic import Semantic, SemanticError
from src.ir import IRGen
from src.optimizer import Optimizer
from src.codegen import VM

def run_code(code):
    try:
        # 1. Parse
        parser = Parser(code)
        prog = parser.parse()

        # 2. Semantic Analysis
        sem = Semantic()
        sem.check_program(prog)

        # 3. IR Generation
        ir = IRGen().gen_program(prog)

        # 4. Optimization
        opt = Optimizer()
        ir = opt.fold_constants(ir)
        ir = opt.dce(ir)

        # 5. Execution
        vm = VM(ir)
        vm.run()
    except Exception as e:
        print(f"Error: {e}")

def repl():
    print("Mini Pattern Language REPL")
    print("Type 'exit' to quit.")
    print("Enter your code snippet (one line at a time, or multiple lines for blocks).")
    print("Note: Since this is a simple REPL, complex multi-line blocks might be tricky.")
    print("It's best to paste full snippets or write single lines.")
    
    while True:
        try:
            user_input = input("mpl> ")
            if user_input.strip() == 'exit':
                break
            if not user_input.strip():
                continue
            
            # Simple heuristic: if line ends with {, keep reading until }
            if user_input.strip().endswith('{'):
                block = user_input + "\n"
                depth = 1
                while depth > 0:
                    line = input("...  ")
                    block += line + "\n"
                    depth += line.count('{') - line.count('}')
                run_code(block)
            else:
                run_code(user_input)
                
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except EOFError:
            break

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # File mode (already implemented in run.py, but added here for completeness)
        with open(sys.argv[1], 'r') as f:
            run_code(f.read())
    else:
        # Interactive Mode
        repl()
