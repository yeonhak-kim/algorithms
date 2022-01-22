# Kakao Open Recruitment Question 1

def solution(id_list, reports, k):
    # key=id : value=reporter
    index_mapping = {}
    report_mapping = {}
    for i, id in enumerate(id_list):
        index_mapping[id] = i
        report_mapping[id] = []
    
    # set that prevents duplicate reports
    seen = set()
    
    # iterate through reports and record history
    for report in reports:
        if report not in seen:
            seen.add(report)
            reporter, reported = report.split()
            report_mapping[reported].append(reporter)
            
    # initialize result array
    answer = [0 for _ in range(len(id_list))]
    
    # iterate through the record history and count the number of emails to be sent to the reporter
    for reported in report_mapping:
        if len(report_mapping[reported]) >= k:
            for reporter in report_mapping[reported]:
                answer[index_mapping[reporter]] += 1
    
    return answer