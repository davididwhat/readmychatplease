import os
import subprocess
import sys


def main():
    if os.name == 'nt':
        os.system("title ReadMyChatPlease")
        
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