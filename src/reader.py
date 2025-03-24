def readTxt(file):
    try:
        with open(file, 'r') as f:
            rows = []
            for line in f:
                row = [int(num) for num in line.strip()]
                if len(row) != 9:
                    print("Each row in the file must contain exactly 9 numbers.")
                    return
                rows.append(row)
            
            if len(rows) != 9:
                print("The file must contain exactly 9 rows.")
                return
            
            print("Sudoku grid successfully read from file:")
            for row in rows:
                print(row)
    except FileNotFoundError:
        print(f"File not found: {file}")
    except ValueError:
        print("The file contains invalid characters. Please ensure it only contains numbers.")
    
    return rows;

        