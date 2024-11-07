from PIL import Image
import numpy as np

image = Image.open("mickey.jpeg")
pixels = image.load()
width, height = image.size

result = np.zeros((height, width, 3), dtype=np.uint8)
kernel = np.array([
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1],
])

kernel_size = len(kernel)

for y in range(height-kernel_size+1):
    for x in range(width-kernel_size+1):
        acc = np.array([0, 0, 0], dtype=float)
        # Get the RGB values of the pixel at (x, y)
        # kernel height
        for k_h in range(kernel_size):
            for k_w in range(kernel_size):
                # kernel width
                r, g, b = pixels[x + k_w, y + k_h]
                acc += np.array([r, g, b]) * kernel[k_h, k_w]
        result[y, x] = np.clip(acc, 0, 255)

final = Image.fromarray(result, "RGB")
final.save("output.jpeg", "JPEG")