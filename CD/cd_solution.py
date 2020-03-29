import sys

# Exceeds time limit when submitting to Kattis

def count_similar(jack_cds, jill_cds):
	jill_counter, jack_counter = 0, 0
	similar_counter = 0

	while jack_counter < len(jack_cds) and jill_counter < len(jill_cds):
		jack_current = jack_cds[jack_counter]
		jill_current = jill_cds[jill_counter]
		if jack_current == jill_current:
			similar_counter += 1
			jill_counter += 1
			jack_counter += 1

		elif jack_current > jill_current:
			jill_counter += 1

		elif jack_current < jill_current:
			jack_counter += 1

	return similar_counter


def solve():
	jack_cds_count, jill_cds_count = [int(i) for i in sys.stdin.readline().strip().split(" ")]
	while jack_cds_count != 0 and jill_cds_count != 0:
		jack_cds, jill_cds = [], []
		for i in range(jack_cds_count):
			jack_cds.append(int(sys.stdin.readline().strip()))

		for i in range(jill_cds_count):
			jill_cds.append(int(sys.stdin.readline().strip()))

		# print(jack_cds)
		# print(jill_cds)

		print(count_similar(jack_cds, jill_cds))
		jack_cds_count, jill_cds_count = [int(i) for i in sys.stdin.readline().strip().split(" ")]

solve()
