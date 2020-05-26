def maxNumber(numbers,lenght,fNumber):
    if(fNumber<numbers[lenght-2]):
        fNumber=numbers[lenght-2]

    if lenght!=0:
        newLen=lenght-1
        return maxNumber(numbers,newLen,fNumber)
    if lenght==0:
        return fNumber


numbers=[10,15,8,2,1,3,45,2,20,16]
firstNumb=numbers[len(numbers)-1]
if len(numbers)==1:
    print(numbers[0])
else:
    print(maxNumber(numbers,len(numbers),firstNumb))