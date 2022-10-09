"""
This problem was asked by Slack.

You are given a string formed by concatenating several words corresponding to the integers zero through nine and then anagramming.

For example, the input could be 'niesevehrtfeev', which is an anagram of 'threefiveseven'. Note that there can be multiple instances of each integer.

Given this string, return the original integers in sorted order. In the example above, this would be 357.
"""

def anagram_bam(string):
    letters={
        'z':{0: 'ero'},
        'o':{1: 'ne'},
        'w':{2: 'to'},
        't':{3: 'hree'},
        'f':{5: 'ive'},
        'u':{4: 'for'},
        's':{7: 'even'},
        'x':{6: 'si'},
        'g':{8: 'eiht'},
        'n':{9: 'ine'}
    }
    solution=dict()
    letters=dict()
    number_strings=['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'] 
    for i in range(len(number_strings)):
        word=number_strings[i]
        if word[:1] in letters:
            nums=letters[word[:1]]
            nums[i]=word
        else:
            letters[word[:1]]={i:word}

    final=[]
    for item in letters:
        print(f'{item} - {letters[item]}')

    for let in string:
        if let in letters:
            print('str', letters[let])
            # op=letters[let]
            # print('string poss:', len(op))
            # for n, n_string in op:
            #     final.append(n)
            #     for l in n_string:
            #         string.replace(l, ' ')
                
            #     print('-'.join(string.split()))
                
    # for let in string:
        
    #     num_option=list(letters[let].keys())
    #     word_len=list(letters[let].values())
    #         # print(f'match: {let} options:{num_option} length:{word_len}')
    #     for x in range(len(num_option)):
    #         if num_option[x] in solution:
    #             solution[num_option[x]]-=1
    #         #     if solution[num_option[x]] == word_len[x]:
    #         #         final.append(num_option[x])
    #         #     else:
    #         #         solution[num_option[x]]+=1
    #         else:
    #             solution[num_option[x]]=word_len[x]
                
            
            
             
    print(solution)

ex_1='niesevehrtfeev'
anagram_bam(ex_1)