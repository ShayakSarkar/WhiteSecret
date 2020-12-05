import os,sys,math

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

container_filename=sys.argv[1]
secret_message=sys.argv[2]
output_filename=sys.argv[3]

print(container_filename,secret_message,output_filename)

buffer=[0 for i in range(100)]

container_file=open(container_filename,"r")
output_file=open(output_filename,"w")

#bits_per_line is the number of bits of secret message present per line
bits_per_line=int(math.ceil(len(secret_message)*8/get_number_of_lines(container_file)))
print("bits_per_line=",bits_per_line)
bin_message=get_binary(secret_message)
print_bin_message(bin_message)

create_output_file(container_file,output_file,bin_message,bits_per_line)

output_file.close()
container_file.close()
