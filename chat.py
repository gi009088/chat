def read_file(filename):
	with open(filename,'r',encoding='utf-8') as f:
		lines = []
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new_lines = []
	preson = None
	for line in lines:
		if line == '陳亭君' or line == 'Yu':
			preson = line
			continue
		elif '2021年' in line:
			new_lines.append(line)
		else :
			new_lines.append(preson + ':' + line)
	return(new_lines)

def write_file(filename, lines):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in lines:
			f.write(line + '\n')
			
def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.csv',lines)

main()