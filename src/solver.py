import reader
import matplotlib 
from matplotlib import pyplot
matplotlib.use('TkAgg') 

def solver():
    table = reader.readTxt("input.txt")  
    
    if solveSudoku(table, 0, 0):
        print("Solved Sudoku:")
        for row in table:
            print(row)
            
            fig, ax = pyplot.subplots(figsize=(5, 5))
            ax.set_axis_off()
            table_colors = [["white" if (i // 3 + j // 3) % 2 == 0 else "lightgrey" for j in range(9)] for i in range(9)]
            table_obj = pyplot.table(cellText=table, loc='center', cellLoc='center', cellColours=table_colors)
            table_obj.auto_set_font_size(False)
            table_obj.set_fontsize(12)
            table_obj.scale(1.2, 1.2)
            pyplot.show()
    else:
        print("No solution exists.")
    return

def validator(pos, table):
    possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    valid_numbers = []

    for num in possibilities:
        if valid_horizontal(table[pos[0]], num) and valid_vertical(pos, num, table) and valid_3x3(pos[0], pos[1], table, num):
            valid_numbers.append(num)
    
    return valid_numbers

def valid_3x3(row, col, table, num):
    startRow = row - (row % 3)
    startCol = col - (col % 3)

    for i in range(3):
        for j in range(3):
            if table[i + startRow][j + startCol] == num:
                return False
    return True

def find_next_free(pos, table):
    for x in range(pos[0], 9):
        for y in range(9):
            if table[x][y] == 0:
                return (x, y)
    return None  

def valid_horizontal(row, num):
    return num not in row

def valid_vertical(pos, num, table):
    column = [table[i][pos[1]] for i in range(9)]
    return num not in column

def solveSudoku(table, row, col):
    if row == 8 and col == 9:
        return True

    if col == 9:
        row += 1
        col = 0

    if table[row][col] != 0:
        return solveSudoku(table, row, col + 1)

    for num in range(1, 10):
        if valid_3x3(row, col, table, num) and valid_vertical((row, col), num, table) and valid_horizontal(table[row], num):
            table[row][col] = num  

            if solveSudoku(table, row, col + 1):
                return True

            table[row][col] = 0

    return False

solver();