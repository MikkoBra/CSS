import os
import csv

"""
Helper function to write rows to a CSV file.

Parameters:
    file_name: Name of the CSV file.
    fields: List of field names.
    rows: List of rows to write.
    write_header: Boolean indicating whether to write the header.
"""
def write_to_csv(file_name, fields, rows, write_header):
    # Create the Data directory if it does not exist
    data_dir = os.path.join(os.path.dirname(__file__), '../../data')
    os.makedirs(data_dir, exist_ok=True)
    
    # Write to CSV file in the Data directory
    file_path = os.path.join(data_dir, file_name)
    with open(file_path, mode='a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        if write_header:
            csvwriter.writerow(fields)  # Write header only once
        csvwriter.writerows(rows)