with open("list.txt") as file_list:
#    data_list = file_list.read()

#for row in data_list:
#print(list_name)
#for line in file_list:
#    print(line)
#print(f"occurences of Darth {data_list.count("Darth")}")
#print(f"occurences of Luke {data_list.count("Luke")}")
#print(f"occurences of Lea {data_list.count("Lea")}")
#data_list = data_list[:-1] + " Eliyho"
    new_list = file_list.readlines()
    i = 0
    for row in new_list:
        print(new_list[i])
        i += 1
    print(new_list)
#for row in data_list:
#    if row == "Luke":
#        new_list = data_list.replace("Luke", "SkyWalker Luke")

#print(data_list)
#print(new_list)
file_list.close()
