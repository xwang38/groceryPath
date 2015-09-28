from bfs import Graph

class ComputePath:

    def __init__(self, mylist, start, end):
        #pass into a list of grocery location (with each element in tuple of x and y coordinates)
        #start: entrance; end: check-out, both in tuple
        self.distance=Graph()
        self.curMin=1000
        self.trackOrder=[]
        self.trackPath=[start]
        self.minPath([start], 0,start,mylist,end, self.trackPath)
        print("test3")
        print("length of path is "+str(self.curMin))
        self.iterateOrder()
        self.distance.paintPath(self.trackPath)
        print("my path is ")
        print(self.trackPath)

        self.start=start
        self.end=end
        self.mylist=mylist

    def minPath(self, trackOrder, curDis, lastPop, mylist, end, trackPath):
        #compute the min BFS path of passing all location in mylist; O(n!)
        if len(mylist)==0:
            curDis+=self.distance.bfs(lastPop,end)
            trackOrder.append(end)
            trackPath.append((self.distance.getItrPath()))
            if (curDis<=self.curMin):
                self.curMin=curDis
                self.trackOrder=trackOrder
                self.trackPath=trackPath
            return
        else:
            for index in range(len(mylist)):
                self.minPath(trackOrder+[mylist[index]], curDis+self.distance.bfs(lastPop, mylist[index]), self.distance.get_lastPop(), mylist[:index]+mylist[index+1:], end, trackPath+self.distance.getItrPath())

    def iterateOrder(self):
        mypath=""
        for ele in self.trackOrder:
            mypath+=str(ele)+" "
        print("order of shopping is: "+mypath)

    def redraw(self,new_row, new_col):
        self.distance.set_graph(new_row,new_col)
        self.curMin=1000
        self.trackOrder=[]
        self.trackPath=[self.start]

        self.minPath([self.start], 0,self.start,self.mylist,self.end, self.trackPath)
        print("length of path is "+str(self.curMin))
        self.iterateOrder()
        self.distance.paintPath(self.trackPath)
        print("my path is ")
        print(self.trackPath)

    def get_para(self):
        return self.distance.get_para()

    def get_trackPath(self):
        return self.trackPath



