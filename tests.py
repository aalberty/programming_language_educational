# NOTE: To add new tests, check out the `new_test_instructions` tag

from lexer import Lexer as lexer
from lexer import _vprint

# #tag_new_test_instructions_start
# 
# Steps to append a new test with cases
#
# #tag_new_test_instructions_end



# #tag_new_test_instructions_start
# 
# STEP 1: Create a test function.
#
# def test_name(case, verbose):
#   should return a stringified expected output from the
#   function getting tested
#
# #tag_new_test_instructions_end

# #tag_value_start
def find_value(case, verbose):
    _vprint(verbose, f'Testing lexer.find_value() for source "{case}"')
    l = lexer(case)
    # finding a value implies that there's already an IDENT found
    l.find_next_token()
    l.find_ident()
    value = l.find_value()

    if value == False:
        return

    _vprint(verbose, f"VALUE = '{value.literal}'")
    _vprint(verbose, '\n')
    return value.literal
# #tag_value_end

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


# #tag_new_test_instructions_start
# 
# 
# Step 2: add cases for the new test by adding an entry like 
# 
# the following --
# 
# "test_name": [
#     [ 'case_i', 'expected_i' ],
# ]
# 
#
# #tag_new_test_instructions_end

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
    ],
    # #tag_tokens_end

    # #tag_value_start
    "find_value": [
        [
            'let x = 5;',
            '5'
        ],
        [
            'let x=10;',
            '10'
        ],
        [
            'let s = "hello";',
            "'hello'"
        ]
    ]
    # #tag_value_end
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
            
            
            # #tag_new_test_instructions_start
            # 
            # Step 3: add an elif check matching the format below to fire as part of the suite
            #
            # #tag_new_test_instructions_end


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



# run_cases(verbose=False)