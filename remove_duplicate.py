import json


def find_duplicate(path: 'str') -> None:
    my_dict = {}
    my_dict1 = {}
    unused = {}
    list1 = []
    j = 0
    pop_list = []

    #  outfile1= open('asd.py',"r+")
    outfile1 = open(path, "r+")

    for i in outfile1.readlines()[:]:
        j += 1
        i = i.strip('\n')
        i = i.strip(' ')

        if ' as' in i:
            var = i[:i.index(' as')]
        else:
            var = i

        # creating json
        if var not in my_dict1 and i != '' and ('import ' in i):
            if ' as ' in i:
                my_dict1[i[:i.index(' as')]] = []
                #print('main   ',my_dict1[i[:i.index(' as')]])
                #print('hello    ',my_dict1.keys())
                unused[i[i.index(' ') + 1:i.index(' as')]] = i[i.index(' as') + 3:]

            else:
                list1.append(i)
                my_dict1[i] = []
                unused[i[i.index(' ') + 1:]] = i[i.index(' ') + 1:]

        # Populating import modelue count
        if i != '' and 'import ' in i:
            if ' as ' in i:
                list1.append(var)
                #print(list1)
                my_dict1[var] += [j]
                #print(my_dict1)
            else:
                list1.append(i)
                my_dict1[i] += [j]

    # creating duplicate json
    unused1 = unused.copy()

    # finding unused imports
    for i, j in unused.items():
        print(i,'    ',j)
        k = str(j) + '.'
        k=k.strip(' ')
        #print('k is ',k)
        outfile1.seek(0)
        for l in outfile1:
            print('l is -> ',l,'   k  ->',k)
            print('ttt   ',k in l)
            if (k in l): #and ('import' not in l):
                print('npnpnp')
                unused1[i] = 'Used'
                break
            else:
                unused1[i] = 'Not Used'

 #   for i in s1:
  #      my_dict[i] = list1.count(i)

    outfile1.close()

    # Removing module which are not repeated
    for a, b in my_dict1.items():
        if len(b) <= 1:
            pop_list.append(a)

    for i in pop_list:
        my_dict1.pop(i)

    print('************************************')
    print('     Duplicate  Import Module    ')
    print('************************************')
    print(my_dict1)
    # print(json.dumps(my_dict1,indent=1))
    # print('\n')
    print('************************************')
    print('         Unused Module')
    print('************************************')
    # print('\n')
    print(unused1)
