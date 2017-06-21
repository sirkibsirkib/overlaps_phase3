from analysis import venn_walk


viral = ['./data/viral/aspop.sorted.tsv', './data/viral/blast.sorted.tsv', './data/viral/truth_really_sorted.tsv']
human = ['./data/human/aspop.sorted.tsv', './data/human/blast.sorted.tsv']
venn_walk('./removed_IDs.txt', human)