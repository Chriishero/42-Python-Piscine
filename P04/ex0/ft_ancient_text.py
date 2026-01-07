
if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    filename = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {filename}")
    try:
        f = open(filename, 'r')
        print("Connection established...\n")
        output = f.read()
        f.close()
        print("RECOVERED DATA:")
        print(output, '\n')
        print("Data recovery complete. Storage unit disconnected.")
    except Exception:
        print("ERROR: Storage vault not found.")
