import sys


''' 
For function determine_tokens
Time Complexity:
Average case: O(n)
    - n is number of chars

Worst case: O(n * h)
    - n is number of chars
    - h is number of words.

The worst case scenario only occurs when a collision in the set occurs
which can cause O(h) for adding'''
def determine_tokens(line, token_set):
    previous_word = ''
    for char in line:
        if char.isalnum() and char.isascii():
            previous_word += char
        elif previous_word != '':
            token_set.add(previous_word.lower())
            previous_word = ''
            continue

'''
For function tokenize
Time Complexity:
average case: O(m * n)
    - m is number of lines
    - n is number of chars in each line

worst case: O(m * n * h)
    - m is number of lines
    - n is number of chars in each line
    - h is number of tokens and only contributes when collisions when adding to the set occurs'''
def tokenize(textFilePath):
    token_set = set()
    with open(textFilePath, 'r', encoding = 'utf-8') as file:
        for line in file.readlines():
            determine_tokens(line, token_set)
    return token_set


'''
For function compare_mapping
Time complexity: O(min(n, m))
n is the number of elements in token_set1
m is the number of elements in token_set2
'''
def compare_mapping(token_set1, token_set2):
    set3 = token_set1.intersection(token_set2)
    return len(set3)

if __name__ == "__main__":
    '''
    Time complexity:
    
    Average case: O(m * n)
        - n is number of chars in each line
        - m is the number of lines in the file 
        
    Worst-case O(m * n * h)
        - h is the number of tokens and only contributes when collisions occur when adding to the set 
        - n is number of chars in each line
        - m is the number of lines in the file 
        
    Intersection of two lists is an additional action that is O(min(t, r)) where t is number of
    elements in token_set1 and r is number of elements in token_set_2. But since it is not a dominant term
    it is not in the time complexity'''

    if len(sys.argv) > 2:
        token_set_1 = tokenize(sys.argv[1])
        token_set_2 = tokenize(sys.argv[2])
        count = compare_mapping(token_set_1, token_set_2)
        print(count)