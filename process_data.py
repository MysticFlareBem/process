import subprocess

def read_file(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
    return data

def process_data(data):
    processed_data = [line.strip().upper() for line in data]
    return processed_data

def write_file(filename, data):
    with open(filename, 'w') as file:
        file.write('\n'.join(data))

def call_other_script():
    subprocess.run(['python', 'other_script.py'])

def main():
    data = read_file('input.txt')
    processed_data = process_data(data)
    write_file('output.txt', processed_data)
    call_other_script()

if __name__ == "__main__":
    main()
