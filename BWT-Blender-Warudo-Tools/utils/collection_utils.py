import bpy


def link_collection_to_scene(
    context: bpy.types.Context, collection: bpy.types.Collection
):
    context.scene.collection.children.link(collection)


def duplicate_collection(
    target_collection: bpy.types.Collection,
    tag: str = "[Export]",
) -> bpy.types.Collection:
    duplicate_target_collection = target_collection.copy()
    duplicate_target_collection.name = f"{target_collection.name} {tag}"

    return duplicate_target_collection


def recurse_collection(
    target_collection: bpy.types.Collection, collection_list: set[bpy.types.Collection]
) -> None:
    for child_collection in target_collection.children_recursive:
        recurse_collection(child_collection, collection_list)
        collection_list.add(child_collection)
