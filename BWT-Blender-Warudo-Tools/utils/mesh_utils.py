import bpy


def apply_all_transform(
    context: bpy.types.Context, target_objects=list[bpy.types.Object]
) -> None:
    if len(target_objects) > 0:
        target_context = context.copy()
        target_context["active_object"] = target_objects[0]
        target_context["selected_objects"] = target_objects

        with context.temp_override(**target_context):
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)


def scan_overlimit_vertex(mesh_object: bpy.types.Object):
    vertex_group_count_limit = 4

    for vertex in mesh_object.data.vertices:
        if len(vertex.groups) > vertex_group_count_limit:
            list({group.weight: group for group in vertex.groups}.keys()).sort()[
                0:vertex_group_count_limit
            ]

    # C.active_object.data.vertices[0].groups[1].weight
    # mesh_object.
