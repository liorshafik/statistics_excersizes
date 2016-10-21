
f = open('Lotto.csv','r')

print ('the file Lotto read - ')
my_string = f.read()


str_spl = my_string.split(",")
b = list(filter(lambda x: x.isnumeric(),str_spl))





print('the end')

