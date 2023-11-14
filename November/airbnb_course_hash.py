"""

This problem was asked by Airbnb.

We're given a hashmap associating each courseId key with a list of courseIds values, which represents that the prerequisites of courseId are courseIds. 
Return a sorted ordering of courses such that we can finish all courses.

Return null if there is no such ordering.

For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}, should return ['CSC100', 'CSC200', 'CSCS300'].


"""
def course_order(courseIds: dict):

  max_len=max([len(l) for l in courseIds.values()])
  # loop through courses for required classes
  for course, req in courseIds.items():
    
    if len(req)==max_len:
      
      order_class=[]
      for c in req:
        if c in courseIds:
          order_class.append(c)
        else:
          return None
          
      order_class.append(course)
      return order_class

  return None








if __name__=='__main__':
  ex_course={
            'CSC300': ['CSC100', 'CSC200'], 
            'CSC200': ['CSC100'], 
            'CSC100': []
  }

  print(f"returns: {course_order(ex_course)}")