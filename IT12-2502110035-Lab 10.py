
import os
import sys

def main():
    try:
        # 1. Use a relative path
        file_path = os.path.join("data", "input.txt")

        # Create the folder and sample file if missing
        os.makedirs("data", exist_ok=True)

        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("Hello World!\nThis is the input file.")

        # Read the file
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        print("File read successfully!")
        print(content)

    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: Permission denied.")

    except OSError as error:
        print("File operation error:", error)

    except Exception as error:
        print("Unexpected error:", error)


if __name__ == "__main__":
    main()
