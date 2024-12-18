import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re

slopes = pd.read_csv("Slopes of lines.csv")
raw = pd.read_csv("Raw Data.csv")
der = pd.read_csv("Derivates kinda.csv")
"""
rows = raw.apply(lambda x: x.iloc[7:],axis=1)
#rows=rows.set_index(raw["Item"])
rowsbetter = rows.transpose()

rowsbetter = rowsbetter.reset_index()

num = 16
print(rowsbetter.head())
plt.plot(rowsbetter[num],rowsbetter.index)
plt.xlabel("time")
plt.ylabel("repeat number")
plt.title("Peak number and time - "+str(num))
plt.show()
"""
"""
pots = slopes.query("Item == 'Large Pot Lid' or Item == 'Medium Pot Lid' or Item == 'Small Pot Lid'")

pots = pots.iloc[:,0:8]

pots = pots.groupby("Radius")
potvals = pots['Average slope'].mean()
print(potvals.head())
radii = list(map(float, potvals.index))
plt.scatter(radii,potvals)
plt.xlabel("radius")
plt.ylabel("2nd derivative")
plt.title("2nd derivative and radius")
plt.show()

print (list(slopes["Item"]))
print(list(slopes["On:"]))
pots = slopes.query("(Item == 'Tape' and `On:` == 'Wood bench') or Item == 'Tape With Small Rad' or Item == 'Tape big radius'")
print(pots["Item"])
pots = pots.iloc[:,0:8]

potvals = pots['Average slope']
print(potvals)
print("AAAAA")
print(potvals.head())
print(pots.head(10))
radii = list(map(float, pots["Radius"]))
print(radii)
print(potvals)
plt.scatter(radii,potvals)
plt.xlabel("radius")
plt.ylabel("2nd derivative")
plt.title("2nd derivative and radius")
plt.show()
"""

surfaces = slopes.query("(Item == 'Tape' and `On:` == 'Wood bench') or Item == 'Tape With Small Rad' or Item == 'Tape big radius'")
surfaces = surfaces[["Radius","Average slope"]]
surfaces = surfaces.groupby("Radius").mean().reset_index()
plt.scatter(list(map(float,surfaces["Radius"])),surfaces["Average slope"])
plt.title("2nd derivative with various radii")
plt.xlabel("radius")
plt.ylabel("2nd derivative")
plt.show()
