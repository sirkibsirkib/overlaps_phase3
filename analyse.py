from analysis import venn_walk
import sys

if len(sys.argv) < 3:
	print('USAGE: [excluded ID list] [file1path] [file2path]...')
	exit()
excepted_list = [int(line.rstrip('\n')) for line in open(sys.argv[1])]
venn_walk(excepted_list,
		  sys.argv[2:])