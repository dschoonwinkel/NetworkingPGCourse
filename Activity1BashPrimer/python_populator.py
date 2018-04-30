import time

file1 = open("some_text.txt", 'w')
file1.close()

write_count = 0
while(True):
    file1 = open("some_text.txt", 'a')
    print("Writing to std_out %d" % write_count)
    file1.write("Writing to file %d \n" % write_count)
    write_count += 1
    time.sleep(3)
    file1.close()

