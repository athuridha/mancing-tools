"""Screen utilities for ROI management."""

import pyautogui as pag
from ..core.engine import ROI

# Default ROI ratio (cx, cy, w, h) relative to screen
DEFAULT_ROI_RATIO = (0.5, 0.84, 0.34, 0.09)

def screen_size() -> tuple[int, int]:
    """Get screen dimensions.
    
    Returns:
        tuple: (width, height)
    """
    w, h = pag.size()
    return int(w), int(h)

def make_default_roi() -> ROI:
    """Create default ROI based on screen size.
    
    Returns:
        ROI: Default region of interest
    """
    sw, sh = screen_size()
    cx, cy, wr, hr = DEFAULT_ROI_RATIO
    w = int(sw * wr)
    h = int(sh * hr)
    x = int(sw * cx - w / 2)
    y = int(sh * cy - h / 2)
    return ROI(x, y, w, h)

def clamp_roi(x: int, y: int, w: int, h: int) -> ROI:
    """Clamp ROI to screen boundaries.
    
    Args:
        x, y, w, h: ROI coordinates and dimensions
        
    Returns:
        ROI: Clamped region of interest
    """
    sw, sh = screen_size()
    w = max(1, min(w, sw))
    h = max(1, min(h, sh))
    x = max(0, min(x, sw - w))
    y = max(0, min(y, sh - h))
    return ROI(x, y, w, h)
