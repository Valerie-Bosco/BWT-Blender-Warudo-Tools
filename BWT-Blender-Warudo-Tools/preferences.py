import bpy

from .modules.ALXAddonUpdater.ALXAddonUpdater.ALX_AddonUpdaterUI import (
    update_settings_ui,
)


class BWT_AddonPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    auto_check_update: bpy.props.BoolProperty(  # type:ignore
        name="Auto-check for Update",
        description="If enabled, auto-check for updates using an interval",
        default=False,
    )  # type:ignore

    updater_interval_months: bpy.props.IntProperty(  # type:ignore
        name="Months",
        description="Number of months between checking for updates",
        default=0,
        min=0,
    )  # type:ignore
    updater_interval_days: bpy.props.IntProperty(  # type:ignore
        name="Days",
        description="Number of days between checking for updates",
        default=7,
        min=0,
        max=31,
    )  # type:ignore
    updater_interval_hours: bpy.props.IntProperty(  # type:ignore
        name="Hours",
        description="Number of hours between checking for updates",
        default=0,
        min=0,
        max=23,
    )  # type:ignore
    updater_interval_minutes: bpy.props.IntProperty(  # type:ignore
        name="Minutes",
        description="Number of minutes between checking for updates",
        default=0,
        min=0,
        max=59,
    )  # type:ignore

    def draw(self, context: bpy.types.Context):
        layout = self.layout

        update_settings_ui(context, layout)
