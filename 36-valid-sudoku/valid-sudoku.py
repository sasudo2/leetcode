class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_row():
            for i in range(9):
                row = board[i]
                unique_values = set(row)
                nums_only = [x for x in row if x!='.']
                if len(unique_values) != len(nums_only) + 1:
                    return False

            return True


        def check_column():
            for i in range(9):
                column = [x[i] for x in board]
                unique_values = set(column)
                nums_only = [x for x in column if x!='.']
                if len(unique_values) != len(nums_only)+1:
                    return False
                
            return True

        def check_block():
            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    block = []
                    indices_i = [i+0, i+1, i+2]
                    indices_j = [j+0, j+1, j+2]
                    for block_i in indices_i:
                        for block_j in indices_j:
                            block.append(board[block_i][block_j])

                    unique_values = set(block)
                    nums_only = [x for x in block if x!='.']
                    if len(unique_values) != len(nums_only)+1:
                        return False

            return True

        if check_block() and check_row() and check_column():
            return True
        
        return False



        