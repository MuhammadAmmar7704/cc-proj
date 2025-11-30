# Symbol Explanations for Sample3.mpl

## Source Code:
```mpl
# Squares and Evens
loop i from 1 to 5 {
  let sq = i * i
  print sq
  if i % 2 == 0 {
    print 888
  }
}
```

---

## Line-by-Line Symbol Explanation

### Line 1: `# Squares and Evens`

| Symbol | Type | Category | Meaning |
|--------|------|----------|---------|
| `#` | Comment Marker | Syntax | Starts a comment |
| `Squares and Evens` | Comment Text | Documentation | Describes program purpose |

**What this line does:** Nothing (comments are ignored)

**Purpose:** Explains that program prints squares and marks even numbers.

---

### Line 2: `loop i from 1 to 5 {`

| Symbol | Type | Category | Meaning |
|--------|------|----------|---------|
| `loop` | Keyword | Control Flow | Loop construct |
| `i` | Identifier | Loop Variable | Counter (auto-declared as `int`) |
| `from` | Keyword | Loop Syntax | Marks start value |
| `1` | Literal | Integer Constant | Initial value of `i` |
| `to` | Keyword | Loop Syntax | Marks end value |
| `5` | Literal | Integer Constant | Final value of `i` (inclusive) |
| `{` | Delimiter | Block Start | Begins loop body |

**What this line does:** 
- Creates loop variable `i` (scope: inside loop only)
- Sets `i = 1` initially
- Will run loop body 5 times with `i` = 1, 2, 3, 4, 5
- After each iteration, increments `i` by 1
- Stops when `i > 5`

**Scope Note:** Variable `i` exists ONLY inside the `{ }` block.

---

### Line 3: `  let sq = i * i`

| Symbol | Type | Category | Meaning |
|--------|------|----------|---------|
| `let` | Keyword | Declaration | Declares integer variable |
| `sq` | Identifier | Variable Name | Stores the square value |
| `=` | Operator | Assignment | Assigns computed value |
| `i` | Identifier | Variable Reference | Loop counter (first operand) |
| `*` | Operator | Multiplication | Arithmetic operator |
| `i` | Identifier | Variable Reference | Loop counter (second operand) |

**What this line does:** 
- Calculates `i * i` (square of i)
- Stores result in new variable `sq`

**Iteration-by-iteration:**
- When `i=1`: `sq = 1 * 1 = 1`
- When `i=2`: `sq = 2 * 2 = 4`
- When `i=3`: `sq = 3 * 3 = 9`
- When `i=4`: `sq = 4 * 4 = 16`
- When `i=5`: `sq = 5 * 5 = 25`

**Scope Note:** `sq` is declared inside loop, so it's recreated each iteration.

---

### Line 4: `  print sq`

| Symbol | Type | Category | Meaning |
|--------|------|----------|---------|
| `print` | Keyword | I/O Statement | Output to console |
| `sq` | Identifier | Variable Reference | The square value to print |

**What this line does:** Prints the current square value.

**Output sequence:** `1`, `4`, `9`, `16`, `25`

---

### Line 5: `  if i % 2 == 0 {`

| Symbol | Type | Category | Meaning |
|--------|------|----------|---------|
| `if` | Keyword | Control Flow | Conditional statement |
| `i` | Identifier | Variable Reference | Loop counter |
| `%` | Operator | Modulo | Remainder after division |
| `2` | Literal | Integer Constant | Divisor (check for even) |
| `==` | Operator | Equality | Comparison operator |
| `0` | Literal | Integer Constant | Expected remainder for even |
| `{` | Delimiter | Block Start | Begins conditional block |

**What this line does:** 
- Calculates `i % 2` (remainder when dividing by 2)
- Checks if remainder equals 0
- If true (i is even), executes block

**Iteration-by-iteration:**
- `i=1`: `1 % 2 = 1`, `1 == 0` → **False** → Skip block
- `i=2`: `2 % 2 = 0`, `0 == 0` → **True** → Run block
- `i=3`: `3 % 2 = 1`, `1 == 0` → **False** → Skip block
- `i=4`: `4 % 2 = 0`, `0 == 0` → **True** → Run block
- `i=5`: `5 % 2 = 1`, `1 == 0` → **False** → Skip block

**Mathematical Concept:** Modulo operator `%` gives remainder:
- Even numbers: `n % 2 = 0`
- Odd numbers: `n % 2 = 1`

---

### Line 6: `    print 888`

| Symbol | Type | Category | Meaning |
|--------|------|----------|---------|
| `print` | Keyword | I/O Statement | Output to console |
| `888` | Literal | Integer Constant | Marker value for even numbers |

**What this line does:** Prints `888` when `i` is even.

**Runs only when:** `i = 2` or `i = 4`

---

### Line 7: `  }`

| Symbol | Type | Category | Meaning |
|--------|------|----------|---------|
| `}` | Delimiter | Block End | Ends if statement |

**What this line does:** Closes the conditional block.

---

### Line 8: `}`

| Symbol | Type | Category | Meaning |
|--------|------|----------|---------|
| `}` | Delimiter | Block End | Ends loop |

**What this line does:** 
- Marks end of loop body
- Triggers increment of `i`
- Jumps back to condition check

---

## Complete Program Execution Trace

```
Iteration 1 (i=1):
  sq = 1 * 1 = 1
  print 1          → Output: 1
  1 % 2 = 1, 1 == 0? No → Skip print 888

Iteration 2 (i=2):
  sq = 2 * 2 = 4
  print 4          → Output: 4
  2 % 2 = 0, 0 == 0? Yes → Run if block
  print 888        → Output: 888

Iteration 3 (i=3):
  sq = 3 * 3 = 9
  print 9          → Output: 9
  3 % 2 = 1, 1 == 0? No → Skip print 888

Iteration 4 (i=4):
  sq = 4 * 4 = 16
  print 16         → Output: 16
  4 % 2 = 0, 0 == 0? Yes → Run if block
  print 888        → Output: 888

Iteration 5 (i=5):
  sq = 5 * 5 = 25
  print 25         → Output: 25
  5 % 2 = 1, 1 == 0? No → Skip print 888

Loop ends (i becomes 6, 6 > 5)

Final Console Output:
1
4
888
9
16
888
25
```

---

## Key Concepts Demonstrated

### 1. Nested Control Structures
```mpl
loop ... {
  if ... {
    # Nested inside loop
  }
}
```
- Loop contains an if statement
- If statement runs every loop iteration
- Creates 2 levels of scope

### 2. Modulo Operator
```mpl
i % 2
```
- Returns remainder after division
- `i % 2 == 0` → i is even
- `i % 2 == 1` → i is odd

### 3. Variable Scope
```mpl
loop i from 1 to 5 {
  let sq = i * i    # sq exists only in this iteration
}
# sq does NOT exist here
# i does NOT exist here
```

### 4. Compound Expressions
```mpl
i % 2 == 0
```
- First: Calculate `i % 2`
- Then: Compare result to `0`
- Precedence: `%` before `==`

---

## Symbol Categories Used

### Keywords (5 used)
- `loop` - Loop construct
- `from`, `to` - Loop syntax
- `let` - Variable declaration
- `print` - Output statement
- `if` - Conditional

### Operators (4 used)
- `=` - Assignment
- `*` - Multiplication
- `%` - Modulo (remainder)
- `==` - Equality comparison

### Delimiters (2 used)
- `{` - Block start (used 2 times)
- `}` - Block end (used 2 times)

### Literals (5 used)
- `1`, `5` - Loop bounds
- `2` - Modulo divisor
- `0` - Comparison value
- `888` - Marker value

### Identifiers (2 used)
- `i` - Loop variable
- `sq` - Square variable

---

## Scope Analysis

```
Global Scope:
  (empty - no global variables)

Loop Scope (created 5 times):
  Variable: i (int)
  Value: 1, then 2, then 3, then 4, then 5
  
  Inner Scope (created 5 times, once per iteration):
    Variable: sq (int)
    Value: 1, then 4, then 9, then 16, then 25
    
    If Scope (created only when i is even):
      (no variables declared here)
```

---

## Type Checking

```
Line 3: let sq = i * i
        ↓        ↓   ↓
       int      int int  ✓ Valid (int * int → int)

Line 5: if i % 2 == 0
           ↓   ↓    ↓
          int int  int  ✓ Valid (all integers)
```

All type checks pass!

---

## Operator Precedence in This Program

```
Expression: i % 2 == 0

Precedence order:
1. % (modulo) - higher precedence
2. == (equality) - lower precedence

Evaluation:
  Step 1: Calculate i % 2
  Step 2: Compare result == 0
  
Example when i=4:
  Step 1: 4 % 2 = 0
  Step 2: 0 == 0 = true (1)
```

---

## Common Patterns

### Pattern 1: Square Calculation
```mpl
let sq = i * i
```
- Multiplies number by itself
- Alternative to power operator (which we don't have)

### Pattern 2: Even/Odd Check
```mpl
if i % 2 == 0 {
  # i is even
}
```
- Standard algorithm for parity check
- Works for any integer

### Pattern 3: Loop with Nested Conditional
```mpl
loop i from 1 to n {
  if condition {
    # runs only sometimes
  }
}
```
- Selective execution within loop
- Combines iteration with branching
