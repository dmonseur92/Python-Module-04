import sys


def read_file() -> None:
    if len(sys.argv) == 2:
        print(f"Accessing file '{sys.argv[1]}'\n")
        try:
            file = sys.argv[1]
            f = open(file)
            print(f.read())
            f.close()
            print(f"File '{sys.argv[1]}' closed.\n")
        except (FileNotFoundError) as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
        except PermissionError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
    else:
        print("Usage: ft_ancient_text.py <file>")

def read_file_improved() -> None:
    if len(sys.argv) == 2:
        print(f"Accessing file '{sys.argv[1]}'\n")
        try:
            file = sys.argv[1]
            f = open(file)
            for line in f:
                print(line[:-1] + "#")
            try:
                saved = input("Enter new file name (or empty): ")
                print(f"Saving data to '{saved}'")
                print(f"Data saved in file '{saved}'")
            except:
            f.close()
            print(f"File '{sys.argv[1]}' closed.\n")
        except (FileNotFoundError) as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
        except PermissionError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
    else:
        print("Usage: ft_ancient_text.py <file>")

if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===")
    read_file()
    read_file_improved()
