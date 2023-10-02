from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
# import tensorflow as tf
# import numpy as np 
# import os
# import tempfile
# from django.conf import settings
# from django.core.files.storage import default_storage
# model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'restnet_best_model.hdf5')

# result = {}
# file_path = os.path.join(settings.STATIC_ROOT,'class_list.txt')
# with open(file_path) as f:
#     for line in f:
#         key, value = line.strip().split()
#         result[int(key)] = value
# model = tf.keras.models.load_model(model_path)

def home(request):
    if request.method == 'POST':
        # image = request.FILES['image']
        # pathh=''
        # # with tempfile.NamedTemporaryFile(suffix='.jpg') as f:
        # #     for chunk in image.chunks():
        # #         f.write(chunk)
        # #     f.seek(0) 
        # #     pathh=f.name    
        # if image:
        #     # Generate a unique filename for the image
        #     filename = default_storage.get_available_name(image.name)
        #     # Save the image to the media directory
        #     path = default_storage.save(filename, image)   
        # path=r'C:\Users\Acer\Desktop\Web\capstone\media'+'\\'+ str(path)
        # # Prepare the image for prediction
        # image = tf.keras.utils.load_img(path, target_size=(224, 224))
        # image = tf.keras.utils.img_to_array(image)
        # image = tf.keras.applications.mobilenet.preprocess_input(image)
        # image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
        # # Make predictions
        # predictions = model.predict(image)
        # top_5_idx = np.argsort(predictions).tolist()[0][-5:]
        # # print(top_5_idx)
        # # print(result)
        # top_five =[result[i] for i in top_5_idx ]
        
        # print(top_five)

        return JsonResponse({'top': 'top_five'})
    return render(request, 'home.html')
