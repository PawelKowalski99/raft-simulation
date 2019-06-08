class Round:
    """
    Holds information about amount of rounds
    """
    count = 0
    def __init__(self):
        """
        Initialization of round counter.
        """
        pass

    def run(self):
        """
        Increase number of round by 1.
        """
        Round.count += 1
