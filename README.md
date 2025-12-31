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

## notes
- check out the `lexer_parser_mix_up` branch for:
    - understanding when the lexer starts taking on too much
    - BONUS testing strat: see `tests.py`