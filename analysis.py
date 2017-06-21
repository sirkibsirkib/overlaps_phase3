def convert(line):
	# idA	idB	O	OHA	OHB	OLA	OLB	K
	# 0		1	2	3	4	5	6	7
	# ^		^	^	^	^	^	^	^
	x = tuple(line.split('\t')[:-1])
	return x[0], x[1], x[2], int(x[3]), int(x[4]), int(x[5]), int(x[6])



except_id_list = [int(line.rstrip('\n')) for line in open('./data/viral/removed_IDs.txt')]

def ok_solution(sol):
	return sol[0] not in except_id_list\
		   	and sol[1] not in except_id_list\
			and (sol[5] > 80 or sol[6] > 80)

def next_sol(file, previous_sol):
	while True:
		line = file.readline().rstrip('\n')
		if line.startswith("idA"):
			continue
		if line==None or len(line.strip()) == 0:
			return None
		sol = convert(line)
		if ok_solution(sol) and sol != previous_sol:
			return sol

def smallest_sol(sols):
	x = None
	for s in sols:
		if s != None:
			if x == None or s < x:
				x = s
	return x

def venn_walk(paths):
	files = list(map(open, paths))
	sols = list(map(lambda x : next_sol(x, None), files))
	counts = dict()
	universal_sol_index = 0
	while True:
		if universal_sol_index % 5000==0 and universal_sol_index > 0:
			print('universal_sol_index:', '{:,}'.format(universal_sol_index), '\t')
		universal_sol_index += 1
		min_sol = smallest_sol(sols)
		if min_sol == None:
			break
		key = tuple(map(lambda x : x==min_sol, sols))
		if key not in counts:
			counts[key] = 1
		else:
			counts[key] += 1
		for i in range(len(paths)):
			if key[i]:
				sols[i] = next_sol(files[i], sols[i])
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
	print('----------end----------')



# venn_walk(["./data/testing/a.txt", "./data/testing/b.txt", "./data/testing/c.txt", "./data/testing/d.txt"])

# print('DONE')