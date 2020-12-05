import os,sys,math
import util

container_filename=sys.argv[1]
secret_message=sys.argv[2]
output_filename=sys.argv[3]

print(container_filename,secret_message,output_filename)

buffer=[0 for i in range(100)]

container_file=open(container_filename,"r")
output_file=open(output_filename,"w")

#bits_per_line is the number of bits of secret message present per line
bits_per_line=int(math.ceil(len(secret_message)*8/util.get_number_of_lines(container_file)))
print("bits_per_line=",bits_per_line)
bin_message=util.get_binary(secret_message)
util.print_bin_message(bin_message)

util.create_output_file(container_file,output_file,bin_message,bits_per_line)

output_file.close()
container_file.close()
