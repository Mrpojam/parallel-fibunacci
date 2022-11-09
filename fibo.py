from threading import Thread

class fiboThread ():
    def __init__ (self):
        Thread.__init__(self)
        self.th = None
        self.value = 0
    
    def run (self, n, parent):
        print(f'thread started, n = {n}, parent = {parent}')
        if n <= 1:
            #print ("reached a leaf!")
            self.value = 1
            return self.value
        # Create new fiboThreads
        thread0 = fiboThread()
        thread1 = fiboThread()

        # Init Threads
        thread0.th = Thread(target = thread0.run, args = (n-1, n))
        thread1.th = Thread(target = thread1.run, args = (n-2, n))
        
        # Start Threads
        thread0.th.start()
        thread1.th.start()

        # Wait until Threads finish
        thread0.th.join()
        thread1.th.join()
        
        # Updating the value
        self.value = thread0.value + thread1.value
        print (f'thread finished, n = {n}, parent = {parent}, value = {self.value}')
        return self.value
        print(self.value)
        
    
    def fibo (self, n):
        self.run (n, -1)
        return self.value

fibo = fiboThread()
print(fibo.fibo(int(input())))
