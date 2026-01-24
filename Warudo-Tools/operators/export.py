from pathlib import Path

import bpy

from ..properties import WT_PG_WarudoToolsSettings


def clone_model(context: bpy.types.Context) -> bpy.types.Collection:
    settings: WT_PG_WarudoToolsSettings = context.window_manager.warudo_tools

    if settings.model_collection is not None:
        target_collection = bpy.data.collections.get(settings.model_collection.name)

        duplicate_collection = target_collection.copy()
        duplicate_collection.name = f"{target_collection.name} [Export]"
        context.scene.collection.children.link(duplicate_collection)

        return duplicate_collection

    return None


def recurse_collections(
        collection: bpy.types.Collection, collection_list: set[bpy.types.Collection]
):
    for collection in collection.children_recursive:
        recurse_collections(collection, collection_list)
        collection_list.add(collection)


def apply_all(context: bpy.types.Context, collection: bpy.types.Collection):
    target_collections = set()
    recurse_collections(collection, target_collections)

    target_objects = [
        collection_object
        for collection in target_collections
        for collection_object in collection.objects
        if (
                collection_object.type in ["MESH", "ARMATURE"]
                and not collection_object.hide_get()
        )
    ]

    target_context = context.copy()
    target_context["active_object"] = target_objects[0]
    target_context["selected_objects"] = target_objects

    with context.temp_override(**target_context):
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)


class WT_OT_WarudoFBXExport(bpy.types.Operator):
    """"""

    bl_label = ""
    bl_idname = "wt.warudo_fbx_export"
    bl_description = "Export the active collection to FBX to the specified path. File name is determined by the active collection."
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return True

    def execute(self, context: bpy.types.Context):
        settings: WT_PG_WarudoToolsSettings = context.window_manager.warudo_tools

        model_collection = settings.model_collection

        if model_collection is not None:
            blend_file_path = settings.export_path
            export_path = (
                Path(blend_file_path)
                if blend_file_path != ""
                else Path(Path(blend_file_path).absolute().anchor)
            )

            duplicate_model_collection = clone_model(context)
            export_path = export_path.joinpath(f"{duplicate_model_collection.name}.fbx")

            apply_all(context, duplicate_model_collection)
            if duplicate_model_collection is not None:
                bpy.ops.export_scene.fbx(
                    filepath=str(export_path),
                    check_existing=True,
                    filter_glob="*.fbx",
                    use_selection=False,
                    use_visible=True,
                    use_active_collection=False,
                    collection=duplicate_model_collection.name,
                    global_scale=1.0,
                    apply_unit_scale=True,
                    apply_scale_options="FBX_SCALE_ALL",
                    use_space_transform=False,
                    bake_space_transform=True,
                    object_types={"ARMATURE", "CAMERA", "EMPTY", "MESH", "OTHER"},
                    use_mesh_modifiers=True,
                    use_mesh_modifiers_render=True,
                    mesh_smooth_type="FACE",
                    colors_type="SRGB",
                    prioritize_active_color=False,
                    use_subsurf=False,
                    use_mesh_edges=False,
                    use_tspace=False,
                    use_triangles=True,
                    use_custom_props=True,
                    add_leaf_bones=True,
                    primary_bone_axis="Y",
                    secondary_bone_axis="X",
                    use_armature_deform_only=False,
                    armature_nodetype="NULL",
                    bake_anim=True,
                    bake_anim_use_all_bones=True,
                    bake_anim_use_nla_strips=True,
                    bake_anim_use_all_actions=True,
                    bake_anim_force_startend_keying=True,
                    bake_anim_simplify_factor=1.0,
                    path_mode="COPY",
                    embed_textures=True,
                    batch_mode="OFF",
                    use_batch_own_dir=False,
                    use_metadata=True,
                    axis_forward="-Y",
                    axis_up="Z",
                )

                bpy.data.collections.remove(
                    duplicate_model_collection,
                    do_unlink=True,
                    do_id_user=True,
                    do_ui_user=True,
                )
        return {"FINISHED"}
