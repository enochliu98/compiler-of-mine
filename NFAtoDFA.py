from extra_func import dfa_init,e_vetex

'''
这里是nfa转化成dfa的主函数
nfa和dfa的表示格式都是矩阵
'''
def NFA_DFA():
    number=0 #number是标志变量用来判断是否完成
    dfa_init() #这里mylist是全局变量，此时mylist已经发生了改变
    while number<len(mylist):
        dfaline=[]
        for i in range(n):
            #print('sdfasdfasdfasdfasdf')
            action=[]
            for j in range(len(mylist[number])):
                #print(mylist[number][j])
                #print(mylist[number][j])
                #print(nfamatrix[mylist[number][j]][i])
                if len(nfamatrix[mylist[number][j]][i])!=0:
                    for lyz in nfamatrix[mylist[number][j]][i]:
                        action.append(lyz)
                #action.append(nfamatrix[mylist[number][j]][i])
            #print(action)
            action=e_vetex(action) #这里进行e闭包处理
            dfaline.append(action)
            #print(dfaline)
            if action not in mylist and len(action)!=0:
                mylist.append(action)

        dfamatrix.append(dfaline)
        number+=1 #进行下一个遍历