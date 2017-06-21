import subprocess
import os.path

from funcs import *






ground_set = read_ground_set()


def run_and_write_counts(t, e, path):
	call_str = ['./rust_overlaps.exe', SRC_PATH, EXACT_PATH, flt_str(e), str(t), '-r', '-t', '-w=6']
	print('CALLING', ' '.join(call_str))
	subprocess.call(call_str)

	real_sols = 0
	fake_sols = 0
	for line in open(EXACT_PATH).readlines()[1:]:
		sol = convert(line)
		case1 = sol in ground_set
		case2 = special_case(sol, ground_set)
		if not case1 and case2:
			print("My solution: ", sol, '\ther solution: ', flip(sol))
		if case1 or case2:
			real_sols += 1
		else:
			fake_sols += 1

	tp = real_sols						#in both sets
	fn = len(ground_set) - real_sols	#in GROUND but not EXACT
	fp = fake_sols						#in EXACT but not GROUND

	print("RECALL IS ", float(tp)/(tp+fn))
	with open(path, "w") as file:
		file.write('{}\n{}\n{}\n'.format(tp, fn, fp))

	return tp, fn, fp


def values(t, e):
	path = counts_path_for(t, e)
	if os.path.isfile(path):
		print(t, flt_str(e), 'found. using existing')
		return read_counts(path)
	else:
		print(t, flt_str(e), 'not found. running and writing')
		return run_and_write_counts(t, e, path)

################################################


e_range = float_range(0.0, 0.072, 0.005)
t_range = range(20, 240, 10)

e_range = [0.01]
t_range = [30]

################################################



results = [
	[
		values(t, e)
	for t in t_range
	]
	for e in e_range
]

# print_2d(results)
# tp, fn, fp
with open(TRUE_POS_PATH, "w") as tp_file,\
		open(FALSE_NEG_PATH, "w") as fn_file,\
		open(FALSE_POS_PATH, "w") as fp_file:
	for row in results:
		for i, val in enumerate(row):
			if i > 0:
				tp_file.write(DELIM)
				fn_file.write(DELIM)
				fp_file.write(DELIM)
			tp_file.write('{}'.format(val[0]))
			fn_file.write('{}'.format(val[1]))
			fp_file.write('{}'.format(val[2]))
		tp_file.write('\n')
		fn_file.write('\n')
		fp_file.write('\n')

print("QUITTING BEFORE I WRITE LEL")
quit()

with open(SETTINGS_PATH, "w") as set_file:
	set_file.write('{}\t{}\n'.format(min(e_range), max(e_range)))
	set_file.write('{}\t{}\n'.format(min(t_range), max(t_range)))

print('e range', min(e_range), '->', max(e_range))
print('t range', min(t_range), '->', max(t_range))