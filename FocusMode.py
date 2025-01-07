import time
import datetime
import os

def focus_mode():
    start_time = datetime.datetime.now()
    print("Focus Mode Started...")
    print("Press Ctrl+C to exit")
    
    try:
        while True:
            current_time = datetime.datetime.now()
            elapsed_time = current_time - start_time
            
            # Save focus time to file
            with open('data/focus.txt', 'a') as f:
                f.write(f"{elapsed_time.seconds//60},")
            
            time.sleep(60)  # Update every minute
            
    except KeyboardInterrupt:
        print("\nFocus Mode Ended")
        return 