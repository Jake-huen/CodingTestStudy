def solution(fees, records):
    def count_calculate(start, end):
        start_hour = int(start.split(":")[0]) * 60
        start_minu = int(start.split(":")[1])
        end_hour = int(end.split(":")[0]) * 60
        end_minu = int(end.split(":")[1])
        return start_hour + start_minu - end_hour - end_minu

    answer = []
    car_record = {}
    car_time = []

    for record in records:
        temp = record.split(" ")
        if temp[1] in car_record:
            car_record[temp[1]].append(temp[0])
        else:
            car_record[temp[1]] = [temp[0]]

    for key in car_record:
        if len(car_record[key]) % 2 == 1:
            car_record[key].append('23:59')
        temp = 0
        for i in range(1, len(car_record[key]), 2):
            temp += count_calculate(car_record[key][i], car_record[key][i - 1])
        car_time.append((key, temp))

        # for time in car_time:
        #     if time <= fees[0]:
        #         answer.append(fees[1])
        #     else:
        #         if (time-fees[0])%fees[2] == 0:
        #             answer.append((time-fees[0])//fees[2]*fees[3] + fees[1])
        #         else:
        #             answer.append(((time-fees[0])//fees[2]+1) * fees[3] + fees[1])
        # return answer

print(solution([180, 5000, 10, 600],
       ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
        "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))