# 🎣 Mancing Tools v1.2.0 - Simple & Advance Mode

## 🚀 What's New

### ✨ Major Features

#### 🎯 Simple Mode (Default)
- **Default startup**: Aplikasi sekarang langsung buka dalam Simple Mode
- **Compact window**: 400x340px window yang always-on-top
- **Essential controls**: Start/Stop, ROI calibration, Debug, Status
- **Easy access**: Quick buttons untuk Settings dan Advance Mode
- **Clean UI**: Card-based layout dengan spacing yang rapih

#### 🖥️ Advance Mode
- **Full features**: Akses semua fitur advanced (Home, Settings, Keybinds, Credit)
- **Quick toggle**: Button "📐 Simple Mode" di topbar untuk switch cepat
- **Enhanced UI**: Topbar yang lebih modern dan clean

#### 📥 System Tray Integration
- **Minimize to tray**: Click minimize button langsung masuk system tray
- **Tray menu**: Right-click untuk Show, Simple Mode, Start/Stop, Exit
- **Quick restore**: Double-click icon untuk restore window
- **Background mode**: Macro bisa jalan di background tanpa ganggu

### 🎨 UI/UX Improvements
- ✅ Better spacing dan padding di semua components
- ✅ Icon-based buttons untuk visual cues (▶/⏹ untuk Start/Stop)
- ✅ Card-based layout untuk organization yang lebih baik
- ✅ Consistent typography dan colors
- ✅ Topbar dengan darker background untuk better contrast

## 📦 Installation

1. Download `mancing.exe` dari releases
2. Jalankan executable (tidak perlu Python)
3. Allow di Windows Defender jika ada warning (false positive)

## 🎮 Quick Start

### Simple Mode (Recommended)
1. Aplikasi langsung buka dalam Simple Mode
2. Click **Drag-select (F2)** untuk kalibrasi ROI
3. Click **▶ Start (F1)** untuk mulai fishing
4. Minimize window akan ke system tray

### Advance Mode
1. Click **🔧 Advance Mode** untuk akses fitur lengkap
2. Customize settings, keybinds, dll
3. Click **📐 Simple Mode** untuk kembali

## ⚙️ System Requirements

- Windows 10/11
- 4GB RAM minimum
- Python 3.8+ (jika run from source)

## 🐛 Bug Fixes & Improvements

- Fixed minimize behavior (now goes to tray)
- Improved window management
- Better state handling between modes
- Enhanced system tray integration

## 📝 Known Issues

- Windows Defender may flag as false positive (safe to ignore)
- Minimize button behavior requires iconify override

## 🔄 Upgrade Notes

### From v1.1.0:
- All settings preserved
- New Simple/Advance mode system
- System tray functionality added
- UI completely redesigned

### Dependencies Added:
- `pystray>=0.19.4` - System tray support

## 👨‍💻 Developer Notes

### New Files:
- `src/gui/simple_window.py` - Simple Mode UI
- `src/utils/system_tray.py` - System tray manager

### Modified Files:
- `src/gui/main_window.py` - Advance Mode & mode switching
- `build.py` - Added pystray hidden imports
- `requirements.txt` - Added pystray dependency

## 📊 Statistics

- **Size**: ~60-65 MB (executable)
- **Startup time**: Simple Mode < 1s
- **Memory usage**: ~80-120 MB average

## 🙏 Credits

**Developer**: Amar ([@athuridha](https://github.com/athuridha))
- Roblox: [xinnercy](https://www.roblox.com/share?code=e089bc5df260ea42890e0e800c13faec)
- Discord: halflucifer

**Made with**:
- Python 3.12
- CustomTkinter (Modern GUI)
- OpenCV (Computer Vision)
- pystray (System Tray)
- pywin32, psutil, pynput (Auto-Pause)

---

## 📥 Download

**[Download mancing.exe](https://github.com/athuridha/mancing-tools/releases/tag/v1.2.0)**

**Full Changelog**: [CHANGELOG.md](CHANGELOG.md)

---

<div align="center">

**Happy Fishing! 🎣**

Made with ❤️ for tukang AFK di indovoice

</div>
