from tkn import TokenType as token_type
from lexer import Lexer as lexer
from parser import Parser as parser
# NOTE: To add new tests, check out the `new_test_instructions` tag

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

def tokenize(case, verbose):
    l = lexer(case)
    tokens = l.tokenize()
    res = ""
    for t in tokens:
        # TODO: this is probably a bad idea; could accidentally hide bugs with EOF behavior
        if t.type == token_type.EOF:
            continue
        else:
            res += f"{t.literal} "
    res = res.strip()
    return res

def parse(case, verbose):
    return





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
# to the global TEST_CASES = {'<test_name>': [[case_1, expected_1], ...]}
#
# #tag_new_test_instructions_end

TEST_CASES = {
    "tokenize": [
        [
            'let x = 5;',
            'LET x = 5 ;'
        ],
        [
            'let test = 10;',
            'LET test = 10 ;'
        ],
        [
            'let test = "this is a string";',
            'LET test = "this is a string" ;'
        ],
        [
            "let test = 'this is a string';",
            'LET test = "this is a string" ;'
        ],
        [
            'let x = (5 + 9);',
            'LET x = ( 5 + 9 ) ;'
        ],
        [
            '+ - * / = ; , ( ) { } < >',
            '+ - * / = ; , ( ) { } < >'
        ],
        [
            '== != <= >=',
            '== != <= >='
        ],
        [
            "function let var const if for else return",
            "FUNCTION LET VAR CONST IF FOR ELSE RETURN"
        ]
    ],

    "parse": [
        ["let x = 5;", "letStatement(ident=x, value=5)"]
    ]
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
    print(f"\nrunning tests: {list(tests)}")

    for test in tests:
        print(f"{padding}{padding}")
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
            #   e.g.:
            #       if 'find_ident' == test:
            #          res = find_ident(case[0], verbose)
            # 
            # #tag_new_test_instructions_end
            if 'tokenize' == test:
                res = tokenize(case[0], verbose)

            if res == case[1]:
                scorecard['passes'] = scorecard['passes'] + 1
                print('Pass.\n')
            else:
                scorecard['fails'] = scorecard['fails'] + 1
                print(f"{scorecard['test_name']} Test {case_counter}/{len(cases)} failed -- res: '{res}'   case: '{case[0]}'    expected: '{case[1]}'")
        # TODO: change this to be a suite summary with an optional test summary after each individual test if `verbose=True`
        print(f"{padding}{padding}")
        print(f"Tests complete. {scorecard['passes']}/{scorecard['test_cases']} passing tests.{padding}Scorecard: {scorecard}")
    return



# run_cases(verbose=False)

# one-off test

case = 'let x = 5;'
l = lexer(case)
tokens = l.tokenize()
p = parser(tokens)
res = p.parse()
print(res)