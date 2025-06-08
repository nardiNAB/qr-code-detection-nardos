import cv2
import os
import matplotlib.pyplot as plt

# Author: Nardos Amde Beyene
# Project: QR Code Detection and Decoding (Multi QR Version)
# Date: June 8, 2025

# Set input and output directories
INPUT_FOLDER = "images"       # Folder with QR code images (from Kaggle and Other Source)
OUTPUT_FOLDER = "results"     # Output folder for results with bounding boxes

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

detector = cv2.QRCodeDetector()

total_images = 0
successful_detections = 0

# Process each image
for filename in os.listdir(INPUT_FOLDER):
    if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        continue

    total_images += 1
    image_path = os.path.join(INPUT_FOLDER, filename)
    img = cv2.imread(image_path)

    if img is None:
        print(f"[ERROR] Could not load {filename}")
        continue

    # Multi QR code detection
    retval, decoded_info, points, _ = detector.detectAndDecodeMulti(img)

    if retval and points is not None and decoded_info:
        successful_detections += 1
        for i in range(len(decoded_info)):
            text = decoded_info[i]
            box = points[i].astype(int)

            # Draw bounding box
            for j in range(4):
                pt1 = tuple(box[j])
                pt2 = tuple(box[(j + 1) % 4])
                cv2.line(img, pt1, pt2, (0, 255, 0), 2)

            # Show decoded text above QR code
            x, y = box[0]
            cv2.putText(img, text, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

            print(f"[SUCCESS] {filename} → QR #{i+1}: {text}")
    else:
        print(f"[FAILURE] {filename} → No QR code detected.")

    # Save result
    result_path = os.path.join(OUTPUT_FOLDER, filename)
    cv2.imwrite(result_path, img)

print("\n=========== Detection Summary ===========")
print(f"Total Images Processed:  {total_images}")
print(f"Images with QR Detected: {successful_detections}")
print(f"Detection Rate:          {successful_detections / total_images:.2%}")

# Display one sample result
sample_result = os.listdir(OUTPUT_FOLDER)[0]
sample_img = cv2.imread(os.path.join(OUTPUT_FOLDER, sample_result))
sample_img_rgb = cv2.cvtColor(sample_img, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(8, 6))
plt.imshow(sample_img_rgb)
plt.title("Sample Multi-QR Detection Output")
plt.axis('off')
plt.tight_layout()
plt.show()