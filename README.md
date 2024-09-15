# To run the script:

python sync.py <source_folder> <replica_folder> <sync_interval_in_seconds> <logfile_path>

<source_folder>: The path to the source folder you want to synchronize.

<replica_folder>: The path to the replica folder that will mirror the source.

<sync_interval_in_seconds>: The time interval (in seconds) between synchronization checks.

<logfile_path>: The path where the log file will be stored.


# Explication 
If the replica folder does not exist, it is created.

If a file or directory exists in the source but not in the replica, it is copied.

If a file in the replica is outdated (based on MD5 hash comparison), it is updated with the newer version from the source.

If a file or directory exists in the replica but not in the source, it is deleted.

Logging: All actions (creation, modification, deletion) are logged both to the console and to the specified log file.
