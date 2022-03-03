
# By Kisothan Suthakaran
# TASK : VERIFY IF THE FOUR GIVEN VERTICES FORM A PARALLELOGRAM OR NOT 

def is_parallelogram(lst):
    lst=[(0,0),(1,1),(1,4),(0,3)]
    magnlst=[]
    list_=[]
    single=[]
    big_list_=[]
    for point1 in lst:
        big_list_.append(single)
        single=[]
        for point2 in lst:
            if point1!=point2:
                x=point2[0]-point1[0]
                y=point2[1]-point1[1]
                list_=[x,y]
                single.append(list_)
    big_list_.remove(big_list_[0])
    angle_list=[]
    for part in big_list_:
        for vector1 in part:
            for vector2 in part:
                if vector1!=vector2:
                    vect1=np.array(vector1)
                    vect2=np.array(vector2)
                    dot=np.dot(vect1,vect2)
                    cosangle=dot/(((vect2[0]**2+vect2[1]**2)**(1/2))*((vect1[0]**2+vect1[1]**2)**(1/2)))
                    angle=np.arccos(cosangle)
                    angle_list.append(angle)
    list1=[]
    for angle in set(angle_list):
        if round(angle,4)==round(((math.pi*2-((max(angle_list))*2))/2),4):
            list1.append(angle)
            list1.append(max(angle_list))
        
    if len(list1)==2 or (len(list1)==1 and list1[0]==np.pi/2) :
        return True
    else:
        return False
    

        
                
    
     
                
                
                
        
         
            




      
