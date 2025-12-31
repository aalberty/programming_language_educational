from lexer import Lexer as lexer
from lexer import _vprint


# #tag_ident_start
def find_ident(case, verbose):
    _vprint(verbose, f'Testing lexer.find_ident() for source "{case}"')
    l = lexer(case)
    l.find_next_token()
    # print(f'pos check: {l.current_position}')
    ident = l.find_ident()

    if ident == False:
        return

    _vprint(verbose, f"IDENT = '{ident.literal}'")
    _vprint(verbose, '\n')
    return ident.literal
# #tag_ident_end

# #tag_tokens_start
def find_tokens(case, verbose):
    _vprint(verbose, f'Testing lexer.find_tokens() for source "{case}"')
    l = lexer(case)
    tokens = l.find_tokens()
    pp_tokens = ""
    for token in tokens:
        pp_tokens += token.literal + " "
    pp_tokens = pp_tokens.strip()
    _vprint(verbose, pp_tokens)
    return pp_tokens
# #tag_tokens_end

# READ ONLY
TEST_CASES = {

    # #tag_ident_start
    "find_ident": [
        [
            'let x = 5;',
            'x'
        ],

        [
            'let x_submarine_69 = 5;',
            'x_submarine_69'
        ],

        [
            'let x=5;',
            'x'
        ],

        [
            'let x;',
            'x'
        ],

        [
            'let',
            None
        ],

    ],
    # #tag_ident_end

    # #tag_tokens_start
    "find_tokens": [
        [
            '+ - * / = ; , ( ) { } < >',
            '+ - * / = ; , ( ) { } < >'
        ],

        [
            '== != <= >=',
            '== != <= >='
        ],
        
        [
            "' '",
            "\' \'"
        ],
       
        [
            '" "',
            '\" \"'
        ] 
    ]
    # #tag_tokens_end
}

def run_cases(verbose: bool):
    padding = "\n\n"

    scorecard_template = {
        "test_name": "",
        "test_cases": 0,
        "passes": 0,
        "fails": 0
    }

    scorecards = []

    test_func = False

    tests = list(TEST_CASES)    
    print(f"{padding}{padding}")
    print(f"running tests: {list(tests)}")
    print(f"{padding}{padding}")

    for test in tests:
        print(f'Test: {test}')
        cases = TEST_CASES[test]
        # make a copy, not a reference
        scorecard = dict(scorecard_template)
        scorecard['test_name'] = test
        scorecard['test_cases'] = len(cases)

        case_counter = 0
        for case in cases:
            case_counter += 1
            print(f"case_{case_counter}: '{case[0]}'")
            res = False
            if 'find_ident' == test:
                res = find_ident(case[0], verbose)
            elif  'find_tokens' == test:
                res = find_tokens(case[0], verbose)

            if res == case[1]:
                scorecard['passes'] = scorecard['passes'] + 1
                print('Pass.\n')
            else:
                scorecard['fails'] = scorecard['fails'] + 1
                print(f"{scorecard['test_name']} Test {case_counter}/{len(cases)} failed -- res: '{res}'   case: '{case[0]}'    expected: '{case[1]}'")
        print(f"Tests complete. Scorecard: {scorecard}")
        print(f"{padding}{padding}")
        print(f"{padding}{padding}")
            
    return



run_cases(verbose=False)