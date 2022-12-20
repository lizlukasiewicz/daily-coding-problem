"""
This problem was asked by Snapchat.

Given a list of possibly overlapping intervals, 
return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], 
you should return [(1, 3), (4, 10), (20, 25)].
"""
def merge_int(lst):
    new=[]
    for i, pair in enumerate(lst):
        merged=[pair[0], pair[1]]
        #pair[0] pair[1]
        for intervals in lst[1:]:
            if intervals[0]< pair[0] <intervals[1]:
                merged.pop(0)
                merged.insert(0, intervals[0])
            # else:
            #     merged[0]+=pair[0]
            if intervals[0]< pair[1] <intervals[1]:
                merged.pop(-1)
                merged.append(intervals[1])
            # else:
            #     merged[1]+=pair[1]
        merged=tuple(merged)
        new.append(merged)
    print(new)



test_int=[(1, 3), (5, 8), (4, 10), (20, 25)]
merge_int(test_int)