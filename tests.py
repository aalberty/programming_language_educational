from lexer import Lexer as lexer

def find_ident(case):
    print(f'Testing lexer.find_ident() for source "{case}"')
    l = lexer(case)
    l.find_next_token()
    # print(f'pos check: {l.current_position}')
    ident = l.find_ident()

    if ident == False:
        return

    print(f"IDENT = '{ident.literal}'")
    print('\n')

cases = [
    'let x = 5;',
    'let x_submarine_69 = 5;',
    'let x=5;',
    'let x;',
    'let'
]

for case in cases:
    find_ident(case)