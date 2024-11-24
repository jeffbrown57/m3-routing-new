from . import routes # noqa: F401
import anvil.server
import threading
import asyncio


@anvil.server.background_task
def run_multiple_threads():
    
    def thread_function(thread_no):
        loop = asyncio.new_event_loop() #Create a need loop for the thread
        asyncio.set_event_loop(loop)
    
        async def print_in_thread(): #This function will run on all threads
            while True:
                print(f"Message from thread {thread_no}")
                await asyncio.sleep(2)  
    
        loop.run_until_complete(print_in_thread())

    threads = []
    
    for i in range(3):  #Creating 3 Threads
        t = threading.Thread(target=thread_function, args=(i,)) 
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

@anvil.server.callable
def run_it():
    anvil.server.launch_background_task('run_multiple_threads')