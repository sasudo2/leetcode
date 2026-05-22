class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters_dict = {
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            '8':"tuv",
            '9':"wxyz"
            }
        strings = []
        for digit in digits:
            letters = letters_dict[digit]
            if strings:
                length = len(strings)
                for x in range(length):
                    top = strings.pop(0)
                    for letter in letters:
                        strings.append(top + letter)
            else:
                for letter in letters:
                    strings.append(letter)
                
        
        return strings