def main():
	lines = read_file('[LINE]品希.txt')
	lines = convert(lines)
	#write_file('output.csv',lines)

def read_file(filename):
	with open(filename,'r',encoding='utf-8') as f:
		lines = []
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	line = []
	preson = None

	px_word = 0
	px_image = 0
	px_sticker = 0
	yu_word = 0
	yu_image = 0
	yu_sticker = 0

	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]

		if name == 'PX':
			if s[2] == '圖片':
				px_image += 1
			elif s[2] == '貼圖':
				px_sticker += 1
			else:
				for m in s[2:]:
					px_word += len(m)
		elif name == 'Yu':
			if s[2] == '圖片':
				yu_image += 1
			elif s[2] == '貼圖':
				yu_sticker += 1
			else:
				for m in s[2:]:
					yu_word += len(m)

	print('Yu說了', yu_word, '個字')
	print('Yu傳了', yu_image, '張圖片')
	print('Yu傳了', yu_sticker, '個貼圖')
	print('PX說了',px_word, '個字')
	print('PX傳了', px_image, '張圖片')
	print('PX傳了', px_sticker, '個貼圖')


def write_file(filename, lines):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in lines:
			f.write(line + '\n')
			
main()
