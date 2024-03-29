import threading
import time
def testing():
    print("This line executed by the main thread {}".format(threading.current_thread().name))
    time.sleep(3)
    
THREADS = []

# testing( )  # Call to function in the main thread
for i in range(0,16):
    t = threading.Thread(target=testing)  # Create a new thread
    THREADS.append(t)
    
    t.start()                          # Start the new thread
    # t.join(1)                           # Wait for the new thread to finish (1 sec)