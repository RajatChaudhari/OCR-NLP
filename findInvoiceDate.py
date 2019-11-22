def findInvDate(inv):
    rulerdoc = nlp(str(inv))
    testlist=([(ent.text, ent.label_, ent.start) for ent in rulerdoc.ents if ent.label_=='INVOICEDATE'])
    for a in testlist:
        index=a[2]
        wordsBefore =[]
        for i in range(1,11):
            wordsBefore.append(str(rulerdoc.__getitem__(index-i)).lower())
            if "invoice" in wordsBefore:
                return rulerdoc.__getitem__(index)
