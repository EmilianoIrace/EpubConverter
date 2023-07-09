# Get the input filename from the command line argument
$input_filename = $args[0]

# Define the output filename
$output_filename = "NewBook.md"

# Define the input and output paths
$input_path = ".\$input_filename"
$output_path = ".\$output_filename"

# Run the ebook-convert command to extract the contents of the EPUB file
pandoc -M document-css=false --extract-media .\ -o .\NewBook.md -i $input_path

# Run the modified_EpubConverter.py script to replace the text in the output file
python EpubConverter.py $output_path