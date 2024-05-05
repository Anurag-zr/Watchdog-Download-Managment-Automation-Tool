import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


def on_created(event):
    print(f"hey, {event.src_path} has been created!")

    if not event.is_directory:
        file_path = event.src_path
        target_dir,file_name = os.path.split(file_path)

        print(file_name)
        print(target_dir)
        target_dir_name = file_name.split(".")[-1]

        if not os.path.exists(os.path.join(target_dir,target_dir_name)):
            os.makedirs(os.path.join(target_dir,target_dir_name))

        shutil.move(file_path, os.path.join(target_dir,target_dir_name,file_name))
        print(f"Moved {file_name} to {target_dir+"/"+target_dir_name}")

    # if file_extension:
        # Remove the dot for the folder name
        # dir_name = file_extension[1:].lower()
        # print (file_extension)

        
        # target_dir = os.path.join(Watcher.DIRECTORY_TO_WATCH, dir_name)
        # Create the directory if it doesn't exist
        # if not os.path.exists(target_dir):
        #     os.makedirs(target_dir)
        # # Move the file
        # shutil.move(file_path, os.path.join(target_dir, file_name))
        # print(f"Moved {file_name} to {target_dir}")

def on_deleted(event):
    print(f"what the f**k! Someone deleted {event.src_path}!")

def on_modified(event):
    print(f"hey buddy, {event.src_path} has been modified")

def on_moved(event):
    print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")


if __name__ == "__main__":
    patterns = ["*.jpg","*.jpeg","*.pdf","*.mp4","*.svg","*.png","*.dmg","*.mkv"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

    my_event_handler.on_created = on_created
    my_event_handler.on_deleted = on_deleted
    my_event_handler.on_modified = on_modified
    my_event_handler.on_moved = on_moved

    # creating observer
    path = "/Users/anuragpandit/Downloads"
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)

    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()