#!/usr/bin/env python3
"""
Macro Mancing Indovoice - Main Entry Point
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Professional Roblox fishing macro with auto-update capabilities.
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.gui import App

def main():
    """Main entry point."""
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
