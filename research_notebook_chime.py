import time
import winsound
import os
from datetime import datetime

SOUND_FILE = "chime.wav"


def play_chime():
    winsound.PlaySound(SOUND_FILE, winsound.SND_FILENAME)


def main():
    interval = 15 * 60  # 15 minutes in seconds
    last_log_time = None
    start_time = datetime.now()

    if not os.path.exists(SOUND_FILE):
        print(
            f"Error: {SOUND_FILE} not found. Please ensure the file is in the same directory as the script."
        )
        return

    print(
        f"Research Log Reminder started at {start_time.strftime('%Y-%m-%d %H:%M:%S')}. Will play {SOUND_FILE} every 15 minutes. Press Ctrl+C to exit."
    )

    try:
        while True:
            if last_log_time:
                print(f"Last log time: {last_log_time.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Time started: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
            time.sleep(interval)
            play_chime()
            last_log_time = datetime.now()
            print("Time to log your research activities!")

    except KeyboardInterrupt:
        print("\nReminder stopped.")


if __name__ == "__main__":
    main()
