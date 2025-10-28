"""Main application window."""

import time
import threading
import re
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import cv2
import numpy as np

from ..core.engine import FishingEngine
from ..core.vision import grab_bgr
from ..utils.config import ConfigManager
from ..utils.screen import make_default_roi, clamp_roi
from ..utils.updater import AutoUpdater
from ..utils.auto_pause import AutoPauseMonitor
from ..version import __version__
from .pages import HomePage, SettingsPage, KeybindsPage, CreditPage

# Windows DPI awareness
try:
    import ctypes
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except Exception:
    pass

# Optional PIL for preview
HAVE_PIL = True
try:
    from PIL import Image
except Exception:
    HAVE_PIL = False

# Optional keyboard for global hotkeys
HAVE_KB = True
try:
    import keyboard
except Exception:
    HAVE_KB = False

# Set appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# GitHub repository for updates
GITHUB_REPO = "athuridha/mancing-tools"


class App(ctk.CTk):
    """Main application window."""
    
    def __init__(self):
        super().__init__()
        self.title("Macro Mancing Indovoice")
        self.geometry("1000x640")
        self.minsize(960, 600)
        
        # Configuration
        self.config_manager = ConfigManager("config/settings.json")
        self.config = self.config_manager.load()
        
        # Auto-updater
        self.updater = AutoUpdater(__version__, GITHUB_REPO)
        
        # State
        self.roi = make_default_roi()
        self.running = False
        self.debug_open = False
        self.worker = None
        self._preview_img = None
        self._tk_bound_pattern = None
        
        # Engine
        self.engine = FishingEngine(self.config)
        self.engine.set_callback("on_green_ratio", self._on_green_ratio)
        self.engine.set_callback("on_red_ratio", self._on_red_ratio)
        self.engine.set_callback("on_action", self._on_action)
        
        # Auto-pause monitor
        self.auto_pause_monitor = AutoPauseMonitor(
            pause_callback=self._on_auto_pause,
            resume_callback=self._on_auto_resume
        )
        
        # UI Variables
        self.var_g = tk.DoubleVar(value=0.0)
        self.var_r = tk.DoubleVar(value=0.0)
        self.var_act = tk.StringVar(value="Idle")
        self.var_status = tk.StringVar(value="Stopped")
        
        # Settings variables
        self.var_green_th = tk.DoubleVar(value=self.config.get("green_th", 0.14))
        self.var_red_th = tk.DoubleVar(value=self.config.get("red_th", 0.10))
        self.var_click_i = tk.DoubleVar(value=self.config.get("click_i", 0.035))
        self.var_idle_i = tk.DoubleVar(value=self.config.get("idle_i", 0.010))
        self.var_hold_s = tk.DoubleVar(value=self.config.get("hold_s", 3.0))
        self.var_down_s = tk.DoubleVar(value=self.config.get("down_s", 0.01))
        self.var_inactive_to = tk.DoubleVar(value=self.config.get("inactive_to", 1.2))
        self.var_recast_delay = tk.DoubleVar(value=self.config.get("recast_delay", 0.30))
        self.var_auto_recast = tk.BooleanVar(value=self.config.get("auto_recast", True))
        
        # Auto-pause variables
        self.var_auto_pause_enabled = tk.BooleanVar(value=self.config.get("auto_pause_enabled", False))
        self.var_pause_on_typing = tk.BooleanVar(value=self.config.get("pause_on_typing", True))
        self.var_pause_on_focus_loss = tk.BooleanVar(value=self.config.get("pause_on_focus_loss", True))
        self.var_auto_pause_resume_delay = tk.DoubleVar(value=self.config.get("auto_pause_resume_delay", 2.0))
        
        # ROI variables
        roi_config = self.config.get("roi", {})
        if roi_config:
            self.roi = clamp_roi(
                roi_config.get("x", self.roi.x),
                roi_config.get("y", self.roi.y),
                roi_config.get("w", self.roi.w),
                roi_config.get("h", self.roi.h)
            )
        self.var_w = tk.IntVar(value=self.roi.w)
        self.var_h = tk.IntVar(value=self.roi.h)
        
        # Keybind
        self.var_key = tk.StringVar(value=self.config.get("key", "F1"))
        
        # Build UI
        self._build_ui()
        self._bind_hotkey(self.var_key.get())
        
        # Start UI update loop
        self._tick_ui()
        
        # Check for updates on startup (non-blocking)
        self.after(2000, lambda: threading.Thread(target=self._check_updates_silent, daemon=True).start())
        
    def _build_ui(self):
        """Build the user interface."""
        # Top bar
        self._build_topbar()
        
        # Content area
        self.content = ctk.CTkFrame(self)
        self.content.pack(fill="both", expand=True)
        
        # Pages
        self.page_home = HomePage(self.content, self)
        self.page_settings = SettingsPage(self.content, self)
        self.page_keybind = KeybindsPage(self.content, self)
        self.page_credit = CreditPage(self.content, self)
        
        # Show home by default
        self._show_page("Home")
        
    def _build_topbar(self):
        """Build top navigation bar."""
        top = ctk.CTkFrame(self, corner_radius=0)
        top.pack(side="top", fill="x")
        
        title = ctk.CTkLabel(top, text="🎣 Macro Mancing Indovoice",
                            font=ctk.CTkFont(size=18, weight="bold"))
        title.pack(side="left", padx=14, pady=10)
        
        # Menu buttons
        self.menu_var = tk.StringVar(value="Home")
        menu = ctk.CTkSegmentedButton(
            top, 
            values=["Home", "Custom Settings", "Keybinds", "Credit"],
            variable=self.menu_var, 
            command=self._on_menu_change
        )
        menu.pack(side="right", padx=12, pady=10)
        
    def _on_menu_change(self, value):
        """Handle menu selection change."""
        self._show_page(value)
        
    def _show_page(self, name: str):
        """Show specific page and hide others."""
        pages = {
            "Home": self.page_home,
            "Custom Settings": self.page_settings,
            "Keybinds": self.page_keybind,
            "Credit": self.page_credit,
        }
        
        # Hide all pages
        for page in pages.values():
            page.pack_forget()
            
        # Show selected page
        if name in pages:
            pages[name].pack(fill="both", expand=True, padx=12, pady=12)
            
    # ==================== Engine Callbacks ====================
    
    def _on_green_ratio(self, ratio: float):
        """Callback for green ratio update."""
        self.var_g.set(ratio)
        
    def _on_red_ratio(self, ratio: float):
        """Callback for red ratio update."""
        self.var_r.set(ratio)
        
    def _on_action(self, action: str):
        """Callback for action update."""
        self.var_act.set(action)
    
    def _on_auto_pause(self):
        """Callback when auto-pause triggers."""
        if self.running:
            self.engine.pause()
            print("[AutoPause] Macro paused")
    
    def _on_auto_resume(self):
        """Callback when auto-pause resumes."""
        if self.running:
            self.engine.resume()
            print("[AutoPause] Macro resumed")
        
    # ==================== UI Controls ====================
    
    def toggle_start(self):
        """Toggle macro start/stop."""
        if not self.running:
            self.running = True
            self.engine.start()
            self._update_button_text()
            self.var_status.set("Running")
            self._update_config()
            
            # Start auto-pause monitor if enabled
            if self.var_auto_pause_enabled.get():
                self.auto_pause_monitor.set_pause_on_typing(self.var_pause_on_typing.get())
                self.auto_pause_monitor.set_pause_on_focus_loss(self.var_pause_on_focus_loss.get())
                self.auto_pause_monitor.set_resume_delay(self.var_auto_pause_resume_delay.get())
                self.auto_pause_monitor.start()
            
            self.worker = threading.Thread(target=self._run_engine, daemon=True)
            self.worker.start()
        else:
            self.running = False
            self.engine.stop()
            
            # Stop auto-pause monitor
            if self.auto_pause_monitor.is_running:
                self.auto_pause_monitor.stop()
            self._update_button_text()
            self.var_status.set("Stopped")
            
    def _run_engine(self):
        """Run the fishing engine in a separate thread."""
        self.engine.run(self.roi)
        
    def _update_button_text(self):
        """Update start/stop button text with current keybind."""
        key = self.var_key.get().strip().upper()
        if self.running:
            self.page_home.btn_start.configure(text=f"Stop ({key})")
        else:
            self.page_home.btn_start.configure(text=f"Start ({key})")
            
    def apply_wh(self):
        """Apply width/height changes to ROI."""
        self.roi = clamp_roi(
            self.roi.x, 
            self.roi.y, 
            int(self.var_w.get()), 
            int(self.var_h.get())
        )
        
    def calibrate_from_cursor(self):
        """Set ROI center to current cursor position."""
        import pyautogui as pag
        x, y = pag.position()
        w = int(self.var_w.get())
        h = int(self.var_h.get())
        self.roi = clamp_roi(x - w // 2, y - h // 2, w, h)
        messagebox.showinfo("Kalibrasi", 
                           f"ROI: x={self.roi.x}, y={self.roi.y}, w={self.roi.w}, h={self.roi.h}")
        
    def calibrate_by_selection(self):
        """Select ROI by dragging on screen."""
        # Minimize aplikasi untuk clear view
        self.iconify()
        
        # Small delay untuk smooth minimize
        self.after(200, self._show_selection_overlay)
    
    def _show_selection_overlay(self):
        """Show selection overlay after minimize."""
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        overlay = tk.Toplevel(self)
        overlay.overrideredirect(True)
        overlay.attributes("-topmost", True)
        try:
            overlay.attributes("-alpha", 0.25)
        except Exception:
            pass
        overlay.configure(bg="black")
        overlay.geometry(f"{sw}x{sh}+0+0")
        canvas = tk.Canvas(overlay, bg="black", highlightthickness=0, cursor="crosshair")
        canvas.pack(fill="both", expand=True)
        
        # Instructions label
        info_label = tk.Label(canvas, 
                             text="Drag untuk pilih area ROI • ESC untuk batal",
                             font=("Arial", 12, "bold"),
                             fg="white",
                             bg="black")
        info_label.place(relx=0.5, rely=0.02, anchor="n")
        
        rect = {"id": None}
        start = {"x": 0, "y": 0}
        
        def restore_app():
            """Restore aplikasi setelah selesai."""
            self.deiconify()
            self.lift()
            self.focus_force()
        
        def on_press(e):
            start["x"], start["y"] = e.x, e.y
            if rect["id"] is not None:
                canvas.delete(rect["id"])
            rect["id"] = canvas.create_rectangle(e.x, e.y, e.x, e.y, 
                                                 outline="white", width=2)
        
        def on_move(e):
            if rect["id"] is not None:
                canvas.coords(rect["id"], start["x"], start["y"], e.x, e.y)
        
        def finish(e):
            x0, y0, x1, y1 = start["x"], start["y"], e.x, e.y
            overlay.destroy()
            restore_app()
            
            x = int(min(x0, x1))
            y = int(min(y0, y1))
            w = int(abs(x1 - x0))
            h = int(abs(y1 - y0))
            if w < 5 or h < 5:
                messagebox.showwarning("Kalibrasi", "Area terlalu kecil. Coba lagi.")
                return
            self.roi = clamp_roi(x, y, w, h)
            self.var_w.set(self.roi.w)
            self.var_h.set(self.roi.h)
            messagebox.showinfo("Kalibrasi", 
                              f"ROI: x={self.roi.x}, y={self.roi.y}, w={self.roi.w}, h={self.roi.h}")
        
        def cancel(_=None):
            overlay.destroy()
            restore_app()
        
        overlay.bind("<Escape>", cancel)
        canvas.bind("<ButtonPress-1>", on_press)
        canvas.bind("<B1-Motion>", on_move)
        canvas.bind("<ButtonRelease-1>", finish)
        
    def toggle_debug(self):
        """Toggle debug window."""
        if self.debug_open:
            self.debug_open = False
            return
        self.debug_open = True
        threading.Thread(target=self._debug_window, daemon=True).start()
        
    def _debug_window(self):
        """Show debug window with ROI overlay."""
        from ..core.vision import calc_color_ratios
        while self.debug_open:
            try:
                frame = grab_bgr(self.roi)
                # Ensure frame is contiguous for OpenCV
                if not frame.flags['C_CONTIGUOUS']:
                    frame = np.ascontiguousarray(frame)
                    
                g, r = calc_color_ratios(frame)
                info = f"G={g:.2f} R={r:.2f}"
                
                # Make a copy to ensure writability
                display_frame = frame.copy()
                cv2.putText(display_frame, info, (6, 18), cv2.FONT_HERSHEY_SIMPLEX, 
                           0.6, (255,255,255), 2, cv2.LINE_AA)
                cv2.imshow("ROI Debug (ESC to close)", display_frame)
                
                if (cv2.waitKey(1) & 0xFF) == 27:
                    self.debug_open = False
                    break
            except Exception as e:
                print(f"Debug window error: {e}")
                self.debug_open = False
                break
        cv2.destroyAllWindows()
        
    # ==================== Settings ====================
    
    def _update_config(self):
        """Update engine config from UI variables."""
        self.config.update({
            "green_th": self.var_green_th.get(),
            "red_th": self.var_red_th.get(),
            "click_i": self.var_click_i.get(),
            "idle_i": self.var_idle_i.get(),
            "hold_s": self.var_hold_s.get(),
            "down_s": self.var_down_s.get(),
            "inactive_to": self.var_inactive_to.get(),
            "recast_delay": self.var_recast_delay.get(),
            "auto_recast": self.var_auto_recast.get(),
            # Auto-pause settings
            "auto_pause_enabled": self.var_auto_pause_enabled.get(),
            "pause_on_typing": self.var_pause_on_typing.get(),
            "pause_on_focus_loss": self.var_pause_on_focus_loss.get(),
            "auto_pause_resume_delay": self.var_auto_pause_resume_delay.get(),
        })
        self.engine.config = self.config
        
    def save_settings(self):
        """Save settings to file."""
        self._update_config()
        self.config["roi"] = {
            "x": self.roi.x, 
            "y": self.roi.y, 
            "w": self.roi.w, 
            "h": self.roi.h
        }
        self.config["key"] = self.var_key.get().strip()
        
        if self.config_manager.save(self.config):
            messagebox.showinfo("Preset", "Settings berhasil disimpan!")
        else:
            messagebox.showerror("Preset", "Gagal menyimpan settings!")
            
    def load_settings(self):
        """Load settings from file."""
        self.config = self.config_manager.load()
        
        # Update variables
        self.var_green_th.set(self.config.get("green_th", 0.14))
        self.var_red_th.set(self.config.get("red_th", 0.10))
        self.var_click_i.set(self.config.get("click_i", 0.035))
        self.var_idle_i.set(self.config.get("idle_i", 0.010))
        self.var_hold_s.set(self.config.get("hold_s", 3.0))
        self.var_down_s.set(self.config.get("down_s", 0.01))
        self.var_inactive_to.set(self.config.get("inactive_to", 1.2))
        self.var_recast_delay.set(self.config.get("recast_delay", 0.30))
        self.var_auto_recast.set(self.config.get("auto_recast", True))
        
        roi_config = self.config.get("roi", {})
        if roi_config:
            self.roi = clamp_roi(
                roi_config.get("x", self.roi.x),
                roi_config.get("y", self.roi.y),
                roi_config.get("w", self.roi.w),
                roi_config.get("h", self.roi.h)
            )
            self.var_w.set(self.roi.w)
            self.var_h.set(self.roi.h)
            
        messagebox.showinfo("Preset", "Settings berhasil dimuat!")
        
    # ==================== Keybinds ====================
    
    def apply_keybind(self):
        """Apply new keybind."""
        key = self.var_key.get().strip()
        ok, msg = self._bind_hotkey(key)
        if ok:
            messagebox.showinfo("Keybind", f"Keybind diset ke: {key.upper()}")
            self._update_button_text()
        else:
            messagebox.showerror("Keybind", msg)
            
    def _canonicalize_key(self, key: str):
        """Normalize key string."""
        if not key:
            return None
        k = key.strip()
        # F-keys
        if re.fullmatch(r"[Ff](\d{1,2})", k):
            n = int(k[1:])
            if 1 <= n <= 24:
                return f"f{n}"
            return None
        # Single char
        if re.fullmatch(r"[A-Za-z0-9]", k):
            return k.lower()
        return None
        
    def _unbind_prev_hotkey(self):
        """Unbind previous hotkey."""
        if HAVE_KB:
            try:
                keyboard.unhook_all_hotkeys()
            except Exception:
                pass
        if self._tk_bound_pattern:
            try:
                self.unbind_all(self._tk_bound_pattern)
            except Exception:
                pass
            self._tk_bound_pattern = None
            
    def _bind_hotkey(self, key: str):
        """Bind hotkey for start/stop."""
        canonical = self._canonicalize_key(key)
        if canonical is None:
            self._set_hotkey_status(False, f"Key tidak valid: {key}")
            return False, f"Key tidak valid: {key}"
            
        self._unbind_prev_hotkey()
        
        if HAVE_KB:
            try:
                keyboard.add_hotkey(canonical, lambda: self._toggle_from_hotkey())
                self._set_hotkey_status(True, f"Global hotkey aktif: {canonical.upper()}")
                return True, "OK"
            except Exception as e:
                self._set_hotkey_status(False, f"Gagal global hotkey: {e}. Fallback lokal.")
                
        # Fallback to local hotkey
        pattern = self._tk_pattern(canonical)
        try:
            self.bind_all(pattern, lambda e: self._toggle_from_hotkey())
            self._tk_bound_pattern = pattern
            self._set_hotkey_status(False, f"Lokal hotkey aktif (butuh fokus): {pattern}")
            return True, "OK"
        except Exception as e:
            self._set_hotkey_status(False, f"Gagal bind lokal: {e}")
            return False, f"Gagal bind: {e}"
            
    def _tk_pattern(self, canonical: str):
        """Convert canonical key to Tkinter pattern."""
        if canonical.startswith("f"):
            return f"<F{canonical[1:]}>"
        return f"<{canonical}>"
        
    def _toggle_from_hotkey(self):
        """Toggle from hotkey press."""
        try:
            self.after(0, self.toggle_start)
        except Exception:
            pass
            
    def _set_hotkey_status(self, global_ok: bool, msg: str):
        """Update hotkey status label."""
        if hasattr(self.page_keybind, 'lbl_hotkey_status'):
            prefix = "GLOBAL ✔ " if global_ok else "LOCAL ⓘ "
            self.page_keybind.lbl_hotkey_status.configure(text=prefix + msg)
            
    # ==================== Auto-Update ====================
    
    def _check_updates_silent(self):
        """Check for updates silently on startup."""
        try:
            update_info = self.updater.check_for_updates()
            if update_info:
                self.after(0, lambda: self._notify_update_available(update_info))
        except Exception as e:
            # Silently fail on startup - don't bother user
            print(f"Silent update check skipped: {e}")
            
    def _notify_update_available(self, update_info):
        """Notify user about available update."""
        msg = f"Update tersedia: v{update_info['version']}\n\n"
        msg += "Ingin download sekarang?"
        if messagebox.askyesno("Update Tersedia", msg):
            self._download_update(update_info)
            
    def check_updates(self):
        """Check for updates (manual)."""
        self.page_credit.btn_update.configure(state="disabled", text="Checking...")
        self.page_credit.lbl_update_status.configure(text="Memeriksa update...")
        
        def check():
            try:
                update_info = self.updater.check_for_updates()
                self.after(0, lambda: self._on_update_check_complete(update_info, None))
            except Exception as e:
                error_msg = str(e)
                # Simplify error message
                if "404" in error_msg or "Not Found" in error_msg:
                    error_msg = "Repository belum dibuat atau tidak ditemukan"
                elif "connect" in error_msg.lower() or "connection" in error_msg.lower():
                    error_msg = "Tidak dapat terhubung ke server"
                else:
                    error_msg = f"Error: {error_msg}"
                self.after(0, lambda: self._on_update_check_complete(None, error_msg))
            
        threading.Thread(target=check, daemon=True).start()
        
    def _on_update_check_complete(self, update_info, error_msg=None):
        """Handle update check completion."""
        self.page_credit.btn_update.configure(state="normal", text="🔄 Cek Update")
        
        if error_msg:
            # Show error
            self.page_credit.lbl_update_status.configure(
                text=f"❌ {error_msg}", 
                text_color="#FF6B6B"
            )
        elif update_info:
            msg = f"Update tersedia: v{update_info['version']}"
            self.page_credit.lbl_update_status.configure(text=f"✅ {msg}", text_color="#4ea3ff")
            if messagebox.askyesno("Update Tersedia", 
                                  f"{msg}\n\nIngin download sekarang?"):
                self._download_update(update_info)
        else:
            self.page_credit.lbl_update_status.configure(
                text="✅ Anda sudah menggunakan versi terbaru!", 
                text_color="#6BCF7F"
            )
            
    def _download_update(self, update_info):
        """Download and install update."""
        self.page_credit.btn_update.configure(state="disabled", text="Downloading...")
        self.page_credit.lbl_update_status.configure(text="Downloading update...")
        
        def download():
            def progress_callback(downloaded, total):
                percent = (downloaded / total * 100) if total > 0 else 0
                self.after(0, lambda: self.page_credit.lbl_update_status.configure(
                    text=f"Downloading: {percent:.0f}%"
                ))
                
            update_file = self.updater.download_update(
                update_info['download_url'], 
                progress_callback
            )
            self.after(0, lambda: self._on_download_complete(update_file))
            
        threading.Thread(target=download, daemon=True).start()
        
    def _on_download_complete(self, update_file):
        """Handle download completion."""
        self.page_credit.btn_update.configure(state="normal", text="Cek Update")
        
        if update_file:
            msg = "Update berhasil didownload!\n\n"
            msg += "Aplikasi akan restart untuk install update."
            if messagebox.showinfo("Update Ready", msg):
                self.updater.install_update(update_file)
                self.quit()
        else:
            self.page_credit.lbl_update_status.configure(
                text="Download gagal!", 
                text_color="red"
            )
            messagebox.showerror("Update Error", "Gagal mendownload update!")
            
    # ==================== UI Update Loop ====================
    
    def _tick_ui(self):
        """Update UI periodically."""
        # Update progress bars
        g = max(0.0, min(1.0, self.var_g.get()))
        r = max(0.0, min(1.0, self.var_r.get()))
        try:
            self.page_home.pb_g.set(g)
            self.page_home.pb_r.set(r)
        except Exception:
            pass
            
        # Update preview
        if HAVE_PIL and self.running:
            try:
                frame = grab_bgr(self.roi)
                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(rgb)
                target_w = max(220, min(680, int(self.roi.w * 0.85)))
                target_h = max(160, min(420, int(self.roi.h * 0.85)))
                self._preview_img = ctk.CTkImage(
                    light_image=img, 
                    dark_image=img, 
                    size=(target_w, target_h)
                )
                self.page_home.preview.configure(image=self._preview_img, text="")
            except Exception:
                self.page_home.preview.configure(
                    text="Preview ROI (aktif saat jalan)", 
                    image=None
                )
                
        self.after(120, self._tick_ui)
