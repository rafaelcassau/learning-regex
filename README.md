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

## sources

https://docs.python.org/3/howto/regex.html

https://youtu.be/K8L6KVGG-7o (Corey Schafer)