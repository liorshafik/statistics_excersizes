import matplotlib.pyplot as plt


#init
fig = plt.figure()
ax = fig.add_subplot(111)
my_string = ""
total = 0
max_value = 37

f = open('tst2.csv','r')

print ('the file read - ')
my_string = f.read()

# clean: 
  
str_spl = my_string.split(",")

b = list(filter(lambda x: x.isnumeric(),str_spl))

# init histogram  - create empty list for histogram:
hist = []
for i in range(max_value):
    hist.append(0)

#count and add to histogram:
for x in b:
    hist[int(x)] += 1
    total += 1

print(total)
norm_hist = list(map(lambda x: x/total*100 ,hist))   
norm_hist_chk = sum(norm_hist)
if norm_hist_chk < 99: 
    print("ERROR #1")
    
#print(norm_hist)


rects1 = ax.bar(range(max_value),norm_hist,color='black')


i = 0
for x in norm_hist: 
    if x ==0: 
        print(i)
    i += 1;
    


f.close()

print('the end')

