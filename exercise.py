digits = ['1','2','3','4','5','6','7','8','9']
en = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
fr = ['un','deux','trois','quatre','cinq','six','sept','huit','neuf']


dictOfWords = dict.fromkeys(digits , en)
# print(dictOfWords)

# d = dict([(k, v) for k,v in zip (digits[::2], en[::2])])
# print(d)


# ic= [{"French":val[0], "English":val[1]} for val in zip(fr, en)]
empty = {}
for i in range(0,9):
    empty[digits[i]] = {"French":fr[i], "English":en[i]}
    # for val in zip(fr,en):
    #     empty[digits[i]] = {"French":val[0], "English":val[1]}
print(empty)

# ww = dict(zip(digits, en))
# print('ww', ww)
# my_dict = {}

# my_list = map(lambda x: my_dict['en': x] , en )
# [print() for item in my_list]
# print(my_list)
