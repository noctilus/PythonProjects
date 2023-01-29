"""
Takes file,reads line by line and exports only unique lines
"""

f = open("emails.txt", "r", encoding="utf8")

readr = f.readlines()
unique_emails = []
n = 0
for line in readr:
    line.strip()
    if line not in unique_emails:
        unique_emails.append(line)

result_file = open('unique_email.txt', 'w', encoding='utf8')

result_file.writelines(unique_emails)
