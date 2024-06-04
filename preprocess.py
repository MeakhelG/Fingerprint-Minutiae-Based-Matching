import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.feature import hessian_matrix, hessian_matrix_eigvals

def high_boost_filtering(img):
    blurred = cv2.GaussianBlur(img, (0, 0), 3)
    sharpened = cv2.addWeighted(img, 1.5, blurred, -0.5, 0)
    return sharpened

def apply_CLAHE(img):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    clahe_img = clahe.apply(img)
    return clahe_img

# def ridge_extraction(gray):
#     # Gunakan teknik ekstraksi fitur, misalnya deteksi tepi Canny
#     edges = cv2.Canny(gray, 50, 150)
#     return edges

# def detect_ridges(gray, sigma=3.0):
#     H_elems = hessian_matrix(gray, sigma=sigma, order='rc')
#     maxima_ridges, minima_ridges = hessian_matrix_eigvals(H_elems)
#     return maxima_ridges, minima_ridges

def main():
    # Mmebaca Gambar
    img = cv2.imread("final_image_2.jpg", 1)

    # High Boost Filtering
    sharpened = high_boost_filtering(img)
    plt.imshow(cv2.cvtColor(sharpened, cv2.COLOR_BGR2RGB))
    plt.title('High Boost Filtering')
    plt.axis('off')
    plt.show()

    # Grayscale the image
    gray = cv2.cvtColor(sharpened, cv2.COLOR_BGR2GRAY)
    plt.imshow(gray, cmap='gray')
    plt.title('Grayscale Image')
    plt.axis('off')
    plt.show()

    # Perform Contrast Limited Adaptive Histogram Equalization (CLAHE)
    clahe_img = apply_CLAHE(gray)
    plt.imshow(clahe_img, cmap='gray')
    plt.title('CLAHE Image')
    plt.axis('off')
    plt.show()

    # # Step 5: Ridge Extraction using Feature Extraction
    # maxima_ridges, minima_ridges = detect_ridges(clahe_img, sigma=2.7)
    # plt.imshow(maxima_ridges, cmap='gray')
    # plt.title('Maxima Ridges')
    # plt.axis('off')
    # plt.show()

    # plt.imshow(minima_ridges, cmap='gray')
    # plt.title('Minima Ridges')
    # plt.axis('off')
    # plt.show()

    # Menyimpan gambar hasil dari maxima ridge dan minima ridge dengan normalisasi nilai pixel
    # maxima_ridges_normalized = cv2.normalize(maxima_ridges, None, 0, 255, cv2.NORM_MINMAX)
    # minima_ridges_normalized = cv2.normalize(minima_ridges, None, 0, 255, cv2.NORM_MINMAX)
    cv2.imwrite("Clahe_2.jpg", clahe_img)
    # cv2.imwrite("maxima_ridges.jpg", maxima_ridges_normalized)
    # cv2.imwrite("minima_ridges.jpg", minima_ridges_normalized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
