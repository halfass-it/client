import platform
import subprocess
import sys

from pypeline.pypeline import Pipeline

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


def run_scons(platform):
  try:
    _ = subprocess.run(['scons', f'platform={platform}'], check=True)
    print(f"'scons platform={platform}' executed successfully.")
  except subprocess.CalledProcessError as e:
    print(f"An error occurred while running 'scons platform={platform}': {e}")
    sys.exit(1)


def main():
  try:
    detected_platform = detect_platform()
    run_scons(detected_platform)
  except Exception as e:
    print(f'Error: {e}')
    sys.exit(1)


if __name__ == '__main__':
  main()
