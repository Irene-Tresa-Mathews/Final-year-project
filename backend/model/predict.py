from .detect_objects import LoadModel

def predict_varicose():
   print("Loading model...")
   confidence, processed_img_path = LoadModel()
   prediction = "Yes" if confidence > 50 else "No"
   return prediction, confidence, processed_img_path