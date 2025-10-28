"""Configuration manager for saving/loading settings."""

import json
import os
from typing import Dict, Any

# Default configuration values
DEFAULT_CONFIG = {
    "roi": {"x": 0, "y": 0, "w": 526, "h": 70},
    "green_th": 0.14,
    "red_th": 0.10,
    "click_i": 0.035,
    "idle_i": 0.010,
    "hold_s": 3.0,
    "down_s": 0.01,
    "inactive_to": 1.2,
    "recast_delay": 0.30,
    "auto_recast": True,
    "active_min_ratio": 0.03,
    "key": "F1",
}

class ConfigManager:
    """Manages application configuration."""
    
    def __init__(self, config_file: str = "config/settings.json"):
        """Initialize configuration manager.
        
        Args:
            config_file: Path to configuration file
        """
        self.config_file = config_file
        self.config = DEFAULT_CONFIG.copy()
        
    def load(self) -> Dict[str, Any]:
        """Load configuration from file.
        
        Returns:
            dict: Loaded configuration
        """
        if not os.path.exists(self.config_file):
            return self.config
            
        try:
            with open(self.config_file, "r", encoding="utf-8") as f:
                loaded = json.load(f)
                self.config.update(loaded)
        except Exception as e:
            print(f"Failed to load config: {e}")
            
        return self.config
        
    def save(self, config: Dict[str, Any] = None) -> bool:
        """Save configuration to file.
        
        Args:
            config: Configuration to save (uses current if None)
            
        Returns:
            bool: True if successful
        """
        if config is not None:
            self.config = config
            
        try:
            # Ensure directory exists
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            
            with open(self.config_file, "w", encoding="utf-8") as f:
                json.dump(self.config, f, indent=2)
            return True
        except Exception as e:
            print(f"Failed to save config: {e}")
            return False
            
    def get(self, key: str, default=None):
        """Get configuration value.
        
        Args:
            key: Configuration key
            default: Default value if key not found
            
        Returns:
            Configuration value
        """
        return self.config.get(key, default)
        
    def set(self, key: str, value):
        """Set configuration value.
        
        Args:
            key: Configuration key
            value: Value to set
        """
        self.config[key] = value
        
    def reset(self):
        """Reset configuration to defaults."""
        self.config = DEFAULT_CONFIG.copy()
