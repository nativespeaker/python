#-*- coding: utf-8 -*-
'''
反编译目录下所有pyc文件的脚本
'''
import os
import sys

total_pyc_count = 0
total_compiled_count = 0

def uncompile_path(path):
	global total_compiled_count, total_pyc_count
	files = os.listdir(path)
	for file in files:
		if os.path.isdir(os.path.join(path, file)):
			print file
			uncompile_path(os.path.join(path, file))
		elif file.endswith('pyc'):
			total_pyc_count += 1
			dest_file = file[:len(file)-1]
			print os.path.join(path, file) + ' -> ' + os.path.join(path, dest_file)
			if dest_file in files:
				choice = raw_input('Py file already exists. Do you want to overwrite it? Y/N')
				if not choice or choice not in 'Yy':
					continue
			total_compiled_count += 1
			os.system('uncompyle2 -o %s %s'%(os.path.join(path, dest_file), os.path.join(path, file)))

def main(argv):
	if len(argv) == 1:
		path = os.getcwd()
	else:
		if os.path.isabs(argv[1]):
			path = argv[1]
		else:
			path = os.path.abspath(argv[1])

	uncompile_path(path)
	print '***************************'
	print 'summary:'
	print 'total pyc count: ' + str(total_pyc_count)
	print 'compiled py file count: ' + str(total_compiled_count)

if __name__ == '__main__':
	main(sys.argv)