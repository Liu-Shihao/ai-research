import os

from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
import torch
from PIL import Image

mode_name = "/Users/liushihao/PycharmProjects/ai-research/model/nlpconnect/vit-gpt2-image-captioning"
model = VisionEncoderDecoderModel.from_pretrained(mode_name)
feature_extractor = ViTImageProcessor.from_pretrained(mode_name)
tokenizer = AutoTokenizer.from_pretrained(mode_name)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)



max_length = 16
num_beams = 4
gen_kwargs = {"max_length": max_length, "num_beams": num_beams}
def predict_step(image_paths):
  images = []
  for image_path in image_paths:
    i_image = Image.open(image_path)
    if i_image.mode != "RGB":
      i_image = i_image.convert(mode="RGB")

    images.append(i_image)

  pixel_values = feature_extractor(images=images, return_tensors="pt").pixel_values
  pixel_values = pixel_values.to(device)

  output_ids = model.generate(pixel_values, **gen_kwargs)

  preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
  preds = [pred.strip() for pred in preds]
  return preds


folder_path = "/Users/liushihao/PycharmProjects/ai-research/images"
file_paths = []
for filename in os.listdir(folder_path):
    print(f'File Name: {filename}')
    file_path = os.path.abspath(os.path.join(folder_path, filename))
    file_paths.append(file_path)

results = predict_step(file_paths)

for image, text in zip(file_paths, results):
    print(f'{image}: {text}')

