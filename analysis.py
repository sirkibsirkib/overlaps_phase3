def convert(line):
	# idA	idB	O	OHA	OHB	OLA	OLB	K
	# 0		1	2	3	4	5	6	7
	# ^		^	^	^	^	^	^	^
	x = tuple(line.split('\t')[:-1])
	return x[0], x[1], x[2], int(x[3]), int(x[4])#, int(x[5]), int(x[6])



# except_id_list = [int(line.rstrip('\n')) for line in open('./data/viral/removed_IDs.txt')]

def ok_solution(sol, excepted_id_list):
	return sol[0] not in excepted_id_list\
		   	and sol[1] not in excepted_id_list\
		# \
		# 	and (sol[5] > 80 or sol[6] > 80)



def next_sol(file, previous_sol, excepted_id_list):
	while True:
		line = file.readline().rstrip('\n')
		if line.startswith("idA"):
			continue
		if line==None or len(line.strip()) == 0:
			return None
		sol = convert(line)
		if ok_solution(sol, excepted_id_list) and sol != previous_sol:
			return sol

def smallest_sol(sols):
	x = None
	for s in sols:
		if s != None:
			if x == None or s < x:
				x = s
	return x


# def almost(x, y):
# 	return True
# 	# return x*0.9 < y or y*0.9 < x
#
# def equivalent_sols(a, b):
# 	if a == None:
# 		return b == None
# 	if b == None:
# 		return a == None
# 	return a[0]==b[0] and a[1]==b[1]\
# 		   and a[2]==b[2]\
# 		   and a[3]==b[3] and a[4]==b[4]\
# 		   and almost(a[5], b[5]) and almost(a[6], b[6])


impossible_solution = ('???eefef','***23r34r','???',-1,-1,-1,-1)

def venn_walk(paths, excepted_id_list=()):
	print(len(excepted_id_list), 'inds in EXCEPT list')
	files = list(map(open, paths))
	sols = list(map(lambda x : next_sol(x, impossible_solution, excepted_id_list), files))
	counts = dict()
	universal_sol_index = 0
	samples = []
	while True:
		if universal_sol_index % 100000==0 and universal_sol_index > 0:
			print('universal_sol_index:', '{:,}'.format(universal_sol_index), '\t')
		universal_sol_index += 1
		min_sol = smallest_sol(sols)
		if min_sol == None:
			break
		key = tuple(map(lambda x : x == min_sol, sols))
		if len(samples) < 200 and key == (False, False, True):
			samples.append(min_sol)
		if key not in counts:
			counts[key] = 1
		else:
			counts[key] += 1
		for i in range(len(paths)):
			if key[i]:
				sols[i] = next_sol(files[i], sols[i], excepted_id_list)
	print('---------DONE---------')
	print('counts:')
	out_lines = [(''.join(map(lambda x : '#' if x else '-', k)) + '\t' + str(v))
			 for k, v in counts.items()]
	for l in sorted(out_lines):
		print(l)
	for i in range(len(files)):
		tot = sum(v for k, v in counts.items() if k[i])
		print(tot, 'total for file', paths[i])

	print('universe:', sum(counts.values()))

	print('samples!')
	for x in samples:
		print(x)
	print('----------end----------')



# venn_walk(["./data/testing/a.txt", "./data/testing/b.txt", "./data/testing/c.txt", "./data/testing/d.txt"])

# print('DONE')