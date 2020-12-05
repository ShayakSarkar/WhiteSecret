def get_binary(msg):
    buffer=""
    for char in msg:
        bin_rep=bin(ord(char))[2:]
        bin_rep="0"*(8-len(bin_rep))+bin_rep
        buffer+=bin_rep
    return buffer

def get_number_of_lines(file):
    count=-1
    buffer=" "
    while(buffer!=""):
        count+=1
        buffer=file.readline()
    file.seek(0,0)
    return count

def create_output_file(container_file,output_file,bin_msg,bits_per_line):
    current_index=0
    print('creating output file')
    while(current_index<len(bin_msg)):
        line=container_file.readline()
        line=line.strip()
        for i in range(bits_per_line):
            if((current_index+i)>=len(bin_msg)):
                break
            char=bin_msg[current_index+i]
            #print(char,end="")
            if(char=='0'):
                line+=" "
            else:
                line+="\t"
        current_index+=bits_per_line
        output_file.writelines([line,'\n'])
        #print()
    
    line=container_file.readline()
    while(line!=""):
        output_file.writelines([line.strip(),'\n'])
        line=container_file.readline()

def print_bin_message(msg):
    temp=[msg[i*8:i*8+8] for i in range(len(msg)//8)]
    for block in temp:
        print(block,end=" ")
    print()

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

def convert_to_plaintext(buffer):
    #print('length of buffer',len(buffer))
    buffer=[buffer[i*8:i*8+8] for i in range(len(buffer)//8)] 
    msg=""
    for block in buffer:
        msg+=chr(int(block,2))
        #print("appended",msg[-1])
    return msg
