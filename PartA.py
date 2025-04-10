import sys
def determine_tokens(line, token_list):
    previous_word = ''
    for char in line:
        if not char.isalnum() and previous_word != '':
            token_list.append(previous_word.lower())
            previous_word = ''
            continue

        previous_word += char

def tokenize(textFilePath):
    token_list = []
    with open(textFilePath) as file:
        for line in file.readlines():
            determine_tokens(line, token_list)
    return token_list

def computeWordFrequencies(token_list):
    token_dict = {}
    for token in token_list:
        if token in token_dict.keys():
            token_dict[token] = token_dict[token] + 1
        else:
            token_dict[token] = 1
    return token_dict

def compare(entry):
    return entry[1]

def print_map(map):
    results = sorted(map.items(), key = compare, reverse = True)
    for entry in results:
        print(entry[0], entry[1])
#Finally, write a method that prints out the word frequency count onto the screen. The print out should be ordered by decreasing frequency (so, the highest frequency words first).

if __name__ == "__main__":
    if len(sys.argv) > 1:
        token_list = tokenize(sys.argv[1])
        map = computeWordFrequencies(token_list)
        print_map(map)