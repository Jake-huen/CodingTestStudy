def solution(id_list, report, k):
    answer = []
    rp=[[]for _ in range(len(id_list))]
    for i in range(len(id_list)):
        rp[i]=id_list[i]
    for i in range(len(id_list)):
        for j in range(len(report)):
            if report[j][0]==id_list[i]:
                rp[i].append(report[j][1])
                print(rp[i])
    # return answer

# id_list : ["muzi", "frodo", "apeach", "neo"]
# report : ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"] => muzi가 frodo신고
# k : 2
# result : [2,1,1,0]
solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)
