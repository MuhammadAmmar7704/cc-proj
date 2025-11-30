# Project Reflection

## Learning Outcomes
Through the design and implementation of the "Mini Pattern Language" compiler, we gained practical experience in the six major phases of compiler construction. We learned how to:
1.  **Formalize Grammar**: Designing the EBNF grammar helped us understand the structure of programming languages and the importance of unambiguous syntax.
2.  **Recursive Descent Parsing**: Implementing the parser manually gave us deep insight into how top-down parsers work and how to handle operator precedence (logic -> equality -> rel -> add -> mul).
3.  **Semantic Analysis**: We learned that parsing is not enough; type checking and scope management are crucial for a correct program. Implementing the symbol table with a stack of scopes was a key learning moment.
4.  **Intermediate Representation (IR)**: Transforming the AST into a linear 3-address code (IR) simplified the code generation process. It showed us how high-level constructs like `loop` and `if` are broken down into jumps and labels.
5.  **Virtual Machine**: Building a simple stack-based (or register-based) VM to execute the IR was rewarding and demonstrated the final step of the compilation pipeline.

## Challenges
-   **Scope Management**: Handling nested scopes for loops and if-statements required careful state management in the Semantic Analyzer. Ensuring variables were declared before use and preventing redeclaration in the same scope was tricky.
-   **Code Generation for Control Flow**: Generating the correct labels and jump instructions for `loop` and `if/else` blocks required careful logic to ensure the control flow was correct (e.g., jumping over the `else` block after the `then` block).
-   **Limitation of Immutability**: Our language does not support variable reassignment (only `let` for declaration), which simplified the compiler but limited the expressiveness of the language.

## Future Improvements
If we had more time, we would implement:
1.  **Mutable Variables**: Add an assignment statement (`x = 5`) to allow updating variables.
2.  **Functions**: Support user-defined functions with arguments and return values.
3.  **Arrays**: Add support for accessing individual elements of sequences (e.g., `s[i]`).
4.  **Better Error Messages**: Improve the parser and semantic analyzer to provide more descriptive error messages with suggestions.
