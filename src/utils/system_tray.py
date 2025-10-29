"""System tray integration for minimize to tray functionality."""

import os
import sys
import threading
from PIL import Image
import pystray
from pystray import MenuItem as Item

class SystemTrayManager:
    """Manages system tray icon and menu."""
    
    def __init__(self, app):
        """Initialize system tray manager.
        
        Args:
            app: Main application instance
        """
        self.app = app
        self.icon = None
        self.tray_thread = None
        self.is_running = False
        
    def create_icon(self) -> pystray.Icon:
        """Create system tray icon from assets.
        
        Returns:
            pystray.Icon object
        """
        # Try to load logo from assets
        icon_path = self._get_icon_path()
        
        try:
            if os.path.exists(icon_path):
                image = Image.open(icon_path)
            else:
                # Create simple colored square as fallback
                image = Image.new('RGB', (64, 64), color='#1f538d')
        except Exception:
            # Fallback to simple icon
            image = Image.new('RGB', (64, 64), color='#1f538d')
        
        # Create menu
        menu = pystray.Menu(
            Item('Show', self.restore_window, default=True),
            Item('Simple Mode', self.toggle_simple_mode),
            pystray.Menu.SEPARATOR,
            Item('Start/Stop', self.toggle_macro),
            pystray.Menu.SEPARATOR,
            Item('Exit', self.quit_app)
        )
        
        return pystray.Icon("Mancing Tools", image, "Mancing Tools", menu)
    
    def _get_icon_path(self) -> str:
        """Get path to icon file.
        
        Returns:
            Path to logo.png or logo.ico
        """
        if getattr(sys, 'frozen', False):
            # Running as compiled executable
            base_path = sys._MEIPASS
        else:
            # Running as script
            base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        
        # Try PNG first, then ICO
        for ext in ['png', 'ico']:
            icon_path = os.path.join(base_path, 'assets', f'logo.{ext}')
            if os.path.exists(icon_path):
                return icon_path
        
        return ""
    
    def start(self):
        """Start system tray icon in background thread."""
        if self.is_running:
            return
        
        self.icon = self.create_icon()
        self.is_running = True
        
        # Run icon in separate thread
        self.tray_thread = threading.Thread(target=self._run_icon, daemon=True)
        self.tray_thread.start()
    
    def _run_icon(self):
        """Run the system tray icon (blocking call)."""
        try:
            self.icon.run()
        except Exception as e:
            print(f"System tray error: {e}")
        finally:
            self.is_running = False
    
    def stop(self):
        """Stop system tray icon."""
        if self.icon and self.is_running:
            try:
                self.icon.stop()
            except Exception:
                pass
            self.is_running = False
    
    def minimize_to_tray(self):
        """Hide window and show only tray icon."""
        self.app.withdraw()  # Hide window
        if not self.is_running:
            self.start()
    
    def restore_window(self, icon=None, item=None):
        """Restore window from tray.
        
        Args:
            icon: System tray icon (from pystray callback)
            item: Menu item (from pystray callback)
        """
        self.app.after(0, self._restore_window_safe)
    
    def _restore_window_safe(self):
        """Thread-safe window restoration."""
        self.app.deiconify()  # Show window
        self.app.lift()       # Bring to front
        self.app.focus_force()  # Give focus
    
    def toggle_simple_mode(self, icon=None, item=None):
        """Toggle simple mode from tray menu.
        
        Args:
            icon: System tray icon (from pystray callback)
            item: Menu item (from pystray callback)
        """
        self.app.after(0, self.app.toggle_simple_mode)
    
    def toggle_macro(self, icon=None, item=None):
        """Toggle macro start/stop from tray menu.
        
        Args:
            icon: System tray icon (from pystray callback)
            item: Menu item (from pystray callback)
        """
        self.app.after(0, self.app.toggle_start)
    
    def quit_app(self, icon=None, item=None):
        """Quit application from tray menu.
        
        Args:
            icon: System tray icon (from pystray callback)
            item: Menu item (from pystray callback)
        """
        self.stop()
        self.app.after(0, self.app.on_closing)
