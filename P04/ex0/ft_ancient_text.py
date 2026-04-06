
if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    filename = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {filename}")
    try:
        with open(filename, 'r') as f:
            print("Connection established...")
            lines = f.readlines()
            print("RECOVERED DATA:")
            for i, line in enumerate(lines, start=1):
                print(f"[FRAGMENT {i:03d}] {line.strip()}")
            print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
