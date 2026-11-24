import sys

print("Total arguments:", len(sys.argv))
print("script name:", sys.argv[0])
print("arguments:", sys.argv[1:])

total = 0
for arg in sys.argv[1:]:
    total += int(arg)

print("sum =:", total)

