#
# Sample Python program for reading inventory.txt file
#
#



#
#
#
def main():
  f = open('inventory.txt')
  lines = f.readlines()
  items = {}
  for line in lines:
    line = line.strip('\n')
    line = line.split('\t')
    items[line[0]] = int(line[1])

  print items
#
# end of def main():
#



if __name__ == "__main__":
  main()
