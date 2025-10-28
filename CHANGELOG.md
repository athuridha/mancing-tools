# Changelog

All notable changes to Macro Mancing Indovoice will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- 📜 **Scrollable Settings Page**: Custom Settings sekarang bisa di-scroll dengan mousewheel
- 📱 **Responsive UI**: Semua pages sekarang responsive terhadap resize window
- 📜 **Scrollable Credit Page**: Credit page juga bisa di-scroll untuk konten yang panjang
- ⌨️ **Press-to-Bind System**: Keybind setup sekarang dengan tekan tombol langsung, tidak perlu ketik manual
- 🎯 **Auto-Minimize on ROI Selection**: Aplikasi otomatis minimize saat drag-select ROI untuk clear view
- 📝 **Selection Instructions**: Instruksi on-screen saat drag-select ROI

### Fixed
- 🐛 **Debug Window**: Fixed OpenCV frame layout error dengan contiguous array
- 🔄 **Update Check Error Handling**: Better error messages untuk update check failures
  - Repository not found → "Repository belum dibuat atau tidak ditemukan"
  - Connection errors → "Tidak dapat terhubung ke server"
  - Silent fail pada startup (tidak ganggu user)
  - Colored status messages (✅ success, ❌ error)

### Improved
- 🎨 **Better UX**: Tidak perlu fullscreen lagi untuk akses tombol Save/Load Preset
- 📐 **Layout**: Grid-based layout yang lebih flexible dan responsive
- 🔄 **Credit Page Design**: 
  - Separated sections dengan visual separators
  - Update button lebih prominent dengan icon
  - Better spacing dan typography
  - Wrapping text untuk update status
  - Added footer message
- ⌨️ **Keybind Page Redesign**:
  - Visual "Press Any Key" button
  - Real-time key detection
  - Clear visual feedback (colors, emojis)
  - Cancel dengan ESC
  - Validation otomatis
  - Supported keys list
- 🎯 **ROI Selection UX**:
  - Auto-minimize aplikasi saat mulai selection
  - Auto-restore setelah selesai
  - On-screen instructions
  - Smooth transitions

---

## [2.0.0] - 2025-10-28

### Added
- 🚀 **Auto-Update System**: Automatic update checking and one-click installation
- 📁 **Professional Structure**: Modular codebase with organized folders
  - `src/core/`: Engine and vision modules
  - `src/gui/`: User interface components
  - `src/utils/`: Utilities (config, updater, screen)
- 📝 **Configuration System**: JSON-based settings with save/load
- 🎨 **Improved UI**: Separated pages for better organization
  - Home page with controls and preview
  - Settings page with all adjustments
  - Keybinds page for hotkey configuration
  - Credit page with update checker
- 📦 **Build System**: Professional build script with PyInstaller
- 📖 **Documentation**: Comprehensive README and inline docs

### Changed
- ♻️ **Refactored**: Complete code restructure from single file to modular
- 🎯 **Engine**: Separated logic into FishingEngine class
- 👁️ **Vision**: Isolated color detection and screen capture
- ⚙️ **Config**: Centralized configuration management

### Improved
- 🔧 **Maintainability**: Easier to update and extend
- 🐛 **Debugging**: Better error handling and logging
- 📊 **Performance**: Optimized screen capture and processing
- 🎮 **UX**: More intuitive interface and controls

### Fixed
- 🔑 **Hotkeys**: Improved global and local hotkey handling
- 🖼️ **Preview**: More stable ROI preview rendering
- 💾 **Settings**: Reliable save/load of configurations

---

## [1.0.0] - 2024-XX-XX

### Initial Release
- ✨ Basic fishing automation
- 🎯 Green bar detection and clicking
- ♻️ Auto recast functionality
- 🖼️ ROI calibration tools
- ⚙️ Custom settings
- 🔑 Global hotkey support (F1)
- 🐛 Debug mode
- 💾 Preset save/load
- 🎨 Modern GUI with CustomTkinter

---

## Future Plans

### [2.1.0] - Planned
- [ ] Multi-game support (different fishing games)
- [ ] Statistics tracking (catches per hour, etc.)
- [ ] Profile system (multiple configurations)
- [ ] Notification system (Discord webhooks?)
- [ ] Advanced detection (machine learning?)

### [2.2.0] - Ideas
- [ ] Plugin system for extensibility
- [ ] Cloud sync for settings
- [ ] Mobile app for remote control
- [ ] Anti-detection features
- [ ] Multi-monitor support improvements

---

**Note**: Dates use YYYY-MM-DD format. Links to releases will be added when published on GitHub.
