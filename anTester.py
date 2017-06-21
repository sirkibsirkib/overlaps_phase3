from analysis import venn_walk
from funcs import find_similar, peek


viral = ['./data/viral/aspop.sorted.tsv', './data/viral/blast.sorted.tsv', './data/viral/viral_minimap.tsv', './data/viral/truth_really_sorted.tsv']
human = ['./data/human/aspop.sorted.tsv', './data/human/blast.sorted.tsv', './data/human/human_minimap.tsv']
viral_expected = [int(line.rstrip('\n')) for line in open('./removed_IDs.txt')]
#
#
# venn_walk(human)
# venn_walk(viral, excepted_id_list=viral_expected)

# find_similar('./data/viral/aspop.sorted.tsv', ('10007','59746','N',-13,-13,124,124), viral_expected)


peek('./data/viral/truth_really_sorted.tsv', 50)