import subprocess

result = subprocess.run(["echo", "hello world"],
                        capture_output=True,
                        text=True,
)

print("Return code:", result.returncode)
print("Stdout", result.stdout.strip())
print("Stderr", result.stderr)