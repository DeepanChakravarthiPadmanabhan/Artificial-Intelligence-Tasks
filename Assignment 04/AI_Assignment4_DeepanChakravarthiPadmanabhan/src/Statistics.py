class Statistics:
    def __init__(self):
        self.Algorithm = None
        self.Heuristic = None
        self.NumberOfExtensions = 0
        self.GoalPathLength = -1
        self.Enqeues = 0
        self.Deqeues = 0
        self.NumberOfInsertionRejectionsDueToAlreadyAvailability = 0
        self.StartTime = -1
        self.EndTime = -1
        self.GoalNodePathCost_fn = -1
        self.GoalNodePathCost_gn = -1
        self.GoalNodePathCost_hn = -1

    def __str__(self):
        str_stats = ''
        str_stats = str_stats + 'The Algorithm is : ' + str(self.Algorithm)
        str_stats = str_stats + '\n'
        str_stats = str_stats + 'The Heuristic is : ' + str(self.Heuristic)
        str_stats = str_stats + '\n'
        str_stats = str_stats + 'The Operations started at : ' + str(self.StartTime)
        str_stats = str_stats + '\n'
        str_stats = str_stats + 'The Operations ended at : ' + str(self.EndTime)
        str_stats = str_stats + '\n'
        str_stats = str_stats + 'The total time taken is : ' + str(self.EndTime - self.StartTime)
        str_stats = str_stats + '\n'
        str_stats = str_stats + 'Number of state transitions to goal : ' + str(self.GoalPathLength)
        str_stats = str_stats + '\n'
        str_stats = str_stats + 'Total Number Of Frontier push : ' + str(self.Enqeues)
        str_stats = str_stats + '\n'
        str_stats = str_stats + 'Total Number Of Frontier pops : ' + str(self.Deqeues)
        str_stats = str_stats + '\n'
        str_stats = str_stats + 'Total Number Of Extensions : ' + str(self.NumberOfExtensions)
        str_stats = str_stats + '\n'
        str_stats = str_stats + 'Total Number Of Insertion Rejections : ' + str(self.NumberOfInsertionRejectionsDueToAlreadyAvailability)
        str_stats = str_stats + '\n'
        str_stats = str_stats + 'Goal f(n) : ' + str(self.GoalNodePathCost_fn)
        str_stats = str_stats + '\n'
        str_stats = str_stats + 'Goal g(n) : ' + str(self.GoalNodePathCost_gn)
        str_stats = str_stats + '\n'
        str_stats = str_stats + 'Goal h(n) : ' + str(self.GoalNodePathCost_hn)
        str_stats = str_stats + '\n'

        return  str_stats

Instance = Statistics()