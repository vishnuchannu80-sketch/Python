# file handling
from pathlib import Path

file_path = Path(__file__).resolve().parent / 'example.txt'

with file_path.open('w', encoding='utf-8') as file:
    file.write('Hello, World!\n')
    file.write('This is a test file.\n')
    file.write('Jai Vysh.\n')

with file_path.open('r', encoding='utf-8') as file:
    content = file.read()

updated_content = content.replace('Jai Vysh', 'torcher Vyshu')

with file_path.open('w', encoding='utf-8') as file:
    file.write(updated_content)

print(updated_content)
