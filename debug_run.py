import sys
from pathlib import Path
from src.parser import Parser
from src.semantic import Semantic
from src.ir import IRGen
from src.optimizer import Optimizer
from src.codegen import VM

def print_section(title):
    print(f"\n{'='*20} {title} {'='*20}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python debug_run.py <source.mpl>")
        sys.exit(1)
    
    src_path = Path(sys.argv[1])
    code = src_path.read_text()
    
    print_section("PHASE 1: SOURCE CODE")
    print(code)

    # 1. Parsing
    print_section("PHASE 2: PARSING (AST)")
    parser = Parser(code)
    prog = parser.parse()
    for stmt in prog.body:
        print(stmt)

    # 2. Semantic Analysis
    print_section("PHASE 3: SEMANTIC ANALYSIS")
    sem = Semantic()
    try:
        sem.check_program(prog)
        print("Semantic Check Passed: All types and scopes are valid.")
        # Print symbol table snapshot if possible (mocking for demo)
        print("Symbol Table (Final State):", sem.scopes)
    except Exception as e:
        print(f"Semantic Error: {e}")
        sys.exit(1)

    # 3. IR Generation
    print_section("PHASE 4: IR GENERATION (Unoptimized)")
    ir_gen = IRGen()
    ir = ir_gen.gen_program(prog)
    for i, instr in enumerate(ir):
        print(f"{i:02}: {instr}")

    # 4. Optimization
    print_section("PHASE 5: OPTIMIZATION")
    opt = Optimizer()
    ir_opt = opt.fold_constants(ir)
    ir_opt = opt.dce(ir_opt)
    for i, instr in enumerate(ir_opt):
        print(f"{i:02}: {instr}")

    # 5. Code Generation / Execution
    print_section("PHASE 6: EXECUTION (VM OUTPUT)")
    vm = VM(ir_opt)
    vm.run()
    
    print_section("FINAL MEMORY STATE")
    print(vm.vars)

if __name__ == '__main__':
    main()
