import bpy

from ..operators import export


class WT_PT_WarudoNPanel(bpy.types.Panel):
    """"""

    bl_label = "Warudo"
    bl_idname = "ALX_PT_WarudoNPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    bl_category = "Warudo"

    @classmethod
    def poll(cls, context):
        return True

    def draw(self, context: bpy.types.Context):
        layout: bpy.types.UILayout = self.layout

        settings = context.window_manager.warudo_tools

        row = layout.row().split(factor=0.25, align=True)
        row.operator(export.WT_OT_WarudoFBXExport.bl_idname, text="FBX", icon="EXPORT")
        row.prop(settings, "export_path", icon="FILE_FOLDER", text="")


def register_interface():
    pass


def unregister_interface():
    pass
