import run

run.Run.unit = "mile"

f = open('runs.txt')
runs = []
for line in f: 
    distance, start, end = [p.strip() for p in line.split(',')]
    runs.append(run.Run(distance, start, end))
f.close()

# Obnoxious short-cut for lines above:
# runs = [run.Run(*[p.strip() for p in line.split(',')]) for line in open('runs.txt')]

print("Runs in file order: ")
for r in runs:
    print(r)


def get_distance(run):
    return run.distance

print("\nRuns sorted by distance (using external method)")
for r in sorted(runs, key=get_distance):
    print(r)


print("\nRuns sorted by pace (using a lambda)")
for r in sorted(runs, key=lambda r : r.raw_pace()):
    print(r)

# Other sorting techniques:
from operator import attrgetter 

print("\nRuns sorted by distance (using attrgetter)")
for r in sorted(runs, key=attrgetter('distance')):
    print(r)

print("\nRuns sorted by distance (using lambda)")
for r in sorted(runs, key=lambda r: r.distance):
    print(r)

print("\nRuns sorted by pace (by instance method) ")
for r in sorted(runs, key=run.Run.raw_pace):
    print(r)