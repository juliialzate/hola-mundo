pintas = ["picas", "treboles", "diamanes", "corazones"]
valores = [ "A", "J", "Q", "K"] + [str(i) for i in range (2,11)]
mazo = [(u,p) for u in valores for p in pintas] + [str(i) for i in range (2,11)] 
for c in mazo: 
    print (c)

