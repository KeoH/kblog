from kblog.models import Publication


class Page(Publication):
    
    def __str__(self):
        return self.title
