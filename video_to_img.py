#!/usr/bin/env python
# coding: utf-8

# In[4]:


from cv2 import VideoCapture,CAP_PROP_FPS,imwrite
import os


# In[5]:


def split_img(path):
    file_name = [i for i in os.listdir(path) if '.MP4' in i.upper() or '.AVI' in i.upper()]
    img_count = 0

    for i in file_name:
        cap = VideoCapture(path + '/' + i)
        fps = int(cap.get(CAP_PROP_FPS))
        count = 0
        while True:
            status, Frame = cap.read()
            if not status:
                break
            if not os.path.exists(path + '/img'):
                os.makedirs(path + '/img')

            if (count % fps == 0) or (count % fps == int(fps/2)):
                imwrite(path + '/img' + '/' + i.split('.')[0] + '_' + '0' * (8-len(str(img_count))) + str(img_count) + '.jpg', Frame)
            
            #imwrite(path + '/img' + '/' + '0' * (8-len(str(img_count))) + str(img_count) + '.jpg', Frame)
            img_count += 1
            print("Create Image : ",path + '/img' + '/' + i.split('.')[0] + '_' + '0' * (8-len(str(img_count))) + str(img_count) + '.jpg')
            count += 1


# In[6]:


print("--Start split video to image--")
video_path = "video"
if not os.path.exists(video_path):
    print("--Create Video folder--")
    os.makedirs(video_path)
else:
    split_img(video_path)
    print("--Done !!--")


# In[ ]:



