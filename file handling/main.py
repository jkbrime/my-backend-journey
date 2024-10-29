'''
file = open('file handling/edit.txt', 'r')
content = file.read()
print(content)
'''

file = open('file handling/edit.txt','w')
new_text = file.write('i love games\n')
file.close

'''
file = open('file handling/edit.txt', 'r')
content = file.read()
print(content)
file.close()
'''

file = open('file handling/edit.txt','a')
file.write('i also love soccer\n')
file.close()

file = open('file handling/edit.txt','r')
content = file.read()
print(content)
file.close()

#The with statement helps us to automate our 



'''
with open('file handling/text.html','w') as file:
    file.write('i love amala')

with open('file handling/text.html','r') as file:
    reader = file.read()
    print(reader)

with open('file handling/download (1).jpg','rb') as file:
    binary_content = file.read()
    print(binary_content[:20])
    
'''
from PIL import Image
with Image.open("file handling/download (1).jpg") as im:
    im.rotate(0).show()
    

