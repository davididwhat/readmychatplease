import subprocess
import sys


def install_modules(modules: list | str) -> None:
    if isinstance(modules, str):
        modules = [modules]
    elif not isinstance(modules, list):
        raise TypeError("Modules should be a list or a string")
    
    if not modules or (isinstance(modules, list) and len(modules) == 0):
        raise ValueError("No modules provided for installation")
    
    for module in modules:
        try:
            __import__(module)
        except ImportError:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", module])
            except subprocess.CalledProcessError as e:
                print(f"Failed to install {module}. Error: {e}")
            except OSError as e:
                print(f"OS error occurred while installing {module}. Error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred while importing {module}: {e}")