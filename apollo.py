##dlqvsluhgCeACpACexwlixoC<CvpduwC<CdpdBlqjCdqgCdvwrxqglqjCOlBBA>
##ddqgCeACwkhCidwkhuCriCwkhCfrpsxwhuCdCzdukhurCdqgCdCirujrwwhqCjrgC<CDoohqCPCWxuulqj
while 1 == 1:
    hamilton = ''
    print("input:")
    hamilton = input()
    print("code:")
    burr = int(input())
    code = [x for x in hamilton]
    code.insert(0, "_")
    out = []
    outside = ''
    trip = True
    negitive = True
    key = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", ",", ".", "/", "<", ">", "?", ";", ":", '"', "'", "[", "]", "{", "}", "|", "-", "_", "=", "+"]
    if(burr < 0):
        burr = burr * -1
        key = key[::-1]
        ##print(key)
        for a in range(len(code)):
            for i in range(len(key)):
                if code[a] == key[i]:
                    c = i + burr
                    while (c >= len(key)):
                        c = 0 + burr
                        if (burr >= len(key)):
                            burr = burr / len(key)
                            burr = round(burr)
                    ## print("thinking" + str(c))
                    out.extend(key[c])
                    c = 0
                i = i + 1
            a = a + 1
        for q in range(len(out)):
            outside = outside + out[q]
            q = q + 1
        print(outside[2:])
        negitive = False
    if(burr > 0 and negitive == True):
        for a in range(len(code)):
            for i in range(len(key)):
                if code[a] == key[i]:
                    c = i + burr
                    while(c >= len(key)):
                        c = 0 + burr
                        if (burr >= len(key)):
                            burr = burr / len(key)
                            burr = round(burr)
                    ##print("thinking" + str(c))
                    out.extend(key[c])
                    c = 0
                i = i + 1
            a = a + 1
        for q in range(len(out)):
            outside = outside + out[q]
            q = q + 1
        print(outside)