def getCurrency(invText):
    doc=nlp(str(invText))
    inr=['Rs.','Rupees','INR','Rs']
    usd=['Dollar','Dollars','USD']
    aud=['AUD']
    gbp=['GBP']
    curr={}
    val=''
    curr["INR"]=len([x.text for x in doc if x.text in inr])
    curr["USD"]=len([x.text for x in doc if x.text in usd])
    curr["AUD"]=len([x.text for x in doc if x.text in aud])
    curr["GBP"]=len([x.text for x in doc if x.text in gbp])
    maximum =max(curr, key=curr.get)
    #print(maximum)
    #print('\n')
    return maximum