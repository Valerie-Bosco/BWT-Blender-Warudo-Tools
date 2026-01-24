import bpy


class WT_PG_WarudoToolsSettings(bpy.types.PropertyGroup):
    export_path: bpy.props.StringProperty(  # type:ignore
        name="Export Path", subtype="FILE_PATH", default=""
    )


def register_properties():
    bpy.types.WindowManager.warudo_tools = bpy.props.PointerProperty(
        type=WT_PG_WarudoToolsSettings
    )


def unregister_properties():
    del bpy.types.WindowManager.warudo_tools
