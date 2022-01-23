# Kakao Open Recruitment 2022 Question 3

import heapq
import math
def solution(fees, records):
    # key=car_no : value=[in_out_time,,]
    io_records = {}
    # ordering
    min_heap = []
    
    # record mapping 
    for record in records:
        time, car_no, _ = record.split()
        if car_no in io_records:
            io_records[car_no].append(time)
        else:
            heapq.heappush(min_heap, car_no)
            io_records[car_no] = [time]
    
    # initialize result array
    total_charges = []
    
    # main logic (pop from heap starting from index 0 to end)
    while min_heap:
        car_no = heapq.heappop(min_heap)
        
        io_record = io_records[car_no]
        total_time = 0
        for i,time in enumerate(io_record):
            hours, minutes = time.split(':')
            if i % 2 == 0:
                total_time -= (int(hours)*60 + int(minutes))
            else:
                total_time += (int(hours)*60 + int(minutes))
        
        # car has not gone out
        if len(io_record) % 2 == 1: 
            total_time += (23*60 + 59)
        
        # compute the total charge
        total_charge = 0
        if total_time > fees[0]:
            # additional fee charged
            total_charge = fees[1] + math.ceil((total_time - fees[0])/fees[2])*fees[3]
        else:
            # base fee charged
            total_charge = fees[1]
        
        # record total charge for each car
        total_charges.append(total_charge)
            
        
    return total_charges