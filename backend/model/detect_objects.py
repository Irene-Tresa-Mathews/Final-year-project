import os
import cv2

from .detector import DetectorTF2

def DetectImagesFromFolder(detector, images_dir, save_output=False, output_dir='output/'):

	for file in os.scandir(images_dir):
		if file.is_file() and file.name.endswith(('.jpg', '.jpeg', '.png')) :
			image_path = os.path.join(images_dir, file.name)
			print(image_path)
			img = cv2.imread(image_path)
			det_boxes = detector.DetectFromImage(img)
			img, confidence  = detector.DisplayDetections(img, det_boxes)

			if save_output:
				img_out = os.path.join(output_dir, file.name)
				cv2.imwrite(img_out, img)
	return confidence, img_out

def LoadModel():
# instance of the class DetectorTF2
	print("Detecting objects...")
	detector = DetectorTF2('C:/Users/irene/project/Project2/backend/model/frozen_model/saved_model', 'C:/Users/irene/project/Project2/backend/model/frozen_model/labelmap.pbtxt')

	return DetectImagesFromFolder(detector, 'C:/Users/irene/project/Project2/backend/static/uploads', save_output=True, output_dir='C:/Users/irene/project/Project2/backend/processed')