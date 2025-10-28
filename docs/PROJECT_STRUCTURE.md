# Project Structure

```
mancing-indovoice/
│
├── 📁 src/                          # Source code utama
│   ├── 📄 __init__.py              # Package initialization
│   ├── 📄 version.py               # Version management untuk auto-update
│   │
│   ├── 📁 core/                    # Core engine & logic
│   │   ├── 📄 __init__.py         
│   │   ├── 📄 engine.py           # FishingEngine - main automation logic
│   │   └── 📄 vision.py           # Computer vision - color detection & screen capture
│   │
│   ├── 📁 gui/                     # User interface
│   │   ├── 📄 __init__.py
│   │   ├── 📄 main_window.py      # Main application window
│   │   └── 📄 pages.py            # UI pages (Home, Settings, Keybinds, Credit)
│   │
│   └── 📁 utils/                   # Utility modules
│       ├── 📄 __init__.py
│       ├── 📄 config.py           # Configuration manager (JSON)
│       ├── 📄 updater.py          # Auto-update system (GitHub releases)
│       └── 📄 screen.py           # Screen utilities (ROI management)
│
├── 📁 config/                       # Configuration files
│   └── 📄 settings.json            # User settings (auto-generated)
│
├── 📁 assets/                       # Assets (icons, images)
│   └── (optional: icon.ico)
│
├── 📁 docs/                         # Documentation
│   ├── 📄 SETUP.md                # Developer setup guide
│   └── 📄 USER_GUIDE.md           # User guide
│
├── 📁 build/                        # Build artifacts (git-ignored)
├── 📁 dist/                         # Distribution (git-ignored)
│   └── 📄 mancing_indovoice.exe   # Final executable
│
├── 📄 main.py                      # Application entry point
├── 📄 build.py                     # Build script for PyInstaller
├── 📄 requirements.txt             # Python dependencies
├── 📄 README.md                    # Main documentation
├── 📄 CHANGELOG.md                 # Version history
├── 📄 LICENSE                      # MIT License
├── 📄 .gitignore                   # Git ignore rules
│
└── 📄 (old files - can be deleted)
    ├── roblox_fishing_macro.py    # Old monolithic file
    ├── roblox_fishing_macro.spec  # Old spec file
    └── fishing_macro_settings.json # Old config file
```

## Module Responsibilities

### 🎯 Core Modules

#### `src/core/engine.py`
- `FishingEngine`: Main automation engine
- `ROI`: Region of Interest dataclass
- Click logic, hold/cast logic
- Auto-recast detection
- Callback system for UI updates

#### `src/core/vision.py`
- Screen capture (MSS)
- Color detection (OpenCV HSV)
- Green/red ratio calculation
- Thread-safe screen grabbing

### 🎨 GUI Modules

#### `src/gui/main_window.py`
- `App`: Main window class
- Engine integration & control
- Keybind management
- Auto-update integration
- UI update loop
- Settings synchronization

#### `src/gui/pages.py`
- `HomePage`: Main controls & preview
- `SettingsPage`: Configuration sliders
- `KeybindsPage`: Hotkey settings
- `CreditPage`: Info & update checker

### 🔧 Utility Modules

#### `src/utils/config.py`
- `ConfigManager`: Settings manager
- JSON save/load
- Default configuration
- Validation

#### `src/utils/updater.py`
- `AutoUpdater`: Update checker
- GitHub API integration
- Download manager
- Version comparison

#### `src/utils/screen.py`
- Screen size detection
- ROI creation & clamping
- Display utilities

## Data Flow

```
User Input → GUI (main_window.py)
    ↓
Settings → ConfigManager (config.py)
    ↓
Engine Config → FishingEngine (engine.py)
    ↓
Screen Capture ← Vision (vision.py)
    ↓
Color Analysis → Engine Logic
    ↓
Mouse Actions → PyAutoGUI
    ↓
Callbacks → GUI Updates
```

## Build Process

```
Source Code (src/)
    ↓
build.py → PyInstaller
    ↓
Bundling dependencies
    ↓
dist/mancing_indovoice.exe
    ↓
GitHub Release
    ↓
Auto-Update System → Users
```

## Update Flow

```
User starts app
    ↓
Check GitHub API (updater.py)
    ↓
New version found?
    ↓ Yes
Notify user
    ↓
User accepts
    ↓
Download new .exe
    ↓
Replace & restart
    ↓
Updated!
```

## Key Improvements from v1.0

### Architecture
- ✅ Modular design (single file → multiple modules)
- ✅ Separation of concerns (engine, GUI, utils)
- ✅ Reusable components
- ✅ Easy to test & maintain

### Features
- ✅ Auto-update system
- ✅ Better configuration management
- ✅ Professional build process
- ✅ Comprehensive documentation

### Code Quality
- ✅ Type hints
- ✅ Docstrings
- ✅ Error handling
- ✅ Clean structure

## Dependencies Overview

### Core Dependencies
- `customtkinter`: Modern GUI framework
- `pyautogui`: Mouse automation
- `opencv-python`: Computer vision
- `numpy`: Array operations
- `mss`: Fast screen capture
- `Pillow`: Image processing

### Auto-Update
- `requests`: HTTP client
- `packaging`: Version comparison

### Optional
- `keyboard`: Global hotkeys (requires admin)

### Development
- `pyinstaller`: Executable builder

## Configuration Schema

```json
{
  "roi": {
    "x": int,      // ROI position X
    "y": int,      // ROI position Y
    "w": int,      // ROI width
    "h": int       // ROI height
  },
  "green_th": float,        // Green threshold (0.0-1.0)
  "red_th": float,          // Red threshold (0.0-1.0)
  "click_i": float,         // Click interval (seconds)
  "idle_i": float,          // Idle interval (seconds)
  "hold_s": float,          // Hold duration (seconds)
  "down_s": float,          // MouseDown duration (seconds)
  "inactive_to": float,     // Inactivity timeout (seconds)
  "recast_delay": float,    // Recast delay (seconds)
  "auto_recast": bool,      // Auto recast enabled
  "active_min_ratio": float,// Min color ratio to be active
  "key": string             // Hotkey (e.g., "F1")
}
```

## Version Management

File: `src/version.py`
```python
__version__ = "2.0.0"  # Update this for releases

VERSION_INFO = {
    "major": 2,
    "minor": 0,
    "patch": 0,
}
```

Update this before each release!

## GitHub Repository Setup

1. Create repo: `mancing-indovoice`
2. Update `GITHUB_REPO` in `src/gui/main_window.py`
3. Push code
4. Create release with tag (e.g., `v2.0.0`)
5. Upload `dist/mancing_indovoice.exe`
6. Users get auto-notification!

---

**This is a professional, scalable, and maintainable structure! 🎉**
