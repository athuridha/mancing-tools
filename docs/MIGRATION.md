# Migration Guide - v1.0 to v2.0

## 📦 Upgrading from Old Version

Jika Anda sudah pakai versi lama (single file), ini panduan untuk migrasi ke v2.0.

---

## 🔄 What Changed?

### Structure
```
OLD (v1.0):                    NEW (v2.0):
roblox_fishing_macro.py   →   src/ (multiple modules)
fishing_macro_settings.json → config/settings.json
(single file)              →   (organized folders)
```

### Features Added
- ✅ Auto-update system
- ✅ Better configuration management
- ✅ Modular code structure
- ✅ Professional documentation
- ✅ Improved UI organization

### Breaking Changes
- ⚠️ Config file location moved
- ⚠️ Import paths changed (only for developers)
- ⚠️ Different executable name

---

## 🚀 Migration Steps for Users

### Option 1: Fresh Install (Recommended)
```bash
# 1. Backup settings lama (optional)
# Copy fishing_macro_settings.json ke tempat aman

# 2. Download v2.0 dari GitHub Releases

# 3. Run mancing_indovoice.exe

# 4. Configure ulang (atau import settings lama)
```

### Option 2: Import Old Settings
```bash
# 1. Install v2.0

# 2. Copy settings lama
# From: fishing_macro_settings.json
# To:   config/settings.json

# 3. Run aplikasi
# Settings akan otomatis dimuat
```

---

## 📝 Settings Migration

### Old Format (v1.0):
```json
{
  "roi": {"x": 697, "y": 892, "w": 526, "h": 70},
  "green_th": 0.14,
  "red_th": 0.1,
  "click_i": 0.035,
  "idle_i": 0.01,
  "hold_s": 3.0,
  "down_s": 0.005
}
```

### New Format (v2.0):
```json
{
  "roi": {"x": 697, "y": 892, "w": 526, "h": 70},
  "green_th": 0.14,
  "red_th": 0.10,
  "click_i": 0.035,
  "idle_i": 0.010,
  "hold_s": 3.0,
  "down_s": 0.01,
  "inactive_to": 1.2,      // NEW
  "recast_delay": 0.30,    // NEW
  "auto_recast": true,     // NEW
  "active_min_ratio": 0.03,// NEW
  "key": "F1"              // NEW
}
```

### Migration Script (Optional):
```python
# migrate_settings.py
import json

# Load old settings
with open('fishing_macro_settings.json', 'r') as f:
    old = json.load(f)

# Add new fields with defaults
new = old.copy()
new['inactive_to'] = 1.2
new['recast_delay'] = 0.30
new['auto_recast'] = True
new['active_min_ratio'] = 0.03
new['key'] = 'F1'

# Save to new location
import os
os.makedirs('config', exist_ok=True)
with open('config/settings.json', 'w') as f:
    json.dump(new, f, indent=2)

print("Migration complete!")
```

---

## 🎯 Feature Mapping

### Old Features → New Location

| Old (v1.0) | New (v2.0) |
|------------|------------|
| Start/Stop button | Home page |
| Calibration tools | Home page |
| Settings sliders | Custom Settings page |
| Keybind setup | Keybinds page |
| Credit info | Credit page |
| Debug window | Home page (same) |
| Preset save/load | Custom Settings page |

### New Features (Not in v1.0)

| Feature | Location |
|---------|----------|
| Auto-update checker | Credit page |
| Version display | Credit page |
| Organized tabs | Top menu bar |
| Better config system | Automatic |
| Modular code | Backend |

---

## 💡 What to Expect

### Same Functionality
- ✅ Fishing automation works sama
- ✅ ROI calibration sama
- ✅ Color detection sama
- ✅ Hotkeys sama (default F1)
- ✅ Debug mode sama

### Improved
- ✅ UI lebih organized
- ✅ Settings lebih accessible
- ✅ Auto-update (major improvement!)
- ✅ Better performance
- ✅ More stable

### Different
- ⚠️ File locations changed
- ⚠️ Config file moved
- ⚠️ Executable name changed
- ⚠️ Tab-based navigation

---

## 🔧 For Developers

### Import Changes

**Old (v1.0):**
```python
# Everything in one file
from roblox_fishing_macro import App, FishingEngine, etc
```

**New (v2.0):**
```python
# Organized modules
from src.gui import App
from src.core.engine import FishingEngine
from src.core.vision import grab_bgr, calc_color_ratios
from src.utils.config import ConfigManager
from src.utils.updater import AutoUpdater
```

### Code Organization

**Old Structure:**
```python
# roblox_fishing_macro.py (1000+ lines)
- Constants
- Helper functions
- ROI class
- App class (GUI + Logic mixed)
- Main function
```

**New Structure:**
```python
# src/core/engine.py
- FishingEngine class (automation logic)

# src/core/vision.py
- Color detection functions

# src/gui/main_window.py
- App class (GUI only)

# src/gui/pages.py
- Page classes (separated)

# src/utils/
- config.py (ConfigManager)
- updater.py (AutoUpdater)
- screen.py (screen utilities)
```

### Extending the Code

**Adding New Feature (v2.0):**

1. Identify module:
   - Core logic → `src/core/engine.py`
   - Vision → `src/core/vision.py`
   - UI → `src/gui/pages.py`
   - Config → `src/utils/config.py`

2. Add feature in appropriate file

3. Update UI if needed

4. Test from source: `python main.py`

5. Build: `python build.py`

Much easier than editing 1000+ line file!

---

## 📚 Documentation

### Old (v1.0):
- Comments in code
- Maybe README

### New (v2.0):
- README.md - Overview
- docs/SETUP.md - Developer guide
- docs/USER_GUIDE.md - User manual
- docs/PROJECT_STRUCTURE.md - Architecture
- CHANGELOG.md - Version history
- QUICK_REFERENCE.md - Quick commands

**Much more comprehensive!**

---

## 🐛 Known Issues & Fixes

### Issue: "Can't find settings"
**Fix:** Create `config/` folder, or run once to auto-generate

### Issue: "Import errors"
**Fix:** Run from project root: `python main.py`

### Issue: "Old .exe not working"
**Fix:** Use new .exe from v2.0 release

### Issue: "Settings not loaded"
**Fix:** Move `fishing_macro_settings.json` to `config/settings.json`

---

## 🎁 Benefits of Upgrading

### For Users:
- ✅ Auto-update (no manual download!)
- ✅ Better organized UI
- ✅ More stable
- ✅ Professional app

### For Developers:
- ✅ Much easier to modify
- ✅ Clear code structure
- ✅ Better documentation
- ✅ Easier to extend

### For Project:
- ✅ Scalable
- ✅ Maintainable
- ✅ Professional
- ✅ Modern

---

## ❓ FAQs

### Q: Do I need to uninstall v1.0?
**A:** No, just delete old .exe if you want. No installation needed for either version.

### Q: Will my settings transfer?
**A:** Manually copy settings file, or reconfigure (takes 1 minute).

### Q: Can I use both versions?
**A:** Yes, but not simultaneously. Keep separate folders.

### Q: Is v2.0 compatible with old games?
**A:** Yes! Same detection algorithm, just better structure.

### Q: Will I lose my presets?
**A:** Only if you don't backup. Copy `fishing_macro_settings.json` before upgrading.

### Q: How do I downgrade?
**A:** Keep old .exe. Can switch anytime.

### Q: Is the source code compatible?
**A:** No, completely restructured. But feature-equivalent.

---

## 🚀 Recommendation

**For most users:**
→ Fresh install v2.0, reconfigure (5 minutes)

**For advanced users:**
→ Migrate settings, explore new features

**For developers:**
→ Study new structure, much better to work with!

---

## 📞 Need Help?

- Check docs/ folder for guides
- GitHub Issues for problems
- Discord for quick help

---

## 🎉 Welcome to v2.0!

Major improvements:
- ✅ Professional structure
- ✅ Auto-update system
- ✅ Better maintainability
- ✅ Complete documentation

**You're gonna love it! 🎣**

---

Made with ❤️ by @xinnercy
