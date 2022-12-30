def solution(entires):
    sorted_entries = sorted(entires, key=lambda e:e["timestamp"])
    curr_max = 0
    max_people = 0
    period = (None,None)
    for i,entry in enumerate(sorted_entries):
        if entry["type"] == "enter":
            curr_max += entry["count"]
        # they leave
        else:
            curr_max -= entry["count"]
        
        # now check
        if curr_max > max_people:
            max_people = curr_max
            period = (entry["timestamp"] , sorted_entries[i+1]["timestamp"])
    return period


entries =[

    {"timestamp": 1526579928, "count": 3, "type": "enter"},
    {"timestamp": 1526579930, "count": 5, "type": "exit"},
    {"timestamp": 1526579935, "count": 7, "type": " enter"},
    {"timestamp": 1526579912, "count": 10, "type": "enter"},
    {"timestamp": 1526580382, "count": 12, "type": "exit"}


]
solution(entries)