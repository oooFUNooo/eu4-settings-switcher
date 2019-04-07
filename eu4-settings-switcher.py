import os
import re
import argparse

def main():

	# Parse Command Line Options
	parser = argparse.ArgumentParser()
	parser.add_argument('eu4path', help = 'path for EU4 settings.txt')
	parser.add_argument('--mod'  , help = 'save/load mod set', action = 'store_true')
	parser.add_argument('--dlc'  , help = 'save/load dlc set', action = 'store_true')
	parser.add_argument('--save' , help = 'specify a file to save', type = str)
	parser.add_argument('--load' , help = 'specify a file to load', type = str)
	args = parser.parse_args()

	# Open Files
	old = open(args.eu4path + '/settings.txt', 'r', encoding = 'utf_8_sig')
	new = open(args.eu4path + '/settings.new', 'w', encoding = 'utf_8_sig')
	if args.save:
		mod = open(args.save, 'w', encoding = 'utf_8_sig')
	if args.load:
		mod = open(args.load, 'r', encoding = 'utf_8_sig')

	# Process settings.txt
	foundflag = False
	innerflag = False
	for line in old:
		if not innerflag:
			if (args.mod and re.match(r'^last_mods=\{', line)) or (args.dlc and re.match(r'^last_dlcs=\{', line)):
				foundflag = True
				innerflag = True
				new.write(line)
				if args.load:
					for modline in mod:
						new.write(modline)
				continue
		if innerflag and re.match(r'^\}', line):
			innerflag = False
			new.write(line)
			continue
		if innerflag:
			if args.save:
				mod.write(line)
			continue
		new.write(line)

	# Not Found
	if not foundflag and args.load:
		if args.mod:
			new.write('last_mods={\n')
		if args.dlc:
			new.write('last_dlcs={\n')
		for modline in mod:
			new.write(modline)
		new.write('}\n')

	# Close Files
	mod.close()
	old.close()
	new.close()

	# Swap settings.txt
	if args.load:
		if os.path.isfile(args.eu4path + '/settings.old'):
			os.remove(args.eu4path + '/settings.old')
		os.rename(args.eu4path + '/settings.txt', args.eu4path + '/settings.old')
		os.rename(args.eu4path + '/settings.new', args.eu4path + '/settings.txt')
	if args.save:
		os.remove(args.eu4path + '/settings.new')


if __name__ == "__main__":
	# execute only if run as a script
	main()
