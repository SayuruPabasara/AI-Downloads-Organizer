#import Observer and FileSystemEventHandler classes from watchdog library
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import time
from pathlib import Path

from config import DOWNLOADS_FOLDER, MODULE_MAPPING

class DownloadHandler(FileSystemEventHandler):      #inherits from FileSystemEventHandler class

    def on_moved(self, event):

        if event.dest_path.endswith(".crdownload"):
            return

        file_path = Path(event.dest_path)
        self.process_download(file_path)

    def process_download(self, file_path):
        self.classify_file(file_path)

    def classify_file(self, file_path):
        file_name=file_path.name

        for module_code, module_name in MODULE_MAPPING.items():
            if module_code in file_name:
                print("Module:",module_name)
                return module_name

        print("No Module Found")
        return None

#blueprint for creating watchers
observer=Observer()

handler=DownloadHandler()

path_to_watch = DOWNLOADS_FOLDER

observer.schedule(handler, path_to_watch, recursive=False)

try:
    observer.start()

    while True:
        time.sleep(1)

except KeyboardInterrupt:
    observer.stop()

#what is a thread? A thread is a separate flow of execution within a program. 
#In Python, the main thread is the initial thread that starts when you run a Python script.
#When you create additional threads (like the observer thread in this case), they run concurrently with the main thread.
#The `join()` method is used to ensure that the main thread waits for the observer thread to finish its execution before proceeding,
#which helps in managing the lifecycle of threads and ensuring that resources are cleaned up properly.

observer.join()
