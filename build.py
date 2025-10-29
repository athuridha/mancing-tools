"""Build script for creating executable with PyInstaller."""

import PyInstaller.__main__
import os
import shutil
from src.version import __version__

def clean_build():
    """Clean previous build artifacts."""
    dirs_to_clean = ['build', 'dist']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"Cleaned {dir_name}/")

def build_executable():
    """Build the executable using PyInstaller."""
    print(f"Building Macro Mancing Indovoice v{__version__}...")
    
    # PyInstaller arguments
    args = [
        'main.py',                          # Entry point
        '--name=mancing',                   # Executable name
        '--onefile',                        # Single file
        '--windowed',                       # No console (GUI only)
        '--clean',                          # Clean cache
        
        # Add data files
        '--add-data=src;src',              # Include src folder
        '--add-data=assets;assets',        # Include assets folder (icon & logo)
        
        # Exclude unnecessary modules to reduce size
        '--exclude-module=matplotlib',
        '--exclude-module=pandas',
        '--exclude-module=scipy',
        '--exclude-module=pytest',
        '--exclude-module=IPython',
        '--exclude-module=notebook',
        '--exclude-module=tkinter.test',
        '--exclude-module=unittest',
        '--exclude-module=doctest',
        '--exclude-module=cv2.aruco',
        '--exclude-module=cv2.bgsegm',
        '--exclude-module=cv2.bioinspired',
        '--exclude-module=cv2.dnn',
        '--exclude-module=cv2.face',
        '--exclude-module=cv2.ml',
        '--exclude-module=cv2.objdetect',
        '--exclude-module=cv2.videoio',
        '--exclude-module=cv2.video',
        
        # Hidden imports (only essential)
        '--hidden-import=customtkinter',
        '--hidden-import=PIL._tkinter_finder',
        '--hidden-import=keyboard',
        '--hidden-import=mss',
        '--hidden-import=cv2',
        '--hidden-import=numpy',
        '--hidden-import=requests',
        '--hidden-import=packaging',
        '--hidden-import=pystray',
        '--hidden-import=pystray._win32',
        '--hidden-import=win32api',
        '--hidden-import=win32con',
        '--hidden-import=win32gui',
        '--hidden-import=psutil',
        '--hidden-import=pynput',
        
        # Optimization
        '--optimize=2',
        '--strip',                          # Strip debug symbols
        '--noupx',                          # Disable UPX (sometimes makes it bigger)
        
        # Icon
        '--icon=assets/logo.ico',
        
        # Version info
        f'--version-file=version_info.txt',
    ]
    
    print("Running PyInstaller...")
    PyInstaller.__main__.run(args)
    print(f"\n✅ Build complete! Executable: dist/mancing.exe")

def create_version_info():
    """Create version info file for Windows executable."""
    from src.version import VERSION_INFO
    
    content = f"""# UTF-8
#
# For more details about fixed file info:
# https://msdn.microsoft.com/en-us/library/ms646997.aspx

VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=({VERSION_INFO['major']}, {VERSION_INFO['minor']}, {VERSION_INFO['patch']}, 0),
    prodvers=({VERSION_INFO['major']}, {VERSION_INFO['minor']}, {VERSION_INFO['patch']}, 0),
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
  ),
  kids=[
    StringFileInfo(
      [
        StringTable(
          u'040904B0',
          [
            StringStruct(u'CompanyName', u'Indovoice'),
            StringStruct(u'FileDescription', u'Macro Mancing Indovoice - Roblox Fishing Automation'),
            StringStruct(u'FileVersion', u'{VERSION_INFO['major']}.{VERSION_INFO['minor']}.{VERSION_INFO['patch']}.0'),
            StringStruct(u'InternalName', u'mancing'),
            StringStruct(u'LegalCopyright', u'© 2025 lamont (@xinnercy)'),
            StringStruct(u'OriginalFilename', u'mancing.exe'),
            StringStruct(u'ProductName', u'Macro Mancing Indovoice'),
            StringStruct(u'ProductVersion', u'{VERSION_INFO['major']}.{VERSION_INFO['minor']}.{VERSION_INFO['patch']}.0')
          ]
        )
      ]
    ),
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)
"""
    
    with open('version_info.txt', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Created version_info.txt")

if __name__ == "__main__":
    print("=" * 60)
    print("Macro Mancing Indovoice - Build Script")
    print("=" * 60)
    
    # Clean previous builds
    clean_build()
    
    # Create version info
    try:
        create_version_info()
    except Exception as e:
        print(f"Warning: Could not create version_info.txt: {e}")
    
    # Build executable
    try:
        build_executable()
        print("\n" + "=" * 60)
        print("Build successful! 🎉")
        print("=" * 60)
        print("\nNext steps:")
        print("1. Test the executable: dist/mancing.exe")
        print("2. Create a GitHub release")
        print("3. Upload the executable as a release asset")
        print("4. Tag the release with version (e.g., v2.0.0)")
    except Exception as e:
        print(f"\n❌ Build failed: {e}")
        raise
