# SQLi-Data-Extractor-Tool
I developed a Python-based tool to detect and exploit SQL Injection (SQLi) vulnerabilities, showcasing my expertise in web application security and ethical hacking. The tool demonstrates proficiency in automating data extraction techniques, particularly through time-efficient binary search methods.
1. SQL Injection Detection:
• The tool tests the given URL for SQLi vulnerabilities by attempting a simple injection (' or 1=1 -- -) and
analyzing the response to determine its existence.
• A secure, programmatic approach is employed using Python's requests library.
2. Binary Search for Data Extraction:
• Once a vulnerability is detected, the tool leverages a binary search algorithm to extract data from the
database, focusing on efficiency and minimizing requests.
• It queries the information_schema.tables to extract table names from the specified database schema
(bWAPP).
3. Row Count Detection:
• Uses SQLi to determine the number of rows (tables) in the database schema by iteratively checking
possible row counts.
4. String Length Detection:
• Identifies the length of each table name using SQLi to determine how many characters to extract for each
entry.
5. Character-by-Character Extraction:
• Retrieves each character of the table name by iteratively comparing ASCII values using the binary search
approach.
• Constructs the table name dynamically, character by character, and displays the results.
6. User Input and Robustness:
• Includes robust error handling for scenarios like unexpected responses or user interruptions (e.g.,
KeyboardInterrupt).
Key Technologies and Skills Demonstrated:
• Web Application Security: Understanding and exploiting SQLi vulnerabilities.
• Binary Search Algorithm: Implemented to optimize data extraction processes, reducing the number of
requests.
• Python Programming: Utilized libraries like requests for HTTP communication and applied structured
programming principles.
• Database Schema Exploration: Extracting metadata from information_schema to identify database structure
and contents.
• Automation: Automating the SQLi exploitation process for faster and consistent results.This project highlights my ability to analyze, exploit, and automate the discovery of vulnerabilities in web applications,
an essential skill for penetration testing and red teaming.
