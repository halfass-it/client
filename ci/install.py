import platform
import subprocess
import sys
import shutil

def detect_platform():
    system = platform.system()
    if system == 'Linux':
        return 'linux'
    elif system == 'Darwin':
        return 'osx'
    elif system == 'Windows':
        return 'windows'
    else:
        raise RuntimeError('Unsupported operating system')

def is_chocolatey_installed():
    return shutil.which("choco") is not None

def install_chocolatey():
    try:
        print("Chocolatey is not installed. Installing Chocolatey...")
        subprocess.run(
            ["@powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", 
             "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"],
            shell=True,
            check=True
        )
        print("Chocolatey installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing Chocolatey: {e}")
        sys.exit(1)

def install_packages_with_chocolatey(packages):
    try:
        subprocess.run(["choco", "install", "-y"] + packages, check=True)
        print(f"Packages {', '.join(packages)} installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing packages: {e}")
        sys.exit(1)

def install(platform):
    if platform == "windows":
        if not is_chocolatey_installed():
            install_chocolatey()
        packages = ["llvm", "mingw", "python", "python3", "scons", "make"]
        install_packages_with_chocolatey(packages)
    else:
        raise RuntimeError("This script only supports Windows. For other platforms, please install manually.")

