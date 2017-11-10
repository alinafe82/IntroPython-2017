#! /usr/bin/env python

"""
Trigram analysis is very simple. Look at each set of three adjacent words in a document. Use the first two words of the set as a key, and remember the fact that the third word followed that key. Once you’ve finished, you know the list of individual words that can follow each two word sequence in the document. For example, given the input:

I wish I may I wish I might
You might generate:

"I wish" => ["I", "I"]
"wish I" => ["may", "might"]
"may I"  => ["wish"]
"I may"  => ["I"]
 """
import random
# import string

# raw_input_list = []
input_string = []
# initial_trigram_key = tuple()
# output_list = []

# Make these strings instead of lists for the str.translate method

# List of chars to remove or replace with a space from input text
# unwanted_punc = ['-',
#                  "'",
#                  ',',
#                  '.',
#                  ')',
#                  '(',
#                  '"',
#                  '?',
#                  ';',
#                  '\n']

# substitution_chars = [' ',
#                       ' ',
#                       ' ',
#                       ' ',
#                       ' ',
#                       ' ',
#                       ' ',
#                       ' ',
#                       ' ',
#                       ' ']
substitution_chars = ' ' * 10
unwanted_punc = '-' + "'" + ',' + '.' + ')' + '(' + '"' + '?' + ';' + '\n'


def replace_unwanted_punctuation(raw_input_string, unwanted_punc,
                                 substitution_chars):
    """ Build up an input string with unwanted punctuation replaced
    in accordance with a string of chars
    :param1 = a string with punctuation
    :param2 = a string of unwanted punctuation
    :param3 = a string of char to substitue for the unwanted punctuation
    :return a string free of unwanted punctuation
    """
    # Now that the read in file is one string. Use str.translate
    # for i, x in enumerate(raw_input_list):
    #     if x in replace_punc:
    #         input_list.append(' ')
    #     else:
    #         input_list.append(x)

    # maketrans returns a table
    transition_table = raw_input_string.maketrans(
        unwanted_punc, substitution_chars)
    input_string = raw_input_string.translate(transition_table)
    return input_string


def create_the_trigram(input_string):
    """ Create a trigram from a list.
    :param1 = a list
    :return = a dictionary, (trigram)
    """
    trigram = {}
    # we need a pair hence the len(input_list) - 2
    #   instead of len(input_list) - 1
    for i in range(len(input_string) - 2):
        # must be a tuple in order to be a key in trigram
        trigram_key = tuple(input_string[i:i + 2])
        trigram_followers = input_string[i + 2]
        # this is so nifty, I had to use it
        trigram.setdefault(trigram_key, []).append(trigram_followers)
    return trigram


def initial_output_list(trigram):
    """Initialize the output list with three elements derived from a
    random trigram key
    :param = dictionary, (trigram)
    :return list
    """
    # Remove - 1
    # random_number = random.randrange(0, len(trigram) - 1)
    random_number = random.randrange(0, len(trigram))
    for i, trigram_key in enumerate(trigram):
        if i == random_number:
            initial_trigram_key = trigram_key
            break
    output_list = list(initial_trigram_key) + trigram[initial_trigram_key]
    return output_list


if __name__ == "__main__":
    with open('./sherlock.txt', 'r') as f_input:
        # Keeping this as one big string so string methods can be used
        # Changing var to reflect that it is a string now
        # raw_input_list = list(f_input.read())
        raw_input_string = f_input.read()

    # Clean up the input
    input_string = replace_unwanted_punctuation(
        raw_input_string, unwanted_punc, substitution_chars)

    # get a list of words, instead of chars
    input_text = "".join(input_string)
    input_string = input_text.split(" ")

    # Create the trigram from the cleaned up input
    trigram = create_the_trigram(input_string)

    # Build the text output.text
    # Start with a random word from the trigram

    output_list = initial_output_list(trigram)

    while(True):
        # Next keyword pair = last two elements of output_list
        new_key = tuple(output_list[-2:])
        try:
            trigram_followers_list = trigram[new_key]
        except KeyError:
            print('exiting')
            break
        random_trigram_followers = random.choice(trigram_followers_list)
        # useless line
        # new_value = random_trigram_followers
        # Don't add list(new_key) to output
        # output_list = output_list + list(new_key) +
        # [random_trigram_followers]
        # output_list = output_list + list(new_key[1]) +
        # [random_trigram_followers]
        output_list = output_list + [random_trigram_followers]
        if len(output_list) > 5000:
            break
    t = " ".join(output_list)
    # print(t)
    with open('trigrams.txt', 'w') as f_output:
        f_output.write(t)