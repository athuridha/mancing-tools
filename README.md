# Macro Mancing Indovoice

<div align="center">

![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

**Professional Roblox Fishing Macro with Auto-Update**

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Build](#build)

</div>

---

## 🎣 Features

### Core Features
- **Automatic Fishing**: Detects green bar and auto-clicks
- **Auto Recast**: Automatically recasts fishing rod when mini-game ends
- **ROI Calibration**: Multiple ways to set detection area
  - Cursor-based positioning
  - Drag-to-select on screen
  - Manual width/height adjustment
- **Debug Mode**: Visual feedback for color detection

### Advanced Features
- **Custom Settings**: Fine-tune all detection thresholds
- **Preset System**: Save and load your configurations
- **Global Hotkeys**: Start/stop from anywhere (F1 default)
- **Live Preview**: Real-time ROI preview and color ratios
- **Professional GUI**: Modern dark-themed interface

### Auto-Update System
- **Automatic Update Check**: Checks for updates on startup
- **One-Click Update**: Download and install updates easily
- **Version Management**: Always stay on the latest version

---

## 📦 Installation

### Option 1: Use Pre-built Executable (Recommended)
1. Download the latest `.exe` from [Releases](https://github.com/xinnercy/mancing-indovoice/releases)
2. Run `mancing_indovoice.exe`
3. That's it! No installation needed.

### Option 2: Run from Source
```bash
# Clone repository
git clone https://github.com/xinnercy/mancing-indovoice.git
cd mancing-indovoice

# Install dependencies
pip install -r requirements.txt

# Run application
python main.py
```

---

## 🚀 Usage

### Quick Start
1. Launch the application
2. Position your Roblox fishing game window
3. Click **"Drag-select ROI"** and select the fishing bar area
4. Press **F1** or click **"Start"** to begin

### Configuration
Navigate to **Custom Settings** to adjust:
- **Green/Red Thresholds**: Detection sensitivity
- **Click Intervals**: Response speed
- **Hold Duration**: Initial cast time
- **Auto Recast Settings**: Timing for automatic recasting

### Keybinds
- Default: **F1** (Start/Stop)
- Customize in **Keybinds** tab
- Supports F1-F12 and single letters/numbers

### ROI Calibration
1. **Kursor → ROI**: Center ROI at current mouse position
2. **Drag-select ROI**: Click and drag to select area
3. **Manual W/H**: Enter specific dimensions

---

## 🏗️ Build from Source

### Build Executable
```bash
# Install PyInstaller
pip install pyinstaller

# Build
python build.py
```

The executable will be in `dist/mancing_indovoice.exe`

### Build Options
Edit `build.py` to customize:
- Icon file
- Console mode (show/hide)
- Additional data files
- Compression options

---

## 📁 Project Structure

```
mancing-indovoice/
├── src/
│   ├── core/              # Core engine and vision
│   │   ├── engine.py      # Fishing automation logic
│   │   └── vision.py      # Color detection & screen capture
│   ├── gui/               # User interface
│   │   ├── main_window.py # Main application window
│   │   └── pages.py       # UI pages (Home, Settings, etc.)
│   ├── utils/             # Utilities
│   │   ├── config.py      # Configuration management
│   │   ├── updater.py     # Auto-update system
│   │   └── screen.py      # Screen utilities
│   └── version.py         # Version information
├── config/                # Configuration files
│   └── settings.json      # User settings (auto-generated)
├── main.py               # Entry point
├── build.py              # Build script
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

---

## ⚙️ Configuration File

Settings are saved to `config/settings.json`:

```json
{
  "roi": {"x": 697, "y": 892, "w": 526, "h": 70},
  "green_th": 0.14,
  "red_th": 0.10,
  "click_i": 0.035,
  "idle_i": 0.010,
  "hold_s": 3.0,
  "down_s": 0.01,
  "inactive_to": 1.2,
  "recast_delay": 0.30,
  "auto_recast": true,
  "key": "F1"
}
```

---

## 🔄 Auto-Update System

The application automatically checks for updates:
- **On Startup**: Silent check in background
- **Manual Check**: Click "Cek Update" in Credit tab
- **Notifications**: Popup when new version available
- **One-Click Install**: Download and restart automatically

### For Developers: Creating Releases
1. Update version in `src/version.py`
2. Build executable: `python build.py`
3. Create GitHub release with tag (e.g., `v2.0.0`)
4. Upload `.exe` as release asset
5. Users will be notified automatically!

---

## 🐛 Troubleshooting

### Hotkey Not Working
- Try running as Administrator for global hotkeys
- Use local hotkeys (requires app focus) as fallback
- Check no other app is using the same key

### Detection Not Accurate
- Recalibrate ROI to match fishing bar exactly
- Adjust green/red thresholds in settings
- Use Debug mode to see detection overlay

### Application Won't Start
- Install Visual C++ Redistributable
- Check antivirus isn't blocking
- Run from command line to see errors

---

## 📝 Credits

**Developer**: lamont (@xinnercy)
- Roblox: [xinnercy](https://www.roblox.com/users/8179160997/)
- Discord: halflucifer

**Support the Project**:
- ⭐ Star this repository
- 🐛 Report bugs via Issues
- 💡 Suggest features
- ☕ Donate (if you want hehe)

---

## 📜 License

MIT License - feel free to use and modify!

---

## 🔗 Links

- **GitHub**: https://github.com/xinnercy/mancing-indovoice
- **Discord**: https://discord.gg/SWzSjeF3
- **Issues**: https://github.com/xinnercy/mancing-indovoice/issues

---

<div align="center">

Made with ❤️ for the Roblox fishing community

**Happy Fishing! 🎣**

</div>
