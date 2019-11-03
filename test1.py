
from PIL import Image
import numpy as np
width, height = 520, 520

image1 = Image.open('sheep.jpg')
image1.show()
image1resized = image1.resize((width, height), Image.BILINEAR)
#image1resized.save("BILINEARSHEEP.jpg")
image1resized.show()
array1 = np.asarray(image1resized)
print("Array 1")
print (array1)

image2 = Image.open('wolf.jpg')
image2.show()
image2resized = image2.resize((width, height), Image.BILINEAR)
# image2resized.save("BILINEARWOLF.jpg")
image2resized.show()
array2 = np.asarray(image2resized)
print("Array 2")
print(array2)

new = array1 + array2
print("COMBINED)")
print(new)

newimage = Image.fromarray(new, 'RGB')
newimage.save('new.jpg')
newimage.show()