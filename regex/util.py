import re


def read_file():
    with open('data.txt', 'r') as f:
        data = f.read()
    return data


def matcher(term, text_to_search):
    # This method is an alias to avoid code duplication
    print(f'Looking for {term}')

    count = 0
    pattern = re.compile(term)
    matches = pattern.finditer(text_to_search)
    for match in matches:
        print(match)
        count += 1
    
    print(f'Matched {count} items.\n')
    return count