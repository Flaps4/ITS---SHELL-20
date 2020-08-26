import os

path =  'C:\\Users\\Felix af Jochnick\\Desktop\\Python skola\\test'

filer = []
for root, dirs, files in os.walk(path):
    for name in files:
        if ".txt" in name:
            filer.append(os.path.join(root, name))

for files in filer:

    print(f"Fil: {files}" , f"Storlek på denna fil är: {os.path.getsize(files)} bytes")
