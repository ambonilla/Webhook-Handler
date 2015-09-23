#!/usr/bin/env python

import daemon
import time

from issue_checker import issue_checker
from config import config
from mysql_handler import mysql_handler

from threading import Thread

from index import py_server

class start:

    def run_issue_checker(self):
        new_issue_checker = issue_checker()
        while True:
            new_issue_checker.run_checker()
            time.sleep(300)

    
    def __init__(self):
        #Attempts to create the table if it doesn't exist
        new_mysql_handler = mysql_handler()
        new_mysql_handler.create_table()
        
        #Start running the daemon
        self.run()

    def run(self):
        with daemon.DaemonContext():
            self.run_issue_checker()

def run_start():
   start()

def run_index():
   py_server()

if __name__ == '__main__':
   thread1 = Thread(target = run_start)
   thread2 = Thread(target = run_index)
   thread1.start()
   thread2.start()
