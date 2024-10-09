import csv
from googlesearch import search

# Read domains from the uploaded "domains.txt" file
domains_to_check = []
with open("urls.txt", "r") as file:
    domains_to_check = [line.strip() for line in file.readlines()]

# Prepare CSV file to save results
output_file = "index_status.csv"

with open(output_file, mode="w", newline="") as csvfile:
    fieldnames = ["urls", "index_status"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Write the headers
    writer.writeheader()
    
    # Iterate over the domains and check their indexing status
    for domain in domains_to_check:
        query = f"site:{domain}"  # Create a query using the "site:" operator
        found = False  # Initialize a flag to check if the domain is indexed

        # Perform the Google search with num=1
        try:
            for _ in search(query, tld="co.in", num=1, stop=1, pause=2):
                found = True
                break  # If a result is found, set found=True and exit the loop
        except Exception as e:
            print(f"An error occurred: {e}")

        # Prepare result row
        index_status = "Indexed" if found else "Not Indexed"
        
        # Write the result to the CSV file
        writer.writerow({"urls": domain, "index_status": index_status})

print(f"Results saved to {output_file}")