from sys import argv

script, filename = argv

def create_word_list(filename):

	word_list = []

	input_file = open(filename)

	for line in input_file:
	    words = line.rstrip().split(" ")
	    for word in words:
	        word_list.append(word)

	input_file.close()

	return word_list


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
	    print "%s %d" % (key, value)


def main():
	print_dict(create_dictionary(create_word_list(filename)))


if __name__ == "__main__":
	main()