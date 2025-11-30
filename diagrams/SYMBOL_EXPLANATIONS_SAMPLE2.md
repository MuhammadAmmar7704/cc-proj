# Symbol Explanations for Sample2.mpl

## Source Code:
```mpl
# Range and condition demo
seq r = range(2, 6)
print r
let a = 3 + 4 * 2
print a
if a > 10 {
  print 1
} else {
  print 0
}
```

---

## Line-by-Line Symbol Explanation

### Line 1: `# Range and condition demo`

| Symbol | Type | Category | Meaning |
|--------|------|----------|---------|
| `#` | Comment Marker | Syntax | Starts a comment (ignored by compiler) |
| `Range and condition demo` | Comment Text | Documentation | Human-readable note |

**What this line does:** Nothing! Comments are skipped during lexical analysis.

**Purpose:** Explains what the program demonstrates.

---

### Line 2: `seq r = range(2, 6)`

| Symbol | Type | Category | Meaning |
|--------|------|----------|---------|
| `seq` | Keyword | Declaration | Declares a sequence variable |
| `r` | Identifier | Variable Name | Name of the sequence |
| `=` | Operator | Assignment | Assigns value to variable |
| `range` | Keyword | Built-in Function | Generates integer sequence |
| `(` | Delimiter | Function Start | Opens parameter list |
| `2` | Literal | Integer Constant | Start value (inclusive) |
| `,` | Delimiter | Separator | Separates arguments |
| `6` | Literal | Integer Constant | End value (inclusive) |
| `)` | Delimiter | Function End | Closes parameter list |

**What this line does:** Creates sequence `r` = [2, 3, 4, 5, 6]

**Note:** Both 2 and 6 are included in the range.

---

### Line 3: `print r`

| Symbol | Type | Category | Meaning |
|--------|------|----------|---------|
| `print` | Keyword | I/O Statement | Outputs to console |
| `r` | Identifier | Variable Reference | The sequence to display |

**What this line does:** Displays `[2, 3, 4, 5, 6]`

---

### Line 4: `let a = 3 + 4 * 2`

| Symbol | Type | Category | Meaning |
|--------|------|----------|---------|
| `let` | Keyword | Declaration | Declares integer variable |
| `a` | Identifier | Variable Name | Name of the variable |
| `=` | Operator | Assignment | Assigns computed value |
| `3` | Literal | Integer Constant | First operand |
| `+` | Operator | Addition | Lower precedence operator |
| `4` | Literal | Integer Constant | Second operand |
| `*` | Operator | Multiplication | **Higher precedence** operator |
| `2` | Literal | Integer Constant | Third operand |

**What this line does:** 
1. Calculates `4 * 2` first (precedence) = `8`
2. Then calculates `3 + 8` = `11`
3. Stores `11` in variable `a`

**Key Concept:** Demonstrates operator precedence (PEMDAS/BODMAS rules)

---

### Line 5: `print a`

| Symbol | Type | Category | Meaning |
|--------|------|----------|---------|
| `print` | Keyword | I/O Statement | Output to console |
| `a` | Identifier | Variable Reference | The value to print |

**What this line does:** Displays `11`

---

### Line 6: `if a > 10 {`

| Symbol | Type | Category | Meaning |
|--------|------|----------|---------|
| `if` | Keyword | Control Flow | Conditional statement |
| `a` | Identifier | Variable Reference | Left operand of comparison |
| `>` | Operator | Comparison | Greater than operator |
| `10` | Literal | Integer Constant | Right operand of comparison |
| `{` | Delimiter | Block Start | Begins true branch |

**What this line does:** 
- Evaluates `a > 10` → `11 > 10` → **True**
- Since true, executes the block inside `{ }`

**Boolean Logic:** In this language, comparisons return:
- `1` for true
- `0` for false

---

### Line 7: `  print 1`

| Symbol | Type | Category | Meaning |
|--------|------|----------|---------|
| `print` | Keyword | I/O Statement | Output to console |
| `1` | Literal | Integer Constant | Value to print (represents "true") |

**What this line does:** Prints `1` (because condition was true)

**This line runs:** Because `a > 10` evaluated to true.

---

### Line 8: `} else {`

| Symbol | Type | Category | Meaning |
|--------|------|----------|---------|
| `}` | Delimiter | Block End | Ends true branch |
| `else` | Keyword | Control Flow | Alternative branch |
| `{` | Delimiter | Block Start | Begins false branch |

**What this line does:** Defines what to do if condition is false.

**This block is skipped:** Because the `if` condition was true.

---

### Line 9: `  print 0`

| Symbol | Type | Category | Meaning |
|--------|------|----------|---------|
| `print` | Keyword | I/O Statement | Output to console |
| `0` | Literal | Integer Constant | Value to print (represents "false") |

**What this line does:** Would print `0` if condition was false.

**This line does NOT run:** Because we took the `if` branch, not `else`.

---

### Line 10: `}`

| Symbol | Type | Category | Meaning |
|--------|------|----------|---------|
| `}` | Delimiter | Block End | Ends else branch |

**What this line does:** Closes the entire if-else statement.

---

## Complete Program Flow

```
Step 1: Skip comment
Step 2: Create r = [2, 3, 4, 5, 6]
Step 3: Print r → Output: [2, 3, 4, 5, 6]
Step 4: Calculate a = 3 + (4 * 2) = 11
Step 5: Print a → Output: 11
Step 6: Check if 11 > 10 → TRUE
Step 7: Print 1 → Output: 1
Step 8-9: Skip else block
Step 10: End program

Final Output:
[2, 3, 4, 5, 6]
11
1
```

---

## Key Concepts Demonstrated

### 1. Comments
```mpl
# This is a comment
```
- Start with `#`
- Continue to end of line
- Completely ignored by compiler
- Used for documentation

### 2. Operator Precedence
```mpl
3 + 4 * 2
```
- `*` has higher precedence than `+`
- Evaluated as `3 + (4 * 2)` = `3 + 8` = `11`
- NOT `(3 + 4) * 2` = `7 * 2` = `14`

### 3. Comparison Operators
```mpl
a > 10
```
- Returns `1` if true
- Returns `0` if false
- Can be used in `if` statements

### 4. If-Else Control Flow
```mpl
if condition {
  # runs if condition is true (non-zero)
} else {
  # runs if condition is false (zero)
}
```

---

## Symbol Categories Used in This Program

### Keywords (7 used)
- `seq` - Sequence declaration
- `range` - Built-in function
- `print` - Output statement
- `let` - Integer declaration
- `if` - Conditional
- `else` - Alternative branch

### Operators (3 used)
- `=` - Assignment
- `+` - Addition
- `*` - Multiplication
- `>` - Greater than comparison

### Delimiters (6 used)
- `(` `)` - Function call parentheses
- `{` `}` - Code block braces
- `,` - Argument separator

### Literals (6 used)
- `2`, `6` - Range bounds
- `3`, `4`, `2` - Arithmetic operands
- `10` - Comparison value
- `1`, `0` - Boolean representations

### Identifiers (2 used)
- `r` - Sequence variable
- `a` - Integer variable

---

## Type Checking in This Program

```
Line 2: seq r = range(2, 6)
        ↓       ↓
       seq     seq  ✓ Types match

Line 4: let a = 3 + 4 * 2
        ↓       ↓
       int     int  ✓ Types match

Line 6: if a > 10
           ↓   ↓
          int int  ✓ Comparison valid
```

All type checks pass! The program is semantically valid.
