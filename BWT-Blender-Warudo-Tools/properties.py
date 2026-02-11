import bpy


class BWT_PG_WarudoToolsSettings(bpy.types.PropertyGroup):
    model_collection: bpy.props.PointerProperty(  # type:ignore
        type=bpy.types.Collection
    )  # type:ignore

    loaded_sanitized_model: bpy.props.PointerProperty(  # type:ignore
        type=bpy.types.Collection
    )  # type:ignore

    export_path: bpy.props.StringProperty(  # type:ignore
        name="Export Path", subtype="FILE_PATH", default=""
    )  # type:ignore


def get_bwt_properties(
    context: bpy.types.Context,
) -> BWT_PG_WarudoToolsSettings:
    """
    :rtype: BWT_PG_WarudoToolsSettings
    """
    return context.window_manager.bwt_warudo_tools_properties


def register_properties():
    bpy.types.WindowManager.bwt_warudo_tools_properties = bpy.props.PointerProperty(
        type=BWT_PG_WarudoToolsSettings
    )


def unregister_properties():
    del bpy.types.WindowManager.bwt_warudo_tools_properties
