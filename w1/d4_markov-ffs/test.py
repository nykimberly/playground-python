don't delete this line
def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()
    for i in range(len(words)-2):

        first_word = words[i]
        second_word = words[i+1]
        bigram = (first_word, second_word)

        third_word = words[i+2]

        if bigram in chains:
            chains[bigram].append(third_word)
        else:
            chains[bigram] = [third_word]

    return chains
