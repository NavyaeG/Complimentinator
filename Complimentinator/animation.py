import customtkinter as ctk
from PIL import Image, ImageTk
from os import walk
import os
import random

class Animation(ctk.CTkFrame):
    def __init__(self, parent, animation_path,compliment):
        super().__init__(master=parent)

        self.animation_path=animation_path
        self.compliment=compliment
        self.animation_id = None

        self.frames = self.import_folder(animation_path)
        self.current_frame = 0
        self.canvas = ctk.CTkCanvas(self, width=300, height=179, bg="#C3B1E1")
        self.canvas.pack(fill="both", expand=True)

        self.cloud0_image = Image.open(self.animation_path+"/cloud1.png")
        self.cloud0_image = self.resize_image_preserve_aspect_ratio(self.cloud0_image,370,208)
        self.cloud0_photo = ImageTk.PhotoImage(self.cloud0_image)
        self.cloud0_x = -250
        self.cloud0_y = 50

        self.cloud1_image = Image.open(self.animation_path+"/cloud2.png")
        self.cloud1_image = self.resize_image_preserve_aspect_ratio(self.cloud1_image,370,208)
        self.cloud1_photo = ImageTk.PhotoImage(self.cloud1_image)
        self.cloud1_x = 170
        self.cloud1_y = 10

        self.cloud2_image = Image.open(self.animation_path+"/cloud3.png")
        self.cloud2_image = self.resize_image_preserve_aspect_ratio(self.cloud2_image,370,208)
        self.cloud2_photo = ImageTk.PhotoImage(self.cloud2_image)
        self.cloud2_x = 0
        self.cloud2_y = 85

        self.update_frame(compliment)
        self.after(100, self.animate)
    
    def resize_image_preserve_aspect_ratio(self, image, desired_width, desired_height):
        original_width, original_height = image.size
        ratio = min(desired_width / original_width, desired_height / original_height)
        new_width = int(original_width * ratio)
        new_height = int(original_height * ratio)
        return image.resize((new_width, new_height), Image.ANTIALIAS)

    def import_folder(self, animation_path):
        subdirectories = [os.path.join(animation_path, d) for d in os.listdir(animation_path) if os.path.isdir(os.path.join(animation_path, d))]
        selected_subdirectory = random.choice(subdirectories)

        image_path = []

        for _, __, files in walk(selected_subdirectory):
            files.sort()
            image_path=[os.path.join(selected_subdirectory, item) for item in files]
        return image_path

    def update_frame(self, compliment):
        frame_path = self.frames[self.current_frame]
        image = Image.open(frame_path)

        desired_width = 192
        desired_height = 192

        image = image.resize((desired_width, desired_height), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(image)

        self.canvas.delete("all")

        self.canvas.create_image(self.cloud2_x, self.cloud2_y, anchor="nw", image=self.cloud2_photo)
        self.canvas.create_image(self.cloud1_x, self.cloud1_y, anchor="nw", image=self.cloud1_photo)
        self.canvas.create_image(self.cloud0_x, self.cloud0_y, anchor="nw", image=self.cloud0_photo)

        
        self.canvas.create_image(-10, 0, anchor="nw", image=self.photo)
        self.canvas.create_text(170, 59, anchor="nw", text=compliment, fill="#7b3781", font=("OCR A Extended", 13, "bold"), width=235)
        self.canvas.create_text(20, 10, anchor="nw", text="💜 Have an amazing day ahead! 💜", fill="#5e2f6f", font=("OCR A Extended", 14, "bold"))
        self.canvas.create_text(20, 17, anchor="nw", text="________________________________", fill="#5e2f6f", font=("OCR A Extended", 14, "bold"))
        self.canvas.create_text(20, -10, anchor="nw", text="________________________________", fill="#5e2f6f", font=("OCR A Extended", 14, "bold"))


        self.current_frame = (self.current_frame + 1) % len(self.frames)
    
    def animate(self):
        self.update_frame(self.compliment)

        self.cloud2_x += 1
        self.cloud1_x += 1
        self.cloud0_x += 1

        if self.cloud2_x > self.canvas.winfo_width():
            self.cloud2_x = -self.cloud2_photo.width()

        if self.cloud1_x > self.canvas.winfo_width():
            self.cloud1_x = -self.cloud1_photo.width()  

        if self.cloud0_x > self.canvas.winfo_width():
            self.cloud0_x = -self.cloud0_photo.width() 

        self.after(100, self.animate)