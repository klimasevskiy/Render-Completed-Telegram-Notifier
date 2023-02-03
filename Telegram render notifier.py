import bpy
import requests

bl_info = {
    "name": "Render Completed Telegram Notifier",
    "author": "Klimasevskiy",
    "version": (1, 0),
    "blender": (3, 3, 0),
    "location": "Render Properties > Render Engine",
    "description": "Sends a Telegram message when render is complete",
    "warning": "this addon is in beta version",
    "doc_url": "https://github.com/klimasevskiy/Render-Completed-Telegram-Notifier",
    "tracker_url": "https://t.me/klimasevskiy",
    "category": "Render"
}

class RenderCompleteOperator(bpy.types.Operator):
    bl_idname = "render.render_complete_operator"
    bl_label = "Render complete operator"

    def execute(self, context):
        print("function executed")
        bot_token = bpy.context.preferences.addons[__name__].preferences.bot_token
        print("bot token set")
        chat_id = bpy.context.preferences.addons[__name__].preferences.chat_id
        print("chat id set")
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        message = "Render has completed.\n____"
        filepath = bpy.context.blend_data.filepath
        print(filepath)
        message += f"\nProject filepath: {filepath}"
        data = {
            "chat_id": chat_id,
            "text": message
        }
        response = requests.post(url, json=data)
        print("Message sent")
        if response.status_code != 200:
            self.report({"WARNING"}, "Could not send message to Telegram. Please check your preferences")
        return {"FINISHED"}


class RenderCompletePanel(bpy.types.AddonPreferences):
    bl_idname = __name__

    bot_token: bpy.props.StringProperty(name="Bot token", description="Bot token")
    chat_id: bpy.props.StringProperty(name="Chat ID", description="Chat ID")

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "bot_token")
        layout.prop(self, "chat_id")

def register():
    print("Addon registered")
    bpy.utils.register_class(RenderCompleteOperator)
    bpy.utils.register_class(RenderCompletePanel)
    bpy.app.handlers.render_complete.append(RenderCompleteOperator.execute)
    bot_token = bpy.context.preferences.addons[__name__].preferences.bot_token
    print(f"bot token: {bot_token}")
    chat_id = bpy.context.preferences.addons[__name__].preferences.chat_id
    print(f"chat_id: {chat_id}")
    bpy.app.handlers.persistent(RenderCompleteOperator.execute)


def unregister():
    print("Addon unregistered")
    bpy.app.handlers.render_complete.remove(RenderCompleteOperator.execute)
    bpy.utils.unregister_class(RenderCompletePanel)
    bpy.utils.unregister_class(RenderCompleteOperator)


if __name__ == "__main__":
    register()
