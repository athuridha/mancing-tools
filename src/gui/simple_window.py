"""Simple mode window - compact view with essential controls."""

import tkinter as tk
import customtkinter as ctk
from .components import ActionButton, StatusBar

class SimpleWindow(ctk.CTkToplevel):
    """Compact simple mode window with essential controls."""
    
    def __init__(self, parent_app):
        """Initialize simple window.
        
        Args:
            parent_app: Main application instance
        """
        super().__init__(parent_app)
        
        self.app = parent_app
        self.title("🎣 Mancing Simple")
        self.geometry("400x340")
        self.resizable(False, False)
        
        # Keep on top
        self.attributes("-topmost", True)
        
        # Center on screen
        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - 400) // 2
        y = (screen_height - 340) // 2
        self.geometry(f"400x340+{x}+{y}")
        
        # Build UI
        self._build_ui()
        
        # Override close button behavior
        self.protocol("WM_DELETE_WINDOW", self.on_close)
    
    def iconify(self):
        """Override iconify to minimize to tray instead."""
        # When user clicks minimize button, go to tray
        self.minimize_to_tray()
    
    def withdraw(self):
        """Override withdraw to properly hide window."""
        super().withdraw()
        
    def _build_ui(self):
        """Build simple mode UI."""
        # Main container
        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=12, pady=12)
        
        # Header with title and version
        header = ctk.CTkFrame(container, fg_color="transparent")
        header.pack(fill="x", pady=(0, 12))
        
        ctk.CTkLabel(header, text="🎣 Mancing Tools", 
                    font=ctk.CTkFont(size=18, weight="bold")).pack(side="left")
        
        from ..version import __version__
        ctk.CTkLabel(header, text=f"v{__version__}",
                    font=ctk.CTkFont(size=10),
                    fg_color=("#3B8ED0", "#1F6AA5"),
                    corner_radius=5,
                    padx=8, pady=3).pack(side="left", padx=(10,0))
        
        # === Control Section ===
        ctrl_card = ctk.CTkFrame(container)
        ctrl_card.pack(fill="x", pady=(0, 10))
        
        ctrl_inner = ctk.CTkFrame(ctrl_card, fg_color="transparent")
        ctrl_inner.pack(fill="x", padx=10, pady=10)
        
        key = self.app.var_key.get().upper()
        self.btn_start = ActionButton(ctrl_inner, text=f"Start ({key})", 
                                      primary=True, width=120,
                                      command=self.app.toggle_start)
        self.btn_start.pack(side="left", padx=(0,8))
        
        StatusBar(ctrl_inner, self.app.var_status, fg_color="transparent").pack(side="left", fill="x", expand=True)
        
        # === ROI Section ===
        roi_card = ctk.CTkFrame(container)
        roi_card.pack(fill="x", pady=(0, 10))
        
        ctk.CTkLabel(roi_card, text="🎯 Kalibrasi ROI",
                    font=ctk.CTkFont(size=13, weight="bold")).pack(anchor="w", padx=10, pady=(10,6))
        
        btn_row = ctk.CTkFrame(roi_card, fg_color="transparent")
        btn_row.pack(fill="x", padx=10, pady=(0,10))
        
        roi_key = self.app.var_roi_key.get().upper()
        ActionButton(btn_row, text=f"Drag-select ({roi_key})", width=170,
                    command=self.app.calibrate_by_selection).pack(side="left", padx=(0,6))
        ActionButton(btn_row, text="Debug", width=100,
                    command=self.app.toggle_debug).pack(side="left")
        
        # === Status Section ===
        status_card = ctk.CTkFrame(container)
        status_card.pack(fill="x", pady=(0, 12))
        
        ctk.CTkLabel(status_card, text="📊 Status",
                    font=ctk.CTkFont(size=13, weight="bold")).pack(anchor="w", padx=10, pady=(10,6))
        
        action_row = ctk.CTkFrame(status_card, fg_color="transparent")
        action_row.pack(fill="x", padx=10, pady=(0,10))
        
        ctk.CTkLabel(action_row, text="Action:", 
                    font=ctk.CTkFont(size=11)).pack(side="left")
        ctk.CTkLabel(action_row, textvariable=self.app.var_act,
                    font=ctk.CTkFont(size=11, weight="bold"),
                    text_color="#4ea3ff").pack(side="left", padx=(8,0))
        
        # === Footer Buttons ===
        footer = ctk.CTkFrame(container, fg_color="transparent")
        footer.pack(fill="x", pady=(0, 0))
        
        ActionButton(footer, text="⚙️ Settings", width=185,
                    command=self.open_settings).pack(side="left", padx=(0,6))
        ActionButton(footer, text="🔧 Advance Mode", width=185,
                    command=self.switch_to_advance).pack(side="left")
    
    def switch_to_advance(self):
        """Switch to advance mode."""
        self.app.exit_simple_mode()
    
    def minimize_to_tray(self):
        """Minimize to system tray."""
        self.app.tray_manager.minimize_to_tray()
        
    def open_settings(self):
        """Open settings in main window."""
        self.app.exit_simple_mode()
        self.app.menu_var.set("Settings")
        self.app._show_page("Settings")
        
    def on_close(self):
        """Handle window close."""
        self.app.on_closing()
        
    def update_start_button(self):
        """Update start/stop button text."""
        key = self.app.var_key.get().upper()
        if self.app.running:
            self.btn_start.configure(text=f"⏹ Stop ({key})")
        else:
            self.btn_start.configure(text=f"▶ Start ({key})")
