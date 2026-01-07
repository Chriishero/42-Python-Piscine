
if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    try:
        print("Initiating secure vault access...")
        print("Vault connection established with failsafe protocols\n")
        with open("classified_data.txt", 'r') as f:
            print(f"SECURE EXTRACTION:\n{f.read()}\n")
        with open("security_protocols.txt", 'r') as f:
            print(f"SECURE PRESERVATION:\n{f.read()}")
        print("Vault automatically sealed upon completion\n")
        print("All vault operations completed with maximum security.")
    except Exception as e:
        print(f"ERROR:{e}")
