import sys
def determine_tokens(line, token_set):
    ''' Time Complexity: O(n)'''
    previous_word = ''
    for char in line:
        if char.isalnum():
            previous_word += char
        elif previous_word != '':
            token_set.add(previous_word.lower())
            previous_word = ''
            continue

def tokenize(textFilePath):
    '''Time Complexity: O(m * n) with O(m) calls, where m is number of lines,
    to function determine_tokens which is O(n) where n is chars in the line'''
    token_set = {}
    with open(textFilePath) as file:
        for line in file.readlines():
            determine_tokens(line, token_set)
    return token_set


def compare_mapping(token_list1, token_list2):
    '''Time complexity: O(min(n, m)) where n is the number of distinct tokens in token_list_1 and m is the
    distinct tokens in token_list2'''
    set1 = set(token_list_1)
    set2 = set(token_list_2)
    set3 = set1.intersection(set2)
    return len(set3)



if __name__ == "__main__":
    '''Total time complexity is O(m * n) since comparing the mapping is an additional 
    action but is smaller than '''
    if len(sys.argv) > 2:
        token_list_1 = tokenize(sys.argv[1])
        token_list_2 = tokenize(sys.argv[2])
        count = compare_mapping(token_list_1, token_list_2)
        print(count)