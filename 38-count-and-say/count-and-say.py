class Solution:
    def countAndSay(self, n: int) -> str:
        rle_sequence = ["1"]
        if n == 1:
            return "".join(rle_sequence)

        def rle(rle_sequence):
            new_sequence = []
            count = 0
            previous = None
            for i in range(len(rle_sequence)):
                if previous == None:
                    previous = rle_sequence[i]
                    count = 1
                elif previous != rle_sequence[i]:
                    new_sequence.append(str(count))
                    new_sequence.append(str(previous))
                    previous = rle_sequence[i]
                    count = 1
                else:
                    count += 1
            new_sequence.append(str(count))
            new_sequence.append(str(previous))
            return new_sequence

        for i in range(n-1):
            rle_sequence = rle(rle_sequence)

        return "".join(rle_sequence)