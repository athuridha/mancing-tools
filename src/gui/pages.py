"""GUI pages for different sections."""

import tkinter as tk
import webbrowser
import customtkinter as ctk

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
        left = ctk.CTkFrame(self.frame)
        left.grid(row=0, column=0, sticky="nsew", padx=(8,6), pady=8)
        left.grid_columnconfigure(0, weight=1)
        
        # Start/Stop header
        header = ctk.CTkFrame(left, fg_color="transparent")
        header.pack(fill="x", padx=10, pady=(10,6))
        self.btn_start = ctk.CTkButton(header, text="Start (F1)", width=110, 
                                       command=self.app.toggle_start)
        self.btn_start.pack(side="left", padx=(0,8))
        ctk.CTkLabel(header, textvariable=self.app.var_status).pack(side="left")
        
        # Calibration group
        cal = ctk.CTkFrame(left)
        cal.pack(fill="x", padx=10, pady=(8,8))
        ctk.CTkLabel(cal, text="Kalibrasi ROI", 
                    font=ctk.CTkFont(weight="bold")).pack(anchor="w", padx=10, pady=(10,6))
        row1 = ctk.CTkFrame(cal, fg_color="transparent")
        row1.pack(fill="x", padx=10, pady=(0,8))
        ctk.CTkButton(row1, text="Kursor → ROI", 
                     command=self.app.calibrate_from_cursor).pack(side="left", padx=(0,8))
        ctk.CTkButton(row1, text="Drag-select ROI", 
                     command=self.app.calibrate_by_selection).pack(side="left", padx=8)
        ctk.CTkButton(row1, text="Debug", 
                     command=self.app.toggle_debug).pack(side="left", padx=8)
        
        # Dimensions
        dim = ctk.CTkFrame(cal, fg_color="transparent")
        dim.pack(fill="x", padx=10, pady=(0,12))
        ctk.CTkLabel(dim, text="W").pack(side="left")
        ctk.CTkEntry(dim, width=70, textvariable=self.app.var_w).pack(side="left", padx=(6,12))
        ctk.CTkLabel(dim, text="H").pack(side="left")
        ctk.CTkEntry(dim, width=70, textvariable=self.app.var_h).pack(side="left", padx=(6,12))
        ctk.CTkButton(dim, text="Terapkan W/H", command=self.app.apply_wh, 
                     width=130).pack(side="left")
        
        # Right: Live Status + Preview
        right = ctk.CTkFrame(self.frame)
        right.grid(row=0, column=1, sticky="nsew", padx=(6,8), pady=8)
        right.grid_columnconfigure(0, weight=1)
        right.grid_rowconfigure(3, weight=1)
        
        head = ctk.CTkFrame(right, fg_color="transparent")
        head.grid(row=0, column=0, sticky="ew", padx=12, pady=(12,6))
        ctk.CTkLabel(head, text="Status Live", 
                    font=ctk.CTkFont(weight="bold")).pack(side="left")
        
        # Progress bars
        bars = ctk.CTkFrame(right)
        bars.grid(row=1, column=0, sticky="ew", padx=12, pady=6)
        bars.grid_columnconfigure(1, weight=1)
        ctk.CTkLabel(bars, text="Green").grid(row=0, column=0, padx=(6,8), pady=(8,4), sticky="w")
        self.pb_g = ctk.CTkProgressBar(bars, height=16)
        self.pb_g.grid(row=0, column=1, padx=(0,12), pady=(8,4), sticky="ew")
        ctk.CTkLabel(bars, text="Red").grid(row=1, column=0, padx=(6,8), pady=(4,8), sticky="w")
        self.pb_r = ctk.CTkProgressBar(bars, height=16)
        self.pb_r.grid(row=1, column=1, padx=(0,12), pady=(4,8), sticky="ew")
        
        self.lbl_action = ctk.CTkLabel(right, textvariable=self.app.var_act, 
                                       font=ctk.CTkFont(size=14))
        self.lbl_action.grid(row=2, column=0, sticky="ew", padx=12, pady=(0,8))
        
        self.preview = ctk.CTkLabel(right, text="Preview ROI (aktif saat jalan)", 
                                   width=460, height=300,
                                   fg_color=("gray20","gray16"), corner_radius=10)
        self.preview.grid(row=3, column=0, sticky="nsew", padx=12, pady=(6,12))
        
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
        
        # Ambang & Interval
        section1 = ctk.CTkFrame(self.scrollable)
        section1.grid(row=0, column=0, sticky="ew", padx=12, pady=(12,8))
        ctk.CTkLabel(section1, text="Ambang & Interval", 
                    font=ctk.CTkFont(weight="bold")).pack(anchor="w", padx=10, pady=(10,6))
        self._slider(section1, "Green ratio ≥", self.app.var_green_th, 0.02, 0.50, 0.01)
        self._slider(section1, "Red ratio ≥", self.app.var_red_th, 0.02, 0.50, 0.01)
        self._slider(section1, "Click interval (s)", self.app.var_click_i, 0.01, 0.10, 0.001)
        self._slider(section1, "Idle interval (s)", self.app.var_idle_i, 0.005, 0.05, 0.001)
        
        # Delay Settings
        section2 = ctk.CTkFrame(self.scrollable)
        section2.grid(row=1, column=0, sticky="ew", padx=12, pady=8)
        ctk.CTkLabel(section2, text="Setting Delay", 
                    font=ctk.CTkFont(weight="bold")).pack(anchor="w", padx=10, pady=(10,6))
        self._slider(section2, "Hold awal (s)", self.app.var_hold_s, 0.5, 10.0, 0.1)
        self._slider(section2, "MouseDown (s)", self.app.var_down_s, 0.005, 0.050, 0.001)
        
        # Auto Recast
        section3 = ctk.CTkFrame(self.scrollable)
        section3.grid(row=2, column=0, sticky="ew", padx=12, pady=8)
        ctk.CTkLabel(section3, text="Auto Recast", 
                    font=ctk.CTkFont(weight="bold")).pack(anchor="w", padx=10, pady=(10,6))
        self._slider(section3, "Inactivity timeout (s)", self.app.var_inactive_to, 0.4, 3.0, 0.1)
        self._slider(section3, "Recast delay (s)", self.app.var_recast_delay, 0.0, 1.0, 0.05)
        sw = ctk.CTkSwitch(section3, text="Aktifkan Auto Recast", 
                          variable=self.app.var_auto_recast)
        sw.pack(anchor="w", padx=10, pady=(6,10))
        
        # Auto-Pause Section
        section4 = ctk.CTkFrame(self.scrollable)
        section4.grid(row=3, column=0, sticky="ew", padx=12, pady=8)
        ctk.CTkLabel(section4, text="⏸️ Auto-Pause", 
                    font=ctk.CTkFont(weight="bold")).pack(anchor="w", padx=10, pady=(10,6))
        
        # Master toggle
        sw_enabled = ctk.CTkSwitch(section4, text="Aktifkan Auto-Pause", 
                                   variable=self.app.var_auto_pause_enabled)
        sw_enabled.pack(anchor="w", padx=10, pady=(6,4))
        
        # Sub-options
        sw_typing = ctk.CTkSwitch(section4, text="  └ Pause saat mengetik di game", 
                                  variable=self.app.var_pause_on_typing)
        sw_typing.pack(anchor="w", padx=10, pady=2)
        
        sw_focus = ctk.CTkSwitch(section4, text="  └ Pause saat window loses focus", 
                                 variable=self.app.var_pause_on_focus_loss)
        sw_focus.pack(anchor="w", padx=10, pady=2)
        
        # Resume delay
        self._slider(section4, "  └ Resume delay (s)", 
                    self.app.var_auto_pause_resume_delay, 0.5, 5.0, 0.5)
        
        # Info text
        info = ctk.CTkLabel(section4, 
                           text="💡 Auto-pause akan menghentikan sementara macro\nsaat Anda mengetik atau Alt+Tab keluar game",
                           font=ctk.CTkFont(size=10),
                           text_color="gray60",
                           justify="left")
        info.pack(anchor="w", padx=10, pady=(6,10))
        
        # Preset buttons - Fixed at bottom
        preset = ctk.CTkFrame(self.scrollable, fg_color="transparent")
        preset.grid(row=4, column=0, sticky="ew", padx=12, pady=(8,12))
        ctk.CTkButton(preset, text="Simpan Preset", 
                     command=self.app.save_settings, width=120).pack(side="left", padx=(0,6))
        ctk.CTkButton(preset, text="Muat Preset", 
                     command=self.app.load_settings, width=120).pack(side="left", padx=6)
        
    def _slider(self, parent, text, var, mn, mx, step):
        """Create a slider row."""
        row = ctk.CTkFrame(parent, fg_color="transparent")
        row.pack(fill="x", padx=10, pady=4)
        ctk.CTkLabel(row, text=text).pack(side="left")
        s = ctk.CTkSlider(row, from_=mn, to=mx, number_of_steps=int((mx-mn)/step))
        s.pack(side="left", fill="x", expand=True, padx=10)
        s.set(var.get())
        val = ctk.CTkLabel(row, text=f"{var.get():.3f}")
        val.pack(side="right", padx=6)
        
        def _on_change(value):
            v = round(float(value), 4)
            var.set(v)
            val.configure(text=f"{v:.3f}")
        s.configure(command=_on_change)
        
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
        self.recording = False
        self._build()
        
    def _build(self):
        """Build keybinds page UI."""
        # Main container
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        
        # Center content
        center = ctk.CTkFrame(self.frame, fg_color="transparent")
        center.grid(row=0, column=0)
        
        # Keybind box
        box = ctk.CTkFrame(center)
        box.pack(padx=20, pady=20)
        
        # Title
        ctk.CTkLabel(box, text="Keybind Start/Stop", 
                    font=ctk.CTkFont(size=16, weight="bold")).pack(padx=20, pady=(20,10))
        
        # Description
        ctk.CTkLabel(box, text="Tekan tombol untuk set keybind baru", 
                    font=ctk.CTkFont(size=11),
                    text_color="gray60").pack(padx=20, pady=(0,15))
        
        # Current key display
        key_frame = ctk.CTkFrame(box)
        key_frame.pack(padx=20, pady=10, fill="x")
        
        ctk.CTkLabel(key_frame, text="Current Key:", 
                    font=ctk.CTkFont(size=12)).pack(side="left", padx=(10,5), pady=10)
        
        self.lbl_current_key = ctk.CTkLabel(key_frame, 
                                           text=self.app.var_key.get().upper(),
                                           font=ctk.CTkFont(size=14, weight="bold"),
                                           text_color="#4ea3ff")
        self.lbl_current_key.pack(side="left", padx=5, pady=10)
        
        # Record button
        self.btn_record = ctk.CTkButton(box, 
                                       text="⌨️ Tekan untuk Set Keybind",
                                       command=self._start_recording,
                                       width=250,
                                       height=50,
                                       font=ctk.CTkFont(size=13, weight="bold"),
                                       corner_radius=10)
        self.btn_record.pack(padx=20, pady=(15,10))
        
        # Status label
        self.lbl_status = ctk.CTkLabel(box, text="", 
                                      font=ctk.CTkFont(size=11),
                                      wraplength=280)
        self.lbl_status.pack(padx=20, pady=(5,10))
        
        # Hotkey status (global/local)
        self.lbl_hotkey_status = ctk.CTkLabel(box, text="",
                                             font=ctk.CTkFont(size=10),
                                             text_color="gray60",
                                             wraplength=280)
        self.lbl_hotkey_status.pack(padx=20, pady=(5,20))
        
        # Supported keys info
        info_frame = ctk.CTkFrame(box, fg_color="transparent")
        info_frame.pack(padx=20, pady=(10,20))
        
        ctk.CTkLabel(info_frame, text="Supported keys:", 
                    font=ctk.CTkFont(size=10, weight="bold"),
                    text_color="gray70").pack(anchor="w")
        ctk.CTkLabel(info_frame, text="• F1-F12 (Function keys)", 
                    font=ctk.CTkFont(size=9),
                    text_color="gray60").pack(anchor="w", padx=(10,0))
        ctk.CTkLabel(info_frame, text="• A-Z (Letters)", 
                    font=ctk.CTkFont(size=9),
                    text_color="gray60").pack(anchor="w", padx=(10,0))
        ctk.CTkLabel(info_frame, text="• 0-9 (Numbers)", 
                    font=ctk.CTkFont(size=9),
                    text_color="gray60").pack(anchor="w", padx=(10,0))
    
    def _start_recording(self):
        """Start recording key press."""
        if self.recording:
            return
            
        self.recording = True
        self.btn_record.configure(text="⏸️ Tekan Tombol Sekarang...", 
                                 fg_color="#FF6B6B")
        self.lbl_status.configure(text="Menunggu input... (ESC untuk batal)", 
                                 text_color="#FFD93D")
        
        # Bind key press event
        self.app.bind("<Key>", self._on_key_press)
    
    def _on_key_press(self, event):
        """Handle key press event."""
        if not self.recording:
            return
            
        # Unbind immediately
        self.app.unbind("<Key>")
        self.recording = False
        
        # Reset button
        self.btn_record.configure(text="⌨️ Tekan untuk Set Keybind", 
                                 fg_color=["#3B8ED0", "#1F6AA5"])
        
        # Check if ESC (cancel)
        if event.keysym == "Escape":
            self.lbl_status.configure(text="Dibatalkan", text_color="gray60")
            return
        
        # Get key name
        key = event.keysym
        
        # Validate key
        valid_keys = []
        # F-keys
        for i in range(1, 13):
            valid_keys.append(f"F{i}")
        # Letters
        for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            valid_keys.append(c.lower())
        # Numbers
        for n in "0123456789":
            valid_keys.append(n)
        
        if key.lower() not in [k.lower() for k in valid_keys]:
            self.lbl_status.configure(text=f"❌ Key '{key}' tidak didukung!", 
                                     text_color="#FF6B6B")
            return
        
        # Normalize key name
        if key.startswith("F") or key.startswith("f"):
            normalized = key.upper()
        else:
            normalized = key.upper()
        
        # Update UI
        self.lbl_current_key.configure(text=normalized)
        self.app.var_key.set(normalized)
        
        # Apply keybind
        ok, msg = self.app._bind_hotkey(normalized)
        
        if ok:
            self.lbl_status.configure(text=f"✅ Keybind set ke: {normalized}", 
                                     text_color="#6BCF7F")
            # Update button text in home page
            self.app._update_button_text()
        else:
            self.lbl_status.configure(text=f"❌ Error: {msg}", 
                                     text_color="#FF6B6B")
        
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
