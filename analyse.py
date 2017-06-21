from analysis import venn_walk
import sys

if len(sys.argv) < 3:
	print('USAGE: [excluded ID list] [file1path] [file2path]...')
	exit()
excepted_list = [int(line.rstrip('\n')) for line in open('./data/viral/removed_IDs.txt')]
venn_walk(excepted_list,
		  sys.argv[2:])