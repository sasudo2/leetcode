# class Solution:
#     def solveSudoku(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         possibility_dict = {}

#         for i in range(9):
#             for j in range(9):
#                 if board[i][j] == '.':
#                     possible_values = {1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1}
#                     for k in range(9):
#                         if board[i][k] != '.':
#                             possible_values.pop(int(board[i][k]), None)
#                     for k in range(9):
#                         if board[k][j] != '.':
#                             possible_values.pop(int(board[k][j]), None)
#                     x = i//3*3
#                     y = j//3*3
#                     for k in range(3):
#                         for l in range(3):
#                             if board[x+k][y+l] != '.':
#                                 possible_values.pop(int(board[x+k][y+l]), None)

#                     possibility_dict[(i,j)] = possible_values.copy()


#         def check_values(possibility_dict, board):
#             def isValidSudoku(board: List[List[str]]) -> bool:
#                 def check_row():
#                     for i in range(9):
#                         row = board[i]
#                         unique_values = set(row)
#                         nums_only = [x for x in row if x != '.']
#                         expected = len(nums_only) + (1 if '.' in row else 0)
#                         if len(unique_values) != expected:
#                             return False

#                     return True


#                 def check_column():
#                     for i in range(9):
#                         column = [x[i] for x in board]
#                         unique_values = set(column)
#                         nums_only = [x for x in column if x!='.']
#                         expected = len(nums_only) + (1 if '.' in column else 0)
#                         if len(unique_values) != expected:
#                             return False
                        
#                     return True

#                 def check_block():
#                     for i in range(0, 9, 3):
#                         for j in range(0, 9, 3):
#                             block = []
#                             indices_i = [i+0, i+1, i+2]
#                             indices_j = [j+0, j+1, j+2]
#                             for block_i in indices_i:
#                                 for block_j in indices_j:
#                                     block.append(board[block_i][block_j])

#                             unique_values = set(block)
#                             nums_only = [x for x in block if x!='.']
#                             expected = len(nums_only) + (1 if '.' in block else 0)
#                             if len(unique_values) != expected:
#                                 return False

#                     return True

#                 if check_block() and check_row() and check_column():
#                     return True
                
#                 return False

#             def drop_used(possibility_dict, value, index):
#                 for k in range(9):
#                     if (index[0], k) in possibility_dict:
#                         possibility_dict[(index[0], k)].pop(value, None)
#                 for k in range(9):
#                     if (k, index[1]) in possibility_dict:
#                         possibility_dict[(k, index[1])].pop(value, None)
#                 x = index[0]//3*3
#                 y = index[1]//3*3
#                 for k in range(3):
#                     for l in range(3):
#                         if (x+k, y+l) in possibility_dict:
#                             possibility_dict[(x+k, y+l)].pop(value, None)

#             def rollback(possibility_dict, value, index):
#                 for k in range(9):
#                     if (index[0], k) in possibility_dict:
#                         possibility_dict[(index[0], k)][value] = 1
#                 for k in range(9):
#                     if (k, index[1]) in possibility_dict:
#                         possibility_dict[(k, index[1])][value] = 1
#                 x = index[0]//3*3
#                 y = index[1]//3*3
#                 for k in range(3):
#                     for l in range(3):
#                         if (x+k, y+l) in possibility_dict:
#                             possibility_dict[(x+k, y+l)][value] = 1
#             valid = isValidSudoku(board)
            
#             if not possibility_dict:
#                 return valid

#             if not valid:
#                 return valid
        
#             possibility_dict = dict(sorted(possibility_dict.items(), key = lambda item: len(item[1])))

#             first_key = next(iter(possibility_dict))
#             least_crowded = (first_key, possibility_dict.pop(first_key))

#             for x in least_crowded[1]:
#                 board[least_crowded[0][0]][least_crowded[0][1]] = str(x)
#                 drop_used(possibility_dict, x, least_crowded[0])
#                 valid = check_values(possibility_dict, board)
#                 if valid:
#                     return valid
#                 board[least_crowded[0][0]][least_crowded[0][1]] = '.'
#                 rollback(possibility_dict, x, least_crowded[0])

#             possibility_dict[least_crowded[0]] = least_crowded[1]
#             return False


#         check_values(possibility_dict, board)
                
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [0] * 9   # bitmask of digits used in each row
        cols = [0] * 9   # bitmask of digits used in each column
        boxes = [0] * 9  # bitmask of digits used in each 3x3 box
        empties = []

        def box_index(r, c):
            return (r // 3) * 3 + (c // 3)

        # Initial pass: build masks and collect empty cells
        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == '.':
                    empties.append((r, c))
                else:
                    bit = 1 << int(v)
                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[box_index(r, c)] |= bit

        def candidates(r, c):
            used = rows[r] | cols[c] | boxes[box_index(r, c)]
            return [d for d in range(1, 10) if not (used & (1 << d))]

        def pick_next_cell(remaining):
            # MRV: choose the empty cell with fewest candidates (O(m) scan, no sort)
            best = None
            best_cands = None
            best_count = 10
            for idx, (r, c) in enumerate(remaining):
                cands = candidates(r, c)
                if len(cands) < best_count:
                    best_count = len(cands)
                    best = idx
                    best_cands = cands
                    if best_count == 1:  # can't do better than 1
                        break
            return best, best_cands

        def backtrack(remaining):
            if not remaining:
                return True

            idx, cands = pick_next_cell(remaining)
            if not cands:
                return False  # dead end, no digit fits here

            r, c = remaining[idx]
            b = box_index(r, c)

            # build the next-level list once, without this cell, without
            # disturbing 'remaining' (so the caller's list stays intact
            # if this whole branch fails and we need to try another digit)
            rest = remaining[:idx] + remaining[idx + 1:]

            for d in cands:
                bit = 1 << d
                board[r][c] = str(d)
                rows[r] |= bit
                cols[c] |= bit
                boxes[b] |= bit

                if backtrack(rest):
                    return True

                # rollback
                board[r][c] = '.'
                rows[r] ^= bit
                cols[c] ^= bit
                boxes[b] ^= bit

            return False

        backtrack(empties)