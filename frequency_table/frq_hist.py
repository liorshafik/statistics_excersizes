import matplotlib.pyplot as plt

#------------------------------------------------------------------------
#------------------------------------------------------------------------
#init
fig = plt.figure()
ax = fig.add_subplot(111)
my_string = ""
total = 0
max_value = 38
b =list({0})
hist = list({0})
norm_hist = list({0})
str_spl = list({0})

f = open('tst2.csv','r')

print ('the file1 read - ')
my_string = f.read()

# clean: 
  
string = my_string.replace("\n",",")

str_spl = string.split(",")


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

print('the end1')

#------------------------------------------------------------------------
#------------------------------------------------------------------------
#init
fig = plt.figure()
ax = fig.add_subplot(211)
my_string = ""
total = 0
max_value = 7
b =list({0})
hist = list({0})
norm_hist = list({0})

f = open('tst3.csv','r')

print ('the file2 read - ')
my_string = f.read()

# clean: 
string = my_string.replace("\n",",")

str_spl = string.split(",")


b = list(filter(lambda x: x.isnumeric(),str_spl))

# init histogram  - create empty list for histogram:

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


rects1 = ax.bar(range(max_value + 1),norm_hist,color='black')


i = 0
for x in norm_hist: 
    if x ==0: 
        print(i)
    i += 1;
    


f.close()

print('the end1')

