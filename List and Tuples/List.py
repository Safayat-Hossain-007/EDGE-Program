myList = ["Apple","Banana","Orange"];
text = "lorem ipsum and blah blah";
for i in text[:5]:
    print(i)

#removing the whitespaces
removedWhiteSpaceText = text.split(" ");
for i in removedWhiteSpaceText:
    print(i)


for i in text:
    print(i.upper());