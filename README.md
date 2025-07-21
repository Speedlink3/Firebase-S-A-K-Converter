# Firebase-S-A-K-Converter – ChatGPT গুরু, Speedlink3 AI #
<h1>🔑 Universal Google Firebase Service Account Key Converter</h1>
<h3>A simple Python tool to convert your Google Firebase Service Account Key between the standard .json format and a safe .env.local format (for use with Next.js, Vercel, and cloud deployment).
Supports both JSON → .env.local and .env.local → JSON directions!</h3>

<h2>✨ Features</h2>
Convert Firebase JSON key to .env string for secure local development or serverless deployment.

Restore from .env line to JSON for Firebase Admin SDK, Google Cloud, or easy migration.

Interactive CLI: No parameters needed; just follow the prompt.

Compatible with Google Firebase Admin SDK, Next.js, Vercel, and any project needing secret management.

<h2>📦 Script</h2>

<details> <summary><b>Show Python Script</b></summary>
import json
import re
import os

print("Firebase Service Account Key Converter")
print("1. JSON file ➡️ .env.local line")
print("2. .env.local line ➡️ JSON file")
choice = input("Choose direction (1 or 2): ").strip()

if choice == "1":
    input_file = input("Enter input JSON filename (e.g., GetServiceAccountKey.json): ").strip()
    if not os.path.isfile(input_file):
        print(f"File not found: {input_file}")
        exit(1)
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    env_value = json.dumps(data, separators=(',', ':'))
    print("\nPaste this line into your .env.local file:\n")
    print(f'FIREBASE_SERVICE_ACCOUNT_KEY={env_value}')
    print("\nDone!")
elif choice == "2":
    input_file = input("Enter input .env file or env line filename (e.g., env_line.txt): ").strip()
    if not os.path.isfile(input_file):
        print(f"File not found: {input_file}")
        exit(1)
    with open(input_file, "r", encoding="utf-8") as f:
        line = f.read().strip()
    match = re.search(r'FIREBASE_SERVICE_ACCOUNT_KEY=(\{.*\})', line)
    if match:
        json_str = match.group(1)
    else:
        json_str = line  # If only the JSON was pasted
    data = json.loads(json_str)
    out_file = input("Enter output filename (e.g., serviceAccountKey.json): ").strip()
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"\nExported to {out_file}\nDone!")
else:
    print("Invalid selection. Run again and choose 1 or 2.")
</details>


<h2>🚀 How to Use</h2>
1. Save the Script
Save the above code as firebase_key_converter.py in your project folder.

2. Run the Script
python firebase_key_converter.py

3. Choose Mode
  1 to convert a Firebase JSON key → .env.local line
  2 to convert a .env.local line → JSON key file

Just follow the on-screen prompts for filenames and output location.

<h2>📚 References</h2>
Firebase Admin SDK: Add credentials
Firebase Service Account Keys
How to store secrets with .env files
Next.js Environment Variables
Official Python Documentation

<h2>⚠️ Security Reminder</h2>
Never commit your actual serviceAccountKey.json or secret .env.local to public repositories!
Always use .gitignore to protect your secrets.

<h2>❤️ Contributing</h2>
Feel free to fork and improve this tool!
Open an issue or PR if you want new features or a web-based version.

<h2>🛡️ License</h2>
MIT License.
Free to use and share with attribution!
