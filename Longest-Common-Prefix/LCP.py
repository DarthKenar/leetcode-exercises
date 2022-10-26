strs = ["flrt","flow","flight"]
respuesta = ""
length = (len(strs))
#print(f"{len(strs[0]) =}")
if length == 1:
    print("")
for j in range(0,(len(strs[0]))-1):
    counter = 0
    for i in range(1,length):
        if strs[0][j] == strs[i][j]:
            counter +=1
    if counter == length-1:
        respuesta = respuesta + strs[0][j]
    else:
        print(respuesta)
        break
