import sys
def determine_tokens(line, token_list):
    ''' Time Complexity: O(n)'''
    previous_word = ''
    for char in line:
        if not char.isalnum() and previous_word != '':
            token_list.append(previous_word.lower())
            previous_word = ''
            continue

        previous_word += char

def tokenize(textFilePath):
    '''Time Complexity: O(m * n) with O(m) calls, where m is number of lines,
    to function determine_tokens which is O(n) where n is chars in the line'''
    token_list = []
    with open(textFilePath) as file:
        for line in file.readlines():
            determine_tokens(line, token_list)
    return token_list

def computeWordFrequencies(token_list):
    '''Time Complexity: O(n)'''
    token_dict = {}
    for token in token_list:
        if token in token_dict.keys():
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

def compare_mapping(map1, map2):
    '''Time complexity: O(n)'''
    map_items_1 = map1.items()
    count = 0
    for entry in map_items_1:
        current_word = entry[0]
        if map2.get(current_word, False):
            count += 1
    return count


if __name__ == "__main__":
    '''Total time complexity is O(m * n + n log n)'''
    if len(sys.argv) > 2:
        token_list_1 = tokenize(sys.argv[1])
        map1 = computeWordFrequencies(token_list_1)
        token_list_2 = tokenize(sys.argv[2])
        map2 = computeWordFrequencies(token_list_2)
        count = compare_mapping(map1, map2)
        print(count)