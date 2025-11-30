# Symbol Explanations for Sample Programs

## SAMPLE1.MPL - Complete Symbol Breakdown

### Source Code:
```mpl
let n = 7
seq s = fibonacci(n)
print s
seq t = range(1, 5)
print t
let x = 2 * 3 + 4
print x
loop i from 0 to 3 {
  print i
}
```

---

## Line-by-Line Symbol Explanation

### Line 1: `let n = 7`

| Symbol | Type | Category | Meaning |
|--------|------|----------|---------|
| `let` | Keyword | Declaration | Declares a new integer variable |
| `n` | Identifier | Variable Name | Name of the variable being created |
| `=` | Operator | Assignment | Assigns a value to the variable |
| `7` | Literal | Integer Constant | The numeric value 7 |

**What this line does:** Creates a variable named `n` and stores the value 7 in it.

---

### Line 2: `seq s = fibonacci(n)`

| Symbol | Type | Category | Meaning |
|--------|------|----------|---------|
| `seq` | Keyword | Declaration | Declares a new sequence (list) variable |
| `s` | Identifier | Variable Name | Name of the sequence being created |
| `=` | Operator | Assignment | Assigns a sequence to the variable |
| `fibonacci` | Keyword | Built-in Function | Generates Fibonacci sequence |
| `(` | Delimiter | Function Call Start | Begins function arguments |
| `n` | Identifier | Variable Reference | Uses the value stored in variable `n` |
| `)` | Delimiter | Function Call End | Ends function arguments |

**What this line does:** Creates a sequence variable `s` containing the first 7 Fibonacci numbers: [0, 1, 1, 2, 3, 5, 8]

**Why it works:** `n` was set to 7 in line 1, so `fibonacci(n)` generates 7 numbers.

---

### Line 3: `print s`

| Symbol | Type | Category | Meaning |
|--------|------|----------|---------|
| `print` | Keyword | I/O Statement | Outputs value to console |
| `s` | Identifier | Variable Reference | The sequence to print |

**What this line does:** Displays the contents of `s` on the screen: `[0, 1, 1, 2, 3, 5, 8]`

---

### Line 4: `seq t = range(1, 5)`

| Symbol | Type | Category | Meaning |
|--------|------|----------|---------|
| `seq` | Keyword | Declaration | Declares a sequence variable |
| `t` | Identifier | Variable Name | Name of the new sequence |
| `=` | Operator | Assignment | Assigns value |
| `range` | Keyword | Built-in Function | Generates number range |
| `(` | Delimiter | Function Call Start | - |
| `1` | Literal | Integer Constant | Start value (inclusive) |
| `,` | Delimiter | Argument Separator | Separates function arguments |
| `5` | Literal | Integer Constant | End value (inclusive) |
| `)` | Delimiter | Function Call End | - |

**What this line does:** Creates sequence `t` = [1, 2, 3, 4, 5]

**Note:** `range(1, 5)` includes both 1 AND 5 (different from Python!)

---

### Line 5: `print t`

| Symbol | Type | Category | Meaning |
|--------|------|----------|---------|
| `print` | Keyword | I/O Statement | Output to console |
| `t` | Identifier | Variable Reference | The sequence to print |

**What this line does:** Displays `[1, 2, 3, 4, 5]`

---

### Line 6: `let x = 2 * 3 + 4`

| Symbol | Type | Category | Meaning |
|--------|------|----------|---------|
| `let` | Keyword | Declaration | Declares integer variable |
| `x` | Identifier | Variable Name | Name of the variable |
| `=` | Operator | Assignment | Assigns value |
| `2` | Literal | Integer Constant | First operand |
| `*` | Operator | Multiplication | Arithmetic operator (higher precedence) |
| `3` | Literal | Integer Constant | Second operand |
| `+` | Operator | Addition | Arithmetic operator (lower precedence) |
| `4` | Literal | Integer Constant | Third operand |

**What this line does:** Calculates `(2 * 3) + 4 = 6 + 4 = 10` and stores in `x`

**Order of Operations:** Multiplication happens BEFORE addition (standard math rules)

---

### Line 7: `print x`

| Symbol | Type | Category | Meaning |
|--------|------|----------|---------|
| `print` | Keyword | I/O Statement | Output to console |
| `x` | Identifier | Variable Reference | The value to print |

**What this line does:** Displays `10`

---

### Line 8: `loop i from 0 to 3 {`

| Symbol | Type | Category | Meaning |
|--------|------|----------|---------|
| `loop` | Keyword | Control Flow | Starts a loop construct |
| `i` | Identifier | Loop Variable | Counter variable (auto-declared) |
| `from` | Keyword | Loop Syntax | Specifies start value |
| `0` | Literal | Integer Constant | Starting value of `i` |
| `to` | Keyword | Loop Syntax | Specifies end value |
| `3` | Literal | Integer Constant | Ending value of `i` (inclusive) |
| `{` | Delimiter | Block Start | Begins loop body |

**What this line does:** Creates a loop where `i` goes from 0 to 3 (runs 4 times: i=0, 1, 2, 3)

**Scope:** Variable `i` only exists inside the loop block

---

### Line 9: `  print i`

| Symbol | Type | Category | Meaning |
|--------|------|----------|---------|
| `print` | Keyword | I/O Statement | Output to console |
| `i` | Identifier | Variable Reference | Current loop counter value |

**What this line does:** Prints the current value of `i` each iteration

**Output:** 
```
0
1
2
3
```

---

### Line 10: `}`

| Symbol | Type | Category | Meaning |
|--------|------|----------|---------|
| `}` | Delimiter | Block End | Ends loop body |

**What this line does:** Marks the end of the loop. After this, `i` no longer exists.

---

## Complete Symbol Categories Summary

### Keywords (Reserved Words - Cannot be used as variable names)
```
let       - Declare integer variable
seq       - Declare sequence variable
print     - Output statement
loop      - Loop construct
from      - Loop start keyword
to        - Loop end keyword
if        - Conditional statement
else      - Alternative branch
fibonacci - Built-in sequence generator
range     - Built-in sequence generator
true      - Boolean literal (value 1)
false     - Boolean literal (value 0)
```

### Operators
```
=         - Assignment
+         - Addition
-         - Subtraction / Negation
*         - Multiplication
/         - Division (integer)
%         - Modulo (remainder)
<         - Less than
<=        - Less than or equal
>         - Greater than
>=        - Greater than or equal
==        - Equality check
!=        - Not equal
&&        - Logical AND
||        - Logical OR
```

### Delimiters
```
(         - Left parenthesis (function calls, grouping)
)         - Right parenthesis
{         - Left brace (code blocks)
}         - Right brace
,         - Comma (argument separator)
```

### Literals
```
Numbers   - Integer constants (e.g., 0, 7, 123)
```

### Identifiers
```
Variables - User-defined names (e.g., n, s, t, x, i)
Rules:    - Must start with letter or underscore
          - Can contain letters, digits, underscores
          - Cannot be a keyword
```

---

## Type System Explanation

### `int` Type
- Stores single integer values
- Declared with `let`
- Examples: `let n = 7`, `let x = 10`
- Can be used in arithmetic: `+`, `-`, `*`, `/`, `%`
- Can be compared: `<`, `>`, `==`, etc.

### `seq` Type
- Stores sequence (list) of integers
- Declared with `seq`
- Can only be created by `fibonacci()` or `range()`
- Cannot do arithmetic on sequences
- Can be printed as a whole
- Examples: `seq s = fibonacci(7)` → `[0, 1, 1, 2, 3, 5, 8]`

---

## Precedence Rules (Highest to Lowest)

1. **Parentheses** `( )`
2. **Unary Minus** `-x`
3. **Multiplication/Division/Modulo** `*`, `/`, `%`
4. **Addition/Subtraction** `+`, `-`
5. **Comparison** `<`, `<=`, `>`, `>=`
6. **Equality** `==`, `!=`
7. **Logical AND** `&&`
8. **Logical OR** `||`

**Example:** `2 + 3 * 4` = `2 + (3 * 4)` = `2 + 12` = `14`

---

## Scope Rules

### Global Scope
Variables declared outside any block:
```mpl
let x = 10    # x is global
```

### Loop Scope
Variables declared in loop header exist only in loop:
```mpl
loop i from 0 to 5 {
  # i exists here
}
# i does NOT exist here
```

### If Scope
Variables in if/else blocks:
```mpl
if x > 5 {
  let y = 10   # y exists only in this block
}
# y does NOT exist here
```

---

## Common Patterns Explained

### Pattern 1: Calculate and Store
```mpl
let result = 2 * 3 + 4
```
- Evaluates expression first: `6 + 4 = 10`
- Then stores in variable `result`

### Pattern 2: Use Variable in Function
```mpl
let n = 7
seq s = fibonacci(n)
```
- First line stores 7 in `n`
- Second line reads `n` (gets 7) and passes to `fibonacci`

### Pattern 3: Loop with Print
```mpl
loop i from 0 to 3 {
  print i
}
```
- Creates temporary variable `i`
- Runs body 4 times with i = 0, 1, 2, 3
- Destroys `i` after loop ends

### Pattern 4: Sequence Generation
```mpl
seq numbers = range(1, 10)
```
- Creates list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
- Stores in variable `numbers`
