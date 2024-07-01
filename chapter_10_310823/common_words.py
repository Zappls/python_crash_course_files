file1 = 'alice.txt'
file2 = 'divine_comedy.txt'
file3 = 'little_women.txt'
file4 = 'moby_dick.txt'
file5 = 'siddhartha.txt'


files = [file1, file2, file3, file4, file5]
every_text = ''
for file in files:
	with open(file, encoding='utf-8') as f:
		every_text += f.read()

print(every_text.lower().count('the'))
print(every_text.lower().count('then'))
print(every_text.lower().count('there'))
print(every_text.lower().count('the '))

