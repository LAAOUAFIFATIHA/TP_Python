def rev(dic):
    new_dic = {v: k for k, v in dic.items()}
    print(new_dic)

dic = {'fatiha': 2, 'badia': 8, 'imane': 77}
rev(dic)