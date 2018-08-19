#Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


class Solution:

    def letterCombinations(self, digits):

        nums = list(d for d in str(digits))
        keymap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                  "6": "mno", "7": "pqrs", "8": "tuv",
                  "9": "wxyz"}

        for n in nums:
            assert n in keymap, \
                "digits must be between 2 and 9 (inclusive)!"

        results = []

        if len(nums) < 1:
            return results

        self.recurse(keymap, nums, 0, "", results)

        return results

    def recurse(self, keymap, nums, i, ss, results):

        if len(ss) == len(nums):
            results.append(ss)
            return

        curr_num = nums[i]

        for char in keymap[curr_num]:
            self.recurse(keymap, nums, i+1, ss+char, results)


sol = Solution()
sol.letterCombinations(234)
