a = []

#Function to accept reference string and frame size.
def accept():
    global a,n,m
    n = int(input("\n Enter the size of reference string : "))
    for i in range(n):
        a.append(input(" Enter [%2d] : " % (i+1)))
    m = int(input("\n Enter page frame size : "))

#First In First Out Page Replacement Algorithm
def __fifo():
    global a,n,m
    f = -1
    page_faults = 0
    page = []
    for i in range(m):
        page.append(-1)

    for i in range(n):
        flag = 0
        for j in range(m):
            if(page[j] == a[i]):
                flag = 1
                break

        if flag == 0:
            f=(f+1)%m
            page[f] = a[i]
            page_faults+=1
            print ("\n%s ->" % (a[i]),)
            for j in range(m):
                if page[j] != -1:
                    print (page[j])
                else:
                    print( "-")
        else:
            print ("\n%d -> No Page Fault" % (a[i]))
            
    print ("\n Total page faults : %d." % (page_faults))

#Least Recently Used Page Replacement Algorithm
def __lru():
    global a,n,m
    x = 0
    page_faults = 0
    page = []
    for i in range(m):
        page.append(-1)

    for i in range(n):
        flag = 0
        for j in range(m):
            if(page[j] == a[i]):
                flag = 1
                break
            
        if flag == 0:
            if page[x] != -1:
                min = 999
                for k in range(m):
                    flag = 0
                    j =  i
                    while j>=0:
                        j-=1
                        if(page[k] == a[j]):
                            flag = 1
                            break
                    if (flag == 1 and min > j):
                        min = j
                        x = k

            page[x] = a[i]
            x=(x+1)%m
            page_faults+=1
            print ("\n%s ->" % (a[i]))
            for j in range(m):
                if page[j] != -1:
                    print (page[j])
                else:
                    print ("-",)
        else:
            print ("\n%s -> No Page Fault" % (a[i]))
            
    print ("\n Total page faults : %s." % (page_faults))

#Optimal Page Replacement Algorithm
def __optimal():
    global a,n,m
    x = 0
    page_faults = 0
    page = []
    for i in range(m):
        page.append(-1)

    for i in range(n):
        flag = 0
        for j in range(m):
            if(page[j] == a[i]):
                flag = 1
                break
            
        if flag == 0:
            if page[x] != -1:
                max = -1
                for k in range(m):
                    flag = 0
                    j =  i
                    while j<n:
                        j+=1
                        if(page[k] == a[j]):
                            flag = 1
                            break
                    if (flag == 1 and min < j):
                        max = j
                        x = k

            page[x] = a[i]
            x=(x+1)%m
            page_faults+=1
            print ("\n%s ->" % (a[i]),)
            for j in range(m):
                if page[j] != -1:
                    print (page[j],)
                else:
                    print ("-"),
        else:
            print ("\n%s -> No Page Fault" % (a[i]))
            
    print ("\n Total page faults : %s." % (page_faults))

    

#Displaying the menu and calling the functions.    
while True:
    print ("\n SIMULATION OF PAGE REPLACEMENT ALGORITHM")
    print (" Menu:")
    print (" 0. Accept.")
    print (" 1. FIFO.")
    print (" 2. LRU.")
    print (" 3. Optimal.")
    print( " 4. Exit.")
    ch = input(" Select : ")

    if ch == '0':
        accept()
        # break
    elif ch == '1':
        __fifo()
    elif ch == '2':
        __lru()
    elif ch == '3':
        __optimal()
    else:
        break
