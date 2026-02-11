from pathlib import Path

import bpy

from . import properties
from .utils import model_utils


class BWT_OT_WarudoFBXExport(bpy.types.Operator):
    """"""

    bl_label = ""
    bl_idname = "bwt.warudo_fbx_export"
    bl_description = "Export the active target_collection to FBX to the specified path. File name is determined by the active target_collection."
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return True

    def execute(self, context: bpy.types.Context):
        bwt_properties = properties.get_bwt_properties(context)

        model_collection = model_utils.get_model_collection(context)

        if model_collection is not None:
            model_name = model_utils.load_sanitize_model(context)

            blend_file_path = bwt_properties.export_path
            export_path = (
                Path(blend_file_path)
                if blend_file_path != ""
                else Path(Path(blend_file_path).absolute().anchor)
            )
            export_path = export_path.joinpath(f"{model_name}.fbx")

            bpy.ops.export_scene.fbx(
                filepath=str(export_path),
                check_existing=True,
                filter_glob="*.fbx",
                use_selection=False,
                use_visible=True,
                use_active_collection=False,
                collection=model_name,
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
            model_utils.discard_model(context)
        return {"FINISHED"}
