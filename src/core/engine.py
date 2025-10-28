"""Core fishing macro engine."""

import time
from dataclasses import dataclass
import pyautogui as pag
from .vision import grab_bgr, calc_color_ratios

# PyAutoGUI safety
pag.FAILSAFE = True
pag.PAUSE = 0.01

@dataclass
class ROI:
    """Region of Interest for screen capture."""
    x: int
    y: int
    w: int
    h: int
    
    def to_monitor(self) -> dict:
        """Convert to MSS monitor dict."""
        return {"left": self.x, "top": self.y, "width": self.w, "height": self.h}

class FishingEngine:
    """Main fishing automation engine."""
    
    def __init__(self, config: dict):
        """Initialize engine with configuration.
        
        Args:
            config: Configuration dictionary with thresholds and settings
        """
        self.config = config
        self.running = False
        self.paused = False  # Auto-pause state
        self.last_active_ts = time.time()
        self.callbacks = {
            "on_green_ratio": None,
            "on_red_ratio": None,
            "on_action": None,
        }
        
    def set_callback(self, event: str, callback):
        """Set callback for events.
        
        Args:
            event: Event name (on_green_ratio, on_red_ratio, on_action)
            callback: Callback function
        """
        if event in self.callbacks:
            self.callbacks[event] = callback
            
    def _notify(self, event: str, *args):
        """Trigger callback if set."""
        if self.callbacks.get(event):
            try:
                self.callbacks[event](*args)
            except Exception:
                pass
    
    def _click_once(self):
        """Execute single mouse click."""
        down_duration = max(0.001, float(self.config.get("down_s", 0.01)))
        pag.mouseDown(button="left")
        time.sleep(down_duration)
        pag.mouseUp(button="left")
        
    def _hold_cast(self):
        """Hold mouse button to cast fishing rod."""
        hold_duration = max(0.1, float(self.config.get("hold_s", 3.0)))
        self._notify("on_action", f"Hold {hold_duration:.2f}s...")
        pag.mouseDown(button="left")
        time.sleep(hold_duration)
        pag.mouseUp(button="left")
        self._notify("on_action", "Monitoring...")
        
    def run(self, roi: ROI):
        """Main fishing loop.
        
        Args:
            roi: Screen region to monitor
        """
        try:
            # Initial cast
            self._hold_cast()
            self.last_active_ts = time.time()
            
            # Main monitoring loop
            while self.running:
                # Check if paused by auto-pause system
                if self.paused:
                    self._notify("on_action", "⏸️ Auto-Paused...")
                    time.sleep(0.5)
                    continue
                
                frame = grab_bgr(roi)
                g_ratio, r_ratio = calc_color_ratios(frame)
                
                # Notify UI
                self._notify("on_green_ratio", g_ratio)
                self._notify("on_red_ratio", r_ratio)
                
                # Check if mini-game is active
                active_min = self.config.get("active_min_ratio", 0.03)
                active_now = max(g_ratio, r_ratio) >= active_min
                
                if active_now:
                    self.last_active_ts = time.time()
                    
                    # Check if we should click (green dominant)
                    green_th = float(self.config.get("green_th", 0.14))
                    if g_ratio >= green_th and g_ratio > r_ratio:
                        self._notify("on_action", "CLICK")
                        self._click_once()
                        time.sleep(float(self.config.get("click_i", 0.035)))
                    else:
                        self._notify("on_action", "Idle")
                        time.sleep(float(self.config.get("idle_i", 0.010)))
                else:
                    # Mini-game inactive - check for auto-recast
                    idle_for = time.time() - self.last_active_ts
                    inactive_to = float(self.config.get("inactive_to", 1.2))
                    
                    if self.config.get("auto_recast", True) and idle_for >= inactive_to:
                        # Time to recast
                        recast_delay = max(0.0, float(self.config.get("recast_delay", 0.30)))
                        if recast_delay > 0:
                            self._notify("on_action", f"Recast in {recast_delay:.2f}s...")
                            time.sleep(recast_delay)
                        self._hold_cast()
                        self.last_active_ts = time.time()
                        time.sleep(0.05)
                    else:
                        self._notify("on_action", "Menunggu mini-game...")
                        time.sleep(float(self.config.get("idle_i", 0.010)))
                        
        except Exception as e:
            self._notify("on_action", f"Error: {e}")
            self.running = False
            
    def start(self):
        """Start the fishing engine."""
        self.running = True
        
    def stop(self):
        """Stop the fishing engine."""
        self.running = False
    
    def pause(self):
        """Pause the fishing engine (for auto-pause)."""
        self.paused = True
    
    def resume(self):
        """Resume the fishing engine (from auto-pause)."""
        self.paused = False
