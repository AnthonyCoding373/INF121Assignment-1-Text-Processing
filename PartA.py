import sys
def determine_tokens(line, token_list):
    ''' Time Complexity: O(n)'''
    previous_word = ''
    for char in line:
        if char.isalnum() and char.isascii():
            previous_word += char
        elif previous_word != '':
            token_list.append(previous_word.lower())
            previous_word = ''
            continue

def tokenize(textFilePath):
    '''Time Complexity: O(m * n) with O(m) calls, where m is number of lines,
    to function determine_tokens which is O(n) where n is chars in the line'''
    token_list = []
    with open(textFilePath, 'r', encoding = 'utf-8') as file:
        for line in file.readlines():
            determine_tokens(line, token_list)
    return token_list

def computeWordFrequencies(token_list):
    '''Time Complexity: O(n) where n is number of tokens'''
    token_dict = {}
    for token in token_list:
        if token_dict.get(token, False):
            token_dict[token] = token_dict[token] + 1
        else:
            token_dict[token] = 1
    return token_dict

def compare(entry):
    '''Time complexity: O(1)'''
    return entry[1]

def print_map(map):
    '''Time Complexity: O(nlogn)'''
    results = sorted(map.items(), key = compare, reverse = True)
    for entry in results:
        print(entry[0], entry[1])

if __name__ == "__main__":
    '''Total time complexity is O(m * n + h log h) where m is number of lines, n is chars, and h is
    distinct tokens'''
    if len(sys.argv) > 1:
        token_list = tokenize(sys.argv[1])
        map = computeWordFrequencies(token_list)
        print_map(map)