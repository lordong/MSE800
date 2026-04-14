import pandas as pd

def main():
    ds = pd.read_csv("dataset1.csv", header=None)
    print(ds)
    
    #Calculate sum and average for each row
    row_sum = ds.sum(axis=1)
    row_avg = ds.mean(axis=1)
    
    #Calculate sum and average for each column
    col_sum = ds.sum()
    col_avg = ds.mean()
    
    #Bind new columns and rows to the dataset
    ds["sum"] = row_sum
    ds["avg"] = row_avg
    ds.loc["sum"] = list(col_sum) + ["", ""]
    ds.loc["avg"] = list(col_avg) + ["", ""]
    print(ds)
    
    #Export dataset to csv file
    ds.to_csv("dataset_output.csv")

if __name__ == "__main__":
    main()
