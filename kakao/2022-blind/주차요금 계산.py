import collections

def convertTime(time):
    hour, minute = time
    return int(hour) * 60 + int(minute)

def solution(fees, records):
    cars = collections.defaultdict()
    times = collections.defaultdict()


    for record in records:
        time, carNum, info = record.split()
        if info == "IN":
            cars[carNum] = time

        if info == "OUT":
            inTime = cars[carNum]
            convertedInTime = convertTime(inTime.split(":"))
            convertedOutTime = convertTime(time.split(":"))
            usedTime = convertedOutTime - convertedInTime
            if carNum in times:
                times[carNum] += usedTime
            else:
                times[carNum]= usedTime
            cars[carNum] = 0

    for key, value in cars.items():
        if value != 0:
            convertedInTime = convertTime(value.split(":"))
            convertedOutTime = convertTime("23:59".split(":"))

            usedTime = convertedOutTime - convertedInTime
            if key in times:
                times[key] += usedTime
            else:
                times[key] = usedTime

    answer = []
    basicTime, basicFee, extraTime, extraFee = fees
    totalFees = collections.defaultdict()

    for key, time in times.items():
        if time <= basicTime:
            totalFees[key] = basicFee
            continue

        totalFee = basicFee
        remainedTime = time - basicTime
        if remainedTime % extraTime == 0:
            totalFee += remainedTime / extraTime * extraFee
        else:
            totalFee += (remainedTime // extraTime +1) * extraFee

        totalFees[key] = int(totalFee)

    sortedDict = sorted(totalFees.items())

    return list(map(lambda x: x[1], sortedDict))


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))