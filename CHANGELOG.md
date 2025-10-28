# Changelog

All notable changes to Macro Mancing Indovoice will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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

### [1.1.0] - Planned
- [ ] Multi-game support (different fishing games)
- [ ] Statistics tracking (catches per hour, etc.)
- [ ] Profile system (multiple configurations)
- [ ] Notification system (Discord webhooks?)
- [ ] Advanced detection (machine learning?)

### [1.2.0] - Ideas
- [ ] Plugin system for extensibility
- [ ] Cloud sync for settings
- [ ] Mobile app for remote control
- [ ] Anti-detection features
- [ ] Multi-monitor support improvements

---

**Note**: Dates use YYYY-MM-DD format. Links to releases will be added when published on GitHub.
