
import sys

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    try:
        archivist_id = input("Input Stream active. Enter archivist ID: ")
        report = input("Input Stream active. Enter status report: ")
        sys.stdout.write(f"\n[STANDARD] Archive status from {archivist_id}: "
                         f"{report}\n")
        sys.stderr.write("[ALERT] System diagnostic: Communication channels "
                         "verified\n")
        sys.stdout.write("[STANDARD] Data Transmission complete.\n")
        print("\nThree-channel communication test successfull.")
    except Exception as e:
        sys.stderr.write(f"[ALERT] Error: {e}")
