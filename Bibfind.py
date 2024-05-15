import subprocess

def write_requirements_to_file(output_file):
    result = subprocess.run(['pip', 'freeze'], capture_output=True, text=True)
    with open(output_file, 'w') as file:
        file.write(result.stdout)

if __name__ == "__main__":
    requirements_file = "requirements.txt"
    write_requirements_to_file(requirements_file)