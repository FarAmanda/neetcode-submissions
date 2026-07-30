class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Checking horizontally
        for i in range(9):
            dict = {}
            for j in range(9):
                inp = board[i][j]
                if inp == ".":
                    continue
                elif inp in dict:
                    print("Failed at horizontal", i, j, board[i][j])
                    return False
                else:
                    dict[inp] = 1

        # Checking Vertically
        for i in range(9):
            dict = {}
            for j in range(9):
                inp = board[j][i]
                if inp == ".":
                    continue
                elif inp in dict:
                    print("Failed at vertical", i, j, board[j][i])
                    return False
                else:
                    dict[inp] = 1


        # Checking each box

        trace = 0
        while(trace != 3):
            shift = 0
            while(shift != 3):
                print("dict clear")
                dict = {}
                for i in range(3):
                    for j in range(3):
                        inp = board[i + (trace * 3)][j + (shift * 3)]
                        print(board[i + (trace * 3)][j + (shift * 3)])
                        if inp == ".":
                            continue
                        elif inp in dict:
                        
                            print("Failed at box", trace, ",", shift,":", i, j)
                            return False
                        else: 
                            dict[inp] = 1
                shift += 1
            trace +=1

        return True




        

