#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict

"""
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.
"""

def is_palindrome(s):
    if len(set(s)) <= 1:
        return True
    for i in range(len(s) // 2):
        if s[i] != s[-i-1]:
            return False
    return True


class Trie:
    def __init__(self):
        self.paths = defaultdict(Trie)
        self.end_idx = -1
        self.word = ""
        self.palindromes_below = []
    
    def add_word(self, word, idx):
        trie = self
        for j, char in enumerate(reversed(word)):
            if is_palindrome(word[:len(word) - j]):
                trie.palindromes_below.append(word[:len(word) - j])
            trie = trie.paths[char]
        trie.end_idx = idx
        trie.word = word


def make_trie(words):
    trie = Trie()
    for i, word in enumerate(words):
        trie.add_word(word, i)
    return trie


def get_palindromes(trie, word):
    palindromes = []
    curr = word
    while curr:
        if trie.end_idx >= 0:
            if not curr[0] in trie.paths:
                return palindromes
        trie = trie.paths[curr[0]]
        curr = curr[1:]
    if trie.end_idx >= 0:
        palindromes.append(trie.word)
    if trie.palindromes_below:
        palindromes.extend(
            [postfix + word[::-1] for postfix in trie.palindromes_below]
        )
    return palindromes


def palindrome_pairs(words):
    trie = make_trie(words)
    pairs = []
    for word in words:
        candidates = get_palindromes(trie, word)
        pairs.extend([
            [word, pair]
            for pair in candidates 
            if pair and pair != word
        ])
    return pairs


if __name__ == "__main__":
    assert is_palindrome("") == True
    assert is_palindrome("ababa") == True
    assert is_palindrome("ab") == False
    inputs = [
        ["abcd","dcba","lls","s","sssll"],
        ["bat","tab","cat"],
        ["run", "nu"]
    ]
    expected = [
        [["abcd", "dcba"], ["dcba", "abcd"], ["s", "lls"], ["lls", "sssll"]],
        [["bat", "tab"], ["tab", "bat"]],
        [["nu", "run"]]
    ]
    for i, item in enumerate(inputs):
        output = palindrome_pairs(item)
        assert len(output) == len(expected[i])
        assert [item in output for item in expected[i]]
    print("success!")