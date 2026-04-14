#Split each line into list, replace empty cell to 0
def parse_line(line):
    parts = line.split(",")
    try:
        result = []
        for part in parts:
            if part.strip() == "":
                result.append(0)
            else:
                result.append(float(part))  #Convert cell value to float value
        
        return result
    except ValueError:
        return False

#Calculate sum and average for each row and column
def calc_data(data, cols_len):
    rows_len = len(data)
    col_sum = []
    col_avg = []
    
    #Initialise sum list of each column
    for col in range(0, cols_len):
        col_sum.append(0)
    
    #Calculate sum and average for each row
    for row in data:
        cur_cols_len = len(row)
        row_sum = 0
        for col in range(0, cols_len):
            if col < cur_cols_len:
                row_sum += row[col]
                col_sum[col] += row[col]
            else:
                row.append(0)       #Append 0 from the end of empty cells until maximum colum
        
        row.append(row_sum)         #Append sum column of row
        row.append(row_sum / cols_len)  #Append average column of row
    
    #Calculate average of each column
    for col in range(0, cols_len):
        col_avg.append(col_sum[col] / rows_len)
        
    #Append sum and average for each column
    data.append(col_sum)
    data.append(col_avg)

#Write result to csv file
def output_result(filename, data, rows_len, cols_len):
    try:
        file = open(filename, "w")
        
        #Write header
        file.write("," + ",".join(str(x + 1) for x in range(0, cols_len)) + ",sum,avg\n")
        
        #Write row one by one
        for row in range(0, rows_len):
            file.write(str(row + 1) + "," + ",".join(str(data[row][x]) for x in range(0, cols_len + 2)) + "\n")
            
        #Write sum of each column
        file.write("sum," + ",".join(str(data[rows_len][x]) for x in range(0, cols_len)) + ",,\n")
        
        #Write average of each column
        file.write("avg," + ",".join(str(data[rows_len + 1][x]) for x in range(0, cols_len)) + ",,\n")
        
    except Exception:
        print("Failed to write file!")
    finally:
        file.close()

#Main function - program entrance
def main():
    try:
        cols_len = 0
        data = []
        
        #Read all lines from csv file
        file = open("dataset1.csv", "r")
        line = file.readline()
        while line != "":
            result = parse_line(line)
            if (result):
                data.append(result)
                if cols_len < len(result):
                    cols_len = len(result)
            line = file.readline()
        
        rows_len = len(data)
        print("Original data: ", data)
        
        #Calculate the sum and average of data
        calc_data(data, cols_len)
        print("Result data: ", data)
        
        #Write result to csv file
        output_result("dataset_result.csv", data, rows_len, cols_len)
        
    except Exception:
        print("Failed to read file!")
    finally:
        file.close()

if __name__ == "__main__":
    main()
