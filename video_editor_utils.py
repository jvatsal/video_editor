import google.generativeai as genai
import os
import PIL.Image
import cv2
import shutil





def video_cleanup(uploaded_files):
    for file in uploaded_files:
        genai.delete_file(file.response.name)