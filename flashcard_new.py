'''
1) User input Yes or No, lower first letter and test
2) concatenation
3) immutable example with try except
4) index out of range error
5) search?
'''
## 1
# def main():
    # user_input = 'Yes'
    # answer = user_input[0].lower()
    # msg = question_handler(answer)
    # print(msg)
    
# def question_handler(ans_str):
    # if ans_str == 'y':
        # response = 'Continue.'
    # elif ans_str == 'n':
        # response = 'Do not continue'
    # else:
        # response = 'Answer undefined'
    # return response
# main()

## 2

# def main():
    # input_string = 'Pithon rocks!'
    # try:
        # input_string[1] = 'y'
        # print(input_string)
    # except TypeError:
        # print('Error. Why?')
# main()

## 3

def main():
    data_entry_1 = 'Errors should never pass silently.'
    data_entry_2 = 'Unless explicitly silenced.'
    data_entry_3 = 'Readability counts.'
    data_list = [data_entry_1, data_entry_2, data_entry_3]
    msg = search_strings(data_list)
    print(msg)
    
def search_strings(data_list):
    search_param = 'expl'
    for entry in data_list:
        if entry.find(search_param) != -1: # Why -1?
            return entry
        else:
            msg = 'No matches'
    return msg
main()

## 4

# def main():
    # orig_msg = 'BOOKMARK YOUR STRING AND LIST METHODS.'
    # new_str = ''
    # for char in orig_msg: # Is there a better way to do this?
        # new_str += char.lower()
    # print('Some good advice:')
    # print(new_str.capitalize())
# main()

## 5

# def main():
    # str_list = [['This', 'is', 'an', 'example'],
                # ['of', 'a', 'two-dimensional', 'list.']]
    # print('1: ' + str_list[0][2][1])
    # print('2: ' + str_list[1][3][0])
    # print('3: ' + str_list[1][0] + '\n')
    
    # for sub_list in str_list:
        # for word in sub_list:
            # msg = word + ' '
            # print(msg, end ='')
# main()

## 6
# def main()