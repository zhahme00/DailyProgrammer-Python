# http://www.reddit.com/r/dailyprogrammer/comments/39ws1x/20150615_challenge_218_easy_todo_list_part_1/

class ToDoList:
    def __init__(self):
        self.list = []

    def AddItem(self, task):
        if task not in self.list:
            self.list.append(task);

    def DeleteItem(self, task):
        try:
            self.list.remove(task);
        except ValueError:
            pass

    def ViewList(self):
        for i, item in enumerate(self.list):
            print("{0} - {1}".format(i + 1, item))

# test run
l = ToDoList()
l.AddItem("clean gutter")
l.AddItem("finish taxes")
l.AddItem("cook weekend meal")
l.DeleteItem("taxes")
l.ViewList()
