from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def detect_flood(image_path):
    # Load the satellite image
    img = Image.open(image_path)
    img_np = np.array(img)

    # Flood detection logic: detect blue-dominant areas
    blue_mask = (img_np[:, :, 2] > 150) & (img_np[:, :, 0] < 100) & (img_np[:, :, 1] < 100)

    # Check if any blue area found
    if np.sum(blue_mask) > 0:
        print("🚨 ALERT: Potential flood detected in the region.")
    else:
        print("✅ No flood detected.")

    # Highlight flood zones in red
    detected_img = img_np.copy()
    detected_img[blue_mask] = [255, 0, 0]  # red overlay

    # Display result
    result_img = Image.fromarray(detected_img)
    result_img.show()  # Opens a window with the image

    # Save output image
    result_img.save("flood_detection_result.jpg")

if __name__ == "__main__":
    detect_flood("download (4).jpeg")
