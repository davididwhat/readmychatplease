import os
import subprocess
import sys
import time


def main():
    python_executable = sys.executable

    subprocess.Popen(
        [python_executable, './src/bot.py'],
        env=os.environ.copy(),
    )

    subprocess.Popen(
        [python_executable, './src/courier.py'],
        env=os.environ.copy(), 
    )



if __name__ == '__main__':
    main()