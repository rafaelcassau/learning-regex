# learning-regex
The purpouse this repository is to maintain some python common regex examples


# How regex works

## Matches
    .     - Any character except new line
    \d    - Digits [0-9]
    \D    - Not a digit [^0-9]
    \w    - Word character [a-zA-Z0-9_]
    \W    - Not a word character [^a-zA-Z0-9_]
    \s    - Whitespace (space, tab, newline) [\t\n\r\f\v]
    \S    - Not whitespace (space, tab, newline) [^ \t\n\r\f\v]

## Anchors
Anchors doesn't match any characters, but identify some positions like
new lines, before or after a space, starts with or ends with,
these special characters are word boundaries characters

    \b    - Word boundary (indicated for white space or non alphanumeric character like new lines)
    \B    - Not a word boundary
    ^     - Beginning of a string
    $     - End of a string
    []    - Matches characters in brackets (characters into [] will match only 1 character in the set,special character into set does not need to be scaped)
    [^ ]  - Matches characters NOT in
    |     - Either Or
    ( )   - Group

## Quantifiers
    *     - 0 or more
    +     - 1 or more
    ?     - 0 or one
    {3}   - Exact number
    {3,4} - Range of numbers (Minimum, Maximum)

## Pattern object methods
```python
pattern = re.compile(r'my_custom_pattern')

# Match pattern only at the beginning of the string.
pattern.match('text_to_search')

# Scan through a string, looking for any location where pattern matches. (return only the first match.)
pattern.search('text_to_search')

# Find all substrings where pattern matches and returns them as a list.
pattern.findall('text_to_search')

# Find all substrings where pattern matches and returns them as an iterator of match objects.
pattern.finditer('text_to_search')

# Find all substrings where pattern matches and replace them by given first parameter.  
pattern.sub('new_content', 'text_to_search')
```

## Match object methods
```python
match = pattern.match('my_custom_string'))

# Return the string matched in the group, if any group was give the default return will be the
# whole match "group(1)"
match.group(int: number = 1)

# Return the start position of the group.
match.start()

# Return the end position of the group.
match.end()

# Return a tuple containing the (start, end) positions of the match.
match.span()
```

## Basic examples
```python
# pattern.match


def test_simple_match_method():
    pattern = re.compile(r'string')
    match = pattern.match('string, that it is')

    assert match.group() == 'string'
    assert match.span() == (0, 6)
    assert match.start() == 0
    assert match.end() == 6


def test_simple_match_method_does_not_match_in_the_middle_of_text():
    pattern = re.compile(r'string')
    match = pattern.match('that it is a string')

    assert match is None


# pattern.search


def test_simple_search_method():
    pattern = re.compile(r'string')
    match = pattern.search('string, that it is')

    assert match.group() == 'string'
    assert match.span() == (0, 6)
    assert match.start() == 0
    assert match.end() == 6


def test_simple_search_method_does_match_in_the_middle_of_text():
    pattern = re.compile(r'string')
    match = pattern.search('that it is a string')

    assert match.group() == 'string'
    assert match.span() == (13, 19)
    assert match.start() == 13
    assert match.end() == 19


def test_simple_search_method_does_match_in_the_middle_of_text_just_one_time():
    pattern = re.compile(r'string')
    match = pattern.search('that it is a string, string it is')

    assert match.group() == 'string'
    assert match.span() == (13, 19)
    assert match.start() == 13
    assert match.end() == 19


# pattern.findall


def test_simple_findall_method_does_match_in_the_whole_text():
    pattern = re.compile(r'string')
    matches = pattern.findall('that it is a string, string it is')
    
    assert matches == ['string', 'string']


def test_simple_findall_method_does_match_in_the_whole_text_not_found():
    pattern = re.compile(r'string')
    matches = pattern.findall('that it is a STRING, STRING it is')
    
    assert matches == []


def test_simple_findall_method_does_match_in_the_whole_text_with_ignore_case_flag():
    pattern = re.compile(r'string', re.IGNORECASE)
    matches = pattern.findall('that it is a STRING, STRING it is')
    
    assert matches == ['STRING', 'STRING']


## pattern.sub


def should_remove_all_special_characteres_with_re_sub_method():
    content = '''
    0 1 2 3 4 5 6 7 8 9 0 \n
    a,b,c,d,e,f,g,h,i,j,k \t
    0-1-2-3-4-5-6-7-8-9-0 \n
    '''
    pattern = re.compile(r'\s|[,-]')  # it is equal to re.compile(r'\W')
    cleaned_content = pattern.sub('', content)

    print(cleaned_content)
    assert cleaned_content == '01234567890abcdefghijk01234567890'


def should_remove_all_alphabetic_and_special_characteres_with_re_sub_method():
    content = '''
    0 1 2 3 4 5 6 7 8 9 0 \n
    a,b,c,d,e,f,g,h,i,j,k \t
    0-1-2-3-4-5-6-7-8-9-0 \n
    '''
    pattern = re.compile(r'\s|[a-zA-Z-,]')  # it is equal to re.compile(r'\D')
    cleaned_content = pattern.sub('', content)

    print(cleaned_content)
    assert cleaned_content == '0123456789001234567890'


def should_remove_all_numeric_and_special_characteres_with_re_sub_method():
    content = '''
    0 1 2 3 4 5 6 7 8 9 0 \n
    a,b,c,d,e,f,g,h,i,j,k \t
    0-1-2-3-4-5-6-7-8-9-0 \n
    '''
    pattern = re.compile(r'\s|[0-9-,]')  # it is equal to re.compile(r'\d|[-,]')
    cleaned_content = pattern.sub('', content)

    print(cleaned_content)
    assert cleaned_content == 'abcdefghijk'
```

## Real world examples
```python
def test_should_match_phone_numbers():
    """
    +55 (16) 1122-1213
    +55 (16) 91122-1213
    ...
    """
    content = read_file()
    match_count = matcher(r'\+\d{2}\s\(\d{2}\)\s\d{4,5}[-.]\d{4}', content)
    assert match_count == 100


def test_should_match_phone_numbers_ends_with_0_or_1():
    """
    +55 (16) 1122-1210
    +55 (16) 91122-1210
    +55 (16) 1122-1211
    +55 (16) 91122-1211
    ...
    """
    content = read_file()
    match_count = matcher(r'\+\d{2}\s\(\d{2}\)\s\d{4,5}[-.]\d{3}[01]', content)
    assert match_count == 20


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


def test_should_match_all_urls_with_re_group_and_findall_method():
    content = '''
    https://www.google.com
    http://coreyms.com
    https://youtube.com
    https://www.nasa.gov
    '''
    pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
    matches = pattern.findall(content)

    assert matches[0] == ('www.', 'google', '.com')
    assert matches[1] == ('', 'coreyms', '.com')
    assert matches[2] == ('', 'youtube', '.com')
    assert matches[3] == ('www.', 'nasa', '.gov')


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
```

## sources

https://docs.python.org/3/howto/regex.html

https://youtu.be/K8L6KVGG-7o (Corey Schafer)