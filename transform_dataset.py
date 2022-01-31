

from math import cos, sin

def cartesien(src= "nouveu.csv", dest= "cartesien.csv") :
    with open(src, "r") as csv :
        with open(dest, "w") as cartesien :
            lines = csv.readlines()
            for line in lines :
                long, lat = line.split(";")
                long, lat = float(long), float(lat)
                x = 6371000 * cos(lat) * cos(long)
                y = -6371000 * cos(lat) * sin(long)

                cartesien.write(
                    f"{x};{y}\n"
                )

def virgule(src= "nouveu.csv", dest= "cartesien.csv") :
    with open(src, "r") as csv :
        with open(dest, "w") as virgule :
            lines = csv.readlines()
            for line in lines :
                new = line.replace(";" , "," )
                virgule.write(new)


# virgule('lots/first_lot.xls', 'lots/1.csv')
# cartesien()
