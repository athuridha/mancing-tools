"""Computer vision utilities for fishing detection."""

import threading
import numpy as np
import cv2
import mss

# HSV color ranges for fishing indicators
HSV_GREEN_LOW  = np.array([35,  70,  70], dtype=np.uint8)
HSV_GREEN_HIGH = np.array([85, 255, 255], dtype=np.uint8)
HSV_RED_LOW1   = np.array([0,   90,  70], dtype=np.uint8)
HSV_RED_HIGH1  = np.array([12, 255, 255], dtype=np.uint8)
HSV_RED_LOW2   = np.array([160, 90,  70], dtype=np.uint8)
HSV_RED_HIGH2  = np.array([179,255, 255], dtype=np.uint8)

# Thread-local MSS instance
_thread_local = threading.local()

def get_thread_sct():
    """Get thread-local MSS instance."""
    sct = getattr(_thread_local, "sct", None)
    if sct is None:
        _thread_local.sct = mss.mss()
        sct = _thread_local.sct
    return sct

def grab_bgr(roi):
    """Capture screen region as BGR numpy array.
    
    Args:
        roi: ROI object with to_monitor() method
        
    Returns:
        numpy.ndarray: BGR image
    """
    mon = roi.to_monitor()
    sct = get_thread_sct()
    img = np.array(sct.grab(mon))
    return img[:, :, :3]  # Remove alpha channel

def calc_color_ratios(frame_bgr: np.ndarray) -> tuple[float, float]:
    """Calculate green and red color ratios in frame.
    
    Args:
        frame_bgr: BGR image as numpy array
        
    Returns:
        tuple: (green_ratio, red_ratio)
    """
    if frame_bgr.size == 0:
        return 0.0, 0.0
        
    hsv = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2HSV)
    
    # Green mask
    green_mask = cv2.inRange(hsv, HSV_GREEN_LOW, HSV_GREEN_HIGH)
    
    # Red mask (wraps around hue)
    red_mask1 = cv2.inRange(hsv, HSV_RED_LOW1, HSV_RED_HIGH1)
    red_mask2 = cv2.inRange(hsv, HSV_RED_LOW2, HSV_RED_HIGH2)
    red_mask = cv2.bitwise_or(red_mask1, red_mask2)
    
    total = float(frame_bgr.shape[0] * frame_bgr.shape[1])
    g_ratio = np.count_nonzero(green_mask) / total
    r_ratio = np.count_nonzero(red_mask) / total
    
    return float(g_ratio), float(r_ratio)
