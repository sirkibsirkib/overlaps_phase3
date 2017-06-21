
SRC_PATH = "./mut0.01.fasta"
GROUND_PATH_1 = "./strain1.sfo_fixed.tsv"
GROUND_PATH_2 = "./strain2.sfo_fixed.tsv"
EXACT_PATH = "./exact.csv"

QUALITY_PATH = "./quality.csv"
TRUE_POS_PATH = "./real_sols.csv"
FALSE_POS_PATH = "./false_pos_count.csv"
FALSE_NEG_PATH = "./false_neg_count.csv"
SETTINGS_PATH = "./settings.txt"


DELIM = '\t'

def convert(line):
	# idA	idB	O	OHA	OHB	OLA	OLB	K
	# 0		1	2	3	4	5	6	7
	# ^		^	^	^	^	^	^	^
	x = tuple(line.split('\t')[:-1])
	return int(x[0]), int(x[1]), x[2], int(x[3]), int(x[4]), int(x[5]), int(x[6])

def read_ground_set():
	lines1 = [line.rstrip('\n') for line in open(GROUND_PATH_1)]
	s = {convert(line) for line in lines1}
	del lines1
	lines2 = [line.rstrip('\n') for line in open(GROUND_PATH_2)]
	s = s.union({convert(line) for line in lines2})
	return s


def float_range(frm, to, step):
	ls = []
	last = frm
	while last < to:
		ls.append(last)
		last += step
	return ls

def flt_str(f):
	if len(str(f)) > 6:
		return '{:.3f}'.format(f)
	return str(f)

def counts_path_for(t, e):
	return "./counts/" + str(t) + "_" + flt_str(e) + ".txt"

def read_counts(path):
	lines = [line.rstrip('\n') for line in open(path)]
	return int(lines[0]), int(lines[1]), int(lines[2])

def flip(x):
	# ida	idb	O	OHA	OHB	OLA	OLB
	return x[0], x[1], x[2], -x[3], -x[4], x[5], x[6]


def special_case(sol, ground_set):
	if sol[2] == 'I':
		flipped = flip(sol)
		return flipped in ground_set
	return False