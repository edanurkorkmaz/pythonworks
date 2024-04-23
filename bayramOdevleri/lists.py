liste = ["345","sadas","324a","14","kemal"]

for string in liste:
    try:
        num = int(string)
        print(string) 
    except ValueError:  
        pass 