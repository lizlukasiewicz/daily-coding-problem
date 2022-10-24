"""
This problem was asked by Airbnb.

We're given a hashmap associating each courseId key with a list of courseIds values, 
which represents that the prerequisites of courseId are courseIds. 
Return a sorted ordering of courses such that we can finish all courses.

Return null if there is no such ordering.

For example, given
 {
    'CSC300': ['CSC100', 'CSC200'], 
    'CSC200': ['CSC100'],  
    'CSC100': []
    }, 
 should return ['CSC100', 'CSC200', 'CSCS300'].


"""

def course_order(hashmap):
    order=[]
    for course in hashmap:
        for prereq in hashmap[course]:
            if hashmap[prereq]:
                order.insert(0, prereq)
            else:
                order.append(prereq)
        order.append(course)
    print(order)

courseId={
    'CSC300': ['CSC100', 'CSC200'], 
    'CSC200': ['CSC100'],  
    'CSC100': []
    }
course_order(courseId)
        # if len(hashmap[course])==0:
        #     order.insert(0, course)