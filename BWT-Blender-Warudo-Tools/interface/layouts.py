import bpy

from .. import export
from .. import properties


class BWT_PT_WarudoNPanel(bpy.types.Panel):
    """"""

    bl_label = "Warudo"
    bl_idname = "BWT_PT_WarudoNPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    bl_category = "Warudo"

    @classmethod
    def poll(cls, context):
        return True

    def draw(self, context: bpy.types.Context):
        layout: bpy.types.UILayout = self.layout

        bwt_properties = properties.get_bwt_properties(context)

        layout.prop(bwt_properties, "model_collection", text="Model")
        row = layout.row().split(factor=0.25, align=True)
        row.operator(export.BWT_OT_WarudoFBXExport.bl_idname, text="FBX", icon="EXPORT")
        row.prop(bwt_properties, "export_path", icon="FILE_FOLDER", text="")


def register_interface():
    pass


def unregister_interface():
    pass
