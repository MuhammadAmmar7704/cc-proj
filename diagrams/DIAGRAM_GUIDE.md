# Complete Diagram Guide for Handwritten Artifacts

## Symbol Legend (Draw this on every page)

```
SYMBOLS USED:
○ = Single Circle = State (DFA) or Non-terminal (Parse Tree)
◎ = Double Circle = Accepting State (DFA) or Terminal (Parse Tree)
□ = Box = Code/Instruction
→ = Arrow = Transition or Derivation
├─ = Tree Branch
```

---

## EXAMPLE 1: `let x = 2 * 3 + 4`

### Phase 1: Lexical Analysis (DFA already provided)
**Tokens Generated:**
```
[LET] [IDENT:x] [=] [NUMBER:2] [*] [NUMBER:3] [+] [NUMBER:4] [EOF]
```

### Phase 2: Syntax Analysis (Parse Tree)
```
                    statement
                        |
                    let_stmt
                   /  |  |  \
                let   x  =  expr
                              |
                            logic
                              |
                           equality
                              |
                             rel
                              |
                             add
                           /  |  \
                         mul  +  mul
                        / | \     |
                       2  *  3    4
```

**What each symbol means:**
- `statement` = Top-level program construct
- `let_stmt` = Variable declaration statement
- `expr` = Expression (can be math, variable, etc.)
- `logic/equality/rel/add/mul` = Precedence levels (mul binds tighter than add)
- Terminal symbols (let, x, =, 2, *, 3, +, 4) = Actual tokens from code

### Phase 3: Semantic Analysis
**Symbol Table:**
```
┌─────────────┬──────────┬──────┬──────┐
│ Scope Level │ Variable │ Type │ Line │
├─────────────┼──────────┼──────┼──────┤
│ Global (0)  │    x     │ int  │  1   │
└─────────────┴──────────┴──────┴──────┘
```

**Type Checking:**
- `2 * 3`: int * int → int ✓
- `(result) + 4`: int + int → int ✓
- `let x = (int)`: Valid assignment ✓

### Phase 4: IR Generation (Three-Address Code)
```
Instruction #  | Operation
─────────────────────────────
00:            | t1 = 2 * 3
01:            | t2 = t1 + 4
02:            | x = t2
```

**What each symbol means:**
- `t1, t2` = Temporary variables (compiler-generated)
- `=` = Assignment
- `*`, `+` = Binary operations

### Phase 5: Optimization (Constant Folding)
```
BEFORE:              AFTER:
t1 = 2 * 3    →      x = 10
t2 = t1 + 4
x = t2
```

**Optimization Applied:** Constant Folding
- Compiler calculated `2 * 3 = 6` at compile time
- Then calculated `6 + 4 = 10` at compile time
- Eliminated temporary variables

### Phase 6: Execution Output
```
Memory State:
┌──────────┬───────┐
│ Variable │ Value │
├──────────┼───────┤
│    x     │  10   │
└──────────┴───────┘

Console Output: (none - no print statement)
```

---

## EXAMPLE 2: `seq s = fibonacci(7)`

### Phase 1: Lexical Analysis
**Tokens:**
```
[SEQ] [IDENT:s] [=] [FIBONACCI] [(] [NUMBER:7] [)] [EOF]
```

### Phase 2: Syntax Analysis
```
                    statement
                        |
                    seq_stmt
                   /  |  |  \
                seq   s  =  seq_expr
                              |
                        SeqFibonacci
                              |
                            expr
                              |
                           Number
                              |
                              7
```

**What each symbol means:**
- `seq_stmt` = Sequence variable declaration
- `seq_expr` = Special expression that returns a sequence
- `SeqFibonacci` = Built-in function to generate Fibonacci numbers

### Phase 3: Semantic Analysis
**Symbol Table:**
```
┌─────────────┬──────────┬──────┬──────┐
│ Scope Level │ Variable │ Type │ Line │
├─────────────┼──────────┼──────┼──────┤
│ Global (0)  │    s     │ seq  │  1   │
└─────────────┴──────────┴──────┴──────┘
```

**Type Checking:**
- `fibonacci(7)`: Takes int, returns seq ✓
- `seq s = seq`: Valid assignment ✓

### Phase 4: IR Generation
```
00: t1 = fib 7
01: s = t1
```

**What each symbol means:**
- `fib` = Special instruction to generate Fibonacci sequence
- `7` = Number of elements to generate

### Phase 5: Optimization
```
No optimization applied
(fib is a complex operation, not constant-foldable)
```

### Phase 6: Execution Output
```
Memory State:
┌──────────┬──────────────────────────┐
│ Variable │         Value            │
├──────────┼──────────────────────────┤
│    s     │ [0, 1, 1, 2, 3, 5, 8]   │
└──────────┴──────────────────────────┘

Console Output: (none - no print statement)
```

---

## EXAMPLE 3: `loop i from 0 to 3 { print i }`

### Phase 1: Lexical Analysis
**Tokens:**
```
[LOOP] [IDENT:i] [FROM] [NUMBER:0] [TO] [NUMBER:3] 
[{] [PRINT] [IDENT:i] [}] [EOF]
```

### Phase 2: Syntax Analysis
```
                    statement
                        |
                    loop_stmt
          /    |    |    |    |    \
       loop   i  from   0   to   3  compound
                                       |
                                      { statement }
                                           |
                                       print_stmt
                                         /    \
                                     print     i
```

**What each symbol means:**
- `loop_stmt` = Loop control structure
- `compound` = Block of statements inside { }
- `print_stmt` = Output statement

### Phase 3: Semantic Analysis
**Symbol Table (Inside Loop):**
```
┌─────────────┬──────────┬──────┬──────┐
│ Scope Level │ Variable │ Type │ Line │
├─────────────┼──────────┼──────┼──────┤
│ Loop (1)    │    i     │ int  │  1   │
└─────────────┴──────────┴──────┴──────┘
```

**Scope Note:** Variable `i` only exists inside the loop.
After loop ends, `i` is destroyed.

### Phase 4: IR Generation (Control Flow)
```
00: i = 0              # Initialize loop variable
01: label L1           # Loop start marker
02: t1 = i <= 3        # Check condition
03: jz t1 L2           # If false, jump to end
04: print i            # Loop body
05: i = i + 1          # Increment
06: jmp L1             # Jump back to start
07: label L2           # Loop end marker
```

**What each symbol means:**
- `label` = Jump target (like a bookmark in code)
- `jz` = "Jump if Zero" (conditional jump)
- `jmp` = Unconditional jump
- `<=` = Less than or equal comparison

### Phase 5: Optimization
```
No optimization applied
(Control flow cannot be simplified)
```

### Phase 6: Execution Output
```
Execution Trace:
i=0: Check 0<=3? Yes → Print 0 → i becomes 1
i=1: Check 1<=3? Yes → Print 1 → i becomes 2
i=2: Check 2<=3? Yes → Print 2 → i becomes 3
i=3: Check 3<=3? Yes → Print 3 → i becomes 4
i=4: Check 4<=3? No  → Exit loop

Console Output:
0
1
2
3

Final Memory:
┌──────────┬───────┐
│ Variable │ Value │
├──────────┼───────┤
│    i     │   4   │
└──────────┴───────┘
```

---

## How to Draw These for Submission

1. **Use separate pages for each example**
2. **Draw all 6 phases for each example**
3. **Add the symbol legend at the top of each page**
4. **Use rulers for tables and boxes**
5. **Use different colors (optional):**
   - Blue for keywords
   - Red for operators
   - Green for values
   - Black for structure

6. **Label each section clearly:**
   ```
   Example 1: let x = 2 * 3 + 4
   ═══════════════════════════════
   Phase 1: Lexical Analysis
   ───────────────────────────────
   [Your diagram here]
   ```
