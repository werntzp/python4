"""
Modified so the subscriber unsubscribes itself after three runs
"""

class Publisher:
    def __init__(self):
        self._subscribers  = []
        self._tobedeleted = [] # track subscribers to be deleted
        
    def subscribe(self, subscriber):
        if subscriber in self._subscribers:
            raise ValueError("Multiple subscriptions are not allowed")
        self._subscribers.append(subscriber)
    
    def unsubscribe(self, subscriber):
        if subscriber not in self._subscribers:
            raise ValueError("Can only unsubscribe subscribers")
        #self._subscribers.remove(subscriber)
        # 4/7 - don't remove, but add to another list
        self._tobedeleted.append(subscriber)
        
    def publish(self, s):
        for subscriber in self._subscribers:
            subscriber(s)
        # 4/7 - if we have ones to be deleted, iterate through to re-build the subscribers list and reset the deleted list    
        if self._tobedeleted:
            self._subscribers = [sub for sub in self._subscribers if sub not in self._tobedeleted]
            self._tobedeleted = []
            
if __name__ == '__main__':
    def multiplier(s):
        #print(2*s)
        pass
    
    class SimpleSubscriber:
        def __init__(self, name, publisher):
            self._name = name
            self._publisher = publisher
            self._count = 0
            publisher.subscribe(self.process)
            
        def process(self, s):
            # added internal count
            self._count += 1
            print(self._name, ":", s.upper())
            # oncer handled 3 messages, tell publisher to unsubscribe
            if self._count >= 3:
                #print("unsubscribing ", self.process)
                # here is where issue arises -- removing now is messing with list during an iteration! 
                # suggestion: instead of removing now, track with items are to be removed, finish the loop
                # and then do the remove                
                # 4/7 - no change here, but added code inside unsubscribe to address the issue
                publisher.unsubscribe(self.process)
        def __repr__(self):
            return self._name

    publisher = Publisher()
    publisher.subscribe(multiplier)
    for i in range(5):
        newsub = SimpleSubscriber("Sub"+str(i), publisher)
        line = input("Input {0}: ".format(i))
        publisher.publish(line)

 
