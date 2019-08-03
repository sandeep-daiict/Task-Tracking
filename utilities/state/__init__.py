class Status:

    def __init__(self, name, status):
        self.next_status = status
        self.name = name
    
    def is_completed(self):
        return self.next_status is None
    