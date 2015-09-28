import tkinter
from ComputePath import ComputePath

row=40
col=40
length=400
length_out=480

class Draw():
    def __init__(self):
        global length_out
        self.mylist=[]

        root=tkinter.Tk()
        root.title("grocery shopping path")
        self.canvas=tkinter.Canvas(root,bg="white",height=length_out, width=length_out)
        self.canvas.pack()
        self.draw_layout()
        self.draw_Pic()
        doneButton=tkinter.Button(root,text="Done with choosing", fg="black")
        doneButton.pack(side='top')
        doneButton.bind('<ButtonPress-1>',self.onClickDone)
        root.mainloop()

    def draw_layout(self):
        global row,col
        y1=int(row/10)
        y2=int(4*row/10)-1
        y3=int(row/2)
        y4=int(8*row/10)-1
        for x in [0,int((col-1)/3),int((2*col-2)/3), col-1]:
            self.draw_aisle((x,y1),(x,y2),'SkyBlue1')
            self.draw_aisle((x,y3),(x,y4),'SkyBlue1')

    def interpolate(self,xpos,ypos):
        #convert x,y coordinates into tkinter positioning
        global row, col, length
        return xpos*length/(col-1)+30, ypos*length/(row-1)+20

    def interpolate_reverse(self,x,y):
        #convert tkinter positioning into x,y coordinates
        global row, col, length
        return min(int((x-30)*(col-1)/length),col-1),min(int((y-20)*(row-1)/length),row-1)

    def draw_aisle(self,tuple1, tuple2, mycolor):
        #given x,y coordinates and draw aisle on canvas
        cord1=self.interpolate(tuple1[0],tuple1[1])
        cord2=self.interpolate(tuple2[0],tuple2[1])
        tmp=self.canvas.create_line(cord1[0],cord1[1],cord2[0],cord2[1],width=20, fill=mycolor)
        self.canvas.tag_bind(tmp,'<ButtonPress-1>',self.onClick)

    def draw_line(self,tuple1, tuple2, mycolor):
        #given x,y coordinates and draw line on canvas (no on-click listener)
        cord1=self.interpolate(tuple1[0],tuple1[1])
        cord2=self.interpolate(tuple2[0],tuple2[1])
        tmp=self.canvas.create_line(cord1[0],cord1[1],cord2[0],cord2[1],width=5, fill=mycolor)


    def onClick(self,event):
        #prompt for user input of grocery location
        print('Got object click')
        self.canvas.create_line(event.x,event.y-4,event.x,event.y+4,width=10,fill='plum1')
        self.mylist.append(self.reverse(self.interpolate_reverse(event.x,event.y)))
        print(self.interpolate_reverse(event.x,event.y))

    def onClickDone(self,event):
        #respond when user are done with choosing location; Compute shortest path
        self.init_graph(self.mylist)

    def init_graph(self,mylist):
        global row, col
        start=self.reverse((col-1,row-1))
        end=self.reverse((0,row-1))
        self.graph=ComputePath(mylist, start, end)
        track_path=self.graph.get_trackPath()
        self.draw_path(track_path)

    def reverse(self,mytuple):
        #(x,y) here == (y,x) in ComputePath
        return mytuple[1],mytuple[0]

    def draw_path(self, path):
        path_list=[]
        for ele in path:
            if isinstance(ele,tuple):
                path_list.append(self.reverse(ele))
            else:
                for ele2 in ele:
                    if isinstance(ele2,tuple):
                        path_list.append(self.reverse(ele2))
        i=0
        while (i<len(path_list)-1):
            self.draw_line(path_list[i],path_list[i+1],'pink1')
            i+=1

    def draw_Pic(self):
        global row, col
        self.pic1=(tkinter.PhotoImage(file='tool-frypan.gif'))
        tmp=self.interpolate(0,int(row/10))
        self.canvas.create_image(tmp[0],tmp[1]-32, image=self.pic1)
        self.pic2=(tkinter.PhotoImage(file='wine.gif'))
        tmp=self.interpolate(int((col-1)/3),int(row/10))
        self.canvas.create_image(tmp[0],tmp[1]-32, image=self.pic2)
        self.pic3=(tkinter.PhotoImage(file='milk.gif'))
        tmp=self.interpolate(int((2*col-2)/3),int(row/10))
        self.canvas.create_image(tmp[0],tmp[1]-32, image=self.pic3)
        self.pic4=(tkinter.PhotoImage(file='vegg.gif'))
        tmp=self.interpolate(int(col-1),int(row/10))
        self.canvas.create_image(tmp[0],tmp[1]-32, image=self.pic4)
        self.pic5=(tkinter.PhotoImage(file='mis.gif'))
        tmp=self.interpolate(0,int(row/2))
        self.canvas.create_image(tmp[0],tmp[1]-32, image=self.pic5)
        self.pic6=(tkinter.PhotoImage(file='cake.gif'))
        tmp=self.interpolate(int((col-1)/3),int(row/2))
        self.canvas.create_image(tmp[0],tmp[1]-32, image=self.pic6)
        self.pic7=(tkinter.PhotoImage(file='ice_cream.gif'))
        tmp=self.interpolate(int((2*col-2)/3),int(row/2))
        self.canvas.create_image(tmp[0],tmp[1]-32, image=self.pic7)
        self.pic8=(tkinter.PhotoImage(file='meat.gif'))
        tmp=self.interpolate(int(col-1),int(row/2))
        self.canvas.create_image(tmp[0],tmp[1]-32, image=self.pic8)

        self.picStart=(tkinter.PhotoImage(file='dor.gif'))
        tmp=self.interpolate(col-1,row-1)
        self.canvas.create_image(tmp[0],tmp[1]+5, image=self.picStart)
        self.picEnd=(tkinter.PhotoImage(file='dollar-sign.gif'))
        tmp=self.interpolate(0,row-1)
        self.canvas.create_image(tmp[0],tmp[1]+5, image=self.picEnd)








