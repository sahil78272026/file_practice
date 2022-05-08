with open("D:\\Python\\Python Course with Notes\\4. Chapter 4\\grades.txt",'r') as f:
    all_data = f.read() 
    lst = all_data.splitlines()
 #   print(lst)
    for i in range(1,len(lst)):
        new_list = lst[i].split()
        print(new_list)
        marks = 0
        for i in new_list:
            marks = marks + int(i)
        print(marks/len(new_list))    
    
    



    
    