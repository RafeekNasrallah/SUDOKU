from tkinter.messagebox import showinfo
from copy import copy, deepcopy
from tkinter import *

matrix = [[0, 0, 0, 0, 0, 0, 7, 0, 0],
     [5, 4, 9, 0, 8, 7, 1, 0, 2],
     [0, 0, 1, 9, 0, 0, 0, 8, 0],
     [0, 0, 0, 2, 0, 0, 8, 0, 1],
     [0, 7, 2, 8, 0, 6, 3, 9, 0],
     [3, 0, 4, 0, 0, 1, 0, 0, 0],
     [0, 2, 0, 0, 0, 9, 4, 0, 0],
     [4, 0, 7, 1, 3, 0, 5, 2, 6],
     [0, 0, 5, 0, 0, 0, 0, 0, 0]]

initmatrix = [[0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0]]

solved = []

def findrows(a, row, num): # gets matrix, row number, and a number, finds whether this number exits in this
    x = 0
    while x != 9:
        if a[x][row] == num:
            return True
        else:
            x = x + 1
    return False
##

def findcols(a, col, num): # gets a matrix, column number, and a number, find whether this number exits in thsi amtrix
    x = 0
    while x != 9:
        if a[col][x] == num:
            return True
        else:
            x = x + 1
    return False


def findblock(i, j): # gets a position in the matix, returns the number of the block
    if i < 3:
        if j < 3:
            return 0
        else:
            if 3 <= j  and j < 6:
                return 1
            else:
                return 2
    if 2 < i and i < 6:
        if j < 3:
            return 3
        else:
            if 3 <= j < 6:
                return 4
            else:
                return 5
    else:
        if i>5:
            if j < 3:
                return 6
            else:
                if 3 <= j < 6:
                    return 7
                else:
                    return 8


def searchblock(a, block, num): # take a matrix, a block number and a number, returns whether this numbers exists int his mblock
    if block == 0:
        for x in range(0, 3):
            for y in range(0, 3):
                if a[x][y] == num:
                    return True
        return False
    if block == 1:
        for x in range(0, 3):
            for y in range(3, 6):
                if a[x][y] == num:
                    return True
        return False
    if block == 2:
        for x in range(0, 3):
            for y in range(6, 9):
                if a[x][y] == num:
                    return True
        return False
    if block == 3:
        for x in range(3, 6):
            for y in range(0, 3):
                if a[x][y] == num:
                    return True
        return False
    if block == 4:
        for x in range(3, 6):
            for y in range(3, 6):
                if a[x][y] == num:
                    return True
        return False
    if block == 5:
        for x in range(3, 6):
            for y in range(6, 9):
                if a[x][y] == num:
                    return True
        return False
    if block == 6:
        for x in range(6, 9):
            for y in range(0, 3):
                if a[x][y] == num:
                    return True
        return False
    if block == 7:
        for x in range(6, 9):
            for y in range(3, 6):
                if a[x][y] == num:
                    return True
        return False
    if block == 8:
        for x in range(6, 9):
            for y in range(6, 9):
                if a[x][y] == num:
                    return True
        return False


def sudorecursive(a): # the main recursive sudoko solver with back tracking!
    global solved
    for i in range(9):
        for j in range(9):
              if a[i][j] == 0:
                for temp in range(1,10):
                    if not (findcols(a, i, temp)) and not (findrows(a, j, temp)) and not (
                    searchblock(a, findblock(i, j), temp)):
                        a[i][j] = temp
                        sudorecursive(a)
                        a[i][j] = 0
                return
    solved = deepcopy(a)

def dosuditerative(mat): # iterative version, simple backtracking (bruteforce :) ) but its nice
    temp=mat
    dict = []
    i = 0
    j = 0
    counter = 1
    while j < 9 and i < 9:
        if temp[i][j] == 0:
            if not (findcols(temp, i, counter)) and not (findrows(temp, j, counter)) and not (
                    searchblock(temp, findblock(i, j), counter)) and counter <= 9:
                temp[i][j] = counter
                oldi = i
                oldj = j
                oldcounter = counter
                dict.append((oldi, oldj, oldcounter))
                counter = 0
                if j == 8:
                    j = 0
                    i = i + 1
                else:
                    j = j + 1
            else:
                if counter > 9:
                    (oldi, oldj, oldcounter) = dict.pop()
                    i = oldi
                    j = oldj
                    counter = oldcounter + 1
                    temp[oldi][oldj] = 0
                else:
                    counter = counter + 1
        else:
            if j == 8:
                j = 0
                i = i + 1
            else:
                j = j + 1
"""
frame1 is the main frame, where you can see the given matrix and where you can try to solve it (changing the global variable matrix will change the sudoko game on frame 1
frame2 is the solution of the given matrix
frame3 is the frame where the user can give his own matrix and then the program will solve it for him
frame4 is where he will be able to see the soluton of the matrix he gave


NOTE: its my first time doing gui :$
"""

def raise_frame2(frame):
    frame.tkraise()
    sudorecursive(original)
    for i in range(9):
        for j in range(9):
            if (i,j) in tuples:
                l2 = Label(f2, text=str(solved[i][j]), font='Helvetica 17 bold',foreground="red")
                l2.grid(row=i, column=j,padx=24, pady=3,ipady=3)
            else:
                l2 = Label(f2, text=str(solved[i][j]), font='Helvetica 17 bold')
                l2.grid(row=i, column=j, padx=24, pady=3, ipady=3)
    b7 =Button(f2, text = 'Back!', command= lambda:raise_frame1(f1))
    b7.grid(row=9,column=5)


def checksol(matri):
    tempo = deepcopy(matri)
    k = 0
    for i in range(9):
        for j in range(9):
            n = txt[k]
            if len(n.get()) != 0:
                if tempo[i][j] == 0:
                    tempo[i][j] = n.get()
                    k = k + 1
            else:
                showinfo("Window", "Please fill everything")
                return
    bool = True
    for i in range(9):
        for j in range(9):
            c = tempo[i][j]
            tempo[i][j] = 0
            if findrows(tempo,j,c):
                bool = False
                info1="wrong row: " + str(j)
                showinfo("Window", info1)
                return
            if findcols(tempo,i,c):
                bool = False
                info2="wrong col: " + str(i)
                showinfo("Window", info2)
                return
            if searchblock(tempo,findblock(i,j),c):
                bool = False
                info3="wrong block: " + str(findblock(i,j))
                showinfo("Window", info3)
                return
            tempo[i][j] = c
    if bool == True:
        showinfo("Window", "Well Done!")


def raise_frame3(f3):
    f3.tkraise()

def raise_frame1(f1):
    f1.tkraise()


def calculate():
    k = 0
    tuples3 = []
    tempmat = deepcopy(initmatrix)
    for i in range(9):
        for j in range(9):
            n = txtboxs[k]
            if len(n.get()) != 0:
                tempmat[i][j]=int(n.get())
                tuples3.append((i,j))
            k = k + 1
    sudorecursive(tempmat)
    f4 = Frame(master)
    f4.grid(row=0, column=0, sticky='news')
    b5 =Button(f4, text = 'Back!', command= lambda:raise_frame1(f1))
    b5.grid(row=9,column=4)
    for i in range(9):
        for j in range(9):
            if (i, j) in tuples3:
                l2 = Label(f4, text=str(solved[i][j]), font='Helvetica 17 bold', foreground="red")
                l2.grid(row=i, column=j, padx=24, pady=3, ipady=3)
            else:
                l2 = Label(f4, text=str(solved[i][j]), font='Helvetica 17 bold')
                l2.grid(row=i, column=j, padx=24, pady=3, ipady=3)
    f4.tkraise()





original = deepcopy(matrix)
testsol = deepcopy(matrix)
tuples = []

for i in range(9):
    for j in range(9):
        if original[i][j] != 0:
            tuples.append((i,j))



master = Tk()
master.geometry('630x450')
f1 = Frame(master)
f2 = Frame(master)
f3 = Frame(master)
for frame in (f1, f2,f3):
    frame.grid(row=0, column=0, sticky='news')
txt = []
counter = 0
for i in range(9):
    for j in range(9):
       if original[i][j] == 0:
            txt.append(Entry(f1,width=6))
            txt[counter].grid(column=j, row=i,padx=10, pady=10,ipady=3)
            counter=counter + 1
       else:
            l1 =Label(f1, text=str(original[i][j]),font='Helvetica 18 bold')
            l1.grid(row=i, column=j)

txtboxs = []
counter = 0
for i in range(9):
    for j in range(9):
        txtboxs.append(Entry(f3,width=6))
        txtboxs[counter].grid(column=j, row=i,padx=10, pady=10,ipady=3)
        counter=counter + 1


b1 = Button(f1, text='Solution!', command=lambda:raise_frame2(f2))
b1.grid(row=9,column=3)
b4 = Button(f3, text='Solve!', command=lambda : calculate())
b4.grid(row=9,column=3)
b2 =Button(f1, text = 'Done!', command= lambda : checksol(matrix))
b2.grid(row=9,column=4)
b3 =Button(f1, text = 'Enter one!', command= lambda:raise_frame3(f3))
b3.grid(row=9,column=5)
b6 =Button(f3, text = 'Back!', command= lambda:raise_frame1(f1))
b6.grid(row=9,column=4)

raise_frame2(f1)
mainloop()


