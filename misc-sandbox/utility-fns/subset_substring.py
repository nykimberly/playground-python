# -*- coding: utf-8 -*-

# xacxzaa
# fxaazxacaaxzoecazxaxaz

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n1 = len(s1)
        n2 = len(s2)
        end = n2 - n1 + 1

        s1_dict = { element: 0 for element in s1 }

        for element in s1:
            s1_dict[element] += 1

        s2_dict = { element: 0 for element in s2[:n1] }

        for element in s2[:n1]:
            s2_dict[element] += 1


        for i in range(0, end):

            if i > 0:
                if s2_dict[s2[i-1]] > 1:
                    s2_dict[s2[i-1]] -= 1
                else:
                    s2_dict.pop(s2[i-1])
                s2_dict[s2[i+n1-1]] = s2_dict.get(s2[i+n1-1], 0) + 1

            if s1_dict == s2_dict:
                return True

        return False