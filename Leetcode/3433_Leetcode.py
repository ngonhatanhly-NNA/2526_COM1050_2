from typing import List
class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        # The result is corresponding to whenever event message is called, check if at that time
        # how many time users are called
        events = sorted(events, key = lambda event: (int(event[1]), 1 if event[0] == "MESSAGE" else 0))
        
        online = [0 for _ in range (numberOfUsers)]    
        res = [0 for _ in range (numberOfUsers)]
        
        for event in events:
            call = event[0]
            time = int(event[1])
            lst_id = list(map(str, event[2].split()))
            
            if call == "OFFLINE":
                for id in lst_id:
                        curr = int(id)
                        online[curr] = time + 60
            
            elif call == "MESSAGE":
                # If here, check online, else, but after 60 seconds will go back onlien, must handle this case too
                if "HERE" in lst_id:
                    for i in range (numberOfUsers):
                        is_online = time >= online[i]
                        if is_online:
                            res[i] += 1
                elif "ALL" in lst_id:
                    res = [res[i] + 1 for i in range (numberOfUsers)]
                else:
                    for id in lst_id:
                        curr = int(id[2:])
                        res[curr] += 1

        return res
