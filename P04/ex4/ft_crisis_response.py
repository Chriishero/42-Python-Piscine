
if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    print("CRISIS ALERT: Attempting access to 'lost_archives.txt'...")
    try:
        with open("lost_archives.txt", 'r') as f:
            print(f"SUCCESS: Archive recovered - '{f.read()}'")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    print("STATUS: Crisis handled, system stable\n")

    print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    try:
        with open("classified_vault.txt", 'r') as f:
            print(f"SUCCESS: Archive recovered - '{f.read()}'")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    print("STATUS: Crisis handled, system maintained\n")

    print("ROUTINE ACCESS: Attempting access to 'standard_archives.txt'...")
    try:
        with open("standard_archive.txt", 'r') as f:
            print(f"SUCCESS: Archive recovered - '{f.read()}'")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    print("STATUS: Normal operations resumed\n")

    print("All crisis scenarios handled successfully. Archives secure.")