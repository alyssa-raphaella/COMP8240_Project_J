## for windows os ## 

# extracts filename in the current dictory and append to file_list.txt
dir /b /a-d >> file_list.txt

# convert each wav file listed in file_list.txt into flac of 16bits (speech-to-text requirement)
FOR /F "tokens=*" %%A IN (file_list.txt) DO sox %%A --rate 16k --bits 16 --channels 1 flac/%%A.flac