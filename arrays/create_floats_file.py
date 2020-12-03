f = open("floats.txt", "w+")

for i in range(10**7):
    f.write('{}'.format(i+i*0.3))
    
f.close()