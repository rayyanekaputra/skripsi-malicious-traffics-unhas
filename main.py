#IMPORT FOLDER OF THE MODULES
import sys
sys.path.extend(['/home/expresidentz/Desktop/skripsi-malicious-traffics-unhas/benign/register',
                 '/home/expresidentz/Desktop/skripsi-malicious-traffics-unhas/benign/posts',
                 '/home/expresidentz/Desktop/skripsi-malicious-traffics-unhas/benign/login',
                 '/home/expresidentz/Desktop/skripsi-malicious-traffics-unhas/malicious/bruteforce',
                 '/home/expresidentz/Desktop/skripsi-malicious-traffics-unhas/malicious/probing',
                 '/home/expresidentz/Desktop/skripsi-malicious-traffics-unhas/',
                 '/home/rayyanekaputra/Desktop/skripsi😭/',
                 '/home/rayyanekaputra/Desktop/skripsi😭/benign/register',
                 '/home/rayyanekaputra/Desktop/skripsi😭/benign/posts',
                 '/home/rayyanekaputra/Desktop/skripsi😭/malicious/bruteforce',
                '/home/rayyanekaputra/Desktop/skripsi😭/malicious/probing',
  
            
                 ])





import time
import threading
from random import randint, choice
from NewPost import NewPost
from AccountMaker import AccountMaker
from BruteforceLoginSelenium import BruteforceLoginSelenium
from BruteforceLoginXMLRPC import BruteforceLoginXMLRPC

def run_new_post():
    while True:
        print("Running run_new_post")
        NewPost()  # Call the NewPost function here
        # Add randomness to the timing
        time.sleep(randint(300, 600))  # Random time between 5 to 10 minutes

def run_account_maker():
    while True:
        print("Running run_account_maker")
        AccountMaker()  # Call the AccountMaker function here
        # Add randomness to the timing
        time.sleep(randint(600, 900))  # Random time between 10 to 15 minutes

def run_bruteforce_selenium():
    while True:
        print("Running run_bruteforce_selenium")
        BruteforceLoginSelenium()  # Call the BruteforceLoginSelenium function here
        # Add randomness to the timing
        time.sleep(randint(1800, 3600))  # Random time between 30 to 60 minutes

def run_bruteforce_xmlrpc():
    while True:
        print("Running run_bruteforce_xmlrpc")
        BruteforceLoginXMLRPC()  # Call the BruteforceLoginXMLRPC function here
        # Add randomness to the timing
        time.sleep(randint(1800, 3600))  # Random time between 30 to 60 minutes

def run_thread(thread_func, min_duration, max_duration):
    while True:
        print(f"Running {thread_func.__name__}")
        thread_func()  # Call the specified thread function
        # Add randomness to the timing
        sleep_duration = randint(min_duration, max_duration)
        print(f"Sleeping for {sleep_duration} seconds.")
        time.sleep(sleep_duration)

def terminate_random_thread(threads):
    while True:
        time.sleep(randint(300, 600))  # Random time between 5 to 10 minutes
        thread_to_terminate = choice(threads)
        print(f"Terminating {thread_to_terminate.name}")
        thread_to_terminate._stop()

if __name__ == "__main__":
    # Start threads for each task
    new_post_thread = threading.Thread(target=run_thread, args=(run_new_post, 300, 600), name="new_post_thread")
    account_maker_thread = threading.Thread(target=run_thread, args=(run_account_maker, 600, 900), name="account_maker_thread")
    bruteforce_selenium_thread = threading.Thread(target=run_thread, args=(run_bruteforce_selenium, 1800, 3600), name="bruteforce_selenium_thread")
    bruteforce_xmlrpc_thread = threading.Thread(target=run_thread, args=(run_bruteforce_xmlrpc, 1800, 3600), name="bruteforce_xmlrpc_thread")

    # Start the threads
    new_post_thread.start()
    account_maker_thread.start()
    bruteforce_selenium_thread.start()
    bruteforce_xmlrpc_thread.start()

    # Start the thread termination manager
    termination_manager_thread = threading.Thread(target=terminate_random_thread, args=([new_post_thread, account_maker_thread, bruteforce_selenium_thread, bruteforce_xmlrpc_thread],))
    termination_manager_thread.start()

    # Keep the main thread alive (you can add an exit condition)
    while True:
        time.sleep(1)

