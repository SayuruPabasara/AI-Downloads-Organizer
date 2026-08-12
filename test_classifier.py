from pathlib import Path
from download_organizer import DownloadHandler
import sys


handler = DownloadHandler()

file_path = Path(sys.argv[1])

result = handler.classify_file(file_path)

print("\nFinal result:", result)