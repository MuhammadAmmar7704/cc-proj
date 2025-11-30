# Complete Lexical Analysis for sample1.mpl

## Source Code:
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

## Complete Token Stream with DFA Trace:

### Line 1: `let n = 7`

| Position | Character | Current State | Next State | Action | Token Generated |
|----------|-----------|---------------|------------|--------|-----------------|
| 1        | 'l'       | S0            | S2         | Continue | - |
| 2        | 'e'       | S2            | S2         | Continue | - |
| 3        | 't'       | S2            | S2         | Continue | - |
| 4        | ' '       | S2            | S0         | Accept | **LET** (keyword) |
| 5        | 'n'       | S0            | S2         | Continue | - |
| 6        | ' '       | S2            | S0         | Accept | **IDENT('n')** |
| 7        | '='       | S0            | S3         | Continue | - |
| 8        | ' '       | S3            | S0         | Accept | **ASSIGN('=')** |
| 9        | '7'       | S0            | S1         | Continue | - |
| 10       | '\n'      | S1            | S0         | Accept | **NUMBER(7)** |
| 10       | '\n'      | S0            | S0         | Accept | **NEWLINE** |

**Tokens for Line 1:** `[LET, IDENT('n'), ASSIGN, NUMBER(7), NEWLINE]`

---

### Line 2: `seq s = fibonacci(n)`

| Position | Character | Current State | Next State | Action | Token Generated |
|----------|-----------|---------------|------------|--------|-----------------|
| 1        | 's'       | S0            | S2         | Continue | - |
| 2        | 'e'       | S2            | S2         | Continue | - |
| 3        | 'q'       | S2            | S2         | Continue | - |
| 4        | ' '       | S2            | S0         | Accept | **SEQ** (keyword) |
| 5        | 's'       | S0            | S2         | Continue | - |
| 6        | ' '       | S2            | S0         | Accept | **IDENT('s')** |
| 7        | '='       | S0            | S3         | Continue | - |
| 8        | ' '       | S3            | S0         | Accept | **ASSIGN** |
| 9-17     | 'fibonacci'| S0→S2        | S2         | Continue | - |
| 18       | '('       | S2            | S0         | Accept | **FIBONACCI** (keyword) |
| 18       | '('       | S0            | S20        | Accept | **LPAREN** |
| 19       | 'n'       | S0            | S2         | Continue | - |
| 20       | ')'       | S2            | S0         | Accept | **IDENT('n')** |
| 20       | ')'       | S0            | S21        | Accept | **RPAREN** |
| 21       | '\n'      | S0            | S0         | Accept | **NEWLINE** |

**Tokens for Line 2:** `[SEQ, IDENT('s'), ASSIGN, FIBONACCI, LPAREN, IDENT('n'), RPAREN, NEWLINE]`

---

### Line 3: `print s`

| Position | Character | Current State | Next State | Action | Token Generated |
|----------|-----------|---------------|------------|--------|-----------------|
| 1-5      | 'print'   | S0→S2         | S2         | Continue | - |
| 6        | ' '       | S2            | S0         | Accept | **PRINT** (keyword) |
| 7        | 's'       | S0            | S2         | Continue | - |
| 8        | '\n'      | S2            | S0         | Accept | **IDENT('s')** |
| 8        | '\n'      | S0            | S0         | Accept | **NEWLINE** |

**Tokens for Line 3:** `[PRINT, IDENT('s'), NEWLINE]`

---

### Line 4: `seq t = range(1, 5)`

| Position | Character | Current State | Next State | Action | Token Generated |
|----------|-----------|---------------|------------|--------|-----------------|
| 1-3      | 'seq'     | S0→S2         | S2         | Continue | - |
| 4        | ' '       | S2            | S0         | Accept | **SEQ** |
| 5        | 't'       | S0            | S2         | Continue | - |
| 6        | ' '       | S2            | S0         | Accept | **IDENT('t')** |
| 7        | '='       | S0            | S3         | Continue | - |
| 8        | ' '       | S3            | S0         | Accept | **ASSIGN** |
| 9-13     | 'range'   | S0→S2         | S2         | Continue | - |
| 14       | '('       | S2            | S0         | Accept | **RANGE** (keyword) |
| 14       | '('       | S0            | S20        | Accept | **LPAREN** |
| 15       | '1'       | S0            | S1         | Continue | - |
| 16       | ','       | S1            | S0         | Accept | **NUMBER(1)** |
| 16       | ','       | S0            | S24        | Accept | **COMMA** |
| 17       | ' '       | S0            | S0         | Skip | - |
| 18       | '5'       | S0            | S1         | Continue | - |
| 19       | ')'       | S1            | S0         | Accept | **NUMBER(5)** |
| 19       | ')'       | S0            | S21        | Accept | **RPAREN** |
| 20       | '\n'      | S0            | S0         | Accept | **NEWLINE** |

**Tokens for Line 4:** `[SEQ, IDENT('t'), ASSIGN, RANGE, LPAREN, NUMBER(1), COMMA, NUMBER(5), RPAREN, NEWLINE]`

---

### Line 5: `print t`

**Tokens:** `[PRINT, IDENT('t'), NEWLINE]`

---

### Line 6: `let x = 2 * 3 + 4`

| Position | Character | Current State | Next State | Action | Token Generated |
|----------|-----------|---------------|------------|--------|-----------------|
| 1-3      | 'let'     | S0→S2         | S2         | Continue | - |
| 4        | ' '       | S2            | S0         | Accept | **LET** |
| 5        | 'x'       | S0            | S2         | Continue | - |
| 6        | ' '       | S2            | S0         | Accept | **IDENT('x')** |
| 7        | '='       | S0            | S3         | Continue | - |
| 8        | ' '       | S3            | S0         | Accept | **ASSIGN** |
| 9        | '2'       | S0            | S1         | Continue | - |
| 10       | ' '       | S1            | S0         | Accept | **NUMBER(2)** |
| 11       | '*'       | S0            | S17        | Accept | **MUL** |
| 12       | ' '       | S0            | S0         | Skip | - |
| 13       | '3'       | S0            | S1         | Continue | - |
| 14       | ' '       | S1            | S0         | Accept | **NUMBER(3)** |
| 15       | '+'       | S0            | S15        | Accept | **PLUS** |
| 16       | ' '       | S0            | S0         | Skip | - |
| 17       | '4'       | S0            | S1         | Continue | - |
| 18       | '\n'      | S1            | S0         | Accept | **NUMBER(4)** |
| 18       | '\n'      | S0            | S0         | Accept | **NEWLINE** |

**Tokens for Line 6:** `[LET, IDENT('x'), ASSIGN, NUMBER(2), MUL, NUMBER(3), PLUS, NUMBER(4), NEWLINE]`

---

### Line 7: `print x`

**Tokens:** `[PRINT, IDENT('x'), NEWLINE]`

---

### Line 8: `loop i from 0 to 3 {`

| Position | Character | Current State | Next State | Action | Token Generated |
|----------|-----------|---------------|------------|--------|-----------------|
| 1-4      | 'loop'    | S0→S2         | S2         | Continue | - |
| 5        | ' '       | S2            | S0         | Accept | **LOOP** (keyword) |
| 6        | 'i'       | S0            | S2         | Continue | - |
| 7        | ' '       | S2            | S0         | Accept | **IDENT('i')** |
| 8-11     | 'from'    | S0→S2         | S2         | Continue | - |
| 12       | ' '       | S2            | S0         | Accept | **FROM** (keyword) |
| 13       | '0'       | S0            | S1         | Continue | - |
| 14       | ' '       | S1            | S0         | Accept | **NUMBER(0)** |
| 15-16    | 'to'      | S0→S2         | S2         | Continue | - |
| 17       | ' '       | S2            | S0         | Accept | **TO** (keyword) |
| 18       | '3'       | S0            | S1         | Continue | - |
| 19       | ' '       | S1            | S0         | Accept | **NUMBER(3)** |
| 20       | '{'       | S0            | S22        | Accept | **LBRACE** |
| 21       | '\n'      | S0            | S0         | Accept | **NEWLINE** |

**Tokens for Line 8:** `[LOOP, IDENT('i'), FROM, NUMBER(0), TO, NUMBER(3), LBRACE, NEWLINE]`

---

### Line 9: `  print i`

**Tokens:** `[PRINT, IDENT('i'), NEWLINE]`

---

### Line 10: `}`

| Position | Character | Current State | Next State | Action | Token Generated |
|----------|-----------|---------------|------------|--------|-----------------|
| 1        | '}'       | S0            | S23        | Accept | **RBRACE** |
| 2        | '\n'      | S0            | S0         | Accept | **NEWLINE** |

**Tokens for Line 10:** `[RBRACE, NEWLINE]`

---

## Complete Token Stream Summary:

```
Token #  | Type          | Value      | Line | Column
---------|---------------|------------|------|-------
1        | LET           | "let"      | 1    | 1
2        | IDENT         | "n"        | 1    | 5
3        | ASSIGN        | "="        | 1    | 7
4        | NUMBER        | 7          | 1    | 9
5        | NEWLINE       | "\n"       | 1    | 10
6        | SEQ           | "seq"      | 2    | 1
7        | IDENT         | "s"        | 2    | 5
8        | ASSIGN        | "="        | 2    | 7
9        | FIBONACCI     | "fibonacci"| 2    | 9
10       | LPAREN        | "("        | 2    | 18
11       | IDENT         | "n"        | 2    | 19
12       | RPAREN        | ")"        | 2    | 20
13       | NEWLINE       | "\n"       | 2    | 21
14       | PRINT         | "print"    | 3    | 1
15       | IDENT         | "s"        | 3    | 7
16       | NEWLINE       | "\n"       | 3    | 8
17       | SEQ           | "seq"      | 4    | 1
18       | IDENT         | "t"        | 4    | 5
19       | ASSIGN        | "="        | 4    | 7
20       | RANGE         | "range"    | 4    | 9
21       | LPAREN        | "("        | 4    | 14
22       | NUMBER        | 1          | 4    | 15
23       | COMMA         | ","        | 4    | 16
24       | NUMBER        | 5          | 4    | 18
25       | RPAREN        | ")"        | 4    | 19
26       | NEWLINE       | "\n"       | 4    | 20
27       | PRINT         | "print"    | 5    | 1
28       | IDENT         | "t"        | 5    | 7
29       | NEWLINE       | "\n"       | 5    | 8
30       | LET           | "let"      | 6    | 1
31       | IDENT         | "x"        | 6    | 5
32       | ASSIGN        | "="        | 6    | 7
33       | NUMBER        | 2          | 6    | 9
34       | MUL           | "*"        | 6    | 11
35       | NUMBER        | 3          | 6    | 13
36       | PLUS          | "+"        | 6    | 15
37       | NUMBER        | 4          | 6    | 17
38       | NEWLINE       | "\n"       | 6    | 18
39       | PRINT         | "print"    | 7    | 1
40       | IDENT         | "x"        | 7    | 7
41       | NEWLINE       | "\n"       | 7    | 8
42       | LOOP          | "loop"     | 8    | 1
43       | IDENT         | "i"        | 8    | 6
44       | FROM          | "from"     | 8    | 8
45       | NUMBER        | 0          | 8    | 13
46       | TO            | "to"       | 8    | 15
47       | NUMBER        | 3          | 8    | 18
48       | LBRACE        | "{"        | 8    | 20
49       | NEWLINE       | "\n"       | 8    | 21
50       | PRINT         | "print"    | 9    | 3
51       | IDENT         | "i"        | 9    | 9
52       | NEWLINE       | "\n"       | 9    | 10
53       | RBRACE        | "}"        | 10   | 1
54       | NEWLINE       | "\n"       | 10   | 2
55       | EOF           | ""         | 11   | 1
```

**Total Tokens: 55**
