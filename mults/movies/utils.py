class CustomStr:
    def __str__(self):
        if self.title:
            res = self.title
        else:
            res = self
        return res