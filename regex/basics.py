import re
from util import matcher


text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacteres (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
'''


sentence = 'Start a sentence with a middle Start and middle end and then bring it to an end'


# pattern.match


def test_simple_match_method():
    pattern = re.compile(r'string')
    match = pattern.match('string, that it is')

    print(match)
    assert match.group() == 'string'
    assert match.span() == (0, 6)
    assert match.start() == 0
    assert match.end() == 6


def test_simple_match_method_does_not_match_in_the_middle_of_text():
    pattern = re.compile(r'string')
    match = pattern.match('that it is a string')

    print(match)
    assert match is None


# pattern.search


def test_simple_search_method():
    pattern = re.compile(r'string')
    match = pattern.search('string, that it is')

    print(match)
    assert match.group() == 'string'
    assert match.span() == (0, 6)
    assert match.start() == 0
    assert match.end() == 6


def test_simple_search_method_does_match_in_the_middle_of_text():
    pattern = re.compile(r'string')
    match = pattern.search('that it is a string')

    print(match)
    assert match.group() == 'string'
    assert match.span() == (13, 19)
    assert match.start() == 13
    assert match.end() == 19


def test_simple_search_method_does_match_in_the_middle_of_text_just_one_time():
    pattern = re.compile(r'string')
    match = pattern.search('that it is a string, string it is')

    print(match)
    assert match.group() == 'string'
    assert match.span() == (13, 19)
    assert match.start() == 13
    assert match.end() == 19


# pattern.findall


def test_simple_findall_method_does_match_in_the_whole_text():
    pattern = re.compile(r'string')
    matches = pattern.findall('that it is a string, string it is')
    
    print(matches)
    assert matches == ['string', 'string']


def test_simple_findall_method_does_match_in_the_whole_text_not_found():
    pattern = re.compile(r'string')
    matches = pattern.findall('that it is a STRING, STRING it is')
    
    print(matches)
    assert matches == []


def test_simple_findall_method_does_match_in_the_whole_text_with_ignore_case_flag():
    pattern = re.compile(r'string', re.IGNORECASE)
    matches = pattern.findall('that it is a STRING, STRING it is')
    
    print(matches)
    assert matches == ['STRING', 'STRING']


# pattern.finditer


def test_simple_finditer_method_does_match_in_the_whole_text():
    pattern = re.compile(r'string')
    matches = pattern.finditer('that it is a string, string it is')
    
    count = 0
    for match in matches:
        print(match)
        count += 1

    assert count == 2


def test_simple_finditer_method_does_match_in_the_whole_text_not_found():
    pattern = re.compile(r'string')
    matches = pattern.finditer('that it is a STRING, STRING it is')
    
    count = 0
    for match in matches:
        print(match)
        count += 1

    assert count == 0


def test_simple_finditer_method_does_match_in_the_whole_text_with_ignore_case_flag():
    pattern = re.compile(r'string', re.IGNORECASE)
    matches = pattern.finditer('that it is a STRING, STRING it is')
    
    count = 0
    for match in matches:
        print(match)
        count += 1

    assert count == 2


# matcher util method


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
    assert matches_count == 204


def test_should_match_only_dots():
    matches_count = matcher(r'\.', text_to_search)
    assert matches_count == 4


def test_should_match_only_digits():
    matches_count = matcher(r'\d', text_to_search)
    assert matches_count == 60


def test_should_match_any_characters_except_digits():
    matches_count = matcher(r'\D', text_to_search)
    assert matches_count == 161


def test_should_match_any_digit_any_lower_any_upper_and_underscore_letters():
    matches_count = matcher(r'\w', text_to_search)
    assert matches_count == 158


def test_should_match_any_special_characters_and_spaces():
    matches_count = matcher(r'\W', text_to_search)
    assert matches_count == 63


def test_should_match_any_spaces_tabs_and_new_lines_characters():
    matches_count = matcher(r'\s', text_to_search)
    assert matches_count == 35


def test_should_match_any_no_space_no_tab_and_no_new_line_characters():
    matches_count = matcher(r'\S', text_to_search)
    assert matches_count == 186


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
    assert matches_count == 5


def test_simple_should_match_exactly_social_number_with_period():
    matches_count = matcher(r'\d\d\d\.\d\d\d\.\d\d\d', text_to_search)
    assert matches_count == 1


def test_simple_should_match_exactly_social_number_with_asterisk():
    matches_count = matcher(r'\d\d\d\*\d\d\d\*\d\d\d', text_to_search)
    assert matches_count == 1


def test_simple_should_match_exactly_social_number_with_score():
    matches_count = matcher(r'\d\d\d-\d\d\d-\d\d\d', text_to_search)
    assert matches_count == 3


if __name__ == '__main__':
    # pattern.match
    test_simple_match_method()
    test_simple_match_method_does_not_match_in_the_middle_of_text()

    # pattern.search
    test_simple_search_method()
    test_simple_search_method_does_match_in_the_middle_of_text()
    test_simple_search_method_does_match_in_the_middle_of_text_just_one_time()

    # pattern.findall
    test_simple_findall_method_does_match_in_the_whole_text()
    test_simple_findall_method_does_match_in_the_whole_text_not_found()
    test_simple_findall_method_does_match_in_the_whole_text_with_ignore_case_flag()

    # pattern.finditer
    test_simple_finditer_method_does_match_in_the_whole_text()
    test_simple_finditer_method_does_match_in_the_whole_text_not_found()
    test_simple_finditer_method_does_match_in_the_whole_text_with_ignore_case_flag()

    # matcher util method
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
    test_simple_should_match_exactly_social_number_with_asterisk()
    test_simple_should_match_exactly_social_number_with_score()


# TODO
# findall
# sub
# flags re.compile(r'start', re.IGNORECASE)