class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        p1 = 0
        out = []
        string_length = len(s)
        word_length = len(words[0])
        counted = {}
        for word in words:
            counted[word] = counted.get(word, 0)+1


        if len(counted) == 1 and len(set(words[0])) == 1 and set(s) == set.union(*[set(x for x in words)]):
            return [x for x in range(0, string_length + 1 - len(words)*word_length)]

        #loop for the entire string length
        #create pointer p2
        #create counting dictionary for words in string
        #loop while word from string is in counted and value of count for the word in string is lessthen or equal to value of count for corresponding word in words.
        #increment the count in counting dictionary
        #increment pointer p2
        #compare the counting dictionary and counted and append p1 to out if same
        #increment p1

        while p1 < string_length:
            p2 = p1
            count_dict = {}
            while s[p2:p2+word_length] in counted and count_dict.get(s[p2:p2+word_length], 0) < counted[s[p2:p2+word_length]]:
                count_dict[s[p2:p2+word_length]] = count_dict.get(s[p2:p2+word_length], 0) + 1
                p2 = p2 + word_length

            if count_dict == counted:
                out.append(p1)
            
            p1 += 1

        return out