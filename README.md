=================================
|| BRANCH: lexer_parser_mix_up ||
=================================

Started down a path of "if the lexer 'sees' an IDENT followed by a `=`, then it 'knows' to look for a value" - was giving the lexer too much to do.  

The lexer simply scans the file for tokens; the parser is the one that ingests tokens to make sure grammar of the file is correct.

Saving this branch as a learning experience; refactoring on `main`.
Also saving because of the testing strat used.


# programming_language_educational
Just messing around

## initial interpreter includes
- basic printing and inputs
- most basic math operations
- simple control structures such as if-statements
- lexer: convert input into tokens
- tokens then fed to a parser (Recursive Descent parser rec.)
- parser produces AST
- interpreter: walks AST, keeps track of variables, does the commands, and produces output

Do one step at a time:
- Tokens
    - Token type enum
    - Token struct
- Lexer
    - Input → tokens
    - No parsing yet
- AST
    - Expressions vs statements
- Parser
    - Recursive descent
    - Operator precedence
- Objects
    - Integer, Boolean, Null, Function
- Environment
    - Map + parent pointer
- Evaluator
    - Walk the AST
    - Return objects
- REPL
    - Tiny loop in main.go

If something feels hard, you’re probably jumping ahead.