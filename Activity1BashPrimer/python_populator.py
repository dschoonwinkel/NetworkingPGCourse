import time

file1 = open("some_text.txt", 'w')
file1.close()

write_count = 0
while(True):
    file1 = open("some_text.txt", 'a')
    file1.write("Writing to file %d \n" % write_count)
    write_count += 1
    time.sleep(1)
    file1.close()

