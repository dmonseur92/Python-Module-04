import sys


def read_file_improved() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    file = sys.argv[1]
    print(f"Accessing file '{file}'\n")
    content = ""
    try:
        f = open(file)
        for line in f:
            line_mod = line.rstrip("\n") + "#"
            print(line_mod)
            content += line_mod + "\n"
        f.close()
        print(f"File '{file}' closed.\n")
    except (FileNotFoundError, PermissionError) as e:
        sys.stderr.write(f"[STDERR] Error opening file '{file}': {e}\n")
    print("Enter new file name (or empty): ", end="", flush=True)
    saved = sys.stdin.readline().strip()
    if saved != "":
        try:
            s = open(saved, "w")
            s.write(content)
            s.close()
            print(f"Saving data to '{saved}'")
            print(f"Data saved in file '{saved}'")
            print(f"File '{saved}' closed.\n")
        except (FileNotFoundError, PermissionError) as e:
            sys.stderr.write(f"[STDERR] Error opening file '{saved}': {e}\n")
    else:
        print("Not saving data.")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===")
    read_file_improved()
