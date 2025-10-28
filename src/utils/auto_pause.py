"""Auto-pause system for detecting user interaction and game focus."""

import time
import threading
import win32gui
import win32process
import psutil
from pynput import keyboard
from typing import Callable, Optional


class AutoPauseMonitor:
    """Monitor for automatic pausing based on user interaction."""
    
    def __init__(self, pause_callback: Callable, resume_callback: Callable):
        """
        Initialize auto-pause monitor.
        
        Args:
            pause_callback: Function to call when macro should pause
            resume_callback: Function to call when macro should resume
        """
        self.pause_callback = pause_callback
        self.resume_callback = resume_callback
        
        # State
        self.is_running = False
        self.is_paused = False
        self.last_activity_time = time.time()
        
        # Settings
        self.pause_on_typing = True
        self.pause_on_focus_loss = True
        self.resume_delay = 2.0  # seconds after last activity to resume
        self.roblox_window_title = "Roblox"  # Partial match
        
        # Threading
        self._monitor_thread: Optional[threading.Thread] = None
        self._keyboard_listener: Optional[keyboard.Listener] = None
        
    def start(self):
        """Start monitoring for auto-pause conditions."""
        if self.is_running:
            return
            
        self.is_running = True
        self.is_paused = False
        self.last_activity_time = time.time()
        
        # Start keyboard listener
        if self.pause_on_typing:
            self._keyboard_listener = keyboard.Listener(on_press=self._on_key_press)
            self._keyboard_listener.start()
        
        # Start monitor thread
        self._monitor_thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self._monitor_thread.start()
        
    def stop(self):
        """Stop monitoring."""
        self.is_running = False
        
        if self._keyboard_listener:
            self._keyboard_listener.stop()
            self._keyboard_listener = None
            
        if self._monitor_thread:
            self._monitor_thread.join(timeout=2.0)
            self._monitor_thread = None
    
    def _on_key_press(self, key):
        """Handle keyboard press events."""
        if not self.is_running or not self.pause_on_typing:
            return
        
        # Check if Roblox window is focused
        if self._is_roblox_focused():
            # User is typing in game
            self._trigger_pause("Typing detected")
            self.last_activity_time = time.time()
    
    def _monitor_loop(self):
        """Main monitoring loop."""
        while self.is_running:
            try:
                # Check window focus
                if self.pause_on_focus_loss and not self._is_roblox_focused():
                    if not self.is_paused:
                        self._trigger_pause("Game window lost focus")
                else:
                    # Check if enough time has passed since last activity
                    time_since_activity = time.time() - self.last_activity_time
                    if self.is_paused and time_since_activity >= self.resume_delay:
                        self._trigger_resume("Activity resumed")
                
                time.sleep(0.5)  # Check every 500ms
                
            except Exception as e:
                print(f"AutoPauseMonitor error: {e}")
                time.sleep(1.0)
    
    def _is_roblox_focused(self) -> bool:
        """Check if Roblox window is currently focused."""
        try:
            hwnd = win32gui.GetForegroundWindow()
            if hwnd == 0:
                return False
            
            # Get window title
            title = win32gui.GetWindowText(hwnd)
            
            # Check if it's Roblox
            if self.roblox_window_title.lower() in title.lower():
                return True
            
            # Alternative: Check process name
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            try:
                process = psutil.Process(pid)
                if "roblox" in process.name().lower():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
            
            return False
            
        except Exception:
            return False
    
    def _trigger_pause(self, reason: str):
        """Trigger pause if not already paused."""
        if not self.is_paused:
            self.is_paused = True
            print(f"[AutoPause] Paused: {reason}")
            if self.pause_callback:
                self.pause_callback()
    
    def _trigger_resume(self, reason: str):
        """Trigger resume if currently paused."""
        if self.is_paused:
            self.is_paused = False
            print(f"[AutoPause] Resumed: {reason}")
            if self.resume_callback:
                self.resume_callback()
    
    def set_pause_on_typing(self, enabled: bool):
        """Enable/disable pause on typing."""
        self.pause_on_typing = enabled
        
        # Restart listener if needed
        if self.is_running:
            if enabled and not self._keyboard_listener:
                self._keyboard_listener = keyboard.Listener(on_press=self._on_key_press)
                self._keyboard_listener.start()
            elif not enabled and self._keyboard_listener:
                self._keyboard_listener.stop()
                self._keyboard_listener = None
    
    def set_pause_on_focus_loss(self, enabled: bool):
        """Enable/disable pause on focus loss."""
        self.pause_on_focus_loss = enabled
    
    def set_resume_delay(self, delay: float):
        """Set delay before auto-resume after activity stops."""
        self.resume_delay = max(0.5, delay)  # Minimum 0.5 seconds
    
    def manual_resume(self):
        """Manually resume (reset activity timer)."""
        self.last_activity_time = 0  # Force resume on next check


# Example usage
if __name__ == "__main__":
    def on_pause():
        print(">>> MACRO PAUSED")
    
    def on_resume():
        print(">>> MACRO RESUMED")
    
    monitor = AutoPauseMonitor(on_pause, on_resume)
    monitor.start()
    
    try:
        print("Auto-pause monitor running. Press Ctrl+C to stop.")
        print("Try typing while Roblox is focused, or switch windows.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping monitor...")
        monitor.stop()
        print("Stopped.")
