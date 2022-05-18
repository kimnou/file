def file_read(file_name):
    with open(file_name,"r")as my_file:
        data=my_file.readlines()
        print(data)
file_read("variable")
