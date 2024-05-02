import csv
import os

# List of input CSV files
input_files = ["Lyna.csv", "Sarah.csv", "aya2.csv", "csv1.csv", "csv2.csv", "rania2.csv"]

# Output CSV file
output_file = "final.csv"

# Function to merge CSV files
def merge_csv(input_files, output_file):
    # Check if output file already exists, if yes, delete it
    if os.path.exists(output_file):
        os.remove(output_file)
    
    # Open output CSV file in write mode
    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        
        # Loop through input files
        for file_name in input_files:
            # Open each input CSV file
            with open(file_name, mode='r', newline='', encoding='utf-8') as infile:
                reader = csv.reader(infile)
                # Write contents to output CSV file
                for row in reader:
                    writer.writerow(row)

# Call the function to merge CSV files
merge_csv(input_files, output_file)

print("CSV files merged successfully!")
