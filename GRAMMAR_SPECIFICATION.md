# Mini Pattern Language - Complete Formal Grammar Specification

## Language Overview

Mini Pattern Language is a domain-specific language designed for numerical pattern generation and manipulation. It supports integer arithmetic, sequence operations (Fibonacci and range generation), control flow (loops and conditionals), and basic I/O operations.

## Lexical Specification

### Keywords
```
let         - Integer variable declaration
seq         - Sequence variable declaration
print       - Output statement
loop        - Loop construct
from        - Loop start bound
to          - Loop end bound
if          - Conditional statement
else        - Alternative branch
true        - Boolean literal (evaluates to 1)
false       - Boolean literal (evaluates to 0)
fibonacci   - Built-in sequence generator
range       - Built-in sequence generator
```

### Operators
```
Arithmetic:
  +         - Addition
  -         - Subtraction or unary negation
  *         - Multiplication
  /         - Integer division
  %         - Modulo (remainder)

Comparison:
  <         - Less than
  <=        - Less than or equal
  >         - Greater than
  >=        - Greater than or equal
  ==        - Equality
  !=        - Inequality

Logical:
  &&        - Logical AND
  ||        - Logical OR

Assignment:
  =         - Assignment operator
```

### Delimiters
```
(           - Left parenthesis
)           - Right parenthesis
{           - Left brace
}           - Right brace
,           - Comma
```

### Literals
```
NUMBER      - Integer literal (sequence of digits)
              Examples: 0, 7, 123, 9999
```

### Identifiers
```
IDENT       - Variable names
              Rules:
                - Must start with letter (a-z, A-Z) or underscore (_)
                - Can contain letters, digits, underscores
                - Cannot be a keyword
              Examples: n, myVar, counter_1, _temp
```

### Comments
```
#           - Single-line comment (from # to end of line)
              Example: # This is a comment
```

### Whitespace
```
SPACE       - Space character (ignored)
TAB         - Tab character (ignored)
NEWLINE     - Line terminator (statement separator)
```

## Regular Expression Patterns

### Token Patterns (Regex)

```regex
Keywords (exact match):
  let|seq|print|loop|from|to|if|else|true|false|fibonacci|range

Identifiers:
  [a-zA-Z_][a-zA-Z0-9_]*
  Note: Must not match any keyword

Numbers (Integer Literals):
  [0-9]+
  Examples: 0, 7, 123, 9999

Operators (Two-Character):
  ==|!=|<=|>=|&&|\|\|

Operators (Single-Character):
  [+\-*/%<>=]

Delimiters:
  [(){},]

Comments:
  #.*
  Note: Matches from # to end of line

Whitespace:
  [ \t]+        (spaces and tabs - ignored)
  \n            (newline - creates NEWLINE token)
```

### Complete Lexical Pattern (Priority Order)

The lexer must check patterns in this order to avoid conflicts:

```regex
1. Whitespace (skip):     [ \t]+
2. Newline:               \n
3. Comments (skip):       #[^\n]*
4. Keywords:              let|seq|print|loop|from|to|if|else|true|false|fibonacci|range
5. Identifiers:           [a-zA-Z_][a-zA-Z0-9_]*
6. Numbers:               [0-9]+
7. Two-char operators:    ==|!=|<=|>=|&&|\|\|
8. Single-char operators: [+\-*/%<>=]
9. Delimiters:            [(){},]
```

### Pattern Matching Examples

```
Input: "let n = 7"

Step 1: "let"   matches keyword pattern    → Token: LET
Step 2: " "     matches whitespace         → Skip
Step 3: "n"     matches identifier pattern → Token: IDENT("n")
Step 4: " "     matches whitespace         → Skip
Step 5: "="     matches operator pattern   → Token: ASSIGN("=")
Step 6: " "     matches whitespace         → Skip
Step 7: "7"     matches number pattern     → Token: NUMBER(7)
```

```
Input: "fibonacci(10)"

Step 1: "fibonacci" matches keyword pattern → Token: FIBONACCI
Step 2: "("         matches delimiter       → Token: LPAREN
Step 3: "10"        matches number pattern  → Token: NUMBER(10)
Step 4: ")"         matches delimiter       → Token: RPAREN
```

```
Input: "i <= 5"

Step 1: "i"     matches identifier pattern → Token: IDENT("i")
Step 2: " "     matches whitespace         → Skip
Step 3: "<="    matches two-char operator  → Token: LE
Step 4: " "     matches whitespace         → Skip
Step 5: "5"     matches number pattern     → Token: NUMBER(5)
```

### Regex-Based Token Recognition

If implementing with regex library:

```python
import re

# Token patterns in priority order
TOKEN_PATTERNS = [
    ('WHITESPACE',  r'[ \t]+'),              # Skip
    ('NEWLINE',     r'\n'),                  # Statement separator
    ('COMMENT',     r'#[^\n]*'),             # Skip
    ('KEYWORD',     r'\b(let|seq|print|loop|from|to|if|else|true|false|fibonacci|range)\b'),
    ('NUMBER',      r'\d+'),                 # Integer literals
    ('IDENT',       r'[a-zA-Z_][a-zA-Z0-9_]*'),  # Identifiers
    ('EQ',          r'=='),                  # Equality
    ('NE',          r'!='),                  # Not equal
    ('LE',          r'<='),                  # Less or equal
    ('GE',          r'>='),                  # Greater or equal
    ('AND',         r'&&'),                  # Logical AND
    ('OR',          r'\|\|'),                # Logical OR
    ('ASSIGN',      r'='),                   # Assignment
    ('LT',          r'<'),                   # Less than
    ('GT',          r'>'),                   # Greater than
    ('PLUS',        r'\+'),                  # Addition
    ('MINUS',       r'-'),                   # Subtraction
    ('MUL',         r'\*'),                  # Multiplication
    ('DIV',         r'/'),                   # Division
    ('MOD',         r'%'),                   # Modulo
    ('LPAREN',      r'\('),                  # Left paren
    ('RPAREN',      r'\)'),                  # Right paren
    ('LBRACE',      r'\{'),                  # Left brace
    ('RBRACE',      r'\}'),                  # Right brace
    ('COMMA',       r','),                   # Comma
]

# Example tokenizer using regex
def tokenize(code):
    tokens = []
    pos = 0
    line = 1
    
    while pos < len(code):
        match = None
        for token_type, pattern in TOKEN_PATTERNS:
            regex = re.compile(pattern)
            match = regex.match(code, pos)
            if match:
                value = match.group(0)
                if token_type not in ('WHITESPACE', 'COMMENT'):
                    tokens.append((token_type, value, line))
                if token_type == 'NEWLINE':
                    line += 1
                pos = match.end()
                break
        
        if not match:
            raise SyntaxError(f'Invalid character at position {pos}')
    
    return tokens
```

## Lexical Grammar (Regular Expressions as Productions)

Using production notation for regular expressions:

```
Lexical Productions (L):

Keywords:
  LET → let
  SEQ → seq
  PRINT → print
  LOOP → loop
  FROM → from
  TO → to
  IF → if
  ELSE → else
  TRUE → true
  FALSE → false
  FIBONACCI → fibonacci
  RANGE → range

Identifiers:
  IDENT → LETTER (LETTER | DIGIT | _)*
  LETTER → a | b | c | ... | z | A | B | C | ... | Z

Numbers:
  NUMBER → DIGIT+
  DIGIT → 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

Two-Character Operators:
  EQ_EQ → ==
  NOT_EQ → !=
  LESS_EQ → <=
  GREATER_EQ → >=
  AND → &&
  OR → ||

Single-Character Operators:
  ASSIGN → =
  PLUS → +
  MINUS → -
  MUL → *
  DIV → /
  MOD → %
  LT → <
  GT → >

Delimiters:
  LPAREN → (
  RPAREN → )
  LBRACE → {
  RBRACE → }
  COMMA → ,

Whitespace (ignored):
  SPACE → ' '
  TAB → \t
  NEWLINE → \n

Comments (ignored):
  COMMENT → # (any character except \n)* \n
```

## Regular Expression Definitions

Using standard regex notation:

```
Token Definitions:

KEYWORD     = let|seq|print|loop|from|to|if|else|true|false|fibonacci|range
IDENT       = [a-zA-Z_][a-zA-Z0-9_]*
NUMBER      = [0-9]+
EQ_EQ       = ==
NOT_EQ      = !=
LESS_EQ     = <=
GREATER_EQ  = >=
AND         = &&
OR          = \|\|
ASSIGN      = =
PLUS        = \+
MINUS       = -
MUL         = \*
DIV         = /
MOD         = %
LT          = <
GT          = >
LPAREN      = \(
RPAREN      = \)
LBRACE      = \{
RBRACE      = \}
COMMA       = ,
WHITESPACE  = [ \t]+
NEWLINE     = \n
COMMENT     = #[^\n]*
```

## Lexical Analysis Algorithm

```
Input: Source code string
Output: List of tokens

Algorithm:
1. Initialize position = 0, line = 1
2. While position < length of source:
   a. Try to match patterns in priority order:
      i.   WHITESPACE → skip, advance position
      ii.  NEWLINE → emit NEWLINE token, increment line
      iii. COMMENT → skip until newline
      iv.  KEYWORD → emit keyword token
      v.   IDENT → emit identifier token
      vi.  NUMBER → emit number token
      vii. Two-char operators → emit operator token
      viii. Single-char operators → emit operator token
      ix.  Delimiters → emit delimiter token
   b. If no match found → error
   c. Advance position by matched length
3. Emit EOF token
4. Return token list
```

## Syntax Grammar (EBNF)

### Program Structure
```ebnf
program      ::= { statement }

statement    ::= let_stmt
               | seq_stmt
               | print_stmt
               | loop_stmt
               | if_stmt
```

### Statements

#### Variable Declarations
```ebnf
let_stmt     ::= "let" IDENT "=" expr NEWLINE

seq_stmt     ::= "seq" IDENT "=" seq_expr NEWLINE
```

#### I/O Statement
```ebnf
print_stmt   ::= "print" expr NEWLINE
```

#### Control Flow Statements
```ebnf
loop_stmt    ::= "loop" IDENT "from" expr "to" expr compound

if_stmt      ::= "if" expr compound [ "else" compound ]

compound     ::= "{" { statement } "}"
```

### Expressions

#### Sequence Expressions
```ebnf
seq_expr     ::= "fibonacci" "(" expr ")"
               | "range" "(" expr "," expr ")"
```

#### General Expressions (with precedence)
```ebnf
expr         ::= logic

logic        ::= equality { ( "&&" | "||" ) equality }

equality     ::= rel { ( "==" | "!=" ) rel }

rel          ::= add { ( "<" | "<=" | ">" | ">=" ) add }

add          ::= mul { ( "+" | "-" ) mul }

mul          ::= unary { ( "*" | "/" | "%" ) unary }

unary        ::= [ "-" ] primary

primary      ::= NUMBER
               | IDENT
               | "(" expr ")"
               | "true"
               | "false"
```

## Operator Precedence (Highest to Lowest)

1. Parentheses: `( )`
2. Unary negation: `-`
3. Multiplicative: `*`, `/`, `%`
4. Additive: `+`, `-`
5. Relational: `<`, `<=`, `>`, `>=`
6. Equality: `==`, `!=`
7. Logical AND: `&&`
8. Logical OR: `||`

## Type System

### Types
```
int         - Integer type (single numeric value)
seq         - Sequence type (list of integers)
```

### Type Rules

#### Variable Declarations
```
let IDENT = expr
  - expr must evaluate to type int
  - IDENT is assigned type int

seq IDENT = seq_expr
  - seq_expr must evaluate to type seq
  - IDENT is assigned type seq
```

#### Expressions
```
NUMBER                    → int
IDENT                     → type of IDENT (from symbol table)
true, false               → int (1 or 0)

Arithmetic operators (+, -, *, /, %):
  int op int              → int

Comparison operators (<, <=, >, >=, ==, !=):
  int op int              → int (1 for true, 0 for false)

Logical operators (&&, ||):
  int op int              → int (1 for true, 0 for false)

Unary negation (-):
  - int                   → int

fibonacci(int)            → seq
range(int, int)           → seq
```

#### Print Statement
```
print expr
  - expr can be type int or seq
  - int: prints the number
  - seq: prints the list in format [n1, n2, ...]
```

#### Loop Statement
```
loop IDENT from expr1 to expr2 { ... }
  - expr1 must be type int (start value)
  - expr2 must be type int (end value)
  - IDENT is automatically declared as type int in loop scope
  - Loop runs from expr1 to expr2 inclusive
```

#### If Statement
```
if expr { ... }
  - expr must be type int
  - Non-zero values are considered true
  - Zero is considered false
```

## Semantic Rules

### Scope Rules
```
1. Global Scope
   - Variables declared outside any block
   - Accessible throughout the program

2. Loop Scope
   - Loop variable (IDENT in loop header) exists only within loop body
   - Variables declared inside loop exist only within loop body

3. If/Else Scope
   - Variables declared inside if/else blocks exist only within that block
```

### Variable Rules
```
1. Variables must be declared before use
2. Variables cannot be redeclared in the same scope
3. Loop variables are implicitly declared (no let/seq needed)
4. Variable lookup follows scope chain (inner to outer)
```

### Type Checking Rules
```
1. Arithmetic operations require int operands
2. Sequence operations (fibonacci, range) return seq type
3. Cannot mix int and seq in operations
4. Print accepts both int and seq
5. Control flow conditions must be int type
```

## Built-in Functions

### fibonacci(n)
```
Signature: fibonacci(int) → seq
Description: Generates the first n Fibonacci numbers
Parameters:
  n - Number of Fibonacci numbers to generate (must be >= 0)
Returns: Sequence of n Fibonacci numbers starting with 0, 1
Example: fibonacci(7) → [0, 1, 1, 2, 3, 5, 8]
```

### range(start, end)
```
Signature: range(int, int) → seq
Description: Generates sequence of integers from start to end
Parameters:
  start - Starting value (inclusive)
  end   - Ending value (inclusive)
Returns: Sequence of integers from start to end
Example: range(1, 5) → [1, 2, 3, 4, 5]
Note: Both bounds are inclusive (unlike Python)
```

## Complete Grammar in BNF

```bnf
<program>      ::= <statement-list>

<statement-list> ::= <statement> | <statement> <statement-list>

<statement>    ::= <let-stmt>
                 | <seq-stmt>
                 | <print-stmt>
                 | <loop-stmt>
                 | <if-stmt>

<let-stmt>     ::= "let" <identifier> "=" <expr> <newline>

<seq-stmt>     ::= "seq" <identifier> "=" <seq-expr> <newline>

<print-stmt>   ::= "print" <expr> <newline>

<loop-stmt>    ::= "loop" <identifier> "from" <expr> "to" <expr> <compound>

<if-stmt>      ::= "if" <expr> <compound>
                 | "if" <expr> <compound> "else" <compound>

<compound>     ::= "{" <statement-list> "}"

<seq-expr>     ::= "fibonacci" "(" <expr> ")"
                 | "range" "(" <expr> "," <expr> ")"

<expr>         ::= <logic-expr>

<logic-expr>   ::= <equality-expr>
                 | <logic-expr> "&&" <equality-expr>
                 | <logic-expr> "||" <equality-expr>

<equality-expr> ::= <rel-expr>
                  | <equality-expr> "==" <rel-expr>
                  | <equality-expr> "!=" <rel-expr>

<rel-expr>     ::= <add-expr>
                 | <rel-expr> "<" <add-expr>
                 | <rel-expr> "<=" <add-expr>
                 | <rel-expr> ">" <add-expr>
                 | <rel-expr> ">=" <add-expr>

<add-expr>     ::= <mul-expr>
                 | <add-expr> "+" <mul-expr>
                 | <add-expr> "-" <mul-expr>

<mul-expr>     ::= <unary-expr>
                 | <mul-expr> "*" <unary-expr>
                 | <mul-expr> "/" <unary-expr>
                 | <mul-expr> "%" <unary-expr>

<unary-expr>   ::= <primary-expr>
                 | "-" <unary-expr>

<primary-expr> ::= <number>
                 | <identifier>
                 | "(" <expr> ")"
                 | "true"
                 | "false"

<identifier>   ::= <letter> { <letter> | <digit> | "_" }

<number>       ::= <digit> { <digit> }

<letter>       ::= "a" | "b" | ... | "z" | "A" | "B" | ... | "Z"

<digit>        ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
```

## Context-Free Grammar (Production Rules)

Using standard production notation where S is the start symbol:

```
Grammar G = (V, T, P, S)

V (Non-terminals):
  S, STMT, LET, SEQ, PRINT, LOOP, IF, COMPOUND, SEQ_EXPR, EXPR, 
  LOGIC, EQUALITY, REL, ADD, MUL, UNARY, PRIMARY, IDENT, NUM

T (Terminals):
  let, seq, print, loop, from, to, if, else, true, false, fibonacci, range,
  &&, ||, ==, !=, <, <=, >, >=, +, -, *, /, %, =, (, ), {, }, ,, 
  identifier, number, newline

P (Productions):

Start Symbol:
  S → STMT_LIST

Program Structure:
  STMT_LIST → STMT
  STMT_LIST → STMT STMT_LIST

Statement Types:
  STMT → LET
  STMT → SEQ
  STMT → PRINT
  STMT → LOOP
  STMT → IF

Variable Declarations:
  LET → let IDENT = EXPR newline
  SEQ → seq IDENT = SEQ_EXPR newline

I/O Statement:
  PRINT → print EXPR newline

Control Flow:
  LOOP → loop IDENT from EXPR to EXPR COMPOUND
  IF → if EXPR COMPOUND
  IF → if EXPR COMPOUND else COMPOUND
  COMPOUND → { STMT_LIST }

Sequence Expressions:
  SEQ_EXPR → fibonacci ( EXPR )
  SEQ_EXPR → range ( EXPR , EXPR )

Expression Hierarchy (with precedence):
  EXPR → LOGIC
  
  LOGIC → EQUALITY
  LOGIC → LOGIC && EQUALITY
  LOGIC → LOGIC || EQUALITY
  
  EQUALITY → REL
  EQUALITY → EQUALITY == REL
  EQUALITY → EQUALITY != REL
  
  REL → ADD
  REL → REL < ADD
  REL → REL <= ADD
  REL → REL > ADD
  REL → REL >= ADD
  
  ADD → MUL
  ADD → ADD + MUL
  ADD → ADD - MUL
  
  MUL → UNARY
  MUL → MUL * UNARY
  MUL → MUL / UNARY
  MUL → MUL % UNARY
  
  UNARY → PRIMARY
  UNARY → - UNARY
  
  PRIMARY → NUM
  PRIMARY → IDENT
  PRIMARY → ( EXPR )
  PRIMARY → true
  PRIMARY → false

Lexical Rules:
  IDENT → letter (letter | digit | _)*
  NUM → digit+
  letter → a | b | c | ... | z | A | B | C | ... | Z
  digit → 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
```

## Derivation Examples

### Example 1: Deriving "let x = 5"

```
S 
→ STMT_LIST
→ STMT
→ LET
→ let IDENT = EXPR newline
→ let x = EXPR newline
→ let x = LOGIC newline
→ let x = EQUALITY newline
→ let x = REL newline
→ let x = ADD newline
→ let x = MUL newline
→ let x = UNARY newline
→ let x = PRIMARY newline
→ let x = NUM newline
→ let x = 5 newline
```

### Example 2: Deriving "2 + 3 * 4"

```
EXPR
→ LOGIC
→ EQUALITY
→ REL
→ ADD
→ ADD + MUL
→ MUL + MUL
→ UNARY + MUL
→ PRIMARY + MUL
→ NUM + MUL
→ 2 + MUL
→ 2 + MUL * UNARY
→ 2 + UNARY * UNARY
→ 2 + PRIMARY * UNARY
→ 2 + NUM * UNARY
→ 2 + 3 * UNARY
→ 2 + 3 * PRIMARY
→ 2 + 3 * NUM
→ 2 + 3 * 4
```

Note: The derivation shows that * binds tighter than + due to grammar structure.

### Example 3: Deriving "if x > 5 { print 1 }"

```
S
→ STMT_LIST
→ STMT
→ IF
→ if EXPR COMPOUND
→ if LOGIC COMPOUND
→ if EQUALITY COMPOUND
→ if REL COMPOUND
→ if REL > ADD COMPOUND
→ if ADD > ADD COMPOUND
→ if MUL > ADD COMPOUND
→ if UNARY > ADD COMPOUND
→ if PRIMARY > ADD COMPOUND
→ if IDENT > ADD COMPOUND
→ if x > ADD COMPOUND
→ if x > MUL COMPOUND
→ if x > UNARY COMPOUND
→ if x > PRIMARY COMPOUND
→ if x > NUM COMPOUND
→ if x > 5 COMPOUND
→ if x > 5 { STMT_LIST }
→ if x > 5 { STMT }
→ if x > 5 { PRINT }
→ if x > 5 { print EXPR newline }
→ if x > 5 { print LOGIC newline }
→ if x > 5 { print EQUALITY newline }
→ if x > 5 { print REL newline }
→ if x > 5 { print ADD newline }
→ if x > 5 { print MUL newline }
→ if x > 5 { print UNARY newline }
→ if x > 5 { print PRIMARY newline }
→ if x > 5 { print NUM newline }
→ if x > 5 { print 1 newline }
```

## Grammar Properties

### Ambiguity
The grammar is **unambiguous** due to:
- Explicit precedence levels in expression rules
- Left-associativity enforced by left-recursive productions
- Clear statement boundaries via newlines and braces

### Recursion
- **Left-recursive:** EXPR productions (LOGIC, EQUALITY, REL, ADD, MUL)
- **Right-recursive:** UNARY production
- **Indirect recursive:** STMT through COMPOUND

### Language Class
- **Context-Free Grammar (CFG)**
- Can be parsed by LR(1) or LL(k) parsers
- Current implementation uses recursive descent (LL parser)

## Example Programs

### Example 1: Basic Arithmetic and Variables
```mpl
let x = 2 * 3 + 4
print x
```
Output: `10`

### Example 2: Fibonacci Sequence
```mpl
let n = 7
seq s = fibonacci(n)
print s
```
Output: `[0, 1, 1, 2, 3, 5, 8]`

### Example 3: Range Generation
```mpl
seq numbers = range(1, 5)
print numbers
```
Output: `[1, 2, 3, 4, 5]`

### Example 4: Loop
```mpl
loop i from 0 to 3 {
  print i
}
```
Output:
```
0
1
2
3
```

### Example 5: Conditional
```mpl
let a = 11
if a > 10 {
  print 1
} else {
  print 0
}
```
Output: `1`

### Example 6: Nested Structures
```mpl
loop i from 1 to 5 {
  let sq = i * i
  print sq
  if i % 2 == 0 {
    print 888
  }
}
```
Output:
```
1
4
888
9
16
888
25
```

## Language Limitations

### Not Supported
```
- Variable reassignment (all variables are immutable after declaration)
- User-defined functions
- Arrays or sequence indexing (cannot access s[0])
- String type
- Floating-point numbers
- While loops (only for loops with known bounds)
- Break/continue statements
- Return statements
- Multiple files or imports
```

### Supported
```
- Integer arithmetic
- Sequence generation (fibonacci, range)
- Control flow (if/else, loops)
- Nested scopes
- Type checking
- Comments
```

## Implementation Notes

The compiler implements all six phases:
1. Lexical Analysis - DFA-based tokenizer
2. Syntax Analysis - Recursive descent parser
3. Semantic Analysis - Symbol table and type checking
4. Intermediate Code Generation - Three-address code
5. Optimization - Constant folding, dead code elimination
6. Code Generation - Virtual machine execution
