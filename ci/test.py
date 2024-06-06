import platform
import subprocess
import sys

import platform
import subprocess
import sys
import os

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


def run_tests(pltf):
  raise RuntimeError('Not implemented')


def main():
  try:
    pltf = detect_platform()
    run_tests(pltf)
  except Exception as e:
    print(f'Error: {e}')
    sys.exit(1)


if __name__ == '__main__':
  main()
