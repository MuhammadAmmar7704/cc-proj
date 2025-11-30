# Complete DFA Diagrams for Mini Pattern Language

## DFA for Complete Lexical Analysis

This DFA recognizes ALL tokens in the Mini Pattern Language.

### States:
- **S0**: Start state
- **S1**: Number (accepting) - recognizes integers
- **S2**: Identifier/Keyword (accepting) - recognizes words
- **S3**: Single '=' 
- **S4**: '==' (accepting)
- **S5**: Single '<'
- **S6**: '<=' (accepting)
- **S7**: Single '>'
- **S8**: '>=' (accepting)
- **S9**: Single '!'
- **S10**: '!=' (accepting)
- **S11**: Single '&'
- **S12**: '&&' (accepting)
- **S13**: Single '|'
- **S14**: '||' (accepting)
- **S15-S23**: Direct accepting states for single-char operators

### Complete Transition Table:

```
┌──────────┬─────────────┬──────────────┬──────────────┬──────────────┐
│  State   │   Input     │  Next State  │   Action     │  Token Type  │
├──────────┼─────────────┼──────────────┼──────────────┼──────────────┤
│   S0     │   [0-9]     │     S1       │   Continue   │      -       │
│   S0     │ [a-zA-Z_]   │     S2       │   Continue   │      -       │
│   S0     │     =       │     S3       │   Continue   │      -       │
│   S0     │     <       │     S5       │   Continue   │      -       │
│   S0     │     >       │     S7       │   Continue   │      -       │
│   S0     │     !       │     S9       │   Continue   │      -       │
│   S0     │     &       │     S11      │   Continue   │      -       │
│   S0     │     |       │     S13      │   Continue   │      -       │
│   S0     │     +       │     S15      │   Accept     │   PLUS       │
│   S0     │     -       │     S16      │   Accept     │   MINUS      │
│   S0     │     *       │     S17      │   Accept     │   MUL        │
│   S0     │     /       │     S18      │   Accept     │   DIV        │
│   S0     │     %       │     S19      │   Accept     │   MOD        │
│   S0     │     (       │     S20      │   Accept     │   LPAREN     │
│   S0     │     )       │     S21      │   Accept     │   RPAREN     │
│   S0     │     {       │     S22      │   Accept     │   LBRACE     │
│   S0     │     }       │     S23      │   Accept     │   RBRACE     │
│   S0     │     ,       │     S24      │   Accept     │   COMMA      │
│   S0     │   space/tab │     S0       │   Skip       │      -       │
│   S0     │   newline   │     S0       │   Accept     │   NEWLINE    │
│   S0     │     #       │   Comment    │   Skip line  │      -       │
├──────────┼─────────────┼──────────────┼──────────────┼──────────────┤
│   S1     │   [0-9]     │     S1       │   Continue   │      -       │
│   S1     │   other     │     S0       │   Accept     │   NUMBER     │
├──────────┼─────────────┼──────────────┼──────────────┼──────────────┤
│   S2     │ [a-zA-Z0-9_]│     S2       │   Continue   │      -       │
│   S2     │   other     │     S0       │   Check KW   │ IDENT/KEYWORD│
├──────────┼─────────────┼──────────────┼──────────────┼──────────────┤
│   S3     │     =       │     S4       │   Accept     │   EQ_EQ      │
│   S3     │   other     │     S0       │   Accept     │   ASSIGN     │
├──────────┼─────────────┼──────────────┼──────────────┼──────────────┤
│   S5     │     =       │     S6       │   Accept     │   LE         │
│   S5     │   other     │     S0       │   Accept     │   LT         │
├──────────┼─────────────┼──────────────┼──────────────┼──────────────┤
│   S7     │     =       │     S8       │   Accept     │   GE         │
│   S7     │   other     │     S0       │   Accept     │   GT         │
├──────────┼─────────────┼──────────────┼──────────────┼──────────────┤
│   S9     │     =       │     S10      │   Accept     │   NE         │
│   S9     │   other     │     ERROR    │   Error      │   ERROR      │
├──────────┼─────────────┼──────────────┼──────────────┼──────────────┤
│   S11    │     &       │     S12      │   Accept     │   AND        │
│   S11    │   other     │     ERROR    │   Error      │   ERROR      │
├──────────┼─────────────┼──────────────┼──────────────┼──────────────┤
│   S13    │     |       │     S14      │   Accept     │   OR         │
│   S13    │   other     │     ERROR    │   Error      │   ERROR      │
└──────────┴─────────────┴──────────────┴──────────────┴──────────────┘
```

### Keyword Recognition (at State S2):
When an identifier is complete, check against keyword list:
```
Keywords: let, seq, print, loop, from, to, if, else, 
          true, false, fibonacci, range

If match → Token type = KEYWORD (specific type)
If no match → Token type = IDENT
```

---

## DFA Diagram to Draw:

```
                    [0-9]
         ┌─────────────────────────┐
         │                         ↓
    ┌────○ S0 (Start)          ◎ S1 (NUMBER)
    │    │                         ↑
    │    │ [a-z,A-Z,_]              │ [0-9]
    │    └─────────────────┐        └─────┘
    │                      ↓
    │                  ◎ S2 (IDENT/KEYWORD)
    │                      ↑
    │                      │ [a-z,A-Z,0-9,_]
    │                      └─────┘
    │
    │    [=]           [=]
    │    ├──→ ○ S3 ────→ ◎ S4 (==)
    │
    │    [<]           [=]
    │    ├──→ ○ S5 ────→ ◎ S6 (<=)
    │
    │    [>]           [=]
    │    ├──→ ○ S7 ────→ ◎ S8 (>=)
    │
    │    [!]           [=]
    │    ├──→ ○ S9 ────→ ◎ S10 (!=)
    │
    │    [&]           [&]
    │    ├──→ ○ S11 ───→ ◎ S12 (&&)
    │
    │    [|]           [|]
    │    ├──→ ○ S13 ───→ ◎ S14 (||)
    │
    │    [+]
    │    ├──→ ◎ S15 (+)
    │
    │    [-]
    │    ├──→ ◎ S16 (-)
    │
    │    [*]
    │    ├──→ ◎ S17 (*)
    │
    │    [/]
    │    ├──→ ◎ S18 (/)
    │
    │    [%]
    │    ├──→ ◎ S19 (%)
    │
    │    [(]
    │    ├──→ ◎ S20 (LPAREN)
    │
    │    [)]
    │    ├──→ ◎ S21 (RPAREN)
    │
    │    [{]
    │    ├──→ ◎ S22 (LBRACE)
    │
    │    [}]
    │    ├──→ ◎ S23 (RBRACE)
    │
    │    [,]
    │    └──→ ◎ S24 (COMMA)
```

---

## Example Traces Through DFA

### Example 1: Tokenizing "loop"

```
Input: l o o p

Step 1: Read 'l'
  State: S0 → S2 (letter detected)
  Buffer: "l"

Step 2: Read 'o'
  State: S2 → S2 (letter/digit loop)
  Buffer: "lo"

Step 3: Read 'o'
  State: S2 → S2
  Buffer: "loo"

Step 4: Read 'p'
  State: S2 → S2
  Buffer: "loop"

Step 5: Read ' ' (space)
  State: S2 → S0 (other character)
  Action: Check if "loop" is keyword
  Result: YES → Token = LOOP
  Accept token, reset buffer
```

### Example 2: Tokenizing "123"

```
Input: 1 2 3

Step 1: Read '1'
  State: S0 → S1 (digit detected)
  Buffer: "1"

Step 2: Read '2'
  State: S1 → S1 (digit loop)
  Buffer: "12"

Step 3: Read '3'
  State: S1 → S1
  Buffer: "123"

Step 4: Read ' ' (space)
  State: S1 → S0 (other character)
  Action: Accept NUMBER
  Result: Token = NUMBER(123)
```

### Example 3: Tokenizing "=="

```
Input: = =

Step 1: Read '='
  State: S0 → S3
  Buffer: "="

Step 2: Read '='
  State: S3 → S4
  Buffer: "=="
  Action: Accept EQ_EQ
  Result: Token = ==
```

### Example 4: Tokenizing "from"

```
Input: f r o m

Step 1: Read 'f'
  State: S0 → S2
  Buffer: "f"

Step 2: Read 'r'
  State: S2 → S2
  Buffer: "fr"

Step 3: Read 'o'
  State: S2 → S2
  Buffer: "fro"

Step 4: Read 'm'
  State: S2 → S2
  Buffer: "from"

Step 5: Read ' '
  State: S2 → S0
  Check: "from" in keywords? YES
  Result: Token = FROM
```

---

## Complete Token List for sample1.mpl

```
Code: let n = 7
      seq s = fibonacci(n)
      print s
      loop i from 0 to 3 {
        print i
      }

Tokens Generated:
01: LET          (keyword)
02: IDENT(n)     (identifier)
03: ASSIGN(=)    (operator)
04: NUMBER(7)    (literal)
05: NEWLINE
06: SEQ          (keyword)
07: IDENT(s)     (identifier)
08: ASSIGN(=)    (operator)
09: FIBONACCI    (keyword)
10: LPAREN       (symbol)
11: IDENT(n)     (identifier)
12: RPAREN       (symbol)
13: NEWLINE
14: PRINT        (keyword)
15: IDENT(s)     (identifier)
16: NEWLINE
17: LOOP         (keyword)
18: IDENT(i)     (identifier)
19: FROM         (keyword)
20: NUMBER(0)    (literal)
21: TO           (keyword)
22: NUMBER(3)    (literal)
23: LBRACE       (symbol)
24: NEWLINE
25: PRINT        (keyword)
26: IDENT(i)     (identifier)
27: NEWLINE
28: RBRACE       (symbol)
29: NEWLINE
30: EOF
```

Each token was recognized by the DFA following the transitions shown above.
