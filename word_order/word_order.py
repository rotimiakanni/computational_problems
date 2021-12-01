from os.path import realpath, join, dirname

'''
Link to problem: https://www.hackerrank.com/challenges/word-order/problem

You are given n words. Some words may repeat. For each word, output its 
number of occurrences. The output order should correspond with the input 
order of appearance of the word. See the sample input/output for clarification.
Note: Each input line ends with a "\n" character.

sample input:
4
bcdef
abcdefg
bcde
bcdef

sample output:
3
2 1 1
'''
word_dict = {}

def check_word(word):
    if word_dict.get(word):
        word_dict[word] += 1
    else:
        word_dict[word] = 1

def word_string(word_dict_):
    return_str  = ' '.join([str(x) for x in list(word_dict_.values())])
    return return_str

input_file = join(dirname(realpath(__file__)), 'sample.txt')
ip_file = open(input_file)

for x in range(int(ip_file.readline())):
    check_word(ip_file.readline().strip())
print(str(len(word_dict)))
print(word_string(word_dict))