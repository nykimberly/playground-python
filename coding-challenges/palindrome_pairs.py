#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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

def palindrome_pairs_failed(list_words):
    """This implementation does not work.
    It is possible that we need to index both sll and s to key s.
    We will need a trie.
    """
    pairs = []
    fwd_ss = {}
    rev_ss = {}
    for word in list_words:
        for i in range(1, len(word) + 1):
            pre, rev_pre = word[:i], word[::-1][:i]
            post, rev_post = word[i:], word[::-1][i:]
            pre_rev = pre[::-1]
            if is_palindrome(post):
                if pre_rev in fwd_ss:
                    pairs.append([pre_rev + fwd_ss[pre_rev], pre + post])
                fwd_ss[pre] = post
            if is_palindrome(rev_post):
                if pre_rev in rev_ss:
                    pairs.append([pre + post, pre_rev + fwd_ss[pre_rev]])
                rev_ss[rev_pre] = rev_post
    return pairs


if __name__ == "__main__":
    assert is_palindrome("") == True
    assert is_palindrome("ababa") == True
    assert is_palindrome("ab") == False
    assert palindrome_pairs_failed(["lls","s","sssll"]) == [["s", "lls"], ["lls", "sssll"]]