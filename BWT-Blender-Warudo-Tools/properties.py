import bpy


class BWT_PG_WarudoToolsSettings(bpy.types.PropertyGroup):
    model_collection: bpy.props.PointerProperty(  # type:ignore
        type=bpy.types.Collection
    )

    export_path: bpy.props.StringProperty(  # type:ignore
        name="Export Path", subtype="FILE_PATH", default=""
    )


def register_properties():
    bpy.types.WindowManager.warudo_tools = bpy.props.PointerProperty(
        type=BWT_PG_WarudoToolsSettings
    )


def unregister_properties():
    del bpy.types.WindowManager.warudo_tools
