# Changelog

All notable changes to Macro Mancing Indovoice will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

---

## [1.2.0] - 2025-10-29

### Added
- 🎨 **Component-Based Architecture**: Professional modular GUI system
  - `src/gui/components.py` with 6 reusable components
  - `Card`: Container with title and icon
  - `StatusBar`: Status indicator with live updates
  - `ProgressIndicator`: Labeled progress bar
  - `ActionButton`: Styled button with primary/secondary variants
  - `SettingSlider`: Slider with live value display
  - `CompactSwitch`: Switch with optional indent support
- ⌨️ **Dual Keybind System**: Separate customizable hotkeys
  - ROI Calibration hotkey (default F2)
  - Macro Start/Stop hotkey (default F1)
  - Both fully customizable in Keybinds page
  - Conflict detection prevents duplicate keys
- 🎯 **Enhanced ROI Calibration**: 
  - F2 hotkey for quick drag-select (customizable)
  - Removed cursor calibration (simplified workflow)
  - Dynamic button text shows current keybind
- 🪟 **Always-On-Top Debug Window**: 
  - Debug overlay now stays above game window
  - Uses `cv2.WND_PROP_TOPMOST` flag
  - Better visibility during gameplay
- 📐 **Compact Window Design**: 
  - Reduced from 1100x700 to 900x600
  - Optimized for macro usage
  - Auto-centered on screen at launch
- 🎨 **Modern UI Refinements**:
  - Clean table layout in Keybinds page
  - Fixed grid alignment (200px, 120px, 150px columns)
  - Visual separators between keybind rows
  - Typography hierarchy (20px → 14px → 11px)
  - Auto-clearing status messages (2s timeout)
  - Icon-labeled settings cards (⚙️, ⏱️, 🔄)
  - Version badge in topbar

### Changed
- 🏗️ **Major Refactor**: HomePage, SettingsPage, KeybindsPage now use components
- 📦 **Build Optimization**: Reduced to 57.5 MB (from 58.1 MB)
  - Excluded unnecessary modules (matplotlib, scipy, pandas, test frameworks)
  - Bytecode optimization level 2
  - Disabled UPX compression (avoids false positives)
- 🎛️ **UI Layout**: Split HomePage into left/right panels for better organization
- ⚙️ **Settings Page**: Uses SettingSlider components, cleaner code
- 🔑 **Keybinds Page**: Complete redesign with table layout and clickable buttons

### Fixed
- 🐛 **Progress Bar Updates**: Fixed `set()` → `set_value()` method calls
- 🖼️ **Preview Sizing**: Adjusted for compact window (180-360px width)
- 📝 **Config Persistence**: Added `roi_key` to settings.json

### Removed
- ❌ **Cursor Calibration**: Removed `calibrate_from_cursor()` feature
- ❌ **PyAutoGUI Import**: No longer needed for cursor-based calibration

---

## [1.1.0] - 2025-10-28

### Added
- ⏸️ **Auto-Pause System**: Intelligent macro pausing
  - Automatically pause when typing in Roblox window
  - Automatically pause when Alt+Tab from Roblox (focus loss)
  - Configurable resume delay (default 2 seconds)
  - Toggle controls in Home page for easy access
  - Separate toggles: "Pause saat mengetik" and "Pause saat Alt+Tab"
  - Real-time status indicator shows "⏸️ Auto-Paused..." during pause
- 🔧 **New Dependencies**: pywin32, psutil, pynput for Windows integration

### Changed
- 🎛️ Moved auto-pause controls from Settings to Home page for better UX
- 📦 Build size optimized to 58.1 MB (from 60.6 MB)

---

## [1.0.0] - 2025-10-28

### Added
- � **Auto-Update System**: Automatic update checking and one-click installation
- 📁 **Professional Structure**: Modular codebase with organized folders
  - `src/core/`: Engine and vision modules
  - `src/gui/`: User interface components
  - `src/utils/`: Utilities (config, updater, screen)
- 📝 **Configuration System**: JSON-based settings with save/load
- 🎨 **Modern UI**: Separated pages for better organization
  - Home page with controls and preview
  - Scrollable Settings page with all adjustments
  - Keybinds page with press-to-bind system
  - Credit page with update checker
- 📜 **Scrollable UI**: Semua pages responsive dengan mousewheel scroll
- ⌨️ **Press-to-Bind Keybinds**: Setup hotkey dengan tekan tombol langsung
- 🎯 **Auto-Minimize ROI Selection**: App minimize otomatis saat drag-select untuk clear view
- 📝 **On-screen Instructions**: Panduan visual saat selection
- 📦 **Build System**: Professional build script dengan PyInstaller dan custom icon
- 📖 **Documentation**: Comprehensive README, USER_GUIDE, dan docs lengkap
- 🎯 **Color Detection**: HSV-based green bar detection
- ♻️ **Auto Recast**: Automatic fishing rod casting
- 🖼️ **ROI Calibration**: Drag-select dan click-based ROI setup
- 🐛 **Debug Window**: Real-time preview dengan OpenCV
- 💾 **Preset System**: Save/Load configurations
- 🔑 **Global Hotkeys**: F6 (start/stop), F7 (hold cast), F8 (exit)

### Fixed
- 🐛 **Debug Window**: Fixed OpenCV frame layout error dengan contiguous array
- 🔄 **Update Check Error Handling**: Better error messages untuk update check failures
  - Repository not found → "Repository belum dibuat atau tidak ditemukan"
  - Connection errors → "Tidak dapat terhubung ke server"
  - Silent fail pada startup (tidak ganggu user)
  - Colored status messages (✅ success, ❌ error)

### Improved
- 🎨 **Better UX**: Grid-based responsive layout
- 📐 **Layout**: Tidak perlu fullscreen untuk akses semua tombol
- 🔄 **Credit Page**: Separated sections, prominent update button, better typography
- ⌨️ **Keybind Page**: Visual feedback, ESC cancel, validation, supported keys list
- 🎯 **ROI Selection**: Auto-minimize/restore, smooth transitions
- � **Maintainability**: Modular structure, easier to extend
- � **Error Handling**: Better debugging dan logging
- 📊 **Performance**: Optimized screen capture dengan MSS dan threading

---

## Future Plans

### [1.3.0] - Planned
- [ ] Statistics tracking (total catches, catches per hour, session time)
- [ ] Profile system (save multiple presets dengan nama)
- [ ] Discord webhook notifications (catches milestone, errors, session summary)
- [ ] Sound/visual alerts (when stopped, rare catch, etc.)

### [1.4.0] - Ideas
- [ ] Failsafe system (max runtime, emergency stop, random delays)
- [ ] Session scheduler (auto start/stop pada waktu tertentu)
- [ ] Plugin system for extensibility
- [ ] Cloud sync for settings
- [ ] Mobile app for remote control
- [ ] Multi-monitor support improvements

---

**Note**: Dates use YYYY-MM-DD format. Links to releases will be added when published on GitHub.
