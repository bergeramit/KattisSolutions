import sys

# Exceeds time limit when submitting to Kattis

def solve():
	jack_cds_count, jill_cds_count = [int(i) for i in sys.stdin.readline().strip().split(" ")]
	while jack_cds_count != 0 and jill_cds_count != 0:
		similar_counter = 0
		jack_cds, jill_cds = set(), set()
		for i in range(jack_cds_count):
			jack_cds.add(sys.stdin.readline().strip())

		for i in range(jill_cds_count):
			jill_cds.add(sys.stdin.readline().strip())

		similar_counter = len(jack_cds & jill_cds)

		print(similar_counter)
		jack_cds_count, jill_cds_count = [int(i) for i in sys.stdin.readline().strip().split(" ")]

solve()
