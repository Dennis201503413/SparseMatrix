
class Node:
    def __init__(self,id):
        self.id = id
        self.up = None
        self.down = None
        self.left = None
        self.right = None

class Matrix:
    def __init__(self):
        self.headers = Node(0)

    def add(self,x,y,value):
        self.add_x_header(x)
        self.add_y_header(y)
        self.insert_node(x,y,value)

    def print_x_headers(self):
        temp = self.headers
        while temp.right != None:
            print(temp.id,end=',')
            temp = temp.right
        print(temp.id)

    def print_y_headers(self):
        temp = self.headers
        while temp.down != None:
            #print(temp.id)
            temp_x = temp
            while temp_x.right!=None:
                print(temp_x.id,end='->')
                temp_x = temp_x.right
            print(temp_x.id)
            temp = temp.down
        temp_x = temp
        while temp_x.right!=None:
            print(temp_x.id,end='->')
            temp_x = temp_x.right
        print(temp_x.id)

    def add_x_header(self,x):
        temp = self.headers
        if temp.right == None:
            new_node = Node(x)
            temp.right = new_node
            new_node.left = temp
        else:
            while (temp.right !=None) and (temp.right.id < x):
                temp = temp.right
            if temp.right==None and temp.id !=x:
                new_node = Node(x)
                temp.right = new_node
                new_node.left = temp
            elif temp.right!=None and temp.right.id !=x:
                #temp = temp.left
                aux = temp.right
                new_node = Node(x)
                temp.right = new_node
                new_node.left = temp
                new_node.right = aux
                aux.left = new_node

    def add_y_header(self,y):
        temp = self.headers
        if temp.down == None:
            new_node = Node(y)
            temp.down = new_node
            new_node.up = temp
        else:
            while (temp.down !=None) and (temp.down.id < y):
                temp = temp.down
            if temp.down==None and temp.id !=y:
                new_node = Node(y)
                temp.down = new_node
                new_node.up = temp
            elif temp.down!=None and temp.down.id !=y:
                #temp = temp.left
                aux = temp.down
                new_node = Node(y)
                temp.down = new_node
                new_node.up = temp
                new_node.down = aux
                aux.up = new_node

    def insert_node(self,x,y,value):
        new_node = Node(value)
        temp_x = self.headers
        temp_y = self.headers
        while temp_x.right!=None:
            temp_x = temp_x.right
            if temp_x.id==x:
                temp_x.down = new_node
                new_node.up = temp_x
        while temp_y.down!=None:
            temp_y = temp_y.down
            if temp_y.id == y:
                temp_y.right = new_node
                new_node.left = temp_y




mat = Matrix()
mat.add(1,4,'value1')
mat.add(2,6,'value2')
mat.add(6,3,'value3')
mat.add(4,1,'value4')
mat.add(7,9,'value5')
mat.add(3,2,'value6')
mat.add(8,10,'value7')
mat.print_x_headers()
mat.print_y_headers()
