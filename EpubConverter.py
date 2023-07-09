### Convert a epub to markdown
### Usage: epub2md.py <epubfile>
### Output: <epubfile>.md

#write the folloing pandoc command in the terminal changing filename
# pandoc -M document-css=false --extract-media .\ -o .\NewBook.md -i 1.epub
# after that
# python modified_EpubConverter.py new\NewBook.md
import sys
import re

def replace_with_whitespace(text):
    # Define the regular expression pattern to match text within curly braces
    pattern = r'\{.*?\}'
    
    # Replace the matched text with a white space
    replaced_text = re.sub(pattern, ' ', text)

    # Define the regular expression pattern to match text inside parentheses () and starting with #
    pattern = r'\(#.*?\)'
    
    # Replace the matched text with a white space
    replaced_text = re.sub(pattern, ' ', replaced_text)

    # Define the regular expression pattern to match text inside square brackets []
    pattern = r'\[\s+\]'
    
    # Replace the matched text with a white space
    replaced_text = re.sub(pattern, ' ', replaced_text)
    
    return replaced_text

# Get the filename from the command line argument
filename ="NewBook.md"

# Perform the search and substitution
with open(filename, 'r', encoding='utf-8') as file:
    input_text = file.read()

output_text = replace_with_whitespace(input_text)

with open(filename, 'w', encoding='utf-8') as file:
    file.write(output_text)

# Print a success message
print("Modified text has been written back to the file.")
