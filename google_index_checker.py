import csv
import time
import requests

# Load the domains to check from a text file
with open("mybabynamemeaning.txt", "r") as file:
    domains_to_check = [line.strip() for line in file.readlines()]

# Prepare CSV file to save results
output_file = "index_status.csv"
with open(output_file, mode="w", newline="") as csvfile:
    fieldnames = ["urls", "index_status"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Function to check if a domain is indexed on Google
    def check_index_status(domain):
        query = f"site:{domain}"
        url = f"https://www.google.com/search?q={query}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            # Check if "did not match any documents" is in the response, indicating not indexed
            if "did not match any documents" in response.text:
                return False
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error checking {domain}: {e}")
            return False

    # Iterate over each domain and check indexing status
    for domain in domains_to_check:
        is_indexed = check_index_status(domain)
        index_status = "Indexed" if is_indexed else "Not Indexed"
        print(f"{domain} - {index_status}")

        # Write the result to CSV
        writer.writerow({"urls": domain, "index_status": index_status})

        # Add a delay to avoid rate-limiting by Google
        time.sleep(5)

print(f"Indexing results saved to {output_file}")
