import csv,time

def findmin(row,searchindex):
    m = row[searchindex[0]]
    index = searchindex[0]
    for i in searchindex:
        if row[i] < m:
            m = row[i]
            index = i
    return [m,index]

time.clock()    
network = []
with open('network.txt','rb') as f:
    reader = csv.reader(f)
    for row in reader:
        for i in range(len(row)):
            if row[i] == '-':
                row[i] = 'n/a'
            else:
                row[i] = int(row[i])
        network.append(row)
originalsum = 0
for row in network:
    for e in row:
        if type(e)==int:
            originalsum += e
originalsum /= 2
print originalsum


searchindex = range(1,len(network))
indices = [0]
mst = []
while len(searchindex) != 0:
    c = []
    index = []
    for i in indices:
        mi = findmin(network[i],searchindex)
        c.append(mi[0])
        index.append(mi[1])
    mc = min(c)
    mci = index[c.index(mc)]
    mst.append(mc)
    searchindex.remove(mci)
    indices.append(mci)

ans = sum(mst)
print originalsum-ans
print str(time.clock()*1000)+'ms'

    
    
        
    

    
    
    




            

            
