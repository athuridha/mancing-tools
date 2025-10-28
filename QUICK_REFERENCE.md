# Quick Reference - Mancing Indovoice

## 🚀 Instant Commands

### Development
```bash
python main.py                    # Run application
pip install -r requirements.txt   # Install dependencies
```

### Building
```bash
python build.py                   # Build executable
```

### Git
```bash
git add .
git commit -m "Your message"
git push
```

---

## 📝 Before Each Release Checklist

- [ ] 1. Update `src/version.py` version number
- [ ] 2. Update `CHANGELOG.md` with changes
- [ ] 3. Test from source: `python main.py`
- [ ] 4. Build: `python build.py`
- [ ] 5. Test executable: `dist/mancing_indovoice.exe`
- [ ] 6. Commit changes: `git add . && git commit -m "Release vX.X.X"`
- [ ] 7. Push: `git push`
- [ ] 8. Create GitHub Release (tag: vX.X.X)
- [ ] 9. Upload `dist/mancing_indovoice.exe` to release
- [ ] 10. Publish release

---

## 🎯 Key Files to Edit

### For New Release:
```
src/version.py          ← Update version number
CHANGELOG.md            ← Add what's new
```

### For Features:
```
src/core/engine.py      ← Automation logic
src/core/vision.py      ← Color detection
src/gui/pages.py        ← UI elements
src/utils/config.py     ← Settings
```

### First Time Setup:
```
src/gui/main_window.py  ← Line 44: Update GITHUB_REPO
```

---

## 📊 Project Structure (Quick View)

```
src/
  core/        → Engine & vision
  gui/         → UI components
  utils/       → Config, updater, screen
config/        → settings.json (auto-generated)
docs/          → Documentation
main.py        → Entry point
build.py       → Build script
```

---

## 🔢 Version Numbering

Format: `MAJOR.MINOR.PATCH`

- **MAJOR**: Breaking changes (1.0.0 → 2.0.0)
- **MINOR**: New features (2.0.0 → 2.1.0)
- **PATCH**: Bug fixes (2.1.0 → 2.1.1)

Examples:
- `2.0.0` - Major restructure
- `2.1.0` - Add new feature
- `2.1.1` - Fix bug

---

## 🐛 Common Issues & Fixes

### "Import Error"
```bash
pip install -r requirements.txt
```

### "PyInstaller not found"
```bash
pip install pyinstaller
```

### "Build failed"
```bash
# Clean and rebuild
rmdir /s build dist
python build.py
```

### "Hotkey not working"
- Run as Administrator (for global)
- Or use local mode (app focus required)

### "Detection not working"
- Recalibrate ROI
- Use Debug mode
- Adjust thresholds in settings

---

## 💻 GitHub Release Process

### Create Release:
1. Go to: `https://github.com/USERNAME/mancing-indovoice/releases`
2. Click: "Create a new release"
3. Tag: `v2.0.0` (match version.py)
4. Title: `Macro Mancing Indovoice v2.0.0`
5. Description: Copy from CHANGELOG.md
6. Upload: `dist/mancing_indovoice.exe`
7. Click: "Publish release"

### Update for Existing Release:
1. Edit release
2. Delete old .exe
3. Upload new .exe
4. Save

---

## ⚙️ Config File Location

```
config/settings.json
```

Auto-generated on first save. Contains:
- ROI position & size
- Detection thresholds
- Timing settings
- Hotkey preference

---

## 🔗 Important Links

```
GitHub Repo:    github.com/USERNAME/mancing-indovoice
Releases:       github.com/USERNAME/mancing-indovoice/releases
Issues:         github.com/USERNAME/mancing-indovoice/issues
Discord:        discord.gg/SWzSjeF3
```

---

## 📱 Support Channels

**Bug Reports:** GitHub Issues
**Quick Help:** Discord
**Feature Requests:** GitHub Issues
**Contributions:** Pull Requests

---

## 🎓 Learning Resources

- **README.md** - Overview & features
- **docs/USER_GUIDE.md** - How to use
- **docs/SETUP.md** - Developer guide
- **docs/PROJECT_STRUCTURE.md** - Code organization
- **CHANGELOG.md** - Version history

---

## 🎨 UI Customization

### Change Colors:
```python
# src/gui/main_window.py
ctk.set_appearance_mode("dark")  # or "light"
ctk.set_default_color_theme("green")  # or "blue", "dark-blue"
```

### Change Window Size:
```python
# src/gui/main_window.py, __init__
self.geometry("1000x640")  # width x height
```

---

## 🔐 Security Notes

- Never commit config files with sensitive data
- .gitignore already excludes settings.json
- Review code before accepting contributions
- Users should download only from official releases

---

## 📈 Future Features Ideas

- [ ] Multiple profiles
- [ ] Statistics tracking
- [ ] Cloud sync
- [ ] Mobile remote control
- [ ] Machine learning detection
- [ ] Multi-game support
- [ ] Plugin system

---

## 🎯 Performance Specs

**Normal Usage:**
- CPU: 5-15%
- RAM: 100-200 MB
- Disk: ~50 MB (executable)

**Requirements:**
- Windows 10/11
- 2GB RAM minimum
- Any screen resolution
- Python 3.8+ (for source)

---

## 🌟 Best Practices

### Development:
✅ Test before committing
✅ Write clear commit messages
✅ Update documentation
✅ Follow code style
✅ Handle errors gracefully

### Distribution:
✅ Test on clean Windows
✅ Include clear instructions
✅ Respond to issues
✅ Release notes in CHANGELOG
✅ Use semantic versioning

---

## 🎁 Credits

**Developer:** lamont (@xinnercy)
- Roblox: [xinnercy](https://www.roblox.com/users/8179160997/)
- Discord: halflucifer

**Special Thanks:**
- CustomTkinter for modern UI
- OpenCV for vision processing
- PyAutoGUI for automation
- MSS for fast screen capture

---

## 📞 Need Help?

1. Check docs/ folder
2. Search GitHub Issues
3. Ask on Discord
4. Create new Issue

---

**This is your quick reference. Bookmark it! 🔖**

Happy Fishing! 🎣
