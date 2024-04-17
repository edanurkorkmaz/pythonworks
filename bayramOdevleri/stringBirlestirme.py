
with open("eda.txt", "w", encoding="utf-8") as file:
    file.write("python cok eglenceli \npython ögrenmek cok zor\npython ogreniyorum.")

first_letters = ""

with open("eda.txt", "r", encoding="utf-8") as file:
   
    content = file.readlines()
    for line in content:
       
        first_letters += line[0]

print(first_letters)
      

