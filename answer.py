def file_read_write_with_filenames():
    # Predefined file names
    input_filename = "example.txt"      # File to read
    output_filename = "modified_example.txt"  # File to write
    
    try:
        # Open the input file for reading
        with open(input_filename, "r") as input_file:
            # Read the content of the file
            content = input_file.read()
        
        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()
        
        # Open the output file for writing
        with open(output_filename, "w") as output_file:
            # Write the modified content to the file
            output_file.write(modified_content)
        
        print(f"Modified content has been written to '{output_filename}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist. Please check the filename.")
    
    except PermissionError:
        print(f"Error: You do not have permission to access '{input_filename}' or '{output_filename}'.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
file_read_write_with_filenames()
