def read_and_modify_file():
    try:
        # Ask user for input file name
        input_file = input("Enter the filename to read: ")
        
        # Open the file for reading
        with open(input_file, 'r') as file:
            content = file.read()
        
        # Modify content (Example: Convert to uppercase)
        modified_content = content.upper()
        
        # Define output file name
        output_file = "modified_" + input_file
        
        # Write the modified content to a new file
        with open(output_file, 'w') as file:
            file.write(modified_content)
        
        print(f"Modified content saved in '{output_file}'")
    
    except FileNotFoundError:
        print("Error: The file does not exist.")
    
    except IOError:
        print("Error: Unable to read/write the file.")

# Run the function
read_and_modify_file()


