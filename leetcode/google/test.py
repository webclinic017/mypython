import collections
import re,copy
<<<<<<< HEAD

=======
>>>>>>> 3d38d3d466f43adfcce9bbddc2bbdce2f68b5979

with open("piclog") as x:

    words = re.findall(r'\w+', x.read().lower())
    print type(words)
    print collections.Counter(words).most_common(10)

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 10)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(9)
    for i in range(10):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')


mapping = {
            '(':')',
            '{':'}',
            '[':']',
        }
print (")" in mapping)

print 1
k=[[i for i in range(10)] for y in range(5)]

k[0][0]=100
print k

l1=["aaa","bb","ccc"]
l1.sort(key=lambda x:len(x))
print ("aa" in "badaa")

