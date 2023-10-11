import time
i=9
j=9
k=9
l=9

while(i>=0):
    while(j>=0):
        while(k>=0):
            while(l>=0):
                num_to_display=[i,j,k,l]
                print(num_to_display)
                time.sleep(0.1)
                l=l-1
            k=k-1
            l=9
        j=j-1
        k=9
    i=i-1
    j=9
