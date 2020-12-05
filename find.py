import os,sys

def convert_to_plaintext(buffer):
    #print('length of buffer',len(buffer))
    buffer=[buffer[i*8:i*8+8] for i in range(len(buffer)//8)] 
    msg=""
    for block in buffer:
        msg+=chr(int(block,2))
        #print("appended",msg[-1])
    return msg

def find_secret_message(file):
    #print('finding secret message')
    line=file.readline()
    #print(len(line))
    buffer=""
    line_number=1
    while(line!=""):
        #print(len(line))
        #print('line number',line_number)
        line_number+=1
        #print("line is ",line)
        i=-2
        temp=""
        while(i>=-len(line) and (line[i]==' ' or line[i]=='\t')):
            #print('character is',line[i])
            if(line[i]=='\t'):
                #print("1")
                temp="1"+temp
            else:
                #print("0")
                temp="0"+temp
            i-=1

        buffer+=temp
        line=file.readline()
        #print("temp",temp)
        #input()

    msg=convert_to_plaintext(buffer)        
    return msg

filename=sys.argv[1]
#print(filename)
file=open(filename,"r")

msg=find_secret_message(file)
print(msg)