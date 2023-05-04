
# task 1
my_strings = ['blaaa', 'bla', 'blaa']

# def sort_word(str):
#     result = sum(1 for i in str if i in 'aeiouOUIEA')
#     return result


# sorted_lst = sorted(my_strings, key=sort_word)
sorted_lst = sorted(my_strings, key=lambda word: sum(1 for i in word if i in 'aeiouOUIEA'))

print(sorted_lst)

# task 2

tuple_list = [(2, 5), (1, 7), (4, 3), (6, 1), (3, 8)] #-->   [(6, 1), (4, 3), (2, 5), (1, 7), (3, 8)]

tuple_list.sort(key = lambda tpl:tpl[1]) 
print(tuple_list)
        

