"""
This harness file will deal with the login part of the code
"""
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.animation import Animation
from kivy.lang import Builder


WINDOW_SIZE = (305, 480)
LOGIN_UI = """
MDScreen:
    name: "Docto365"
    on_enter:
        app.anim(back)
        app.anim1(back1)
        app.icon_animation(icon)
        app.text_animation(label)
    MDFloatLayout:
        MDFloatLayout:
            id: back
            size_hint_y: .6
            pos_hint: {"center_y": 1.8}
            radius: [0, 0, 0, 50]
            canvas:
                Color:
                    rgb: (79/255, 195/255, 247/255, 1)
                Ellipse:
                    size: self.size
                    pos: self.pos
        MDFloatLayout:
            id: back1
            size_hint_y: .6
            pos_hint: {"center_y": 0.8}
            radius: [0, 0, 0, 50]
            canvas:
                Color:
                    rgb: (79/255, 195/255, 247/255, 1)
                Ellipse:
                    size: self.size
                    pos: self.pos
        MDIconButton:
            id: icon
            icon: "account-circle"
            pos_hint: {"center_x": .5, "center_y": .8}
            user_font_size: "60sp"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
        MDLabel:
            id: label
            text: f"[font=Arial]Docto365[/font]"
            markup: True
            pos_hint: {"center_y": .75}
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            font_style: "H5"
            opacity: 0
        MDTextField:
            id: email
            hint_text: "Email ID"
            helper_text: "Enter email ID"
            helper_text_mode: "on_focus"
            size_hint_x: .8
            pos_hint: {"center_x": .5, "center_y": .46}
            current_hint_text_color: 21/255, 101/255, 192/255, 1
            color_mode: "custom"
            line_color_focus: 79/255, 195/255, 247/255, 1
        MDTextField:
            id: password
            hint_text: "Password"
            password: True
            helper_text: "Enter Password"
            helper_text_mode: "on_focus"
            size_hint_x: .8
            pos_hint: {"center_x": .5, "center_y": .38}
            current_hint_text_color: 21/255, 101/255, 192/255, 1
            color_mode: "custom"
            line_color_focus: 79/255, 195/255, 247/255, 1
        MDFillRoundFlatButton:
            id: login_button
            text: "Login"
            pos_hint: {"center_x": .5, "center_y": .2}
            size_hint_x: .5
            md_bg_color: 1, 0, 0, 1
        MDTextButton:
            id: did_you_forget_text_button
            text: "forgot your password?"
            pos_hint: {"center_x": .5, "center_y": .1}
            font_style: "Body2"
            text_color: (1, 0, 0, 1)
"""


class LoginApp(MDApp):
    """
    This is the class for Login UI
    """

    def build(self):
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(Builder.load_string(LOGIN_UI))
        return self.screen_manager

    def change_screen(self, name):
        self.screen_manager.current = name

    def anim(self, widget):
        anim = Animation(pos_hint={"center_y": 1.16})
        anim.start(widget)

    def anim1(self, widget):
        anim = Animation(pos_hint={"center_y": .85})
        anim.start(widget)

    def icon_animation(self, widget):
        anim = Animation(pos_hint={"center_y": .8})
        anim += Animation(pos_hint={"center_y": .85})
        anim.start(widget)

    def text_animation(self, widget):
        anim = Animation(opacity=0, duration=2)
        anim += Animation(opacity=1)
        anim.start(widget)


if __name__ == "__main__":
    app = LoginApp()
    app.run()
