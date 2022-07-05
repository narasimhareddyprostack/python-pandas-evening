#read text file and print no of lines, words and char
f = open('data.txt','r')
data = f.readlines()
lc=wc=cc=0
for line in data:
    lc = lc+1
    cc = cc + len(line)
    word = line.split()
    wc = wc+len(word)
    
print(lc)
print(wc)
print(cc)
