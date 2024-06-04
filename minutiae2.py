import cv2
import numpy as np
from scipy.spatial import KDTree

# Fungsi untuk ekstraksi minutiae dari gambar sidik jari

def extract_minutiae(image):
    print("Ekstraksi minutiae dimulai.")
    # Mengkonversi ke citra grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print("Konversi ke grayscale selesai.")
    # thresholding
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    print("Thresholding selesai.")
    # thinning untuk mendapatkan garis-garis tengah
    thinned = thinning(binary)
    print("Thinning selesai.")
    # ekstraksi minutiae dari garis tengah
    minutiae = []
    for y in range(1, thinned.shape[0] - 1):
        for x in range(1, thinned.shape[1] - 1):
            if thinned[y][x] == 255:
                num_neighbors = np.sum(thinned[y-1:y+2, x-1:x+2]) // 255 - 1
                if num_neighbors == 1:
                    minutiae.append((x, y, 'ending'))
                elif num_neighbors > 2:
                    minutiae.append((x, y, 'bifurcation'))
    print(f"Ekstraksi minutiae selesai. Total minutiae ditemukan: {len(minutiae)}")
    return minutiae

# Fungsi untuk melakukan thinning 

def thinning(image):
    print("Proses thinning dimulai.")
    size = np.size(image)
    skel = np.zeros(image.shape, np.uint8)
    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    done = False
    while not done:
        eroded = cv2.erode(image, element)
        temp = cv2.dilate(eroded, element)
        temp = cv2.subtract(image, temp)
        skel = cv2.bitwise_or(skel, temp)
        image = eroded.copy()
        zeros = size - cv2.countNonZero(image)
        if zeros == size:
            done = True
    print("Proses thinning selesai.")
    return skel

# Fungsi untuk mencocokkan dua set minutiae menggunakan kd tree

def match_minutiae(minutiae1, minutiae2, threshold=10):
    print("Proses pencocokan minutiae dimulai.")
    tree = KDTree([(x, y) for x, y, _ in minutiae2])
    matched = []
    for i, m1 in enumerate(minutiae1):
        if i % 100 == 0:
            print(f"Proses pencocokan: {i}/{len(minutiae1)}")
        dist, idx = tree.query((m1[0], m1[1]), distance_upper_bound=threshold)
        if dist < threshold:
            matched.append((m1, minutiae2[idx]))
    print(f"Proses pencocokan minutiae selesai. Total matched minutiae: {len(matched)}")
    return matched

# Fungsi untuk menampilkan minutiae pada gambar

def draw_minutiae(image, minutiae):
    for x, y, m_type in minutiae:
        if m_type == 'ending':
            cv2.circle(image, (x, y), 5, (0, 255, 0), 2)  # Hijau untuk ending
        elif m_type == 'bifurcation':
            cv2.circle(image, (x, y), 5, (255, 0, 0), 2)  # Biru untuk bifurcation
    return image

# Fungsi untuk menentukan kecocokan sidik jari

def is_fingerprint_match(matched_minutiae, total_minutiae1, total_minutiae2, match_threshold=0.3):
    match_count = len(matched_minutiae)
    match_ratio1 = match_count / total_minutiae1
    match_ratio2 = match_count / total_minutiae2
    print(f"Match ratio (image1): {match_ratio1:.2f}")
    print(f"Match ratio (image2): {match_ratio2:.2f}")
    return match_ratio1 >= match_threshold and match_ratio2 >= match_threshold

# Mmebaca dua gambar sidik jari

image1 = cv2.imread("./minima_ridges.jpg")
image2 = cv2.imread("./maxima_ridges.jpg")

if image1 is None:
    print("Error: Gagal memuat gambar minima_ridges.jpg")
    exit(1)
if image2 is None:
    print("Error: Gagal memuat gambar maxima_ridges.jpg")
    exit(1)
print("Gambar berhasil dimuat.")

# Ekstraksi minutiae dari kedua gambar

minutiae1 = extract_minutiae(image1)
minutiae2 = extract_minutiae(image2)

# Mencocokkan kedua set minutiae

matched_minutiae = match_minutiae(minutiae1, minutiae2)

# Tentukan kecocokan sidik jari

if is_fingerprint_match(matched_minutiae, len(minutiae1), len(minutiae2)):
    print("Sidik jari cocok.")
else:
    print("Sidik jari tidak cocok.")

# Gambar minutiae yang ditemukan 

image1_with_minutiae = draw_minutiae(image1.copy(), minutiae1)
image2_with_minutiae = draw_minutiae(image2.copy(), minutiae2)

# Tampilkan gambar-gambar yang telah dimodifikasi

cv2.imshow("Fingerprint 1 with Minutiae", image1_with_minutiae)
cv2.imshow("Fingerprint 2 with Minutiae", image2_with_minutiae)

# Tampilkan hasil pencocokan

for minutia1, minutia2 in matched_minutiae:
    cv2.circle(image1_with_minutiae, (minutia1[0], minutia1[1]), 5, (0, 0, 255), 2)  # Merah untuk matched minutiae
    cv2.circle(image2_with_minutiae, (minutia2[0], minutia2[1]), 5, (0, 0, 255), 2)  # Merah untuk matched minutiae

cv2.imshow("Matched Fingerprint 1", image1_with_minutiae)
cv2.imshow("Matched Fingerprint 2", image2_with_minutiae)
cv2.waitKey(0)
cv2.destroyAllWindows()