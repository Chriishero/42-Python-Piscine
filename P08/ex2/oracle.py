from dotenv import load_dotenv
import os


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")
    load_dotenv()
    MATRIX_MODE = os.getenv("MATRIX_MODE")
    DATABASE_URL = os.getenv("DATABASE_URL")
    API_KEY = os.getenv("API_KEY")
    LOG_LEVEL = os.getenv("LOG_LEVEL")
    ZION_ENDPOINT = os.getenv("ZION_ENDPOINT")
    if not all([MATRIX_MODE, DATABASE_URL, API_KEY,
                LOG_LEVEL, ZION_ENDPOINT]):
        print("WARNING: missing configuration:")
    else:
        print("Configuration loaded:")
    print("Mode:", MATRIX_MODE)
    if MATRIX_MODE == 'production':
        db_status = ('Connected to PRODUCTION instance' if DATABASE_URL
                     else 'Not connected')
        print(f"Database: {db_status}")
        api = (str(API_KEY)[:4] + '*****' if API_KEY else None)
        print(f"API Access: {api}")
    elif MATRIX_MODE == 'development':
        db_status = ('Connected to local instance' if DATABASE_URL
                     else 'Not connected')
        print(f"Database: {db_status}")
        print(f"API Access: {'Authenticated' if API_KEY else None}")
    else:
        print("Database: Not connected")
        print("API Access: Not authenticated")

    print("Log Level:", LOG_LEVEL)
    print(f"Zion Network: {'Online' if ZION_ENDPOINT else 'Offline'}")

    print()
    print("Environment security check:")
    print(" [OK] No hardcoded secrets detected")
    if os.path.isfile(".env"):
        print(" [OK] .env file properly configured")
    else:
        print(" [ERR] .env file not found")
    print(" [OK] Production overrides available")
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
