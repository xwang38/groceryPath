row=40
col=40

class Vertex:
    def __init__(self,x_pos, y_pos, element):
        self.xPos=x_pos
        self.yPos=y_pos
        self.element=element
        self.visited=False

    def get_element(self):
        return self.element

    def set_element(self, element):
        self.element=element

    def get_pos(self):
        return self.xPos, self.yPos

    def getVisited(self):
        return self.visited

    def setVisited(self):
        self.visited=True

    def setUnvisited(self):
        self.visited=False

class Graph:
    def __init__(self):
        self.makeGraph()

    def set_graph(self,new_row, new_col):
        global row,col
        row=new_row
        col=new_col
        self.makeGraph()

    def makeGraph(self):
        #new row or col has to be divisible by 10
        global row, col
        self.graph=[[] for i in range(row)]
        for i in range(int(row/10)):
            for j in range(col):
                self.graph[i].append(Vertex(i,j,'|'))
        for i in range(int(4*row/10),int(5*row/10)):
            for j in range(col):
                self.graph[i].append(Vertex(i,j,'|'))
        for i in range(int(8*row/10),row):
            for j in range(col):
                self.graph[i].append(Vertex(i,j,'|'))
        for i in range(int(row/10),int(4*row/10)):
            for j in range(col):
                if j in [0,int((col-1)/3),int((2*col-2)/3), col-1]:
                    self.graph[i].append(Vertex(i,j,'o'))
                else:
                    self.graph[i].append(Vertex(i,j,'|'))
        for i in range(int(row/2),int(8*row/10)):
            for j in range(col):
                if j in [0,int((col-1)/3),int((2*col-2)/3), col-1]:
                    self.graph[i].append(Vertex(i,j,'o'))
                else:
                    self.graph[i].append(Vertex(i,j,'|'))


    def bfs(self, start, end):
        self.restoreUnvisited()
        #compute the BFS path from start to end; start and end should be tuple of x and y coordinate
        start=self.interpolate(start)
        end=self.interpolate(end)
        parent={}
        queue=[]
        queue.append(start)
        start.setVisited()
        self.last=end
        while (queue):
            curV=queue.pop(0)
            for eleV in self.adjacent(curV):
                if eleV.get_pos()==end.get_pos():
                    parent[eleV]=curV
                    self.travelPath=list(self.getPath(parent, start, end))
                    self.itr_path()
                    if eleV.get_element()=='o':
                        self.last=curV
                    return self.path_length
                if eleV.getVisited()==False and eleV.get_element()=='|':
                    parent[eleV]=curV
                    queue.append(eleV)
                    eleV.setVisited()
    def get_lastPop(self):
        return self.last.get_pos()

    def getPath(self, parent, start, end):
        path=[end]
        while path[-1].get_pos()!=start.get_pos():
            #print("current "+str(path[-1].get_pos()))
            path.append(parent[path[-1]])
        return reversed(path)

    def adjacent(self, myVertex):
        # adjacent nodes is vertex that is above, left, right or below myVertex
        if myVertex.get_element==0:
            return
        x,y=myVertex.get_pos()
        neighbors=[]
        if self.inside(x-1,y):
            neighbors.append(self.graph[x-1][y])
        if self.inside(x+1,y):
            neighbors.append(self.graph[x+1][y])
        if self.inside(x,y-1):
            neighbors.append(self.graph[x][y-1])
        if self.inside(x,y+1):
            neighbors.append(self.graph[x][y+1])
        return neighbors


    def inside(self, x, y):
        #if this vertex is within map
        global row, col
        if x>=0 and x<=row-1 and y>=0 and y<=col-1:
            return True
        return False

    def iterate(self):
        #printout the map
        global row, col
        for i in range(row):
            myLine=""
            for j in range(col):
                myLine+=str(self.graph[i][j].get_element())+'\t'
            print(myLine)

    def itr_path(self):
        self.path_length=-1
        tmp=[]
        for location in self.travelPath:
            tmp.append(location.get_pos())
            self.path_length+=1


    def getItrPath(self):
        path=[]
        for location in self.travelPath[1:]:
            path.append(location.get_pos())
        return path

    def interpolate(self,mytuple):
        tmp=list(mytuple)
        return self.graph[tmp[0]][tmp[1]]

    def restoreUnvisited(self):
        for i in self.graph:
            for j in i:
                j.setUnvisited()

    def paintPath(self, mylist):
        #mylist contains points that you need pass;
        for ele in mylist:
            if (isinstance(ele,tuple)):
                    self.interpolate(ele).set_element('*')
            else:
                for i in ele:
                    if (isinstance(i,tuple)):
                        self.interpolate(i).set_element('*')
        self.iterate()

    def get_para(self):
        global row, col
        return row,col