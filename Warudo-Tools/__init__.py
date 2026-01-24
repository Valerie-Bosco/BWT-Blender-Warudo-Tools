import bpy

from .interface.layouts import register_interface, unregister_interface
from .modules.ALXAddonUpdater.ALXAddonUpdater.ALX_AddonUpdater import Alx_Addon_Updater
from .modules.ALXModuleManager.ALXModuleManager.ALX_ModuleManager import (
    Alx_Module_Manager,
)

bl_info = {
    "name": "Warudo-Tools",
    "author": "Valerie Bosco[Valerie Arhal]",
    "description": "",
    "warning": "",
    "version": (0, 1, 0),
    "blender": (3, 6, 0),
    "category": "3D View",
    "location": "",
    "doc_url": "https://github.com/Valerie-Bosco/Warudo-Tools/wiki",
    "tracker_url": "https://github.com/Valerie-Bosco/Warudo-Tools/issues",
}

module_manager = Alx_Module_Manager(path=__path__, globals=globals(), mute=True)
addon_updater = Alx_Addon_Updater(
    path=__path__,
    bl_info=bl_info,
    engine="Github",
    engine_user_name="Valerie-Bosco",
    engine_repo_name="Warudo-Tools",
    manual_download_website="https://github.com/Valerie-Bosco/Warudo-Tools/releases/tag/main_branch_latest",
)

from .properties import register_properties, unregister_properties


def register():
    module_manager.developer_register_modules()
    addon_updater.register_addon_updater(True)

    register_properties()

    register_interface()

    bpy.context.preferences.use_preferences_save = True


def unregister():
    module_manager.developer_unregister_modules()
    addon_updater.unregister_addon_updater()

    unregister_properties()

    unregister_interface()


if __name__ == "__main__":
    register()
