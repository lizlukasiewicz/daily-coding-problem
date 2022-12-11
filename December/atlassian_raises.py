"""

This problem was asked by Atlassian.

MegaCorp wants to give bonuses to its employees based on how many lines of codes they have written. 
They would like to give the smallest positive amount to each worker consistent with the constraint 
that if a developer has written more lines of code than their neighbor, they should receive more money.

Given an array representing a line of seats of employees at MegaCorp, determine how much each one should get paid.

For example, given [10, 40, 200, 1000, 60, 30], you should return [1, 2, 3, 4, 2, 1].

"""
def raises(employees):
    stack=[0]*len(employees)
    base=1
    for i, lines in enumerate(employees[:-1]):
        next=i+1
        if lines < employees[next]:
            stack[i]+=base
            base+=1
        else:
            stack[i]+=base
            base-=1
    stack[-1]+=base
    print(stack)

emp_code=[10, 40, 200, 1000, 60, 30]
raises(emp_code)