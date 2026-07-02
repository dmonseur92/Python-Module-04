def secure_archive(
    file: str,
    action: str,
    content: str = ""
) -> tuple[bool, str]:
    if (action == "read"):
        try:
            with open(file) as f:
                content = f.read()
                return (True, content)
        except (FileNotFoundError, PermissionError) as e:
            return (False, str(e))
    elif (action == "write"):
        try:
            with open("new_file.txt", "w") as n:
                n.write(content)
                return (True, "Content successfully written to file")
        except (FileNotFoundError, PermissionError) as e:
            return (False, str(e))
    else:
        return (False, "Invalid action")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a  nonexistent file:")
    print(secure_archive("non.txt", "read"))
    print()
    print("Using 'secure_archive' to read from an  inaccessible file:")
    print(secure_archive("denied.txt", "read"))
    print()
    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("test.txt", "read"))
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("test.txt", "write", "blablabla"))
