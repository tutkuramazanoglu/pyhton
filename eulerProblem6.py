totalSquare=0
total=0
for i in range(101):
    totalSquare+=i*i
    total+=i;
total=total*total
difference=total-totalSquare
print(difference)
