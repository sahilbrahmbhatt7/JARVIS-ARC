
# #Run Jarvis
# import multiprocessing


# def startJarvis():
#     print("Process 1 is running")
#     from main import start
#     start()

# # run hot word
# def listenHotword(state):
#     print("Process 2 is running")
#     from engine.features import hotword
#     hotword(state)

# def listenClap():
#     print("Process 3 (Clap) is running")
#     from engine.clapFun import listen_clap
#     listen_clap()

# #We Use MultiThreding 
# # Start both processes
# if __name__ == '__main__':
#         state = multiprocessing.Value('i', 0)  # 0 = IDLE, 1 = LISTENING, 2 = PROCESSING
#         p1 = multiprocessing.Process(target=startJarvis)
#         p2 = multiprocessing.Process(target=listenHotword,args=(state,))
#         p3 = multiprocessing.Process(target=listenClap)
#         p1.start()
#         p2.start()
#         p3.start()
#         p1.join()

#         if p2.is_alive():
#             p2.terminate()
#             p2.join()
        
#         if p3.is_alive():
#             p3.terminate()
#             p3.join()

#         print("system stop")

# Run Jarvis using Threading
import threading


def startJarvis():
    print("Thread 1 is running")
    from main import start
    start()


def listenHotword():
    print("Thread 2 is running")
    from engine.voice.hotword import hotword
    hotword()


def listenClap():
    print("Thread 3 (Clap) is running")
    from engine.voice.clapFunction import listen_clap
    listen_clap()


if __name__ == '__main__':

    t1 = threading.Thread(target=startJarvis)
    t2 = threading.Thread(target=listenHotword, daemon=True)
    t3 = threading.Thread(target=listenClap, daemon=True)

    t1.start()
    t2.start()
    t3.start()

    # Wait for Jarvis main thread to finish
    t1.join()

    print("system stop")