#This code was entirely written by Chat-GPT 3
#Barely anything waas edited by me
#If you find any errors or want to make a suggestion please
#Find me at Github = ALEXDEX367
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
window.borderless = False
window.title = "GPT-Craft 0.1.6"

app = Ursina()

cube_texture = load_texture('texture2.jfif') #If you want to change the Textures, change "texture2.jfif" to any image for a texture
sky_texture = load_texture('sky.png') #Same here as above, change "sky.png" to any image you want

class Voxel(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=cube_texture,
            color=color.white,
            highlight_color=color.dark_gray, #This is the highlighted texture, change it to any colour you want
        )

    def input(self, key): #This defines what LMB click and RMB click do. (LMB = Breaking blocks, RMB = Placing blocks)
        if self.hovered:
            if key == 'right mouse down':
                voxel = Voxel(position=self.position + mouse.normal)
            if key == 'left mouse down':
                destroy(self)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture=sky_texture,
            scale=10000,
            double_sided=True
        )

for z in range(8):
    for x in range(8):
        voxel = Voxel(position=(x, 0, z))

player = FirstPersonController()
sky = Sky()

app.run()

