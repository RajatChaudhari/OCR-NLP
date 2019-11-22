def findOrgs(invData):
    doc = nlp(str(invData))
        #matches = matcher(doc)
    tokens=[t.text for t in doc]

    j=[t.i for t in doc if t.text.lower() in ['party:-','to']]
    k=[t.i for t in doc if t.text.lower() in ['particulars','description']]

    if len(j)>0:
        part1=' '.join(tokens[0:j[len(j)-1]])
        doc1=nlp(part1)

        #if len(j)>1:
        #    part2=' '.join(tokens[j[0]:j[1]])
        #    doc2=nlp(part2)
        if len(k)>0:
            part2=' '.join(tokens[j[0]:k[0]])
            doc2=nlp(part2)
        else:
            part2=' '.join(tokens[j[0]:])
            doc2=nlp(part2)
    else:
        part1=' '.join(tokens[0:k[0]])
        doc1=nlp(part1)
        part2=' '.join(tokens[k[0]:])
        doc2=nlp(part2)

    vendor=[]
    company=[]
    for t1 in doc1.sents:
        docv=nlp(t1.text)

        [vendor.append(a.text) for a in docv.ents if a.label_=="ORG"]
        #[print(a.text) for a in docv.ents if a.label_=="ORG"]

    for t2 in doc2.sents:
        docc=nlp(t2.text)
        [company.append(b.text) for b in docc.ents if b.label_=="ORG"]
        #[print(b.text) for b in docc.ents if b.label_=="ORG"]
    