data = [['red','sports','domestic','yes'],['red','sports','domestic','no'],['yellow','suv','domestic','no'],
['yellow','sports','domestic','no'],['red','sports','domestic','yes'],['yellow','sports','imported','yes'],
['yellow','suv','imported','no'],['yellow','suv','imported','yes'],['red','suv','imported','no'],
['red','sports','imported','yes']]

num_data = 10
stolen_y = 0
stolen_n = 0
for x in range (num_data):
    if data[x][3] == 'yes':
        stolen_y = stolen_y + 1
    else:
        stolen_n = stolen_n + 1

Pstolen_y = stolen_y/num_data
Pstolen_n = stolen_n/num_data

print ('\nP(stolen)="yes":'+str(Pstolen_y))
print ('P(stolen)="no":'+str(Pstolen_n))

color = input("\nEnter color:")
type = input("Enter type:")
origin = input("Enter origin:")

X = [color,type,origin]
print ('\nNew tuple is:')
print (X)

col_stolen_y = 0
col_stolen_n = 0
type_stolen_y = 0
type_stolen_n = 0
org_stolen_y = 0
org_stolen_n = 0

for x in range (num_data):
    if data[x][0]==X[0] and data[x][3]=='yes':
        col_stolen_y = col_stolen_y + 1
    if data[x][0]==X[0] and data[x][3]=='no':
        col_stolen_n = col_stolen_n + 1
    if data[x][1]==X[1] and data[x][3]=='yes':
        type_stolen_y = type_stolen_y + 1
    if data[x][1]==X[1] and data[x][3]=='no':
        type_stolen_n = type_stolen_n + 1
    if data[x][2]==X[2] and data[x][3]=='yes':
        org_stolen_y = org_stolen_y + 1
    if data[x][2]==X[2] and data[x][3]=='no':
        org_stolen_n = org_stolen_n + 1

Pcol_stolen_y = col_stolen_y/stolen_y
Pcol_stolen_n = col_stolen_n/stolen_n

Ptype_stolen_y = type_stolen_y/stolen_y
Ptype_stolen_n = type_stolen_n/stolen_n

Porg_stolen_y = org_stolen_y/stolen_y
Porg_stolen_n = org_stolen_n/stolen_n

print ("\nProbability that color is:"+X[0]+" and is stolen is:"+str(Pcol_stolen_y))
print ("Probability that color is:"+X[0]+" and is not stolen is:"+str(Pcol_stolen_n))
print ("\nProbability that type is:"+X[1]+" and is stolen is:"+str(Ptype_stolen_y))
print ("Probability that type is:"+X[1]+" and is not stolen is:"+str(Ptype_stolen_n))
print ("\nProbability that origin is:"+X[2]+" and is stolen is:"+str(Porg_stolen_y))
print ("Probability that origin is:"+X[2]+" and is not stolen is:"+str(Porg_stolen_n))

P_y = Pcol_stolen_y*Ptype_stolen_y*Porg_stolen_y
print ("\nProbability that X is stolen:"+str(P_y))
P_n = Pcol_stolen_n*Ptype_stolen_n*Porg_stolen_n
print ("Probability that X is not stolen:"+str(P_n))

CP_y = P_y*Pstolen_y
print ("\nConditional Probability that X is stolen:"+str(CP_y))
CP_n = P_n*Pstolen_n
print ("Conditional Probability that X is not stolen:"+str(CP_n))

if (CP_y>CP_n):
    print ("\nX Belongs to class: Stolen(yes)")
else:
    print ("\nX Belongs to class: Stolen(no)")




 #Output
 # color =red ,type = sports, origin = domestic