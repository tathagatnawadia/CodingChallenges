import re
store = []
def main():
  text = raw_input()
  text = text.lower()
  text = re.sub(r'[^\w]', ' ', text)
  words = text.split(" ")
  for x in words:
	  for y in words:
		  if match(x,y) == 1:
			  print x+" "+y

def match(str1,str2):
	if len(str1)>=3 and len(str2)>=3 and str1 != str2 and not any(str1 in s for s in store) and not any(str2 in p for p in store):
		if str1[0] == str2[0] and str1[1] == str2[1] and str1[2] == str2[2]:
			store.append(str1)
			store.append(str2)
		        return 1
	else:
		return 0
if __name__ == '__main__':
    main()