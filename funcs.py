from analysis import ok_solution, next_sol


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




# ////////////////////

def peek(path, num):
	print('PEEKING INTO', path)
	count = 0
	for line in open(path):
		count += 1
		print(line.rstrip('\n'))
		if count > num: return


def find(path, sol):
	pos = 0
	a_file = open(path)
	while True:
		a_next = next(a_file)
		if a_next==None:
			return
		if a_next == sol:
			print("YES FOUND IT AT POS", pos)
			break
		pos += 1
		if pos % 1000 == 0 and pos  > 0:
			print('havent found it until', a_next)

def find_similar(path, sol, excepted_id_list):
	print('finding similar to ', sol, 'in', path)
	max_id = max(sol[0], sol[1])
	a_file = open(path)
	a_next = None
	while True:
		a_next = next_sol(a_file, a_next, excepted_id_list)
		if a_next[0] > max_id:
			return
		if a_next==None:
			return
		if (a_next[0] == sol[0] and a_next[1] == sol[1]):
			if a_next == sol:
				print(a_next, "EXACT")
			else:
				print(a_next, "SAME ORIENTATION")
		elif (a_next[0] == sol[1] and a_next[1] == sol[0]):
			print(a_next, "OPPOSITE ORIENTATION")


# print(*counts("./data/viral/aspop.sorted.tsv",
# 			  "./data/viral/truth.tsv"
# 			  ))

# find("./data/viral/truth_really_sorted.tsv", ('100000', '10016', 'N', -121, -121, 130, 130))
# find_similar("./data/viral/truth_really_sorted.tsv", ('100000', '10016', 'N', -121, -121, 130, 130))

# print(*counts("./data/viral/aspop.sorted.tsv",
# 			  "./data/viral/truth_really_sorted.tsv"
# 			  ))
# print(*counts("./data/viral/blast.sorted.tsv",
# 			  "./data/viral/truth_really_sorted.tsv"
# 			  ))
# print(*counts("./data/viral/aspop.sorted.tsv",
# 			  "./data/viral/blast.sorted.tsv"
# 			  ))
#
#
# find_similar("./data/viral/truth_really_sorted.tsv", ('100000', '100282', 'N', -95, -95, 156, 156))
# find_similar("./data/viral/truth_really_sorted.tsv", ('100000', '102201', 'N', -62, -63, 188, 188))
# find_similar("./data/viral/truth_really_sorted.tsv", ('100000', '102333', 'N', -114, -118, 133, 133))
# find_similar("./data/viral/truth_really_sorted.tsv", ('100000', '102587', 'N', -47, -47, 204, 204))
# find_similar("./data/viral/truth_really_sorted.tsv", ('100000', '10316', 'N', -26, -27, 224, 224))
# peek("./data/viral/blast.sorted.tsv", 850)
