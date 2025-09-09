filename = input("Enter the filename to read: ")

try:
    # Try to open the input file
    with open(filename, "r") as infile:
        content = infile.read()
        print("📖 Original file content:\n", content)

    # Modify the content (example: uppercase)
    modified_content = content.upper()

    # Write modified content to a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as outfile:
        outfile.write(modified_content)

    print(f"✅ Modified content written to {new_filename}")

except FileNotFoundError:
    print("❌ Error: The file was not found.")
except PermissionError:
    print("❌ Error: You don’t have permission to read this file.")
except Exception as e:
    print("⚠️ An unexpected error occurred:", e)