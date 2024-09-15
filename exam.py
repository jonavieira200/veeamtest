import os
import shutil
import hashlib
import time
import logging
import argparse

def calculate_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def sync_folders(source, replica):
    if not os.path.exists(replica):
        os.makedirs(replica)
    for foldername, subfolders, filenames in os.walk(source):
        replica_foldername = foldername.replace(source, replica, 1)
        
        if not os.path.exists(replica_foldername):
            os.makedirs(replica_foldername)
            logging.info(f'file created called {replica_foldername}')
            print(f'File created called {replica_foldername}')

        for filename in filenames:
            source_file = os.path.join(foldername, filename)
            replica_file = os.path.join(replica_foldername, filename)
            
            if not os.path.exists(replica_file) or calculate_md5(source_file) != calculate_md5(replica_file):
                shutil.copy2(source_file, replica_file)
                logging.info(f'File coppied {source_file} -> {replica_file}')
                print(f'File coppied {source_file} -> {replica_file}')
    
    for foldername, subfolders, filenames in os.walk(replica):
        source_foldername = foldername.replace(replica, source, 1)

        if not os.path.exists(source_foldername):
            shutil.rmtree(foldername)
            logging.info(f'Removed file {foldername}')
            print(f'Removed file {foldername}')
            continue

        for filename in filenames:
            replica_file = os.path.join(foldername, filename)
            source_file = os.path.join(source_foldername, filename)

            if not os.path.exists(source_file):
                os.remove(replica_file)
                logging.info(f'Removed file {replica_file}')
                print(f'Removed file {replica_file}')

def setup_logging(log_file):
    logging.basicConfig(
        filename=log_file,
        filemode='a',
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

def main(source, replica, interval, log_file):
    setup_logging(log_file)

    while True:
        logging.info("Starting")
        print("Starting")
        sync_folders(source, replica)
        logging.info("Finished")
        print("Finished")
        time.sleep(interval)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='syncronization')
    parser.add_argument('source', type=str, help='source')
    parser.add_argument('replica', type=str, help='replica')
    parser.add_argument('interval', type=int, help='time interval')
    parser.add_argument('log_file', type=str, help='log file name')

    args = parser.parse_args()

    main(args.source, args.replica, args.interval, args.log_file)
