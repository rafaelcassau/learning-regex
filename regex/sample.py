""" 
"""


import re


text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacteres (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

+55 (16) 91122-1134
+55 (16) 91122-1134

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mt. T
'''


sentence = 'Start a sentence with a middle Start and middle end and then bring it to an end'


def matcher(term, text_to_search):
    print(f'Looking for {term}')

    count = 0
    pattern = re.compile(term)
    matches = pattern.finditer(text_to_search)
    for match in matches:
        print(match)
        count += 1
    
    print(f'Matched {count} items.\n')
    return count


def test_should_match_abc():
    matches_count = matcher(r'abc', text_to_search)
    assert matches_count == 1


def test_should_match_ABC():
    matches_count = matcher(r'ABC', text_to_search)
    assert matches_count == 1


def test_should_match_url():
    matches_count = matcher(r'coreyms\.com', text_to_search)
    assert matches_count == 1


def test_should_match_any_characters_except_new_lines():
    matches_count = matcher(r'.', text_to_search)
    assert matches_count == 213


def test_should_match_only_dots():
    matches_count = matcher(r'\.', text_to_search)
    assert matches_count == 7


def test_should_match_only_digits():
    matches_count = matcher(r'\d', text_to_search)
    assert matches_count == 30


def test_should_match_any_characters_except_digits():
    matches_count = matcher(r'\D', text_to_search)
    assert matches_count == 203


def test_should_match_any_digit_any_lower_any_upper_and_underscore_letters():
    matches_count = matcher(r'\w', text_to_search)
    assert matches_count == 165


def test_should_match_any_special_characters_and_spaces():
    matches_count = matcher(r'\W', text_to_search)
    assert matches_count == 68


def test_should_match_any_spaces_tabs_and_new_lines_characters():
    matches_count = matcher(r'\s', text_to_search)
    assert matches_count == 43


def test_should_match_any_no_space_no_tab_and_no_new_line_characters():
    matches_count = matcher(r'\S', text_to_search)
    assert matches_count == 190


def test_should_match_new_line_Ha_and_after_space_Ha():
    matches_count = matcher(r'\bHa', text_to_search)
    assert matches_count == 2


def test_should_match_second_Ha_from_Haha_word_ignore_new_line_and_space_boundaries():
    matches_count = matcher(r'\BHa', text_to_search)
    assert matches_count == 1


def test_should_match_starts_with_Start():
    matches_count = matcher(r'^Start', sentence)
    assert matches_count == 1


def test_should_match_two_Start():
    matches_count = matcher(r'Start', sentence)
    assert matches_count == 2


def test_should_match_ends_with_end():
    matches_count = matcher(r'end$', sentence)
    assert matches_count == 1


def test_should_match_two_end():
    matches_count = matcher(r'end', sentence)
    assert matches_count == 2


def test_simple_should_match_social_number():
    matches_count = matcher(r'\d\d\d.\d\d\d.\d\d\d', text_to_search)
    assert matches_count == 2


def test_simple_should_match_exactly_social_number_with_period():
    matches_count = matcher(r'\d\d\d\.\d\d\d\.\d\d\d', text_to_search)
    assert matches_count == 1


def test_simple_should_match_exactly_social_number_with_score():
    matches_count = matcher(r'\d\d\d-\d\d\d-\d\d\d', text_to_search)
    assert matches_count == 1


if __name__ == '__main__':
    test_should_match_abc()
    test_should_match_ABC()
    test_should_match_url()
    test_should_match_any_characters_except_new_lines()
    test_should_match_only_dots()
    test_should_match_only_digits()
    test_should_match_any_characters_except_digits()
    test_should_match_any_digit_any_lower_any_upper_and_underscore_letters()
    test_should_match_any_special_characters_and_spaces()
    test_should_match_any_spaces_tabs_and_new_lines_characters()
    test_should_match_any_no_space_no_tab_and_no_new_line_characters()
    test_should_match_new_line_Ha_and_after_space_Ha()
    test_should_match_second_Ha_from_Haha_word_ignore_new_line_and_space_boundaries()
    test_should_match_starts_with_Start()
    test_should_match_two_Start()
    test_should_match_ends_with_end()
    test_should_match_two_end()
    test_simple_should_match_social_number()
    test_simple_should_match_exactly_social_number_with_period()
    test_simple_should_match_exactly_social_number_with_score()


# TODO
# findall
# match
# search
# sub
# flags re.compile(r'start', re.IGNORECASE)