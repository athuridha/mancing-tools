"""Auto-update system for checking and downloading updates from GitHub."""

import requests
import os
import sys
import subprocess
import tempfile
from typing import Optional, Tuple
from packaging import version as pkg_version

class AutoUpdater:
    """Handles automatic update checking and installation."""
    
    def __init__(self, current_version: str, github_repo: str):
        """Initialize auto-updater.
        
        Args:
            current_version: Current application version
            github_repo: GitHub repository in format "owner/repo"
        """
        self.current_version = current_version
        self.github_repo = github_repo
        self.api_url = f"https://api.github.com/repos/{github_repo}/releases/latest"
        
    def check_for_updates(self) -> Optional[dict]:
        """Check if new version is available.
        
        Returns:
            dict: Update info if available, None otherwise
            Contains: version, download_url, release_notes
        """
        try:
            response = requests.get(self.api_url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            latest_version = data.get("tag_name", "").lstrip("v")
            
            # Compare versions
            if self._is_newer_version(latest_version, self.current_version):
                # Find Windows executable in assets
                download_url = None
                for asset in data.get("assets", []):
                    name = asset.get("name", "").lower()
                    if name.endswith(".exe"):
                        download_url = asset.get("browser_download_url")
                        break
                
                if download_url:
                    return {
                        "version": latest_version,
                        "download_url": download_url,
                        "release_notes": data.get("body", ""),
                        "release_name": data.get("name", ""),
                    }
        except Exception as e:
            print(f"Update check failed: {e}")
            
        return None
        
    def _is_newer_version(self, latest: str, current: str) -> bool:
        """Compare version strings.
        
        Args:
            latest: Latest version string
            current: Current version string
            
        Returns:
            bool: True if latest is newer
        """
        try:
            return pkg_version.parse(latest) > pkg_version.parse(current)
        except Exception:
            # Fallback to string comparison
            return latest > current
            
    def download_update(self, download_url: str, progress_callback=None) -> Optional[str]:
        """Download update file.
        
        Args:
            download_url: URL to download from
            progress_callback: Optional callback(bytes_downloaded, total_bytes)
            
        Returns:
            str: Path to downloaded file, or None if failed
        """
        try:
            response = requests.get(download_url, stream=True, timeout=30)
            response.raise_for_status()
            
            total_size = int(response.headers.get('content-length', 0))
            
            # Create temporary file
            temp_dir = tempfile.gettempdir()
            temp_file = os.path.join(temp_dir, "mancing_indovoice_update.exe")
            
            downloaded = 0
            with open(temp_file, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        if progress_callback:
                            progress_callback(downloaded, total_size)
                            
            return temp_file
        except Exception as e:
            print(f"Download failed: {e}")
            return None
            
    def install_update(self, update_file: str) -> bool:
        """Install downloaded update.
        
        Args:
            update_file: Path to update executable
            
        Returns:
            bool: True if installation started successfully
        """
        try:
            # Start update installer and exit current application
            if sys.platform == "win32":
                # Run installer and exit
                subprocess.Popen([update_file], shell=True)
                return True
        except Exception as e:
            print(f"Installation failed: {e}")
            
        return False
        
    def check_and_notify(self) -> Optional[dict]:
        """Convenience method to check and return update info.
        
        Returns:
            dict: Update information if available
        """
        return self.check_for_updates()
