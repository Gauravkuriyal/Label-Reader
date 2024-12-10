from transformers import AutoModel, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('ucaslcl/GOT-OCR2_0', trust_remote_code=True)
model = AutoModel.from_pretrained('ucaslcl/GOT-OCR2_0', trust_remote_code=True, low_cpu_mem_usage=True, device_map='cuda', use_safetensors=True, pad_token_id=tokenizer.eos_token_id)
model = model.eval().cuda()

def OCRModel(image_url):
    # print("url ",image_url)
    res = model.chat(tokenizer, image_url, ocr_type='ocr')
    # print()
    # print("##################################################################")
    # print()
    # print(res)
    return res





#original code

# from transformers import AutoModel, AutoTokenizer

# tokenizer = AutoTokenizer.from_pretrained('ucaslcl/GOT-OCR2_0', trust_remote_code=True)
# model = AutoModel.from_pretrained('ucaslcl/GOT-OCR2_0', trust_remote_code=True, low_cpu_mem_usage=True, device_map='cuda', use_safetensors=True, pad_token_id=tokenizer.eos_token_id)
# model = model.eval().cuda()


# # input your test image
# image_file = './uploaded_images/Screenshot 2024-11-07 031221.png'

# # plain texts OCR
# res = model.chat(tokenizer, image_file, ocr_type='ocr') #going to use this maybe

# # format texts OCR:
# # res = model.chat(tokenizer, image_file, ocr_type='format')

# # fine-grained OCR:
# # res = model.chat(tokenizer, image_file, ocr_type='ocr', ocr_box='')
# # res = model.chat(tokenizer, image_file, ocr_type='format', ocr_box='')
# # res = model.chat(tokenizer, image_file, ocr_type='ocr', ocr_color='')
# # res = model.chat(tokenizer, image_file, ocr_type='format', ocr_color='')

# # multi-crop OCR:
# # res = model.chat_crop(tokenizer, image_file, ocr_type='ocr')
# # res = model.chat_crop(tokenizer, image_file, ocr_type='format')

# # render the formatted OCR results:
# # res = model.chat(tokenizer, image_file, ocr_type='format', render=True, save_render_file = './demo.html')

# print()
# print("##################################################################")
# print()
# print(res)

