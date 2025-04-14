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
    to function determine_tokens which is O(n) where n is number of chars in the line'''
    token_list = []
    with open(textFilePath, 'r', encoding = 'utf-8') as file:
        for line in file.readlines():
            determine_tokens(line, token_list)
    return token_list

def computeWordFrequencies(token_list):
    '''Time Complexity
    O(n) on average but can degrade to O(n^2) where n is number of tokens
    if many collisions occur'''
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
    '''Total time complexity
     Average case: O(m * n + h log h) 
             -m is number of lines
             -n is number of chars
             -h is distinct tokens
             -r is number of tokens (not part of term, but included here for reference)
     The term O(r) is not added to the average cost since it is linear and thus does not
     dominate the expression. 
        
     Worst Case scenario: O(m * n + h log h + r^2)
             -m is number of lines
             -n is number of chars
             -h is distinct tokens
             -r is number of tokens

     The worst case scenario occurs only if collisions happen while accessing/adding to the dictionary
     There is no one-dominating term since the time complexity depends
     on the file parsed through to determine which term will dominates.
     
     Summary: 
        To summarize O(m * n) happens from reading all the lines in the file and processing the
        characters in each line.
        The O(h log h) is added from sorting all the distinct tokens.
        Finally the term O(r^2) occurs when trying to access/add to the dictionary results in collisions.
     '''

    if len(sys.argv) > 1:
        token_list = tokenize(sys.argv[1])
        map = computeWordFrequencies(token_list)
        print_map(map)