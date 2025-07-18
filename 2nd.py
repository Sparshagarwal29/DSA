def locate_card(cards,qurey) :
    postion = 0 
    while postion < len(cards) :
        if cards [postion] ==  qurey:
            return postion
        postion +=1

        if(postion == len(cards)):
            return -1
    return -1
# test case :
# 1-- if query is in middle of the list 
# 2-- if query is at the end of the list
# 3 - if querry is at the start of the list 
# 4 -- if only one element that is qureey is their 
# 5 -- no qurey in the list
# 6 --  list is empty 
# 7 -- list has repeting elements 
# 8 qury is present multiple times in the list

test = []
# test case 1
test.append ({
    'input' : {
        'cards' : [13,11,10,7,4,3,1,0],
        'qurey' : 1
    },
    'output' : 6
})
# test case 2
test.append ({
    'input' : {
        'cards' : [13,11,10,7,4,3,1,0],
        'qurey' : 0
    },
    'output' : 7
})
# test case 3
test.append ({
    'input' : {
        'cards' : [13,11,10,7,4,3,1,0],
        'qurey' : 13
    },
    'output' : 0
})
# test case 4
test.append ({
    'input' : {
        'cards' : [-7],
        'qurey' : -7
    },
    'output' : 0
})
# test case 5
test.append ({
    'input' : {
        'cards' : [13,11,10,7,4,3,1,0],
        'qurey' : 8
    },
    'output' : -1
})
# test case 6
test.append ({
    'input' : {
        'cards' : [],
        'qurey' : 8
    },
    'output' : -1
})
# test case 7
test.append ({
    'input' : {
        'cards' : [8,8,8,8,4,4,3,1,0],
        'qurey' : 3
    },
    'output' : 6
})
# test case 8
test.append ({
    'input' : {
        'cards' : [13,11,10,7,7,3,1,0],
        'qurey' : 7
    },
    'output' : 3
})




for i in test:
    input_data = i['input']
    expected_output = i['output']
    actual_output = locate_card(input_data['cards'], input_data['qurey'])
    if actual_output == expected_output:
        print(f"Test passed for input {input_data}. Expected: {expected_output}, Got: {actual_output}")
    else:
        print(f"Test failed for input {input_data}. Expected: {expected_output}, Got: {actual_output}")