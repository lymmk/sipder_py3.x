class UrlManager:
    def __init__(self):
        self.urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None or url in self.old_urls:
            return
        if url not in self.urls and url not in self.old_urls:
            self.urls.add(url)

    def has_new_url(self):
        return len(self.urls) != 0

    def get_new_url(self):
        new_url = self.urls.pop()
        if new_url not in self.old_urls:
            return new_url
        return None

    def add_new_urls(self, new_urls):
        if len(new_urls) != 0:
            for new_url in new_urls:
                self.add_new_url(new_url)
