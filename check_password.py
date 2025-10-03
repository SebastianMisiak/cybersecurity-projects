import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python check_password.py <password>")
        sys.exit(1)

    candidate = sys.argv[1].strip()

    # Load real password
    with open("real_password.txt", "r") as f:
        real_password = f.read().strip()

    if candidate == real_password:
        print("✅ Correct password!")
        sys.exit(0)
    else:
        print("❌ Wrong password.")
        sys.exit(1)

if __name__ == "__main__":
    main()