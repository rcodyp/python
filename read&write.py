#to read files
count_files = open("C:/ITS CODING/Python/countries.txt","r")
print(count_files.readable())
print(count_files.readlines()[0])
count_files.close()

#to write files
cout= open("C:/ITS CODING/Python/newfile.txt","w")
print(cout.readable())
cout.write('this is new file')

#to add text in files
cout= open("C:/ITS CODING/Python/newfile.txt","a")
cout.write('\nthis is more new line')

