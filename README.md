QR Code Detection and Decoding (Multi QR Support)

    Author: Nardos Amde Beyene
    Course: Computer Vision
    Date: June 8, 2025

Project Description
    This project detects and decodes multiple QR codes in static images using OpenCV’s QRCodeDetector. It supports automatic annotation, decoding, and visual output saving for analysis and presentation. The system was evaluated on sample test images including 

Technologies Used
    Python 3.14
    OpenCV (cv2)
    Matplotlib

Folder Structure
    images/ → Input images (Kaggle + test cases)
    results/ → Output images with bounding boxes + decoded text
    main.py → Detection script
    report.pdf → Academic report (generated from this project)
    presentation.pptx → Presentation slides

How to Run
    1. Install dependencies:
        pip install opencv-python matplotlib
    2. Place images into the /images folder.
    3. Run the script:
        python main.py
    4. Processed images will be saved to /results with bounding boxes and decoded text.