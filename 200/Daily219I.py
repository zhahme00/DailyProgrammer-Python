# http://www.reddit.com/r/dailyprogrammer/comments/3a64hq/20150617_challenge_219_intermediate_todo_list/

class TodoList:
    def __init__(self):
        # category -> [task1, task2,...] lookup
        self.categories = {}
 
 
    def add(self, task, *category):
        for c in category:
            if c in self.categories:
                self.categories[c].append(task)
            else:
                self.categories[c] = [task]
 
    def remove(self, task):
        for task_list in self.categories.values():
            try:
                task_list.remove(task)
            except ValueError:
                pass
 
    def view(self, *category):
        if len(category) == 0:
            s = set()
            for category_task in [task_list for task_list in self.categories.values()]:
                s.update([task for task in category_task])
            self.__printout__(s)
            return
 
        s = set(self.categories[category[0]])
        for c in category[1:]:
            s = s & set(self.categories[c])
 
        self.__printout__(s, category)
 
 
    def __printout__(self, iterable, *category):
        # output category header
        if len(category) == 0:
            print("-- ALL --")
        else:
            # todo: fix trailing comma
            print("-- ", end='')
            for c in [cat for cat in category[0]]:
                print(c.upper(), end=',')
            print(" --")
 
        for i, task in enumerate(iterable):
            print("{} - {}".format(i + 1, task))
 
 
if __name__ == "__main__":
    l = TodoList()
    l.add('mow front lawn', 'home', 'zee')
    l.add("call handyman to fix window", "zee")
    l.add('renew club membership', 'zee', 'home')
    l.add('cook dinner on weekend :)', 'home', 'wife')
    l.add('take dog to park', 'wife', 'zee')
    l.view()
