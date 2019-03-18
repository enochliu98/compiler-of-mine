
'''
myset:这里传递进来一个list
里面存储的是dfs的一个新状态
返回的是处理完闭包的新的list
'''
def e_vetex(myset):
    # 这里定义一个递归嵌套函数，用来处理e—闭包问题
    def s(q):
        nonlocal myset  # 已经把上层函数中的myset进行了改变
        if q not in myset:
            myset.append(q)

        for p in e[q]:
            if p!=-1:
                s(p)


    iter_myset=tuple(myset) #这里用iter_myset代替myset，因为myset在计算过程中被改变,使用tuple1是防止改变
    for i in iter_myset: #循环myset中的每一个元素
        j=i #这里用j来代替i，防止i被改变
        s(j)
    # for i in myset:
    #     j=i#这里用j代替i用来防止i在过程中被改变
    #     print(e)
    #     while e[j][0]!=-1:
    #         for k in e[j]:
    #             if k not in myset:##这里是为了防止重复出现
    #                 myset.append(k)
    #                 j=e[j]

    return  myset



'''
这里用于对dfa的初始化
'''
def dfa_init():

    #S为初始状态集合
    global mylist
    myset=S
    mini_mylist=e_vetex(myset)
    mylist.append(mini_mylist)
    #由于这里声明了global所以不用再返回