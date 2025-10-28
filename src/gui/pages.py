"""GUI pages for different sections."""

import tkinter as tk
import webbrowser
import customtkinter as ctk
from .components import (Card, StatusBar, ProgressIndicator, 
                        ActionButton, CompactSwitch, SettingSlider)

class HomePage:
    """Home page with main controls."""
    
    def __init__(self, parent, app):
        self.frame = ctk.CTkFrame(parent)
        self.app = app
        self._build()
        
    def _build(self):
        """Build home page UI."""
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        
        # Left: Controls
        self._build_left_panel()
        
        # Right: Status & Preview
        self._build_right_panel()
    
    def _build_left_panel(self):
        """Build left control panel."""
        left = ctk.CTkFrame(self.frame)
        left.grid(row=0, column=0, sticky="nsew", padx=(6,4), pady=6)
        left.grid_columnconfigure(0, weight=1)
        
        # Start/Stop section
        header = ctk.CTkFrame(left, fg_color="transparent")
        header.pack(fill="x", padx=8, pady=(8,4))
        
        self.btn_start = ActionButton(header, text="Start (F1)", primary=True,
                                      width=100, command=self.app.toggle_start)
        self.btn_start.pack(side="left", padx=(0,6))
        
        StatusBar(header, self.app.var_status, fg_color="transparent").pack(side="left")
        
        # Calibration card
        cal_card = Card(left, title="Kalibrasi ROI", icon="🎯")
        cal_card.pack(fill="x", padx=8, pady=(6,6))
        
        btn_row = ctk.CTkFrame(cal_card.content, fg_color="transparent")
        btn_row.pack(fill="x", pady=(0,6))
        
        # Get ROI key dynamically
        roi_key = self.app.var_roi_key.get().upper()
        ActionButton(btn_row, text=f"Drag-select ({roi_key})", width=140,
                    command=self.app.calibrate_by_selection).pack(side="left", padx=(0,4))
        ActionButton(btn_row, text="Debug", width=80,
                    command=self.app.toggle_debug).pack(side="left", padx=4)
        
        # Dimensions
        dim = ctk.CTkFrame(cal_card.content, fg_color="transparent")
        dim.pack(fill="x")
        
        ctk.CTkLabel(dim, text="W", font=ctk.CTkFont(size=11)).pack(side="left")
        ctk.CTkEntry(dim, width=60, textvariable=self.app.var_w, height=26).pack(side="left", padx=(4,8))
        ctk.CTkLabel(dim, text="H", font=ctk.CTkFont(size=11)).pack(side="left")
        ctk.CTkEntry(dim, width=60, textvariable=self.app.var_h, height=26).pack(side="left", padx=(4,8))
        ActionButton(dim, text="Apply", command=self.app.apply_wh, width=80).pack(side="left")
        
        # Auto-Pause card
        pause_card = Card(left, title="Auto-Pause", icon="⏸️")
        pause_card.pack(fill="x", padx=8, pady=(6,6))
        
        CompactSwitch(pause_card.content, text="Aktifkan",
                     variable=self.app.var_auto_pause_enabled).pack(anchor="w", pady=(0,1))
        CompactSwitch(pause_card.content, text="Pause saat ketik", indent=True,
                     variable=self.app.var_pause_on_typing).pack(anchor="w", pady=1)
        CompactSwitch(pause_card.content, text="Pause saat Alt+Tab", indent=True,
                     variable=self.app.var_pause_on_focus_loss).pack(anchor="w", pady=(1,2))
    
    def _build_right_panel(self):
        """Build right status panel."""
        right = ctk.CTkFrame(self.frame)
        right.grid(row=0, column=1, sticky="nsew", padx=(4,6), pady=6)
        right.grid_columnconfigure(0, weight=1)
        right.grid_rowconfigure(3, weight=1)
        
        # Status header
        head = ctk.CTkFrame(right, fg_color="transparent")
        head.grid(row=0, column=0, sticky="ew", padx=10, pady=(10,4))
        ctk.CTkLabel(head, text="📊 Status Live", 
                    font=ctk.CTkFont(size=13, weight="bold")).pack(side="left")
        
        # Progress indicators
        progress_frame = ctk.CTkFrame(right)
        progress_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=4)
        
        self.pb_g = ProgressIndicator(progress_frame, label="Green")
        self.pb_g.pack(fill="x", pady=(6,3))
        
        self.pb_r = ProgressIndicator(progress_frame, label="Red")
        self.pb_r.pack(fill="x", pady=(3,6))
        
        # Action label
        self.lbl_action = ctk.CTkLabel(right, textvariable=self.app.var_act, 
                                       font=ctk.CTkFont(size=13))
        self.lbl_action.grid(row=2, column=0, sticky="ew", padx=10, pady=(0,6))
        
        # Preview
        self.preview = ctk.CTkLabel(right, text="Preview ROI (aktif saat jalan)", 
                                   width=380, height=240,
                                   fg_color=("gray20","gray16"), 
                                   corner_radius=8,
                                   font=ctk.CTkFont(size=11))
        self.preview.grid(row=3, column=0, sticky="nsew", padx=10, pady=(4,10))
        
    def pack(self, **kwargs):
        """Pack the frame."""
        self.frame.pack(**kwargs)
        
    def pack_forget(self):
        """Hide the frame."""
        self.frame.pack_forget()


class SettingsPage:
    """Settings page for custom configuration."""
    
    def __init__(self, parent, app):
        self.frame = ctk.CTkFrame(parent)
        self.app = app
        self._build()
        
    def _build(self):
        """Build settings page UI with scrollable frame."""
        # Make frame responsive
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        
        # Create scrollable frame
        self.scrollable = ctk.CTkScrollableFrame(self.frame, fg_color="transparent")
        self.scrollable.grid(row=0, column=0, sticky="nsew", padx=8, pady=8)
        self.scrollable.grid_columnconfigure(0, weight=1)
        
        # Threshold & Interval Card
        card1 = Card(self.scrollable, title="Ambang & Interval", icon="⚙️")
        card1.grid(row=0, column=0, sticky="ew", padx=12, pady=(12,8))
        
        SettingSlider(card1.content, "Green ratio ≥", self.app.var_green_th, 
                     0.02, 0.50, 0.01).pack(fill="x", pady=4)
        SettingSlider(card1.content, "Red ratio ≥", self.app.var_red_th, 
                     0.02, 0.50, 0.01).pack(fill="x", pady=4)
        SettingSlider(card1.content, "Click interval (s)", self.app.var_click_i, 
                     0.01, 0.10, 0.001).pack(fill="x", pady=4)
        SettingSlider(card1.content, "Idle interval (s)", self.app.var_idle_i, 
                     0.005, 0.05, 0.001).pack(fill="x", pady=4)
        
        # Delay Settings Card
        card2 = Card(self.scrollable, title="Setting Delay", icon="⏱️")
        card2.grid(row=1, column=0, sticky="ew", padx=12, pady=8)
        
        SettingSlider(card2.content, "Hold awal (s)", self.app.var_hold_s, 
                     0.5, 10.0, 0.1).pack(fill="x", pady=4)
        SettingSlider(card2.content, "MouseDown (s)", self.app.var_down_s, 
                     0.005, 0.050, 0.001).pack(fill="x", pady=4)
        
        # Auto Recast Card
        card3 = Card(self.scrollable, title="Auto Recast", icon="🔄")
        card3.grid(row=2, column=0, sticky="ew", padx=12, pady=8)
        
        SettingSlider(card3.content, "Inactivity timeout (s)", self.app.var_inactive_to, 
                     0.4, 3.0, 0.1).pack(fill="x", pady=4)
        SettingSlider(card3.content, "Recast delay (s)", self.app.var_recast_delay, 
                     0.0, 1.0, 0.05).pack(fill="x", pady=4)
        
        CompactSwitch(card3.content, text="Aktifkan Auto Recast", 
                     variable=self.app.var_auto_recast).pack(anchor="w", pady=(6,4))
        
        # Preset buttons
        preset = ctk.CTkFrame(self.scrollable, fg_color="transparent")
        preset.grid(row=3, column=0, sticky="ew", padx=12, pady=(8,12))
        
        ActionButton(preset, text="💾 Simpan Preset", 
                    command=self.app.save_settings, width=140).pack(side="left", padx=(0,6))
        ActionButton(preset, text="📂 Muat Preset", 
                    command=self.app.load_settings, width=140).pack(side="left", padx=6)
        
    def pack(self, **kwargs):
        """Pack the frame."""
        self.frame.pack(**kwargs)
        
    def pack_forget(self):
        """Hide the frame."""
        self.frame.pack_forget()


class KeybindsPage:
    """Keybinds configuration page."""
    
    def __init__(self, parent, app):
        self.frame = ctk.CTkFrame(parent)
        self.app = app
        self.recording_type = None  # "macro" or "roi"
        self._build()
        
    def _build(self):
        """Build keybinds page UI."""
        # Main container
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        
        # Center content
        center = ctk.CTkFrame(self.frame, fg_color="transparent")
        center.grid(row=0, column=0)
        center.grid_columnconfigure(0, weight=1)
        
        # Title section
        title_frame = ctk.CTkFrame(center, fg_color="transparent")
        title_frame.pack(pady=(30,20))
        
        ctk.CTkLabel(title_frame, text="⌨️ Keybind Settings", 
                    font=ctk.CTkFont(size=20, weight="bold")).pack()
        ctk.CTkLabel(title_frame, text="Klik tombol keybind untuk mengubah", 
                    font=ctk.CTkFont(size=12),
                    text_color="gray60").pack(pady=(8,0))
        
        # Keybinds table - clean grid layout
        table = ctk.CTkFrame(center)
        table.pack(padx=40, pady=(10,20))
        
        # Configure grid weights for proper alignment
        table.grid_columnconfigure(0, weight=0, minsize=200)  # Label column - fixed width
        table.grid_columnconfigure(1, weight=0, minsize=120)  # Button column - fixed width
        table.grid_columnconfigure(2, weight=0, minsize=150)  # Status column - fixed width
        
        # Header (optional, can remove if too much)
        # ctk.CTkLabel(table, text="Function", font=ctk.CTkFont(size=11, weight="bold"),
        #             text_color="gray60").grid(row=0, column=0, padx=20, pady=(15,10), sticky="w")
        # ctk.CTkLabel(table, text="Key", font=ctk.CTkFont(size=11, weight="bold"),
        #             text_color="gray60").grid(row=0, column=1, padx=10, pady=(15,10))
        
        # Macro Start/Stop
        self._build_keybind_row(table, 0, "macro",
                               "🎣 Start/Stop Macro",
                               self.app.var_key)
        
        # Separator line
        separator = ctk.CTkFrame(table, height=1, fg_color=("gray70", "gray30"))
        separator.grid(row=1, column=0, columnspan=3, sticky="ew", padx=20, pady=10)
        
        # ROI Calibration
        self._build_keybind_row(table, 2, "roi",
                               "🎯 ROI Calibration",
                               self.app.var_roi_key)
        
        # Bottom info
        info_frame = ctk.CTkFrame(center, fg_color="transparent")
        info_frame.pack(pady=(15,30))
        
        ctk.CTkLabel(info_frame, text="💡 Supported keys: F1-F12, A-Z, 0-9", 
                    font=ctk.CTkFont(size=11),
                    text_color="gray55").pack()
    
    def _build_keybind_row(self, parent, row, bind_type, label, var):
        """Build a single keybind row with perfect alignment."""
        # Label - left aligned
        lbl = ctk.CTkLabel(parent, text=label, 
                          font=ctk.CTkFont(size=14),
                          anchor="w")
        lbl.grid(row=row, column=0, padx=(20,10), pady=18, sticky="w")
        
        # Key button - center aligned, consistent width
        key_btn = ctk.CTkButton(parent,
                               text=var.get().upper(),
                               command=lambda: self._start_recording(bind_type),
                               width=100,
                               height=38,
                               font=ctk.CTkFont(size=15, weight="bold"),
                               fg_color=("gray75", "gray25"),
                               hover_color=("gray70", "gray30"),
                               text_color=("#1f538d", "#4ea3ff"),
                               corner_radius=8)
        key_btn.grid(row=row, column=1, padx=10, pady=18)
        
        # Status label - left aligned, consistent width
        status_lbl = ctk.CTkLabel(parent, text="",
                                 font=ctk.CTkFont(size=11),
                                 width=150,
                                 anchor="w")
        status_lbl.grid(row=row, column=2, padx=(10,20), pady=18, sticky="w")
        
        # Store references
        if bind_type == "macro":
            self.macro_btn = key_btn
            self.macro_status = status_lbl
        else:
            self.roi_btn = key_btn
            self.roi_status = status_lbl
    
    def _start_recording(self, bind_type):
        """Start recording key press for specific keybind."""
        if self.recording_type is not None:
            return
            
        self.recording_type = bind_type
        
        if bind_type == "macro":
            btn = self.macro_btn
            status = self.macro_status
        else:
            btn = self.roi_btn
            status = self.roi_status
        
        # Change button appearance
        btn.configure(text="...", 
                     fg_color="#FF6B6B",
                     hover_color="#FF5555")
        status.configure(text="Press key (ESC cancel)", 
                        text_color="#FFD93D")
        
        # Bind key press event
        self.app.bind("<Key>", self._on_key_press)
    
    def _on_key_press(self, event):
        """Handle key press event."""
        if self.recording_type is None:
            return
            
        bind_type = self.recording_type
        
        # Get references
        if bind_type == "macro":
            btn = self.macro_btn
            status = self.macro_status
            var = self.app.var_key
        else:
            btn = self.roi_btn
            status = self.roi_status
            var = self.app.var_roi_key
        
        # Unbind immediately
        self.app.unbind("<Key>")
        self.recording_type = None
        
        # Reset button appearance
        btn.configure(fg_color=("gray75", "gray25"),
                     hover_color=("gray70", "gray30"))
        
        # Check if ESC (cancel)
        if event.keysym == "Escape":
            btn.configure(text=var.get().upper())
            status.configure(text="")
            return
        
        # Get key name
        key = event.keysym
        
        # Validate key
        valid_keys = []
        for i in range(1, 13):
            valid_keys.append(f"F{i}")
        for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            valid_keys.append(c.lower())
        for n in "0123456789":
            valid_keys.append(n)
        
        if key.lower() not in [k.lower() for k in valid_keys]:
            btn.configure(text=var.get().upper())
            status.configure(text="❌ Invalid key", 
                           text_color="#FF6B6B")
            self.app.after(2000, lambda: status.configure(text=""))
            return
        
        # Normalize key name
        normalized = key.upper()
        
        # Check if key already in use
        other_var = self.app.var_roi_key if bind_type == "macro" else self.app.var_key
        if normalized == other_var.get().upper():
            btn.configure(text=var.get().upper())
            status.configure(text="❌ Already in use", 
                           text_color="#FF6B6B")
            self.app.after(2000, lambda: status.configure(text=""))
            return
        
        # Update button text
        btn.configure(text=normalized)
        var.set(normalized)
        
        # Apply keybind
        if bind_type == "macro":
            ok, msg = self.app._bind_hotkey(normalized)
            if ok:
                status.configure(text="✅ Updated", text_color="#6BCF7F")
                self.app._update_button_text()
            else:
                status.configure(text="❌ Failed", text_color="#FF6B6B")
        else:
            ok, msg = self.app._bind_roi_hotkey(normalized)
            if ok:
                status.configure(text="✅ Updated", text_color="#6BCF7F")
                # Update home page button if needed
                try:
                    # This will be visible after navigation
                    pass
                except:
                    pass
            else:
                status.configure(text="❌ Failed", text_color="#FF6B6B")
        
        # Clear status after 2 seconds
        self.app.after(2000, lambda: status.configure(text=""))
        
    def pack(self, **kwargs):
        """Pack the frame."""
        self.frame.pack(**kwargs)
        
    def pack_forget(self):
        """Hide the frame."""
        self.frame.pack_forget()


class CreditPage:
    """Credit and update page."""
    
    def __init__(self, parent, app):
        self.frame = ctk.CTkFrame(parent)
        self.app = app
        self._build()
        
    def _build(self):
        """Build credit page UI."""
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        
        # Center container with scrollable frame
        scrollable = ctk.CTkScrollableFrame(self.frame, fg_color="transparent")
        scrollable.grid(row=0, column=0, sticky="nsew", padx=12, pady=12)
        scrollable.grid_columnconfigure(0, weight=1)
        
        # Version info at top
        from ..version import __version__
        version_frame = ctk.CTkFrame(scrollable, fg_color="transparent")
        version_frame.grid(row=0, column=0, pady=(10,5))
        ctk.CTkLabel(version_frame, text=f"🎣 Macro Mancing Indovoice", 
                    font=ctk.CTkFont(size=18, weight="bold")).pack()
        ctk.CTkLabel(version_frame, text=f"Version {__version__}", 
                    font=ctk.CTkFont(size=12), 
                    text_color="gray70").pack(pady=(5,0))
        
        # Separator
        separator1 = ctk.CTkFrame(scrollable, height=2, fg_color=("gray70", "gray30"))
        separator1.grid(row=1, column=0, sticky="ew", padx=50, pady=15)
        
        # Credit Section
        credit_box = ctk.CTkFrame(scrollable)
        credit_box.grid(row=2, column=0, sticky="ew", padx=20, pady=10)
        
        ctk.CTkLabel(credit_box, text="Credit", 
                    font=ctk.CTkFont(size=16, weight="bold")).pack(pady=(15,10))
        
        # Roblox Account
        roblox_frame = ctk.CTkFrame(credit_box, fg_color="transparent")
        roblox_frame.pack(pady=(5,10), padx=20)
        ctk.CTkLabel(roblox_frame, text="Roblox Account", 
                    font=ctk.CTkFont(size=13, weight="bold")).pack(pady=(5,3))
        roblox_url = "https://www.roblox.com/share?code=e089bc5df260ea42890e0e800c13faec&type=Profile&source=ProfileShare&stamp=1761572014538"
        roblox_lbl = ctk.CTkLabel(roblox_frame,
                                  text="lamont (@xinnercy)",
                                  font=ctk.CTkFont(size=12, underline=True),
                                  text_color="#4ea3ff",
                                  cursor="hand2")
        roblox_lbl.pack()
        roblox_lbl.bind("<Button-1>", lambda e: webbrowser.open(roblox_url))
        
        # Discord
        discord_frame = ctk.CTkFrame(credit_box, fg_color="transparent")
        discord_frame.pack(pady=(5,15), padx=20)
        ctk.CTkLabel(discord_frame, text="Discord", 
                    font=ctk.CTkFont(size=13, weight="bold")).pack(pady=(5,3))
        discord_url = "https://discord.gg/SWzSjeF3"
        disc_lbl = ctk.CTkLabel(discord_frame,
                                text="halflucifer",
                                font=ctk.CTkFont(size=12, underline=True),
                                text_color="#4ea3ff",
                                cursor="hand2")
        disc_lbl.pack()
        disc_lbl.bind("<Button-1>", lambda e: webbrowser.open(discord_url))
        
        # Separator
        separator2 = ctk.CTkFrame(scrollable, height=2, fg_color=("gray70", "gray30"))
        separator2.grid(row=3, column=0, sticky="ew", padx=50, pady=15)
        
        # Update Section
        update_box = ctk.CTkFrame(scrollable)
        update_box.grid(row=4, column=0, sticky="ew", padx=20, pady=(10,20))
        
        ctk.CTkLabel(update_box, text="Software Update", 
                    font=ctk.CTkFont(size=16, weight="bold")).pack(pady=(15,10))
        
        ctk.CTkLabel(update_box, text="Cek apakah ada versi terbaru", 
                    font=ctk.CTkFont(size=11),
                    text_color="gray60").pack(pady=(0,10))
        
        # Update button
        self.btn_update = ctk.CTkButton(update_box, 
                                       text="🔄 Cek Update", 
                                       command=self.app.check_updates,
                                       width=220, 
                                       height=40,
                                       font=ctk.CTkFont(size=13, weight="bold"),
                                       corner_radius=8)
        self.btn_update.pack(pady=(5,12))
        
        # Update status
        self.lbl_update_status = ctk.CTkLabel(update_box, 
                                             text="", 
                                             font=ctk.CTkFont(size=11),
                                             wraplength=300)
        self.lbl_update_status.pack(pady=(0,15))
              
    def pack(self, **kwargs):
        """Pack the frame."""
        self.frame.pack(**kwargs)
        
    def pack_forget(self):
        """Hide the frame."""
        self.frame.pack_forget()
