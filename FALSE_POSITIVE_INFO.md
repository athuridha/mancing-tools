# ⚠️ False Positive Virus Detection

## Kenapa Windows Defender/Antivirus mendeteksi sebagai virus?

**BUKAN VIRUS!** Ini adalah **false positive** yang umum terjadi pada aplikasi automation Python.

### Alasan Teknis:

1. **PyInstaller Bundling**
   - Executable dibuat dengan PyInstaller yang mem-bundle Python interpreter + semua libraries
   - Antivirus tidak mengenali struktur file ini dan menganggap "suspicious"

2. **Automation Features**
   - `PyAutoGUI`: Mouse clicking automation
   - `keyboard`: Global hotkey listening
   - `pynput`: Keyboard event detection
   - Antivirus mendeteksi ini sebagai "keylogger behavior" padahal cuma untuk auto-pause

3. **Windows API Access**
   - `pywin32`: Mengakses window title dan focus detection
   - Diperlukan untuk fitur auto-pause (detect Roblox window)

4. **Unsigned Executable**
   - Code signing certificate mahal ($300-500/tahun)
   - Open source project tidak punya budget untuk signing

5. **Low Reputation Score**
   - File baru, belum banyak yang download
   - Windows SmartScreen belum "trust" file ini

---

## ✅ Cara Mengatasi False Positive

### Opsi 1: Whitelist/Exclude (Recommended)

**Windows Defender:**
1. Buka **Windows Security** → **Virus & threat protection**
2. Klik **Manage settings** di "Virus & threat protection settings"
3. Scroll ke bawah, klik **Add or remove exclusions**
4. Klik **Add an exclusion** → **Folder**
5. Pilih folder tempat `mancing.exe` berada

**Kaspersky/Avast/AVG/etc:**
- Cari menu "Exclusions" atau "Whitelist"
- Add folder/file `mancing.exe`

### Opsi 2: Allow When Running

Ketika Windows Defender block:
1. Klik **"More info"**
2. Klik **"Run anyway"**

### Opsi 3: Build Sendiri (Most Trusted)

Kalau masih curiga, build sendiri dari source code:

```bash
# Clone repository
git clone https://github.com/athuridha/mancing-tools.git
cd mancing-tools

# Install dependencies
pip install -r requirements.txt

# Build
python build.py

# Executable di folder dist/
```

---

## 🔍 Verify Source Code (100% Open Source)

Semua source code bisa dilihat di:
- **GitHub**: https://github.com/athuridha/mancing-tools
- **No obfuscation**, semua readable
- **No telemetry**, tidak ada data collection
- **No network calls** kecuali update checker (optional)

### Key Files:
- `src/core/engine.py` - Fishing automation logic
- `src/core/vision.py` - OpenCV screen detection
- `src/utils/auto_pause.py` - Keyboard & window detection
- `src/gui/` - User interface
- `build.py` - Build script (transparent)

---

## 📊 VirusTotal Scan

Upload `mancing.exe` ke https://www.virustotal.com untuk second opinion:
- **Expected**: 2-5 detections dari 70+ scanners
- **Common flags**: "Generic", "Heuristic", "ML detection"
- **Not**: "Trojan.Banker", "Ransomware", specific malware names

False positive patterns:
- ✅ `Win32.Generic` - Generic heuristic
- ✅ `ML.Attribute` - Machine learning flag
- ✅ `HeurEngine` - Behavior analysis
- ❌ `Trojan.Stealer` - Specific malware (ini baru masalah!)

---

## 🛡️ Safety Guarantees

1. **Open Source**: Semua kode bisa di-audit
2. **No Admin Required**: Tidak minta elevated privileges
3. **No Network**: Hanya HTTP GET ke GitHub untuk update check
4. **No Persistence**: Tidak auto-start, tidak edit registry
5. **Sandboxed**: Hanya akses folder sendiri untuk config

---

## 🤔 Still Not Sure?

**Jangan percaya! Build sendiri:**

```bash
# Install Python 3.12
# Download dari python.org

# Clone & build
git clone https://github.com/athuridha/mancing-tools.git
cd mancing-tools
pip install -r requirements.txt
python build.py

# Check build.py untuk lihat PyInstaller command
# No hidden steps, semua transparent
```

**Atau run langsung dari source:**

```bash
python main.py
```

Tidak perlu percaya executable yang di-download! 🔒

---

## 📧 Questions?

Buka issue di GitHub: https://github.com/athuridha/mancing-tools/issues

**Remember**: Real malware tidak publish source code mereka! 😉
