class Group:
    def __init__(self, lst):
        self.students = sorted(lst)
    def __str__(self):
        return ", ".join(self.students)
    def __len__(self):
        return len(self.students)
    def __getitem__(self, pos):
        return self.students[pos]


gr = Group(["Иванов","Акаев","Симашко"])
print(gr)
print(len(gr))
for st in gr: print(st)
for i in range(len(gr)): print(gr[i])
for i, st in enumerate(gr): print(i+1, st)