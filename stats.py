
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


#possibilité de stockage json : 
#{faire le stockage au fur et à mesure de avancement de la partie}
# { tout dump à la fin de la partie}