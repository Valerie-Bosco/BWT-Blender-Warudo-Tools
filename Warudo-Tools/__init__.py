import bpy


bl_info = {
    "name": "AlxWarudoTools",
    "author": "Valeria Bosco[Valy Arhal]",
    "description": "",
    "warning": "",
    "version": (0, 1, 0),
    "blender": (4, 0, 0),
    "category": "3D View",
    "location": "",
    "doc_url": "https://github.com/Valery-AA/AlxWarudoTools/wiki",
    "tracker_url": "https://github.com/Valery-AA/AlxWarudoTools/issues",
}




def register():

    bpy.context.preferences.use_preferences_save = True


def unregister():
    pass

if __name__ == "__main__":
    register()
