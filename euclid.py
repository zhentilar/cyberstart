import math

# Öklid mesafesi fonksiyonu
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# 2D uzayda noktaların tanımlanması
points = [(1, 2), (4, 6), (5, 9), (8, 3), (0, 0)]

# Mesafeleri saklayacağımız liste
distances = []

# Her nokta çifti arasındaki mesafeyi hesaplayıp distances listesine ekleme
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafenin bulunması
min_distance = min(distances)

# Sonuçların yazdırılması
print("Hesaplanan mesafeler:", distances)
print("Minimum mesafe:", min_distance)
