thonimport requests

class InstagramParser:
    def __init__(self, usernames, max_posts):
        self.usernames = usernames
        self.max_posts = max_posts

    def scrape(self):
        posts_data = []
        for username in self.usernames:
            posts_data.extend(self._scrape_user_posts(username))

        return posts_data[:self.max_posts]

    def _scrape_user_posts(self, username):
        url = f'https://www.instagram.com/{username}/'
        response = requests.get(url)
        posts = self._parse_posts(response.text)
        return posts

    def _parse_posts(self, html_content):
        # This is a mock function to simulate parsing Instagram's HTML content.
        # In a real scraper, this would involve parsing the HTML and extracting the post data.
        return [
            {
                "pk": "3482602799815487662",
                "media_type": 2,
                "code": "DBUsMt4yHCu",
                "caption": "Sample post caption",
                "like_count": 500,
                "comment_count": 30,
                "user": {"username": "sampleuser"},
                "image_versions2": {"candidates": [{"url": "https://example.com/image.jpg"}]}
            }
        ]