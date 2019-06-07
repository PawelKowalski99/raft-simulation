class Round:
    """
    Holds information about amount of rounds
    """
    def __init__(self):
        """
        Initialization of round counter.
        """
        self.count = 0

    def run(self):
        """
        Increase number of round by 1.
        """
        self.count += 1
