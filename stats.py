
from datetime import datetime
def time_checker():
    
    now = datetime.now()
    now = now.strftime("%H:%M:%S")
    return now

def time_diff(start, end):
    diff = end - start
    return diff

if __name__ == "__main__":
    start = time_checker()
    print(start)
    end = time_checker()
    print(end)
    print(time_diff(start,end))
    print(time_diff(start,end).total_seconds())