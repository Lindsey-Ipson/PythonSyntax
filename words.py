def print_upper_words(list, letter_set):
    """For a list of words, prints out each word 
    on a separate line in uppercase letters
    if that words starts one of the letters
    in given set of letters"""

    for word in list:
        for letter in letter_set:
            if word.startswith(letter):
                print(word.upper())


# this should print "HELLO", "HEY", "YO", and "YES"

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], {"g", "y"})