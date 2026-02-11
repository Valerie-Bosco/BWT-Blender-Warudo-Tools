import bpy

from . import collection_utils, mesh_utils
from .. import properties


def get_model(context: bpy.types.Context) -> list[bpy.types.Object]:
    """
    get objects from "BWT_PG_WarudoToolsSettings -> model_collection" recursively


    :param context:
    :return:
    :rtype list[bpy.types.Object]:
    """
    target_collections = set()
    get_model_collection_list(context)

    return [
        collection_object
        for collection in target_collections
        for collection_object in collection.objects
        if (
            collection_object.type in ["MESH", "ARMATURE", "EMPTY"]
            and collection_object.hide_get() == False
        )
    ]


def get_model_collection(context: bpy.types.Context) -> bpy.types.Collection:
    return properties.get_bwt_properties(context).model_collection


def get_model_collection_list(
    context: bpy.types.Context,
) -> set[bpy.types.Collection] | None:
    model_collection = get_model_collection(context)

    if model_collection is not None:
        model_collection_list = {model_collection}
        collection_utils.recurse_collection(model_collection, model_collection_list)
        return model_collection_list
    return None


def load_sanitize_model(context: bpy.types.Context) -> str:
    """
    :param context:
    :return model name:
    """

    working_collection = properties.get_bwt_properties(
        context
    ).loaded_sanitized_model = collection_utils.duplicate_collection(
        get_model_collection(context), "[Export]"
    )

    mesh_utils.apply_all_transform(context, get_model(context))

    return working_collection.name


def discard_model(context: bpy.types.Context) -> None:
    if properties.get_bwt_properties(context).loaded_sanitized_model is not None:
        bpy.data.collections.remove(
            properties.get_bwt_properties(context).loaded_sanitized_model,
            do_unlink=True,
            do_id_user=True,
            do_ui_user=True,
        )
