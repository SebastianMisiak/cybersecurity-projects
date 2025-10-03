import subprocess

# Open passwords file
with open("passwords.txt", "r") as f:
    for line in f:
        password = line.strip()

        # Run check_password.py with subprocess
        result = subprocess.run(
            ["python3", "check_password.py", password],
            capture_output=True,
            text=True
        )

        # Print what happened
        print(f"Trying: {password} -> {result.stdout.strip()}")

        # If success, break
        if result.returncode == 0:
            print(f"Found password: {password}")
            break