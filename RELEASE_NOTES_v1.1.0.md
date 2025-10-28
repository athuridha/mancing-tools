# v1.1.0 - Auto-Pause System 🎉

## 🆕 What's New

### ⏸️ Auto-Pause System
Fitur baru yang bikin macro lebih aman dan natural!

**Features:**
- ⌨️ **Auto-pause saat mengetik** - Macro berhenti otomatis ketika kamu ketik di Roblox
- 🪟 **Auto-pause saat Alt+Tab** - Macro berhenti otomatis ketika window Roblox kehilangan focus
- ⏱️ **Configurable resume delay** - Delay 2 detik sebelum resume (bisa diatur)
- 🎛️ **Toggle controls di Home page** - Mudah nyalakan/matikan langsung dari halaman utama
- 👁️ **Real-time status** - Status indicator menunjukkan `⏸️ Auto-Paused...` saat pause

**Cara Pakai:**
1. Buka Macro Mancing Indovoice
2. Di Home page, aktifkan **`Aktifkan Auto-Pause`**
3. Pilih opsi yang diinginkan:
   - ✅ Pause saat mengetik
   - ✅ Pause saat Alt+Tab
4. Start macro seperti biasa
5. Macro akan pause otomatis sesuai setting!

---

## 🔧 Technical Improvements
- 📦 Build size optimized: **58.1 MB** (dari 60.6 MB)
- 🪟 Integrated Windows API untuk window detection (pywin32)
- ⚡ Real-time keyboard listener (pynput)
- 🎯 Better UX dengan controls di Home page

---

## 📋 Requirements
- Windows 10/11
- Roblox Indovoice Server

---

## 📥 Installation
1. Download **`mancing.exe`** dari Assets di bawah
2. Jalankan file (Windows Defender mungkin warning, klik "More Info" → "Run Anyway")
3. Enjoy fishing! 🎣

---

## ⚠️ Important Notes
- Tool ini **HANYA untuk Indovoice Server**
- Pastikan Roblox window title contains `Roblox`
- Auto-pause bekerja dengan keyboard listener & window focus detection
- Kalau auto-pause tidak bekerja, pastikan app di-run as Administrator

---

## 🐛 Bug Reports & Feature Requests
Ada masalah atau ide? [Open an issue](https://github.com/athuridha/mancing-tools/issues)

---

## 📝 Full Changelog
https://github.com/athuridha/mancing-tools/compare/v1.0.0...v1.1.0

### Added
- ⏸️ Auto-Pause System with keyboard and window focus detection
- 🔧 New dependencies: pywin32, psutil, pynput

### Changed
- 🎛️ Moved auto-pause controls from Settings to Home page
- 📦 Optimized build size to 58.1 MB

---

**Previous version:** [v1.0.0](https://github.com/athuridha/mancing-tools/releases/tag/v1.0.0)
