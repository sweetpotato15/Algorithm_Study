from math import ceil

def time_to_fee(minute, fees):
    if minute <= fees[0] :
        return fees[1]
    else:
        answer = fees[1] + ceil((minute - fees[0]) / fees[2]) * fees[3]
        return answer

def solution(fees, records):
    cars = [i[6:10] for i in records]
    cars = sorted(list(set(cars)))

    record = {x : [] for x in cars}
    for i in records :
        time = int(i[:2]) * 60 + int(i[3:5])
        car = i[6:10]
        record[car].append(time)

    answer = []
    for i in record.values():
        if len(i) % 2 != 0:
            i.append(23*60+59)
        minute = sum(i[1::2]) - sum(i[0::2])
        fee = time_to_fee(minute, fees)
        answer.append(fee)
    return answer