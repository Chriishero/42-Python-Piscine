
if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    try:
        with open("lost_archive.txt", 'r') as f:
            content = f.read().strip()
            print(f"SUCCESS: Archive recovered - '{content}'")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
    print("STATUS: Crisis handled, system stable")
    print()

    print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    try:
        with open("classified_vault.txt", 'r') as f:
            content = f.read().strip()
            print(f"SUCCESS: Archive recovered - '{content}'")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
    print("STATUS: Crisis handled, security maintained")
    print()

    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    try:
        with open("standard_archive.txt", 'r') as f:
            content = f.read().strip()
            print(f"SUCCESS: Archive recovered - '{content}'")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
    print("STATUS: Normal operations resumed")
    print()

    print("All crisis scenarios handled successfully. Archives secure.")
