"""
"""


import re


def read_file():
    with open('data.txt', 'r') as f:
        data = f.read()
    return data


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


def test_should_match_phone_numbers_without_9_prefix():
    content = read_file()
    match_count = matcher(r'\+\d{2}\s\(\d{2}\)\s\d{4}[-.]\d{4}', content)
    assert match_count == 50


def test_should_match_phone_numbers_with_9_prefix():
    content = read_file()
    match_count = matcher(r'\+\d{2}\s\(\d{2}\)\s\d{5}[-.]\d{4}', content)
    assert match_count == 50


def test_should_match_phone_numbers():
    content = read_file()
    match_count = matcher(r'\+\d{2}\s\(\d{2}\)\s\d{4,5}[-.]\d{4}', content)
    assert match_count == 100


def test_should_match_phone_numbers_ends_with_0():
    content = read_file()
    match_count = matcher(r'\+\d{2}\s\(\d{2}\)\s\d{4,5}[-.]\d{3}[0]', content)
    assert match_count == 10


def test_should_match_phone_numbers_ends_with_1():
    content = read_file()
    match_count = matcher(r'\+\d{2}\s\(\d{2}\)\s\d{4,5}[-.]\d{3}[0]', content)
    assert match_count == 10


def test_should_match_phone_numbers_ends_with_0_or_1():
    content = read_file()
    match_count = matcher(r'\+\d{2}\s\(\d{2}\)\s\d{4,5}[-.]\d{3}[01]', content)
    assert match_count == 20


def test_should_match_all_words_ends_with_at_except_bat():
    content = '''
    cat
    mat
    pat
    bat
    '''
    match_count = matcher(r'[^b]at', content)
    assert match_count == 3


def test_should_match_prefix_Mrdot_mr():
    content = '''
    Mr. Schafer
    Mr Smith
    Ms Davis
    Mrs. Robinson
    Mr. T
    '''
    match_count = matcher(r'Mr\.?\s[A-Z]\w*', content)
    assert match_count == 3


def test_should_match_prefix_Mrdot_Mr_and_complete_first_name():
    content = '''
    Mr. Schafer
    Mr Smith
    Ms Davis
    Mrs. Robinson
    Mr. T
    '''
    match_count = matcher(r'Mr\.?\s[A-Z]\w+', content)
    assert match_count == 2


def test_should_match_all_prefix_with_regex_groups():
    content = '''
    Mr. Schafer
    Mr Smith
    Ms Davis
    Mrs. Robinson
    Mr. T
    '''
    match_count = matcher(r'M(r|s|rs)\.?\s[A-Z]\w*', content)
    assert match_count == 5


def test_should_match_all_prefix_with_regex_groups_more_readble():
    content = '''
    Mr. Schafer
    Mr Smith
    Ms Davis
    Mrs. Robinson
    Mr. T
    '''
    match_count = matcher(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*', content)
    assert match_count == 5


def test_should_match_all_valid_emails():
    content = '''
    RafaelCassau@gmail.com
    rafael.cassau@university.edu
    rafael-cassau-89@my-work.net
    rafael_cassau89@gmail.com.br
    invalid-email1.com
    invalid-email2@
    invalid-email3@com
    invalid-email4@gmail_2.com
    '''
    match_count = matcher(r'[a-zA-Z0-9-_+.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', content)
    assert match_count == 4


def test_should_match_all_urls_with_re_group():
	content = '''
	https://www.google.com
	http://coreyms.com
	https://youtube.com
	https://www.nasa.gov
	'''
	pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
	matches = list(pattern.finditer(content))

	count = 0
	for match in matches:
		print(match)
		count += 1
	print(f'Matched {count} items.')

	assert matches[0].group(0) == 'https://www.google.com'  # group(0) always the whole match
	assert matches[0].group(1) == 'www.'
	assert matches[0].group(2) == 'google'
	assert matches[0].group(3) == '.com'

	assert matches[1].group(0) == 'http://coreyms.com'  # group(0) always the whole match
	assert matches[1].group(1) == None
	assert matches[1].group(2) == 'coreyms'
	assert matches[1].group(3) == '.com'

	assert matches[2].group(0) == 'https://youtube.com'  # group(0) always the whole match
	assert matches[2].group(1) == None
	assert matches[2].group(2) == 'youtube'
	assert matches[2].group(3) == '.com'

	assert matches[3].group(0) == 'https://www.nasa.gov'  # group(0) always the whole match
	assert matches[3].group(1) == 'www.'
	assert matches[3].group(2) == 'nasa'
	assert matches[3].group(3) == '.gov'


def test_should_replace_group_two_by_group_three_with_re_sub():
	content = '''
	https://www.google.com
	http://coreyms.com
	https://youtube.com
	https://www.nasa.gov
	'''
	pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
	
	# replace group(2) "www." optional by group(3) "domain-name"
	# the final string is without "http://" and "https://" prefix because this pattern
	# is out of the group's scope
	replaced_urls = pattern.sub(r'\2\3', content)
	print(replaced_urls)

	assert replaced_urls == '''
	google.com
	coreyms.com
	youtube.com
	nasa.gov
	'''


if __name__ == '__main__':
	# file
	test_should_match_phone_numbers_without_9_prefix()
	test_should_match_phone_numbers_with_9_prefix()
	test_should_match_phone_numbers()
	test_should_match_phone_numbers_ends_with_0()
	test_should_match_phone_numbers_ends_with_1()
	test_should_match_phone_numbers_ends_with_0_or_1()

	# unit
	test_should_match_all_words_ends_with_at_except_bat()
	test_should_match_prefix_Mrdot_mr()
	test_should_match_prefix_Mrdot_Mr_and_complete_first_name()
	test_should_match_all_prefix_with_regex_groups()
	test_should_match_all_prefix_with_regex_groups_more_readble()
	test_should_match_all_valid_emails()
	test_should_match_all_urls_with_re_group()
	test_should_replace_group_two_by_group_three_with_re_sub()
