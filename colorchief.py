import matplotlib.image as mpimg
import matplotlib
import matplotlib.pyplot as plt
from scipy.spatial import distance
import numpy as np

colorlist=[]
colordist=[]
final={}
for name, hexi in matplotlib.colors.cnames.iteritems():
     colorlist.append([name.encode('ascii'), hexi.encode('ascii')])
#print colorlist

def hex_to_rgb(value):
    """Return (red, green, blue) for the color given as #rrggbb."""
    value = value.lstrip('#')
    lv = len(value)
    return list(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

for i in colorlist:
	temp=hex_to_rgb(i[1])
	i[1]=temp
#colorlist=sorted(colorlist, key=lambda x:x[1])
#print colorlist

def caldistance(val):
	dist=[]
	for i in colorlist:
		dist.append(([i[0],distance.euclidean(i[1],val)]))
	return dist

from PIL import Image

img = Image.open('test.jpg')
img = img.resize([120,120]) 
image= np.array(img)
#print image
'''
plt.imshow(image)
plt.show()
'''
for i in xrange(len(image)):
	for j in xrange(0,len(image[i]),10):
		ans=caldistance(image[i][j])
		ans=sorted(ans, key=lambda x:x[1])
		#print ans[0]
		if(ans[0][0] not in final):
			final[ans[0][0]]=1
		else:
			final[ans[0][0]]+=1
		#j+=100
	#i+=100

final=sorted(final.items(), key=lambda x: x[1], reverse=True)

#print final
leng= len(final)
leng= leng*0.2
i=0
total=100
while(i<leng):
	cal=(final[i][1]*100)/1440.
	total-=cal
	print final[i][0],"=",cal,"%"
	i+=1
print "Others=",total,"%"









