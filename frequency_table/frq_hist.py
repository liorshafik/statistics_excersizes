
f = open('Lotto.csv','r')

print ('the file Lotto read - ')
my_string = f.read()

# clean: 
str_spl = my_string.split(",")
b = list(filter(lambda x: x.isnumeric(),str_spl))

hist = []
for i in range(60):
    hist.append(0)

#count and add to histogram:
for x in b:
    hist[int(x)] += 1
 
      

print(hist)
print('the end')

