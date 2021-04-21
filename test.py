from requests import get
from bs4 import BeautifulSoup as bs

one="merhaba:7\nmerhaba nasılsın:6\n"
one=one.replace("\n",":")
one=one.split(":")
i=0
while i<len(one):
    j=i+2
    l=one[i]
    while j<len(one)-1:
        m=one[j]
        if m.find(l)>-1:
            one[i+1] = str(int(one[i+1])-int(one[j+1]))
        j+=2
    i+=2
kelime=""
i=0
while i<len(one)-1:
    kelime+=one[i]
    if int(one[i+1])<0:
        kelime += ":0\n"
    else:
        kelime += f":{one[i+1]}\n"
    i+=2
print(kelime)



# girdi="merhaba,merhaba nasılsın,merhaba gençlik"
# girdi=girdi.split(",")
# girdi.sort(reverse=True)
# for i in girdi:
#     if kelime.find(i)>0:
#         count=kelime.find(i)
#         kelime=kelime.replace(girdi[1],"",count)
# print(kelime)




