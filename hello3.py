import re
store = [192,273]
solution = []
toggle = 0
def main():
	lower = int(input())
	upper = int(input())
	toggle = 0
	swagger = 0
	while swagger < upper:
		current = store[toggle]
		toggler()
		part1 = cur/10
		part2 = cur%10
		

def reverse(a):
	a = str(a)
	return int(a[::-1])

def toggler():
	if toggle == 0:
		toggle = 1
	else:
		toggle = 0
if __name__ == '__main__':
    main()