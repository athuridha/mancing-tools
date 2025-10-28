"""Reusable GUI components."""

import tkinter as tk
import customtkinter as ctk


class Card(ctk.CTkFrame):
    """Card component with title and content area."""
    
    def __init__(self, parent, title="", icon="", **kwargs):
        super().__init__(parent, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        
        if title:
            header = ctk.CTkFrame(self, fg_color="transparent")
            header.grid(row=0, column=0, sticky="ew", padx=8, pady=(8,4))
            
            title_text = f"{icon} {title}" if icon else title
            ctk.CTkLabel(header, text=title_text,
                        font=ctk.CTkFont(size=13, weight="bold")).pack(side="left")
        
        self.content = ctk.CTkFrame(self, fg_color="transparent")
        self.content.grid(row=1, column=0, sticky="nsew", padx=8, pady=(0,8))
        

class StatusBar(ctk.CTkFrame):
    """Status bar with indicators."""
    
    def __init__(self, parent, status_var, **kwargs):
        super().__init__(parent, **kwargs)
        self.status_var = status_var
        
        self.status_label = ctk.CTkLabel(self, textvariable=status_var,
                                         font=ctk.CTkFont(size=12))
        self.status_label.pack(side="left", padx=10)
        
    def set_status(self, text, color=None):
        """Update status text and color."""
        self.status_var.set(text)
        if color:
            self.status_label.configure(text_color=color)


class ProgressIndicator(ctk.CTkFrame):
    """Progress bar with label."""
    
    def __init__(self, parent, label="", **kwargs):
        super().__init__(parent, fg_color="transparent", **kwargs)
        self.grid_columnconfigure(1, weight=1)
        
        ctk.CTkLabel(self, text=label, font=ctk.CTkFont(size=11)).grid(
            row=0, column=0, padx=(4,6), sticky="w"
        )
        
        self.progress = ctk.CTkProgressBar(self, height=14)
        self.progress.grid(row=0, column=1, sticky="ew", padx=(0,8))
        self.progress.set(0)
        
    def set_value(self, value):
        """Update progress value (0-1)."""
        self.progress.set(max(0.0, min(1.0, value)))


class ActionButton(ctk.CTkButton):
    """Styled action button."""
    
    def __init__(self, parent, text="", icon="", primary=False, **kwargs):
        display_text = f"{icon} {text}" if icon else text
        
        if primary:
            super().__init__(parent, text=display_text,
                           font=ctk.CTkFont(size=13, weight="bold"),
                           height=32, **kwargs)
        else:
            super().__init__(parent, text=display_text,
                           height=28, **kwargs)


class SettingSlider(ctk.CTkFrame):
    """Setting slider with label and value display."""
    
    def __init__(self, parent, label, variable, min_val, max_val, step, **kwargs):
        super().__init__(parent, fg_color="transparent", **kwargs)
        self.variable = variable
        
        ctk.CTkLabel(self, text=label, font=ctk.CTkFont(size=11)).pack(side="left")
        
        slider = ctk.CTkSlider(self, from_=min_val, to=max_val,
                              number_of_steps=int((max_val - min_val) / step))
        slider.pack(side="left", fill="x", expand=True, padx=10)
        slider.set(variable.get())
        
        self.value_label = ctk.CTkLabel(self, text=f"{variable.get():.3f}",
                                        font=ctk.CTkFont(size=11))
        self.value_label.pack(side="right", padx=6)
        
        def on_change(value):
            v = round(float(value), 4)
            variable.set(v)
            self.value_label.configure(text=f"{v:.3f}")
        
        slider.configure(command=on_change)


class CompactSwitch(ctk.CTkSwitch):
    """Compact switch with smaller font."""
    
    def __init__(self, parent, text="", indent=False, **kwargs):
        display_text = f"  └ {text}" if indent else text
        font_size = 10 if indent else 12
        
        super().__init__(parent, text=display_text,
                        font=ctk.CTkFont(size=font_size), **kwargs)
