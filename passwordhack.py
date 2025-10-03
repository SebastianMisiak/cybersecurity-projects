import subprocess

with open("passwords.txt", "r") as f:
    for line in f:
        password = line.strip()

        result = subprocess.run(["python3", 'check_password.py', password], capture_output= True, text = True)

        print(f"Tring {password} --> {result.stdout.strip()}")

        if result.returncode == 0:
            print(f"Password Cracked: {password}")
            break