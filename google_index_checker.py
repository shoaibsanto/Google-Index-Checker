import csv
import time
import requests
import streamlit as st
from io import StringIO

# Streamlit interface
st.title("Google Indexing Checker")

# Upload the file containing URLs
uploaded_file = st.file_uploader("Upload a TXT file with URLs", type="txt")

if uploaded_file is not None:
    # Read the uploaded file
    domains_to_check = [line.strip() for line in uploaded_file.read().decode("utf-8").splitlines()]

    # Prepare CSV file data in memory
    output = StringIO()
    fieldnames = ["urls", "index_status"]
    writer = csv.DictWriter(output, fieldnames=fieldnames)
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
            st.write(f"Error checking {domain}: {e}")
            return False

    # Display a header for indexing results
    st.write("Indexing Results:")

    # Iterate over each domain and check indexing status
    for domain in domains_to_check:
        is_indexed = check_index_status(domain)
        index_status = "Indexed" if is_indexed else "Not Indexed"
        
        # Display each result on a new line without JSON format
        st.write(f"{domain} - {index_status}")

        # Write the result to in-memory CSV
        writer.writerow({"urls": domain, "index_status": index_status})

        # Add a delay to avoid rate-limiting by Google
        time.sleep(5)

    # Convert in-memory CSV to downloadable file
    st.download_button(
        label="Download results as CSV",
        data=output.getvalue(),
        file_name="index_status.csv",
        mime="text/csv"
    )
