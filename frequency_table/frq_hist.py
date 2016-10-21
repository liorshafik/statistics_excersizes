
f = open('Lotto.csv','r')

print ('the file Lotto read - ')
my_string = f.read()


str_spl = my_string.split(",")
b = list(filter(lambda x: x.isnumeric(),str_spl))

# init histogram  - create empty list for histogram
hist = []
for i in range(60):
    hist.append(0)


for x in b:
    hist[int(x)] += 1
 
      

print(hist)
print('the end')

