# Folder Synchronization Script
This Python script synchronizes the contents of a source folder to a replica folder, ensuring that the replica becomes an exact mirror of the source. It performs one-way synchronization, meaning that the contents of the replica will be modified to match the source, but not the other way around.

# Features
One-way synchronization: Ensures the replica folder matches the source folder exactly.
Periodic execution: You can set the synchronization to run at specific intervals.
File integrity check: Uses MD5 hashing to compare files and only copies files if they are new or modified.
Automatic folder creation: Creates missing directories in the replica if they exist in the source.
Automatic removal of files and directories: Deletes files and directories from the replica if they no longer exist in the source.
Logging: Logs all synchronization actions, including file copies, deletions, and directory changes, to both the console and a log file.
# Requirements
Python 3.x
No third-party libraries required
# Usage
To run the script, use the following command:

python sync.py <source_folder> <replica_folder> <sync_interval_in_seconds> <logfile_path>

<source_folder>: The path to the source folder you want to synchronize.

<replica_folder>: The path to the replica folder that will mirror the source.

<sync_interval_in_seconds>: The time interval (in seconds) between synchronization checks.

<logfile_path>: The path where the log file will be stored.

# Example:

python sync.py /path/to/source /path/to/replica 60 /path/to/logfile.log

This will synchronize the source folder to the replica every 60 seconds and log the actions to logfile.log.

# How It Works
Initial Setup: If the replica folder does not exist, it is created.

Synchronization: The script walks through all directories and files in the source:
If a file or directory exists in the source but not in the replica, it is copied.
If a file in the replica is outdated (based on MD5 hash comparison), it is updated with the newer version from the source.
Cleanup: The script also walks through the replica:
If a file or directory exists in the replica but not in the source, it is deleted.
Logging: All actions (creation, modification, deletion) are logged both to the console and to the specified log file.
