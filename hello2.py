import re
store = []
def main():
  count = 0
  while count < 3:
	  text = input()
	  number = int(text)
	  if count == 0 and number > 0:
		  count = count + 1
		  store.append(number)
	  elif count == 1 and number >= 0:
	  	  count = count + 1
		  store.append(number)
	  elif count == 2 and number > 0:
		  count = count + 1
		  store.append(number)
	  else:
		  print "Invalid Input"

  m1 = (store[0]-store[2])/store[1]
  m2 = store[2]/store[1]
  m3 = (m1*100/(m1+m2))
  if m3 == 0:
	  print "Total Down Time: 0"
	  print "0"
	  print "0"
	  print "100"
	  exit
  print m1
  print m2
  print str(m3)+"%"
if __name__ == '__main__':
    main()