from settings import Colors, Fonts
import customtkinter as ctk


class SettingsButtons(ctk.CTkButton):
    def __init__(self, parent, text, func=None):
        super().__init__(
            master=parent,
            text=text,
            command=func,
            font=ctk.CTkFont(family=Fonts.NORMAL, size=Fonts.NORMAL_SIZE),
            fg_color=Colors.BUTTON,
            hover_color=Colors.BUTTON_HOVER,
        )


class SettingsEntry(ctk.CTkEntry):
    def __init__(self, parent, textvariable):
        super().__init__(
            master=parent,
            textvariable=textvariable,
            font=ctk.CTkFont(family=Fonts.NORMAL, size=Fonts.NORMAL_SIZE),
        )

        self.pack(expand=True, fill="x", padx=10, pady=5)
