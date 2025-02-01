import bpy
from . import MainPanel
from ..model_selection.active_object import *
from ..warnings.ops_fix_old_UI import check_old_UI
from .. import __package__ as base_package
from .menu_configure import row_scale


class PANEL_PT_MustardUI_InitPanel_External(MainPanel, bpy.types.Panel):
    bl_label = "External Add-ons"
    bl_parent_id = "PANEL_PT_MustardUI_InitPanel"
    bl_options = {"DEFAULT_CLOSED"}

    @classmethod
    def poll(cls, context):
        if check_old_UI():
            return False

        res, arm = mustardui_active_object(context, config=1)
        addon_prefs = context.preferences.addons[base_package].preferences
        return res and addon_prefs.developer

    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon="EXPORT")

    def draw(self, context):

        layout = self.layout

        res, arm = mustardui_active_object(context, config=1)
        rig_settings = arm.MustardUI_RigSettings

        box = layout.box()
        box.label(text="Enable Support", icon="MODIFIER")
        row = box.row()
        row.prop(rig_settings, "diffeomorphic_support")
        if rig_settings.diffeomorphic_support:

            box = layout.box()

            box.label(text="Diffeomorphic Settings", icon="OUTLINER_DATA_SURFACE")

            box2 = box.box()
            box2.label(text="Morphs", icon="SHAPEKEY_DATA")
            col = box2.column()
            col.prop(rig_settings, "diffeomorphic_emotions_units")
            col.prop(rig_settings, "diffeomorphic_emotions")
            if rig_settings.diffeomorphic_emotions:
                row = col.row(align=True)
                row.label(text="Custom morphs")
                row.scale_x = row_scale
                row.prop(rig_settings, "diffeomorphic_emotions_custom", text="")
            col.prop(rig_settings, "diffeomorphic_facs_emotions_units")
            col.prop(rig_settings, "diffeomorphic_facs_emotions")
            col.prop(rig_settings, "diffeomorphic_body_morphs")
            if rig_settings.diffeomorphic_body_morphs:
                row = col.row(align=True)
                row.label(text="Custom morphs")
                row.scale_x = row_scale
                row.prop(rig_settings, "diffeomorphic_body_morphs_custom", text="")

            box2.separator()
            row = box2.row(align=True)
            row.label(text="Disable Exceptions")
            row.scale_x = row_scale
            row.prop(rig_settings, "diffeomorphic_disable_exceptions", text="")

            box = box.box()
            box.label(text="  Current morphs number: " + str(rig_settings.diffeomorphic_morphs_number))
            box.operator('mustardui.morphs_check')


def register():
    bpy.utils.register_class(PANEL_PT_MustardUI_InitPanel_External)


def unregister():
    bpy.utils.unregister_class(PANEL_PT_MustardUI_InitPanel_External)
