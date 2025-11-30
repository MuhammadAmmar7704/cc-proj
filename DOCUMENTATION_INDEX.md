# Complete Documentation Index

## 📁 Your Project Structure

```
mini_pattern_lang/
├── src/                          # Compiler source code
│   ├── lexer.py                  # Phase 1: Lexical Analysis
│   ├── parser.py                 # Phase 2: Syntax Analysis
│   ├── ast.py                    # AST node definitions
│   ├── semantic.py               # Phase 3: Semantic Analysis
│   ├── ir.py                     # Phase 4: IR Generation
│   ├── optimizer.py              # Phase 5: Optimization
│   └── codegen.py                # Phase 6: Code Generation (VM)
│
├── examples/                     # Test programs
│   ├── sample1.mpl              # Fibonacci, range, loops
│   ├── sample2.mpl              # Conditionals, precedence
│   ├── sample3.mpl              # Nested structures
│   └── sample_fib.mpl           # Simple fibonacci demo
│
├── diagrams/                     # 📊 HANDWRITTEN ARTIFACTS
│   ├── 01_dfa_lexical.png       # ✅ DFA diagram (reference)
│   ├── 02_parse_tree_let_n_7.png # ✅ Parse tree example 1
│   ├── 03_parse_tree_loop.png   # ✅ Parse tree example 2
│   ├── 04_symbol_table.png      # ✅ Symbol table example
│   ├── COMPLETE_DFA.md          # 📖 Full DFA specification
│   ├── SAMPLE1_LEXICAL_TRACE.md # 📖 Token-by-token trace
│   ├── SYMBOL_EXPLANATIONS_SAMPLE1.md  # 📖 What each symbol means
│   ├── SYMBOL_EXPLANATIONS_SAMPLE2.md  # 📖 Symbol meanings
│   ├── SYMBOL_EXPLANATIONS_SAMPLE3.md  # 📖 Symbol meanings
│   └── DIAGRAM_GUIDE.md         # 📖 How to draw diagrams
│
├── run.py                        # Main compiler runner
├── debug_run.py                  # Shows all 6 phases
├── run_tests.py                  # Runs all test cases
├── interactive_repl.py           # Interactive mode
├── app.py                        # 🌐 Streamlit web UI
├── README.md                     # Project overview
├── REFLECTION.md                 # 1-page reflection
├── ARTIFACTS.md                  # Handwritten artifact guide
└── submission.tar.gz             # Ready for submission
```

---

## 📚 Documentation Files Explained

### For Understanding the Code

1. **SYMBOL_EXPLANATIONS_SAMPLE1.md**
   - Line-by-line breakdown of sample1.mpl
   - What EVERY symbol means (let, seq, fibonacci, etc.)
   - Type system explanation
   - Precedence rules
   - **USE THIS:** To understand what each token represents

2. **SYMBOL_EXPLANATIONS_SAMPLE2.md**
   - Explains sample2.mpl (conditionals)
   - Operator precedence demonstration
   - If-else control flow
   - **USE THIS:** To explain comparison operators and branching

3. **SYMBOL_EXPLANATIONS_SAMPLE3.md**
   - Explains sample3.mpl (nested structures)
   - Modulo operator explanation
   - Scope analysis
   - **USE THIS:** To explain nested loops and conditionals

### For Drawing DFA

4. **COMPLETE_DFA.md**
   - Full state transition table
   - All 24+ states explained
   - How keywords are recognized
   - Example traces (how "loop" becomes LOOP token)
   - **USE THIS:** To draw the complete DFA by hand

5. **SAMPLE1_LEXICAL_TRACE.md**
   - Character-by-character trace of sample1.mpl
   - Shows DFA state changes for every input
   - Complete token stream (55 tokens)
   - **USE THIS:** To demonstrate lexical analysis in viva

### For Drawing Parse Trees

6. **DIAGRAM_GUIDE.md**
   - Parse tree structures for 3 examples
   - Shows grammar derivations
   - Symbol table examples
   - IR code examples
   - **USE THIS:** To draw parse trees and other phase diagrams

### Reference Images

7. **01_dfa_lexical.png** - DFA diagram (copy this!)
8. **02_parse_tree_let_n_7.png** - Parse tree for `let n = 7`
9. **03_parse_tree_loop.png** - Parse tree for loop statement
10. **04_symbol_table.png** - Symbol table with scopes

---

## 🎯 How to Use These for Your Submission

### For Handwritten Artifacts (Required)

You need to submit **3 handwritten artifacts**:

#### 1. DFA (Lexical Analysis)
**What to draw:** The complete DFA from COMPLETE_DFA.md
**Reference:** 01_dfa_lexical.png
**Steps:**
1. Open COMPLETE_DFA.md
2. Look at the state transition table
3. Draw circles for each state (S0, S1, S2, etc.)
4. Draw arrows with labels (digit, letter, =, etc.)
5. Use double circles for accepting states

#### 2. Parse Trees (2 required)
**What to draw:** Two parse trees from DIAGRAM_GUIDE.md
**Reference:** 02_parse_tree_let_n_7.png, 03_parse_tree_loop.png
**Suggestions:**
- Tree 1: `let n = 7` (simple)
- Tree 2: `loop i from 0 to 3 { print i }` (complex)

#### 3. Symbol Table
**What to draw:** Symbol table from DIAGRAM_GUIDE.md
**Reference:** 04_symbol_table.png
**Show:** Global scope and Loop scope example

---

## 🖥️ For the Viva Demonstration

### Option 1: Streamlit UI (Recommended)
```bash
streamlit run app.py
```
- Beautiful web interface
- Shows all 6 phases
- Type code and compile live
- Impresses the instructor!

### Option 2: Debug Mode
```bash
python debug_run.py examples/sample1.mpl
```
- Shows AST, IR, Optimization, Memory
- Good for explaining phases

### Option 3: Test Runner
```bash
python run_tests.py
```
- Runs all 3 test cases
- Shows they all pass

---

## 📝 For Explaining Symbols (During Viva)

When the instructor asks "What does this symbol mean?", use:

**For sample1.mpl:**
- Open `SYMBOL_EXPLANATIONS_SAMPLE1.md`
- Find the line they're asking about
- Read the "What this line does" section

**For sample2.mpl:**
- Open `SYMBOL_EXPLANATIONS_SAMPLE2.md`

**For sample3.mpl:**
- Open `SYMBOL_EXPLANATIONS_SAMPLE3.md`

Each file has:
- Symbol-by-symbol breakdown
- Type information
- Execution trace
- Output explanation

---

## 🎓 For Understanding Compiler Phases

### Phase 1: Lexical Analysis
**Read:** COMPLETE_DFA.md, SAMPLE1_LEXICAL_TRACE.md
**Key Point:** DFA converts characters to tokens

### Phase 2: Syntax Analysis
**Read:** DIAGRAM_GUIDE.md (Parse Tree sections)
**Key Point:** Tokens → AST using grammar rules

### Phase 3: Semantic Analysis
**Read:** SYMBOL_EXPLANATIONS files (Type Checking sections)
**Key Point:** Check types and scopes

### Phase 4: IR Generation
**Read:** DIAGRAM_GUIDE.md (IR sections)
**Key Point:** AST → Three-address code

### Phase 5: Optimization
**Read:** DIAGRAM_GUIDE.md (Optimization sections)
**Key Point:** Constant folding, dead code elimination

### Phase 6: Code Generation
**Read:** DIAGRAM_GUIDE.md (Output sections)
**Key Point:** Execute IR on virtual machine

---

## ✅ Submission Checklist

- [ ] Print 4 diagram images (01-04.png)
- [ ] OR draw them by hand using the .md guides
- [ ] Print REFLECTION.md (1 page)
- [ ] Print annotated code (src/*.py with comments)
- [ ] Prepare submission.tar.gz
- [ ] Test Streamlit app works
- [ ] Practice explaining symbols using SYMBOL_EXPLANATIONS files
- [ ] Practice running debug_run.py for viva

---

## 🚀 Quick Start for Viva

1. **Start Streamlit:**
   ```bash
   cd /home/r64/Desktop/Desktop/Academics/mini_pattern_lang
   streamlit run app.py
   ```

2. **Open symbol explanations in another window:**
   - SYMBOL_EXPLANATIONS_SAMPLE1.md
   - SYMBOL_EXPLANATIONS_SAMPLE2.md
   - SYMBOL_EXPLANATIONS_SAMPLE3.md

3. **Have debug_run.py ready:**
   ```bash
   python debug_run.py examples/sample1.mpl
   ```

4. **Know your test cases:**
   - Sample1: Fibonacci, range, loops
   - Sample2: Conditionals, precedence
   - Sample3: Nested structures, modulo

---

## 💡 Tips for Viva

1. **When asked about a symbol:**
   - Ctrl+F in SYMBOL_EXPLANATIONS file
   - Find the symbol
   - Read the "Meaning" column

2. **When asked about DFA:**
   - Open COMPLETE_DFA.md
   - Show the transition table
   - Trace an example (e.g., "loop" → LOOP)

3. **When asked about phases:**
   - Run debug_run.py
   - Point to each section
   - Explain what changed

4. **When asked about output:**
   - Show Streamlit app
   - Type code
   - Click "Compile & Run"
   - Show all tabs

---

## 📞 Quick Reference

**All Keywords:**
let, seq, print, loop, from, to, if, else, true, false, fibonacci, range

**All Operators:**
=, +, -, *, /, %, <, <=, >, >=, ==, !=, &&, ||

**Types:**
- int (single integer)
- seq (sequence of integers)

**Built-in Functions:**
- fibonacci(n) → generates n Fibonacci numbers
- range(start, end) → generates numbers from start to end (inclusive)

---

Good luck with your submission and viva! 🎉
