def solution(fees, records):
    answer = []
    parking = dict()
    feeTotal = dict()
    for record in records:
        recordToList = record.split(" ")
        if recordToList[2] == "IN":
            parking[recordToList[1]] = recordToList[0]
        elif recordToList[2] == "OUT":
            if recordToList[1] in feeTotal :
                feeTotal[recordToList[1]] += calculateTime(parking[recordToList[1]],recordToList[0])
            else :
                feeTotal[recordToList[1]] = calculateTime(parking[recordToList[1]],recordToList[0])
            del parking[recordToList[1]]
    for remain in parking :
        if str(remain) in feeTotal :
            feeTotal[str(remain)] += calculateTime(parking[remain],"23:59")
        else : 
            feeTotal[str(remain)] = calculateTime(parking[remain],"23:59")
    feee = sorted(feeTotal)

    for fee in feee:
        answer.append(calFee(feeTotal[fee],fees))

    return answer

def calculateTime(inTime,outTime):
    inTimeHour = inTime.split(':')
    outTimeHour = outTime.split(':')
    inMin = int(inTimeHour[0]) * 60 + int(inTimeHour[1])
    outMin = int(outTimeHour[0]) * 60 + int(outTimeHour[1])
    return outMin - inMin

def calFee(time,fees):
    if time < fees[0]:
        return fees[1]
    else :
        if (time - fees[0]) % fees[2] != 0 :
            feeee = fees[1] + ((time - fees[0])//fees[2]+1) * fees[3]
        else :
            feeee = fees[1] + ((time - fees[0])//fees[2]) * fees[3]
        return feeee

    