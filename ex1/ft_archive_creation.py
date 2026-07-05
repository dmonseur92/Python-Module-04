import sys


def read_file_improved() -> None:
    if len(sys.argv) == 2:
        print(f"Accessing file '{sys.argv[1]}'\n")
        try:
            file = sys.argv[1]
            f = open(file)
            content = f.read()
            print(content)
            f.close()
            print(f"File '{sys.argv[1]}' closed.\n")
            print("Transform data: \n")
            new_content = ""
            for line in content.split("\n"):
                if line != "":
                    print(line + "#")
                    new_content += line + "#\n"
            saved = input("\nEnter new file name (or empty): ")
            if saved != "":
                try:
                    s = open(saved, "w")
                    s.write(new_content)
                    print(f"Saving data to '{saved}'")
                    print(f"Data saved in file '{saved}'")
                    s.close()
                    print(f"File '{saved}' closed.\n")
                except (FileNotFoundError, PermissionError) as e:
                    print(f"Error opening file '{sys.argv[1]}': {e}")
            else:
                print("Not saving data.")
        except (FileNotFoundError) as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
        except PermissionError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
    else:
        print("Usage: ft_ancient_text.py <file>")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===")
    read_file_improved()
