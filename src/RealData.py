from math import floor
from math import cos
from math import acos

def readInstance(filepath):
    file = open(filepath)
    
    d = 0
    matriz = []
    
    ewt = ""

    while(True):
        line = file.readline()
        if(line.startswith("DIMENSION")):
            line = line.split()
            d = int(line[-1])
            break

    while(True):
        line = file.readline()
        if(line.startswith("EDGE_WEIGHT_TYPE")):
            line = line.split()
            ewt = line[-1]
            break

    if(ewt == "EXPLICIT"):
        ewf = ""
        while(True):
            line = file.readline()
            if(line.startswith("EDGE_WEIGHT_FORMAT")):
                line = line.split()
                ewf = line[-1]
                break
        
        while(not file.readline().startswith("EDGE_WEIGHT_SECTION")):
            continue
        
        if(ewf ==  "FULL_MATRIX"):
            for i in range(d):
               matriz.append(list(map(int,file.readline().split())))
               
        elif(ewf == "UPPER_ROW"):
            buffer = []
            line = file.readline()
            while(not (line.startswith("DISPLAY_DATA_SECTION") or line.startswith("EOF"))):
                buffer.extend([int(i) for i in line.split()])
                line = file.readline()
            
            for i in range(d):
                matriz.insert(0, d*[0])

            for i in range(d):
                for j in range(i+1,d):            
                    matriz[i][j] = buffer.pop(0)
                    matriz[j][i] = matriz[i][j]

        #elif(ewf == "LOWER_ROW"):
        
        #elif(ewf == "UPPER_DIAG_ROW"):

        elif(ewf == "LOWER_DIAG_ROW"):
            buffer = []
            line = file.readline()
            while(not (line.startswith("DISPLAY_DATA_SECTION") or line.startswith("EOF"))):
                buffer.extend([int(i) for i in line.split()])
                line = file.readline()
            
            for i in range(d):
                matriz.insert(0, d*[0])

            for i in range(d):
                for j in range(i+1):            
                    matriz[i][j] = buffer.pop(0)
                    matriz[j][i] = matriz[i][j]

        #elif(ewf == "UPPER_COL"):
        #elif(ewf == "LOWER_COL"):
        #elif(ewf == "UPPER_DIAG_COL"):
        #elif(ewf == "LOWER_DIAG_COL"):

    elif(ewt == "EUC_2D"):
        while(not file.readline().startswith("NODE_COORD_SECTION")):
            continue
        
        coords = []
        for i in range(d):
            line = file.readline().split()
            coords.append( (float(line[1]), float(line[2])) )
        
        for i in range(d):
            line = []
            for j in range(d):
                line.append(distEuc(coords[i],coords[j]))
            matriz.append(line)

    elif(ewt == "GEO"):
        while(not file.readline().startswith("NODE_COORD_SECTION")):
            continue
        
        coords = []
        for i in range(d):
            line = file.readline().split()
            coords.append( (float(line[1]), float(line[2])) )

        for i in range(d):
            coords[i] = convertLatLong(coords[i])

        for i in range(d):
            line = []
            for j in range(d):
                line.append(distGeo(coords[i],coords[j]))
            matriz.append(line)        

    elif(ewt == "ATT"):
        while(not file.readline().startswith("NODE_COORD_SECTION")):
            continue
        
        coords = []
        for i in range(d):
            line = file.readline().split()
            coords.append( (float(line[1]), float(line[2])) )
        
        for i in range(d):
            line = []
            for j in range(d):
                line.append(distAtt(coords[i],coords[j]))
            matriz.append(line)
    
    else:
        print("Edge wight type: " + ewt + " not suported")

    return d, matriz

def distEuc(v1,v2):
    return floor( (( (v1[0] - v2[0])**2 + (v1[1] - v2[1])**2 ) ** 0.5) + 0.5)

def convertLatLong(coords):
    PI = 3.141592
    degX, degY = int(coords[0]), int(coords[1])
    minX, minY = coords[0]-degX, coords[1]-degY
    radX, radY = PI*(degX + 5.0*minX/3.0)/180.0, PI*(degY + 5.0*minY/3.0)/180.0
    return radX, radY

def distGeo(v1,v2):
    RRR = 6378.388
    q1 = cos(v1[1] - v2[1])
    q2 = cos(v1[0] - v2[0])
    q3 = cos(v1[0] + v2[0])
    return int(RRR * acos(0.5 * ( (1.0+q1) * q2 - (1.0-q1) * q3) ) + 1.0)

def distAtt(v1,v2):
    rij =((( (v1[0] - v2[0])**2 + (v1[1] - v2[1])**2 )/10) ** 0.5)
    tij = int(rij+0.5)
    
    if(tij < rij):
        return tij+1
    else:
        return tij
