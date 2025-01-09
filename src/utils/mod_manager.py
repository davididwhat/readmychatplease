import subprocess
import sys


def install_modules(modules: list | str) -> None:
    if isinstance(modules, str):
        try:
            __import__(module)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", modules])
    else:
        for module in modules:
            try:
                __import__(module)
            except ImportError:
                subprocess.check_call([sys.executable, "-m", "pip", "install", module])

