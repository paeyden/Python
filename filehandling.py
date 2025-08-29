def modify_content(content):
    
    #Simple modification function:
    #Converts all text to uppercase.
    
    return content.upper()

try:
    # 🧪 Ask user for input file
    filename = input("Enter the name of the file to read: ")

    # Open and read file
    with open(filename, "r") as file:
        content = file.read()

    # Modify the content
    modified = modify_content(content)

    # Create a new output file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as file:
        file.write(modified)

    print(f"✅ File successfully modified and saved as '{new_filename}'")

except FileNotFoundError:
    print("❌ Error: File not found. Please check the filename and try again.")
except PermissionError:
    print("❌ Error: You don’t have permission to read this file.")
except Exception as e:
    print(f"⚠️ An unexpected error occurred: {e}")
