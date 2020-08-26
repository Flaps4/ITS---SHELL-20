name = "c:\hej\test\hello.txt"
position = name.index("\\", 3)
print("A: ", position)
print("B: ", name[position + 1:len(name)])
if "hej" in name:
    print("C: JA")
