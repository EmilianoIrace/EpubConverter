### Convert a epub to markdown
### Usage: epub2md.py <epubfile>
### Output: <epubfile>.md

#write the folloing pandoc command in the terminal changing filename
"""
-i filename -M document-css=false --extract-media .\new\ -o .\new\NewBook.md
"""


import re

def replace_with_whitespace(text):
    # Define the regular expression pattern to match text within curly braces
    pattern = r'\{.*?\}'
    
    # Replace the matched text with a white space
    replaced_text = re.sub(pattern, ' ', text)

    # Define the regular expression pattern to match text inside parentheses () and starting with #
    pattern = r'\(#.*?\)'
    
    # Replace the matched text with a white space
    replaced_text = re.sub(pattern, ' ', text)

    # Define the regular expression pattern to match text inside square brackets []
    pattern = r'\[\s+\]'
    
    # Replace the matched text with a white space
    replaced_text = re.sub(pattern, ' ', text)
    
    return replaced_text

# Read the input text from a .md file with specified encoding
filename = "new\NewBook.md"
with open(filename, 'r', encoding='utf-8') as file:
    input_text = file.read()

# Perform the search and substitution
output_text = replace_with_whitespace(input_text)

# Overwrite the file with the modified text using specified encoding
with open(filename, 'w', encoding='utf-8') as file:
    file.write(output_text)

# Print a success message
print("Modified text has been written back to the file.")
