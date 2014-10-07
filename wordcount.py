from sys import argv
import string

filename = argv[1]

def create_word_list(filename):

	word_list = []

	input_file = open(filename)

	for line in input_file:
	    words = line.rstrip().split()
	    for word in words:
	    	word = string.lower(remove_punc(word))
	        word_list.append(word)

	input_file.close()

	return word_list


def remove_punc(word):
	
	no_punc = ""

	for char in word:
		if char not in '!,./?-";':
			no_punc = no_punc + char

	return no_punc


def create_dictionary(input_list):

	word_count = {}

	for item in input_list:
	    if word_count.get(item):
	        word_count[item] += 1
	    else:
	        word_count[item] = 1

	return word_count


def print_dict(input_dict):

	for key, value in input_dict.iteritems():
	    print key, value

def sort_and_print(input_dict):

	sorted_list = sorted(input_dict.iteritems(), key=lambda (k, v): (v, k))
	#sorted_list.reverse()
	for item in sorted_list:
		print item[0], item[1]


def main():
	sort_and_print(create_dictionary(create_word_list(filename)))


if __name__ == "__main__":
	main()