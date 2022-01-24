
i = 0
num_lines = 0
with open("c.txt", 'r') as f:
    for line in f:
        num_lines += 1
    
for x in range(num_lines):
    keys_file = open("c.txt")
    lines = keys_file.readlines()
    a = lines[x].rstrip()
    if a[0] == "-":
      
      k = 0
      while (k==0):
          a = lines[x+1].rstrip()
          if a[0] == " ":
             i = i+1
          if a[0] == "-":
             k = 1
      print(i)

    else:
      print("S")


