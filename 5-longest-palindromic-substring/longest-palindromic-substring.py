class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        longest = s[0]

        def find(s, left, right, longest):
            longest = longest
            substring = None
            while True:
                if left < 0 or right >= length:
                    break
                if s[left] == s[right]:
                    substring = s[left:right+1]
                    if len(substring) > len(longest):
                        longest = substring
                    left = left - 1
                    right = right + 1
                else:
                    break
            return longest
        
        for i in range(0, length):

            if s[i-1:i+2] == s[i-1:i+2][::-1] and i > 0 and i < length:
                left = i - 1
                right = i + 1
                string = find(s, left, right, longest)
                if len(longest) < len(string):
                    longest = string
            if s[i:i+2] == s[i:i+2][::-1] and i<length:
                left = i
                right = i+1
                string = find(s, left, right, longest)
                if len(longest) < len(string):
                    longest = string
            if s[i-1:i+1] == s[i-1:i+1][::-1] and i > 0:
                left = i-1
                right = i
                string = find(s, left, right, longest)
                if len(longest) < len(string):
                    longest = string
        return longest
                  