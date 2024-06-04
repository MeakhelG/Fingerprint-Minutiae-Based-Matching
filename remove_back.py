import cv2
import numpy as np

imgOri = cv2.imread('C:/Users/inez/Downloads/Fingerprint-Matching (minutiae) 2/Fingerprint-Matching (minutiae)/input/f1.jpeg')
cv2.imshow("Image Original",imgOri)

# K-MEANS
# Mengubah gambar menjadi array 2D
img_flat = imgOri.reshape((-1, 3)).astype(np.float32)

# Menentukan jumlah cluster (k)
k = 2
max_iter = 100
epsilon = 0.2

# Inisialisasi centroid 
np.random.seed(42)
centroids = img_flat[np.random.choice(img_flat.shape[0], k, replace=False)]

for i in range(max_iter):
    # Mengitung jarak setiap piksel ke centroid
    distances = np.linalg.norm(img_flat[:, np.newaxis] - centroids, axis=2)

    # Menentukan label untuk setiap piksel
    labels = np.argmin(distances, axis=1)

    # Update Centroid
    new_centroids = np.array([img_flat[labels == j].mean(axis=0) for j in range(k)])

    # Cek konvergensi
    if np.all(np.abs(new_centroids - centroids) < epsilon):
        break

    centroids = new_centroids

# Identifikasi label untuk background dan object berdasarkan intensitas (asumsi bg memiliki intensitas rata2 yg lebih rendah dibanding object)
background_label = np.argmin(centroids.sum(axis=1))
object_label = np.argmax(centroids.sum(axis=1))

# Membuat mask objek
object_mask = (labels == object_label).astype(np.uint8).reshape(imgOri.shape[:2])

# Menggunakan mask untuk mendapatkan objek saja
object_only = np.zeros_like(imgOri)
object_only[object_mask == 1] = imgOri[object_mask == 1]

# Membuat background menjadi putih
background = np.ones_like(imgOri, dtype=np.uint8) * 255
background_only = background.copy()
background_only[object_mask == 1] = 0

# Mengabungkan object dan bcakground
final_image = background_only + object_only


# # GRABCUT
# #Removing the background
# height, width = imgOri.shape[:2]

# #Create a mask holder
# mask = np.zeros(imgOri.shape[:2],np.uint8)

# #Grab Cut the object
# bgdModel = np.zeros((1,65),np.float64)
# fgdModel = np.zeros((1,65),np.float64)

# #Hard Coding the Rect… The object must lie within this rect.
# rect = (10,10,width-30,height-30)
# cv2.grabCut(imgOri,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
# mask = np.where((mask==2)|(mask==0),0,1).astype("uint8")
# img1 = imgOri*mask[:,:,np.newaxis]

# #Get the background
# background = cv2.absdiff(imgOri,img1)

# #Change all pixels in the background that are not black to white
# background[np.where((background > [0,0,0]).all(axis = 2))] = [255,255,255]

# #Add the background and the image
# final_image = background + img1


cv2.imshow('image', final_image )
cv2.imwrite("final_image_2.jpg",final_image)

cv2.waitKey(0)
cv2.destroyAllWindows()