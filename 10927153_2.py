# 演算法分析機測
# 學號: 10927153 / 10927248 /10927256
# 姓名: 吳上玲 / 連翊安 / 姜美羚
# 中原大學資訊工程系

import numpy as np

def find_path( mapp, node1) -> bool:
    
    global node
    
    if len(path) == node+1 and path[ len(path)-1 ] == 1 :
        # path存在所有通路且回到起點
        return True
    
    for i in range( 1, node+1 ): # 1~最後一點
        saved = False   # 判斷是否已存在path中
        for j in range(len(path)) :
            if path[j] == i and ( len(path) != node or i != path[0] ):
                # 當path中已存在此數 且 非(遍歷後正回到起點)的狀況
                saved = True
                
        if saved : #跳過此數字的路徑
            continue
        
        if mapp[node1][i] : # 當此路徑為通
            if i == path[0] and len(path) != node :
                # 提前能回到起點需跳過此次,還沒把所有點都走過就回到1
                continue
            
            path.append(i)  # 將數字加至路徑path
            mapp[node1][i] = 0
            mapp[i][node1] = 0  # 將雙向通路關閉
            #print(node1, i) # test
            if find_path( mapp, i ) is False :  # 遞迴查找路徑
                # 若此路不通 須將先前通路開回且取消此路徑
                #print("delete", node1, i)   # test
                mapp[node1][i] = 1
                mapp[i][node1] = 1
                path.pop() 
            else :
                return True
                
    if len(path) != node+1 or path[ len(path)-1 ] != 1 :
        # 遍歷所有通路都無法進入 則 證明此路不通
        return False
            
    

while True :
    str = input("continue? (Y/N)")
    if str == "Y" or str == 'y':
        pass
    elif str == "N" or str == 'n':
        break
    else :
        print("I don't care anymore, bye :) ")
        break
    
    str = input("\n\ninput (node side): ")
    num = str.split(' ')
    node = int(num[0])    # 輸入的all頂點數
    side = int(num[1])    # 輸入的all邊數
    mapp = np.zeros([11,11]) # 建立10*10的陣列
    path = list()  # Save Hamiltonian Path
    path.append(1)    # 從1出發
    i = 1
    while str != "0 0" or str == "\n":
        str = input(f"side {i} (node1 node2): ")
        num = str.split(' ')
        node1 = int(num[0])    #輸入數字1
        node2 = int(num[1])    #輸入數字2
        mapp[node1, node2] = True
        mapp[node2, node1] = True
        i = i + 1
        
    if str != "0 0" :
        print( "It's syntax error!" )
    else :
        if find_path(mapp, path[0]) is False : # 地圖, 走過第幾個點, 從起點開始
            print("It doesn't have Hamiltonian Path.")
        else : 
            print( "\n\n", path, "\n\n" )
        
