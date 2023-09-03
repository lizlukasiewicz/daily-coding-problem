"""
This problem was asked by Google.

A girl is walking along an apple orchard with a bag in each hand. 
She likes to pick apples from each tree as she goes along, 
but is meticulous about not putting different kinds of apples in the same bag.

Given an input describing the types of apples she will pass on her path, in order, 
determine the length of the longest portion of her path that consists of just two types of apple trees.

For example, given the input [2, 1, 2, 3, 3, 1, 3, 5], 
the longest portion will involve types 1 and 3, with a length of four.
"""

def orchard(input:list):
    apple_type={}
    max_count=0
    left=0
    for right in range(len(input)):
        # add type of apple to the basket, iteration of type tree in row
        apple_type[input[right]]=apple_type.get(input[right], 0)+1

        # condition WHEN APPLE TYPE EXCEEDS 2
        while len(apple_type) > 2:
            #remove type of apple from basket starting with LEFT
            apple_type[input[left]]-=1
            
            # condition REMOVE apple type when ==0
            if apple_type[input[left]] == 0:
                del apple_type[input[left]]
            #continue moving keft side of window
            left+=1
        # update max length of trees subarray to max between curr_max and right-left+1
        max_count= max(max_count, right-left+1)
    # return max count
    return max_count


if __name__ == '__main__':
    trees=[2, 1, 2, 3, 3, 1, 3, 5]
    print(orchard(trees))