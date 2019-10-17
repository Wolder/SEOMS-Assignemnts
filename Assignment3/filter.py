import csv
import statistics
import math

file_name = input("Enter file name (with extension): ")
filter_type = input("Enter filter type (median or mean): ")
points_to_process = input("Points to process per filtering (int): ")
data = list(csv.reader(open(file_name), delimiter = ','))


# KML params
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

# Start of KML Doc
file = open(str(file_name).split(".")[0]+'_'+d_type+'_'+filter_type+'.kml', 'w')
file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
file.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
file.write("<Document>\n")
file.write("<name>"+str(file_name)+"</name>\n")
file.write("<description>"+str(file_name)+" trajectory translated from a CSV file.</description>\n")
file.write("<Style>\n")
file.write("<LineStyle>\n")
file.write("<color>"+str(color)+"</color>\n")
file.write("<width>"+width+"</width>\n")
file.write("</LineStyle>\n")
file.write("</Style>\n")
file.write("<Placemark>\n")
file.write("<LineString>\n")
file.write("<coordinates>\n")

#/home/wolder/AndroidStudioProjects/SEOMS-Assignemnts/Assignment3/Biking.csv

# Init
points_array = []
index = 1
temp_array_size = 0;
batch = []
result_array = []

j = 1
i = 0

for row in data:
    i += 1
    try:
        if i > 1:
            print(i)
            for r in range (int(points_to_process)):
                #reference_row = data[i + r - (int(points_to_process))/2]
                reference_row = data[i + r]
                new_point = [float(reference_row[index+1]), float(reference_row[index])]
                batch.append(new_point)
            points_array.append(batch)

            batch = []

    except IndexError:
        continue
    



for batch in range(len(points_array)): #For each batch
    xlist = []
    ylist = []
    for point in range(len(points_array[batch])):
        xlist.append((points_array[batch][point])[0])
        ylist.append((points_array[batch][point])[1])
         
    if filter_type == "median":
        new_filtered_point = [statistics.median(xlist), statistics.median(ylist)]
        result_array.append(new_filtered_point)

    if filter_type == "mean":
        new_filtered_point = [statistics.mean(xlist), statistics.mean(ylist)]
        result_array.append(new_filtered_point)
        
        
for point in result_array:
    file.write(str(point[0]) + "," + str(point[1]) + "\n")


file.write("</coordinates>\n")
file.write("</LineString>\n")
file.write("</Placemark>\n")
file.write("</Document>\n")
file.write("</kml>")

print ("File Created. ")
print ("Press ENTER to exit. ")
input()
file.close()