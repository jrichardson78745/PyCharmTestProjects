#list
words = ['wood','cat','bird']

#for loop
for w in words:
    print (w)

#while loop
c = 0
while True:
    if c == 5:
        c += 1
        continue

    #print ('in a while loop with c = %d') c
    print (c)
    if c >= 10:
        break

    c += 1

print ('all loops complete')
