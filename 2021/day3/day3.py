#parte 1-------------------------
# grate = ""
# erate = ""
# counter = 0
# with open("input3.txt","r") as f:
#     number = f.readlines()
#     for i in range(len(number[0])-1):
#         for  lines in number:
#             if lines[i] == '0' : counter-=1 
#             else: counter+= 1
#         if counter > 0:
#             grate+='1'
#             erate+='0'
#         else:
#             grate+='0'
#             erate+='1'
#         counter = 0
# f.close()
# print(int(erate,base=2)*int(grate, base=2)) 

#parte2-----------------------------------------
orate = []
crate = []
counter = 0
with open("input3.txt","r") as f:
    number = f.readlines()
    orate = number
    crate = number
    for i in range(len(orate[0])-1):
        if(len(orate)==1):break
        for  lines in orate:
            if lines[i] == '0' : counter-=1 
            else: counter+= 1
        if counter>=0:
            orate=[e for e in orate if e[i]=='1']
        else:
            orate=[e for e in orate if e[i]=='0']
        counter=0
    for i in range(len(crate[0])-1):
        if(len(crate)==1):break
        for  lines in crate:
            if lines[i] == '0' : counter-=1 
            else: counter+= 1
        if counter<0:
            crate=[e for e in crate if e[i]=='1']
        else:
            crate=[e for e in crate if e[i]=='0']
        counter=0
    print(orate)
    print(crate)
print(int(crate[0],base=2)*int(orate[0], base=2)) 