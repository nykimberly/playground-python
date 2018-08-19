class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lst = []
        closing_brackets = {")":"(", "}":"{", "]":"["}

        if len(s) == 0:
            return True

        for char in s:

            # if char is closing bracket but nothing is in lst => invalid
            if char in closing_brackets and not lst:
                return False

            # if char is in closing but lst.pop is not its counterpart => invalid
            if char in closing_brackets:
                top_stack = lst.pop()
                if closing_brackets[char] != top_stack:
                    return False

            # if char is not a closing bracket, then add to stack
            if char not in closing_brackets:
                lst.append(char)

        if not lst:
            return True
        else:
            return False