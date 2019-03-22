# learning-regex
The purpouse this repository is to maintain some python common regex examples


# How regex works

## Matches
    .     - Any character except new line
    \d    - Digit (0-9)]
    \D    - Not a digit (0-9)
    \w    - Word character (a-z, A-Z, 0-9, _)
    \W    - Not a word character
    \s    - Whitespace (space, tab, newline)
    \S    - Not whitespace (space, tab, newline)

## Anchors
does not match any characters, but identify some positions like
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


## sources

https://youtu.be/K8L6KVGG-7o (Corey Schafer)