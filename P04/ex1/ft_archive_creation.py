
if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    filename = "new_discovery.txt"
    print(f"Initializing new storage unit: {filename}")
    try:
        f = open(filename, 'x')
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        content = ("[ENTRY 001] New quantum algorithm discovered\n"
                   "[ENTRY 002] Efficiency increased by 347%\n"
                   "[ENTRY 003] Archived by Data Archivist trainee")
        f.write(content)
        f.close()
        print(content, '\n')
        print("Data inscription complete. Storage unit sealed.")
        print(f"Archive '{filename}' ready for long-term preservation.")
    except Exception:
        print("ERROR: Storage unit already exist.")
