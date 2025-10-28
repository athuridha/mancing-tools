# Setup Instructions

## Panduan Lengkap Setup dan Deploy

### 1. Setup Development Environment

```bash
# Install semua dependencies
pip install -r requirements.txt

# Install PyInstaller untuk build
pip install pyinstaller
```

### 2. Testing Application

```bash
# Jalankan dari source
python main.py
```

### 3. Build Executable

```bash
# Build executable
python build.py

# Hasil ada di: dist/mancing_indovoice.exe
```

### 4. Setup GitHub Repository (Untuk Auto-Update)

#### A. Create Repository
1. Buat repository baru di GitHub: `mancing-indovoice`
2. Push semua kode:
```bash
git init
git add .
git commit -m "Initial commit v2.0.0"
git branch -M main
git remote add origin https://github.com/USERNAME/mancing-indovoice.git
git push -u origin main
```

#### B. Update Repository Name di Code
Edit `src/gui/main_window.py` line 44:
```python
GITHUB_REPO = "USERNAME/mancing-indovoice"  # Ganti USERNAME dengan GitHub username Anda
```

#### C. Create First Release
1. Build executable: `python build.py`
2. Pergi ke GitHub → Releases → Create new release
3. Tag version: `v2.0.0`
4. Release title: `Macro Mancing Indovoice v2.0.0`
5. Deskripsi: Copy dari CHANGELOG.md
6. Upload file: `dist/mancing_indovoice.exe`
7. Publish release

### 5. Update Workflow (Untuk Update Selanjutnya)

Setiap kali mau release update:

```bash
# 1. Update version di src/version.py
# Contoh: ubah dari "2.0.0" ke "2.1.0"

# 2. Update CHANGELOG.md dengan perubahan

# 3. Commit changes
git add .
git commit -m "Release v2.1.0"
git push

# 4. Build executable baru
python build.py

# 5. Create new GitHub release
# - Tag: v2.1.0
# - Upload: dist/mancing_indovoice.exe

# 6. Users akan otomatis dapet notifikasi update!
```

### 6. Testing Auto-Update

1. Jalankan aplikasi versi lama
2. Buat release baru di GitHub dengan version lebih tinggi
3. Restart aplikasi → akan muncul notifikasi update
4. Klik "Yes" → download otomatis → install

### 7. Distribution

#### Untuk Pengguna:
- Download `mancing_indovoice.exe` dari [Releases](https://github.com/USERNAME/mancing-indovoice/releases)
- Jalankan langsung, no installation needed
- Update otomatis saat ada versi baru

#### Untuk Developer:
- Clone repository
- Install requirements: `pip install -r requirements.txt`
- Run: `python main.py`
- Build: `python build.py`

### 8. Troubleshooting Build

#### Error: "PyInstaller not found"
```bash
pip install pyinstaller
```

#### Error: "Module not found"
```bash
pip install -r requirements.txt
```

#### Error: "Permission denied"
- Run as Administrator
- Disable antivirus temporarily

#### Build berhasil tapi .exe tidak jalan
- Check Windows Defender/Antivirus
- Test di komputer lain
- Add exception untuk .exe di antivirus

### 9. Optional: Add Icon

1. Buat atau download icon (.ico format)
2. Simpan di `assets/icon.ico`
3. Uncomment line di `build.py`:
```python
'--icon=assets/icon.ico',
```
4. Build ulang

### 10. File Structure Overview

```
mancing-indovoice/
├── src/                    # Source code
│   ├── core/              # Core logic
│   ├── gui/               # User interface
│   ├── utils/             # Utilities
│   └── version.py         # Version info ← UPDATE INI untuk release baru
├── config/                # Config files (auto-generated)
├── assets/                # Icons, images (optional)
├── docs/                  # Documentation
├── main.py               # Entry point
├── build.py              # Build script
├── requirements.txt      # Dependencies
├── README.md            # Main documentation
├── CHANGELOG.md         # Version history ← UPDATE INI untuk release baru
├── LICENSE              # MIT License
└── .gitignore          # Git ignore rules
```

### 11. Important Files to Update on Each Release

1. **src/version.py** - Update version number
2. **CHANGELOG.md** - Add changes
3. **README.md** - Update if needed (features, usage, etc.)
4. **Build** - Run `python build.py`
5. **GitHub Release** - Create with new tag and upload .exe

---

## Quick Commands Reference

```bash
# Development
python main.py                 # Run from source
pip install -r requirements.txt  # Install deps

# Building
python build.py               # Build executable

# Git
git add .
git commit -m "message"
git push

# Distribution
# Upload dist/mancing_indovoice.exe to GitHub Releases
```

---

## Support

- GitHub Issues: Report bugs dan feature requests
- Discord: Join server untuk bantuan
- Email: Contact developer

Happy fishing! 🎣
