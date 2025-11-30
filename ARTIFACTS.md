# Compiler Project Artifacts

## 1. Lexical Analysis - DFA (Finite Automaton)

**Instructions for Handwritten Diagram:**
Draw a state transition diagram with the following states and transitions.
- **Start State (0)**: The initial state.
- **Number State (1)**: Double circle (Accepting state).
- **ID/Keyword State (2)**: Double circle (Accepting state).
- **Operator States**: Separate accepting states for `=`, `+`, `-`, etc.

**Transitions:**
1.  **From Start (0)**:
    - Input `[0-9]` → Go to **State 1** (Number).
    - Input `[a-z A-Z _]` → Go to **State 2** (ID).
    - Input `+`, `-`, `*`, `/`, `(`, `)`, `{`, `}` → Go to respective **Final States** (e.g., State_Plus, State_LBrace).
    - Input `=` → Go to **State 3**.
    - Input `!` → Go to **State 4**.
    - Input `<` → Go to **State 5**.
    - Input `>` → Go to **State 6**.

2.  **From State 1 (Number)**:
    - Input `[0-9]` → Stay in **State 1**.
    - Other input → **Accept** token `NUMBER`.

3.  **From State 2 (ID)**:
    - Input `[a-z A-Z 0-9 _]` → Stay in **State 2**.
    - Other input → **Accept** token `IDENT` (or `KEYWORD` if in keyword list).

4.  **From State 3 (=)**:
    - Input `=` → Go to **State_Eq** (Accept `==`).
    - Other input → **Accept** token `=`.

5.  **From State 4 (!)**:
    - Input `=` → Go to **State_Neq** (Accept `!=`).

6.  **From State 5 (<)**:
    - Input `=` → Go to **State_Le** (Accept `<=`).
    - Other input → **Accept** token `<`.

---

## 2. Syntax Analysis - Parse Trees

**Instructions:**
Draw the tree structure for the following two statements.

### Derivation 1: `let n = 7`

```text
      statement
          |
       let_stmt
     /  |   |   \
  "let" ID "="  expr
        |        |
       "n"     logic
                 |
              equality
                 |
                rel
                 |
                add
                 |
                mul
                 |
               unary
                 |
              primary
                 |
               NUMBER
                 |
                "7"
```

### Derivation 2: `print n + 1`

```text
       statement
           |
       print_stmt
        /     \
    "print"   expr
               |
             logic
               |
            equality
               |
              rel
               |
              add
             / | \
          mul "+" mul
           |       |
         unary   unary
           |       |
        primary primary
           |       |
          ID     NUMBER
           |       |
          "n"     "1"
```

---

## 3. Semantic Analysis - Symbol Table

**Instructions:**
Draw a table representing the scopes during the execution of the following code snippet:

```mpl
let x = 10
loop i from 0 to 5 {
    let y = i * x
}
```

**Symbol Table Snapshot (Inside Loop):**

| Scope Level | Variable Name | Type  |
|-------------|---------------|-------|
| Global (0)  | x             | int   |
| Loop (1)    | i             | int   |
| Loop (1)    | y             | int   |

**Explanation:**
- **Global Scope**: Contains `x` (int).
- **Loop Scope**: Created when entering the loop. Contains loop variable `i` (int) and local variable `y` (int).
- When looking up `x` inside the loop, the compiler checks Loop Scope (not found) -> Global Scope (found).
