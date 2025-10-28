# User Guide - Macro Mancing Indovoice

## 📖 Panduan Lengkap Penggunaan

### 🚀 Getting Started

#### First Time Setup
1. **Download & Run**
   - Download `mancing_indovoice.exe` dari GitHub Releases
   - Jalankan file (tidak perlu install)
   - Windows Defender mungkin warning → klik "More info" → "Run anyway"

2. **Kalibrasi ROI (Region of Interest)**
   - Buka game Roblox fishing
   - Di aplikasi, pilih salah satu metode kalibrasi:
     - **Drag-select**: Paling mudah, tinggal drag area fishing bar
     - **Kursor → ROI**: Taruh kursor di tengah fishing bar, klik button
     - **Manual**: Set width/height manual

3. **Start Fishing!**
   - Tekan **F1** atau klik tombol **Start**
   - Aplikasi akan otomatis detect dan click green bar
   - Auto recast saat mini-game selesai

---

### 🎮 Controls & Hotkeys

#### Default Hotkey
- **F1**: Start/Stop macro (bisa diubah di tab Keybinds)

#### Buttons
- **Start (F1)**: Mulai automation
- **Stop (F1)**: Stop automation
- **Kursor → ROI**: Set ROI dari posisi kursor
- **Drag-select ROI**: Pilih area dengan drag
- **Debug**: Show detection overlay (tekan ESC untuk tutup)

---

### ⚙️ Custom Settings Explained

#### Ambang & Interval Section

**Green ratio ≥** (Default: 0.14)
- Threshold untuk detect hijau
- Nilai tinggi = lebih strict (hanya hijau terang)
- Nilai rendah = lebih loose (termasuk hijau gelap)
- **Rekomendasi**: 0.12 - 0.16

**Red ratio ≥** (Default: 0.10)
- Threshold untuk detect merah
- Gunakan untuk filter false positive
- **Rekomendasi**: 0.08 - 0.12

**Click interval** (Default: 0.035s)
- Jeda antar klik saat hijau detect
- Nilai kecil = spam click cepat
- Nilai besar = click lebih slow
- **Rekomendasi**: 0.03 - 0.05s

**Idle interval** (Default: 0.010s)
- Jeda saat tidak ada aksi
- Affects responsiveness
- **Rekomendasi**: 0.01 - 0.02s

#### Delay Settings Section

**Hold awal** (Default: 3.0s)
- Berapa lama tahan mouse untuk cast
- Tergantung game (fishing rod type)
- **Rekomendasi**: 2.5 - 4.0s

**MouseDown** (Default: 0.01s)
- Durasi klik individual
- Biasanya tidak perlu diubah
- **Rekomendasi**: 0.005 - 0.02s

#### Auto Recast Section

**Inactivity timeout** (Default: 1.2s)
- Berapa lama tunggu sebelum recast
- Setelah mini-game hilang
- **Rekomendasi**: 1.0 - 2.0s

**Recast delay** (Default: 0.30s)
- Jeda sebelum cast ulang
- Biar smooth, tidak langsung
- **Rekomendasi**: 0.2 - 0.5s

**Aktifkan Auto Recast** (Default: ON)
- Toggle auto recast on/off
- Jika OFF, harus manual cast ulang

---

### 🎯 Tips & Tricks

#### Optimal ROI Placement
1. ROI harus cover seluruh fishing bar (hijau & merah)
2. Jangan terlalu besar (include background)
3. Jangan terlalu kecil (potong bar)
4. Test dengan Debug mode

#### Best Settings for Different Games
Different fishing games mungkin perlu settings berbeda:

**Fast-paced games**:
- Green threshold: 0.12
- Click interval: 0.03s
- Hold awal: 2.5s

**Slow-paced games**:
- Green threshold: 0.16
- Click interval: 0.04s
- Hold awal: 3.5s

#### Performance Tips
1. **Close unnecessary apps** untuk CPU/RAM
2. **Run game in windowed mode** lebih stable
3. **Disable game effects** kalau ada option
4. **Use fixed ROI** jangan moving window

#### Avoiding Detection
> **Disclaimer**: Use at your own risk. Some games prohibit automation.

- Add random delays (future feature)
- Don't run 24/7
- Take breaks manually
- Use human-like patterns

---

### 🐛 Debugging Issues

#### "Not Clicking" Problem
1. **Check ROI**: Use Debug mode, pastikan green terdetect
2. **Adjust threshold**: Lower green_th di settings
3. **Re-calibrate**: ROI mungkin bergeser
4. **Check game**: Pastikan fishing bar visible

#### "Clicking Too Much" Problem
1. **Increase threshold**: Higher green_th
2. **Increase interval**: More delay between clicks
3. **Check ROI**: Mungkin terlalu besar, detect false positive

#### "Not Recasting" Problem
1. **Enable Auto Recast**: Check switch di settings
2. **Adjust timeout**: Increase inactivity_timeout
3. **Check bar disappears**: Debug mode untuk confirm

#### "Hotkey Not Working" Problem
1. **Global vs Local**:
   - Global (admin): Works everywhere
   - Local: Only when app has focus
2. **Try different key**: Mungkin conflict
3. **Run as admin**: For global hotkey
4. **Check keyboard module**: Must be installed

---

### 💾 Presets & Configuration

#### Saving Preset
1. Adjust semua settings sesuai keinginan
2. Klik **"Simpan Preset"** di Custom Settings
3. Settings saved to `config/settings.json`

#### Loading Preset
1. Klik **"Muat Preset"**
2. All settings akan restore from file
3. Useful untuk switch between games

#### Manual Config Edit
File: `config/settings.json`

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

Edit dengan text editor, restart app.

---

### 🔄 Using Auto-Update

#### Automatic Check
- App checks for updates on startup
- Notification popup jika ada update baru
- Click "Yes" untuk download & install

#### Manual Check
1. Go to **Credit** tab
2. Click **"Cek Update"** button
3. Follow prompts if update available

#### Update Process
1. App downloads new .exe
2. Notification saat selesai download
3. Click OK → app restart dengan version baru
4. Old version otomatis replaced

---

### 📊 Understanding the UI

#### Home Page
- **Start/Stop button**: Main control
- **Status label**: Running/Stopped
- **Progress bars**: Green & Red detection levels
- **Action label**: Current action (Hold, Click, Idle, etc.)
- **Preview**: Live ROI preview (when running)

#### Custom Settings Page
- All threshold & timing adjustments
- Preset save/load buttons

#### Keybinds Page
- Change start/stop hotkey
- Shows global vs local status

#### Credit Page
- Version information
- Developer links
- Update checker

---

### 🎓 Advanced Usage

#### Multiple Profiles (Manual)
1. Create multiple config files: `config/profile1.json`, `config/profile2.json`
2. Copy `config/settings.json` struktur
3. Before running, rename yang mau dipakai jadi `settings.json`

#### Running Multiple Instances
- Currently not supported (single instance)
- Future feature untuk multi-window

#### Custom Keybinds
Supported keys:
- **F1-F12**: Function keys
- **A-Z**: Single letters
- **0-9**: Numbers

Not supported (yet):
- Combinations (Ctrl+F1, etc.)
- Special keys (Space, Enter, etc.)

---

### ⚠️ Important Notes

#### Safety
- **PyAutoGUI Failsafe**: Move mouse ke corner untuk emergency stop
- **ESC in Debug**: Close debug window
- **Task Manager**: Force close jika stuck

#### Performance
- CPU usage normal: 5-15%
- RAM usage: ~100-200 MB
- Minimal impact on game FPS

#### Compatibility
- **OS**: Windows 10/11
- **Python**: 3.8+ (untuk run from source)
- **Screen**: Works on any resolution
- **Multiple monitors**: Select correct monitor

---

### 🆘 Getting Help

#### Common Issues
1. Check [Troubleshooting](#-debugging-issues) section
2. Use Debug mode untuk diagnose
3. Try default settings first

#### Still Need Help?
- **GitHub Issues**: Report bugs dengan detail
- **Discord**: Join untuk live help
- **Include**:
  - OS version
  - App version
  - Screenshot of issue
  - Settings yang dipakai

---

### 📈 Best Practices

✅ **DO:**
- Kalibrasi ROI dengan benar
- Test settings dengan Debug mode
- Save preset saat udah optimal
- Update aplikasi regularly
- Take breaks (for you, not bot 😄)

❌ **DON'T:**
- Run di game yang explicitly ban macros
- Share account credentials
- Run 24/7 without monitoring
- Use extreme settings (too fast = suspicious)
- Forget to update

---

## Quick Reference Card

```
╔══════════════════════════════════════════════╗
║         QUICK REFERENCE CARD                 ║
╠══════════════════════════════════════════════╣
║ START/STOP:           F1 (customizable)      ║
║ EMERGENCY STOP:       Move mouse to corner   ║
║ DEBUG MODE:           Click Debug button     ║
║ CLOSE DEBUG:          Press ESC              ║
║                                              ║
║ OPTIMAL SETTINGS:                            ║
║   Green threshold:    0.12 - 0.16            ║
║   Click interval:     0.03 - 0.05s           ║
║   Hold duration:      2.5 - 4.0s             ║
║   Recast timeout:     1.0 - 2.0s             ║
║                                              ║
║ FILES:                                       ║
║   Settings:           config/settings.json   ║
║   Logs:               (none currently)       ║
╚══════════════════════════════════════════════╝
```

---

**Happy Fishing! 🎣**

Need more help? Check [docs/SETUP.md](SETUP.md) for developer guide.
