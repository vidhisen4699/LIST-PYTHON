binary_number = [1, 0, 0, 1, 1, 0, 1, 1]
sum1=0
k=1
i=len(binary_number)-1
while i>=0:
    # binary_number[i]*1
    sum1=sum1+binary_number[i]*k
    i=i-1
    k=k*2
print("Binary to Decimal Number",sum1)    

