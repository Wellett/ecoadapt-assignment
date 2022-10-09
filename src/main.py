#!/usr/bin/env python3

""" 
Main file for the EcoAdapt modbus proof of concept
"""
TASK_TIMEOUT = 2    # period of repeating task
CANCEL_TIMEOUT = 8  # time to run test for in s

from threading import Timer,Event,Thread
import time


def main():
    thread = repeating_thread(TASK_TIMEOUT, callback_print)
    thread.start()
    time.sleep(CANCEL_TIMEOUT)
    thread.cancel()


# dumb callback just for a test
# Prints time to check interval
def callback_print():
    print(time.time())

# A basic repeating timer class to run repeated samples
# Will execue the callback every "timeout" s until cancle is called 
class repeating_thread(Thread):
    def __init__(self, timeout, callback):
        Thread.__init__(self)
        self.stopped = Event()
        self.timeout = timeout
        self.callback = callback

    def run(self):
        while not self.stopped.wait(self.timeout):
            self.callback()

    def cancel(self):
        self.stopped.set()


# Here to test this Module/proof of concept
# If integrated into a system this script may be run as a module
if __name__ == "__main__":
    main()


