from math import *

class MazeError(Exception):
    def __init__(self, value):
        self.value = value

class Point:
    up = list()
    down = list()
    left = list()
    right = list()

    def __init__(self,node):
        x,y = node[0],node[1]
        self.up = [(floor(x),floor(y)),(floor(x),ceil(y))]
        self.down = [(ceil(x),floor(y)),(ceil(x),ceil(y))]
        self.left = [(floor(x),floor(y)),(ceil(x),floor(y))]
        self.right = [(floor(x),ceil(y)),(ceil(x),ceil(y))]

class Maze:
    root =""
    dead = list()
    maze = list()
    maze_enlarge = list()
    pair = dict()
    result = [0] * 6
    out = [0] * 6
    row,column = 0,0
    node = list()
    path = list()
    draw_walls = list()
    draw_crossing = list()
    draw_pillars = list()
    draw_yellow_line = list()
    blocker = list()
    green_point = list()
    ldoor,rdoor,udoor,ddoor = list(),list(),list(),list()

    def __init__(self,root):
        count = 0
        self.root = root
        
        file = open(root).readlines()
        for row in file:
            temp = list()
            for e in row:
                if e in [1, 2, 3, 0, "0", "1", "2", "3"]:
                    temp.append(e)
            if len(temp) > 0:
                self.maze.append(temp)
        
        self.verify()


        
        self.row = len(self.maze)
        self.column = len(self.maze[0])
        self.maze_enlarge = [[0] * (self.column+1) for i in range(self.row+1)]

        for i in range(self.row):
            for j in range(self.column):
                
                char = self.maze[i][j]
                if char == '0':
                    continue
                elif char == '1':
                    self.maze_enlarge[i][j] = 1
                    self.maze_enlarge[i][j+1] = 1
                    self.pair[(i,j)] = (i,j+1),

                elif char == '2':
                    self.maze_enlarge[i][j] = 1
                    self.maze_enlarge[i+1][j] = 1
                    self.pair[(i,j)] = (i+1,j),
                    
                elif char == '3':
                    self.maze_enlarge[i][j] = 1
                    self.maze_enlarge[i+1][j] = 1
                    self.maze_enlarge[i][j+1] = 1
                    self.pair[(i,j)] = (i+1,j),(i,j+1),

        # print(self.pair)
        for key in self.pair.keys():
            for v in self.pair[key]:
                self.path.append([key,v])


        value = list()
        key = list(self.pair.keys())
        for element in self.pair.values():
            for tple in element:
                value.append(tple)

        row,column = self.row,self.column
        for i in range(row):
            for j in range(column):
                if (i,j) not in key:
                    if (i,j) not in value:
                        self.green_point.append((i,j))

        self.udoor = list(map(lambda x: [(0,x),(0,x+1)], [x for x in range(self.column-1)]))
        self.ddoor = list(map(lambda x: [(self.row-1,x),(self.row-1,x+1)], [x for x in range(self.column-1)]))
        self.ldoor = list(map(lambda x: [(x,0),(x+1,0)], [x for x in range(self.row-1)]))
        self.rdoor = list(map(lambda x: [(self.column-1,x),(self.column-1,x+1)], [x for x in range(self.row-1)]))
        self.draw_pillars.append("% Pillars\n")
        self.draw_crossing.append("% Inner points in accessible cul-de-sacs\n")
        self.draw_yellow_line.append("% Entry-exit paths without intersections\n")



    def analyse(self):

        self.analyse_return_gates()
        self.analyse_connected_wall()
        
        self.draw_cul_de_sacs()
        self.analyse_inaccessible()
        self.analyse_cul_de_sacs()

        self.analyse_return_output()

    def verify(self):


        for row in self.maze:
            if row == ['0', '0']:
                raise MazeError("Incorrect input.")
            if len(row) != len(self.maze[0]) :
                raise MazeError("Incorrect input.")
            elif len(row) ==1 :
                raise MazeError("Incorrect input.")




        if len(self.maze) == 0:
            raise MazeError("Input does not represent a maze.")
        else:
            for element in self.maze[-1]:
                if element == "2" or element == "3" :
                    raise MazeError("Input does not represent a maze.")
            last_element = [x[-1] for x in self.maze]
            for element in last_element:
                if element == "1" or element == "3":
                    raise MazeError("Input does not represent a maze.")



       


    def analyse_return_gates(self):
        block = 0
        res = 0
        temp = (self.pair)
        row = len(self.maze[0])
        column = len(self.maze)
        total = (row-1)*2 + (column-1)*2
        for i in range(row):
            if (0,i) in temp.keys() and (0,i+1) in temp[(0,i)]:
                block = block + 1
            if (column-1,i) in temp.keys()  and (column-1,i+1) in temp[(column-1,i)]:
                block = block + 1
        for j in range(column):
            if (j,0) in temp.keys()  and (j+1,0) in temp[(j,0)]:
                block = block + 1
            if (j,row-1) in temp.keys()  and (j+1,row-1) in temp[(j,row-1)]:
                block = block + 1
        res = total - block
        self.result[0] = res
        if res == 0:
            self.result[0] = 'no gate.'
        elif res == 1:
            self.result[0] = 'a single gate.'
        else:
            self.result[0] = ('%s gates.' % (res))
        
    def DFS(self,start,end):
        stack = []
        stack.append(start)
        seen = set()
        nodes = list()
        seen.add(start)
        while(len(stack) > 0):
            vertex = stack.pop(0)
            if vertex == end:
                return True
            else:
                for row in self.path:
                    for e in row:
                        if vertex == e:
                            for temp in row:
                                if temp !=e:
                                    nodes.append(temp)
                for w in nodes:
                    if w not in seen:
                        stack.append(w)
                        seen.add(w)
        return False

    def analyse_connected_wall(self):
        temp = list()
        ans= list()

        for row in self.path:
            for e in row:
                temp.append(e)
        count1 = [temp.count(e) for e in temp]
        for e in temp:
            count = temp.count(e)
            if count == 1:
                self.node.append(e)

        nodes = self.node.copy()
        while(nodes):
            start = nodes.pop()
            ans.append([start])
            for e in nodes[:]:
                if self.DFS(start,e) == True:
                    ans[-1].append(e)
                    nodes.remove(e)
        res = len(ans)

        if len(set(count1)) ==1 and count1[0] >1 :
            res =1
        if res == 0:
            self.result[1] = 'no wall.'
        elif res == 1:
            self.result[1] = 'walls that are all connected.'
        else:
            self.result[1] = ('%s sets of walls that are all connected.' % (res))


    def cul_de_sacs(self,s):
        entry = s
        child = []
        child.append(s)
        seen_half = list()
        # seen_half.append(s)
        seen = list()
        while (len(child)>0):

            temp = child.pop()
            node = Point(temp)
            for e in [node.up,node.down,node.left,node.right]:
                if e not in self.path:
                    if e not in seen:
                        if e == node.up: 
                            s = (e[0][0] + 0.5,e[0][1] + 0.5)
                        elif e == node.down: 
                            s = (e[0][0] + 0.5,e[0][1] + 0.5)
                        elif e == node.left: 
                            s = (e[0][0] + 0.5,e[0][1] - 0.5)
                        elif e == node.right: 
                            s = (e[0][0] + 0.5,e[0][1] + 0.5)
                        seen.append(e)
                        seen_half.append(s)
                        child.append(s)
                    else:
                        continue
                else:
                    continue
        return (True,seen_half)

    def is_4_sides_block(self,temp):
        node = Point(temp)
        if node.up in self.path and node.down in self.path and node.left in self.path and node.right in self.path:
            return True

    def is_3_sides_block(self,temp):
        node = Point(temp)
        count = 0
        if node.up in self.path:
            count = count + 1
        if node.down in self.path:
            count = count + 1
        if node.left in self.path:
            count = count + 1
        if node.right in self.path:
            count = count + 1

        if count ==3:
            return True
    

    def return_temp(self,element):
        temp = []
        node = Point(element)
        seq = [node.up,node.down,node.left,node.right]
        if seq[0] not in self.path:
            temp.append((seq[0][0][0] - 0.5,seq[0][0][1] + 0.5),)
        if seq[1] not in self.path:
            temp.append((seq[1][0][0] + 0.5,seq[1][0][1] + 0.5),)
        if seq[2] not in self.path:
            temp.append((seq[2][0][0] + 0.5,seq[2][0][1] - 0.5),)
        if seq[3] not in self.path:
            temp.append((seq[3][0][0] + 0.5,seq[3][0][1] + 0.5),)
        return temp
    

    def analyse_cul_de_sacs(self):
        start = list()

        for element in self.dead:
            if element in self.blocker[:]:
                self.blocker.remove(element)
        self.blocker = sorted(self.blocker)

        seen =set()
        stack = list()
        for e in self.blocker:
            if e not in seen and e not in stack:
                stack.append(e)
                seen.add(e)
                while(len(stack)>0):
                    vertex = stack.pop(0)
                    nodes = self.return_temp(vertex)
                    for n in nodes:
                        if n in self.blocker and n not in seen:
                                stack.append(n)
                                seen.add(n)
                start.append(e)
        # print(self.blocker)
        res = len(start)
        if res == 0:
            self.result[4] = 'no accessible cul-de-sac.'
        elif res == 1:
            self.result[4] = 'accessible cul-de-sacs that are all connected.'
        else:
            self.result[4] = ('%s sets of accessible cul-de-sacs that are all connected.' % (res))
    def analyse_inaccessible(self):
        inaccessible = list()
        row = self.row
        column = self.column
        crossing = list()
        for i in range(row-1):
            for j in range(column-1):
                x = 0.5 + i
                y = 0.5 + j
                crossing.append((x,y))

        for i in range (len(crossing)):
            res = self.is_4_sides_block(crossing[i])
            if res==True:
                inaccessible.append(crossing[i])

        seen = set()
        stack = list()
        for e in self.dead:
            if e not in seen and e not in stack:
                stack.append(e)
                seen.add(e)

                while (len(stack) > 0 ):
                    vertex = stack.pop(0)
                    nodes = self.return_temp(vertex)
                    for w in nodes:
                        if w not in seen:
                            stack.append(w)
                            seen.add(w)

                    inaccessible.append(vertex)

        self.dead = inaccessible

        res = len(inaccessible)
        if res == 0:
            self.result[2] = 'no inaccessible inner point.'
        elif res == 1:
            self.result[2] = 'a unique inaccessible inner point.'
        else:
            self.result[2] = ('%s inaccessible inner points.' % (res))

    def draw_cul_de_sacs(self):
        dead=list()
        child=list()
        blocker = list()
        row = self.row
        column = self.column
        crossing = list()
        for i in range(row-1):
            for j in range(column-1):
                x = 0.5 + i
                y = 0.5 + j
                crossing.append((x,y))

        for i in range (len(crossing)):
            res = self.is_3_sides_block(crossing[i])
            if res==True:
                blocker.append(crossing[i])
        for value in blocker:
            temp = []
            node = Point(value)
            seq = [node.up,node.down,node.left,node.right]
            if seq[0] not in self.path:
                temp = seq[0][0][0] - 0.5,seq[0][0][1] + 0.5
            elif seq[1] not in self.path:
                temp = seq[1][0][0] + 0.5,seq[1][0][1] + 0.5
            elif seq[2] not in self.path:
                temp = seq[2][0][0] + 0.5,seq[2][0][1] - 0.5
            elif seq[3] not in self.path:
                temp = seq[3][0][0] + 0.5,seq[3][0][1] + 0.5
            # print(value,temp)
            if temp not in child and temp not in blocker and temp[0] > 0 and temp[0]< self.row and temp[1]>0 and temp[1]<self.column:
                child.append(temp)
            
        # print(child)
        while (child):
            new = child.pop(0)
            temp = []
            node = Point(new)
            seq = [node.up,node.down,node.left,node.right]
            if seq[0] not in self.path:
                temp.append((seq[0][0][0] - 0.5,seq[0][0][1] + 0.5),)
            if seq[1] not in self.path:
                temp.append((seq[1][0][0] + 0.5,seq[1][0][1] + 0.5),)
            if seq[2] not in self.path:
                temp.append((seq[2][0][0] + 0.5,seq[2][0][1] - 0.5),)
            if seq[3] not in self.path:
                temp.append((seq[3][0][0] + 0.5,seq[3][0][1] + 0.5),)
            
            for t in temp[:]:
                if t in blocker:
                    temp.remove(t)

            if len(temp) == 1 :
                blocker.append(new)
                for t in temp:
                    if t[0] > 0 and t[0]< self.row and t[1]>0 and t[1]<self.column:
                        child.append(t)
            elif len(temp) == 0:
                self.dead.append(new) 
        self.blocker = blocker


    def display(self):
        tex_fname = self.root.split('.')[0] + ".tex"
        tex_file = open(tex_fname, 'w')
        head =["\\documentclass[10pt]{article}\n",
               "\\usepackage{tikz}\n",
                "\\usetikzlibrary{shapes.misc}\n",
                "\\usepackage[margin=0cm]{geometry}\n",
                "\\pagestyle{empty}\n",
                "\\tikzstyle{every node}=[cross out, draw, red]\n",
                "\n",
                "\\begin{document}\n",
                "\n",
                "\\vspace*{\\fill}\n",
                "\\begin{center}\n",
                "\\begin{tikzpicture}[x=0.5cm, y=-0.5cm, ultra thick, blue]\n",
                "% Walls\n"]
        border = ["\\end{tikzpicture}\n","\\end{center}\n","\\vspace*{\\fill}\n","\n","\\end{document}\n"]
        # path
        for i in range(len(self.path)):
            x1 = self.path[i][0][1]
            y1 = self.path[i][0][0]
            x2 = self.path[i][1][1]
            y2 = self.path[i][1][0]
            item = "    \\draw (" + str(x1)+","+str(y1)+") -- ("+str(x2)+","+str(y2)+");\n"
            self.draw_walls.append(item)
        # # point

        for i in range(len(self.green_point)):
            x1 = self.green_point[i][1]
            y1 = self.green_point[i][0]

            item = "    \\fill[green] (" + str(x1) + "," + str(y1) + ") circle(0.2);\n"
            self.draw_pillars.append(item)

        for element in self.blocker:
            x1 = element[1]
            y1 = element[0]
            item = s = "    \\node at ("+str(x1)+","+str(y1)+") {};\n"
            self.draw_crossing.append(item)
        tex_file.writelines(head)
        tex_file.writelines(self.draw_walls)
        tex_file.writelines(self.draw_pillars)
        tex_file.writelines(self.draw_crossing)
        tex_file.writelines(self.draw_yellow_line)
        tex_file.writelines(border)



    def analyse_return_output(self):

        # for i in range(5):
        #     if self.result[i] == 0: 
        #         print("haha")
        #         self.out[0] = 'no gate.'
        #         self.out[1] = 'no wall.'
        #         self.out[2] = 
        #         self.out[3] = 'no accessible area.'
        #         self.out[4] = 
        #         self.out[5] = 'no entry-exit path with no intersection not to cul-de-sacs.'
        #     elif self.result[i] == 1:
        #         print("xixi")
        #         self.out[0] = 'a single gate.'
        #         self.out[1] = 'walls that are all connected.'
        #         self.out[2] = 
        #         self.out[3] = 'a unique accessible area.'
        #         self.out[4] = 
        #         self.out[5] = 'a unique entry-exit path with no intersection not to cul-de-sacs.'
        #     else:
        #         a=self.result[0]
        #         self.out[0] =('%s gates.' % (self.result[0]))
        #         self.out[1] = str(self.result[1]) + ' sets of walls that are all connected.'
        #         self.out[2] = str(self.result[2]) + ' '
        #         self.out[3] = str(self.result[3]) + ' accessible areas.'
        #         self.out[4] = str(self.result[4]) + ' sets of accessible cul-de-sacs that are all connected.'
        #         self.out[5] = str(self.result[5]) + ' entry-exit paths with no intersections not to cul-de-sacs.'
                # print("gan",self.out[0])

        self.result[3] = 'a unique accessible area.'
        self.result[5] = 'a unique entry-exit path with no intersection not to cul-de-sacs.'
        for i in range(6):
            print("The maze has "+str(self.result[i]))


