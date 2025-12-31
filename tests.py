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
            #   e.g.:
            #       if 'find_ident' == test:
            #          res = find_ident(case[0], verbose)
            # 
            # #tag_new_test_instructions_end


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