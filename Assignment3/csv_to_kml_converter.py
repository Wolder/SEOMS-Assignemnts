import csv
#Input the file name."JoeDupes3_forearth"
fname = input("Enter file name (with extension): ")
data = csv.reader(open(fname), delimiter = ',')
type_of_coords = input("Enter either 'gps' or 'phone': ")
d_type = 'phone'
if type_of_coords == 'phone':
    index = 3
elif type_of_coords == 'gps':
    index = 1
    d_type = 'gps'
else:
    print("You mistyped.... Start over you retard.") 
    exit(0)   

setparams = input("Do you want to adjust paramters? (y/n) ")
if setparams == "y":
    color = input("Enter color (ex. #fc0303): ")
    width = input("Linewidts (ex. 5): ")
else:
    color = "#fc0303"
    width = "4"
    
f = open(str(fname).split(".")[0]+'_'+d_type+'.kml', 'w')

f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
f.write("<Document>\n")
f.write("<Placemark>\n")
f.write("<name>"+str(fname)+"</name>\n")
f.write("<description>"+str(fname)+" trajectory translated from a CSV file.</description>\n")
f.write("<Style>\n")
f.write("<LineStyle>\n")
f.write("<color>"+str(color)+"</color>\n")
f.write("<width>"+width+"</width>\n")
f.write("</LineStyle>\n")
f.write("</Style>\n")
f.write("<LineString>\n")
f.write("<coordinates>\n")


i = 0
for row in data:
    i += 1
    if i > 1:
        f.write(str(row[index+1]) + "," + str(row[index]) + "\n")


f.write("</coordinates>\n")
f.write("</LineString>\n")
f.write("</Placemark>\n")
f.write("</Document>\n")
f.write("</kml>")
      

print ("File Created. ")
print ("Press ENTER to exit. ")
input()
f.close()