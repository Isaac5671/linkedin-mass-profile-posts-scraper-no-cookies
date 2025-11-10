thonimport requests
from bs4 import BeautifulSoup

class LinkedInParser:
    def __init__(self):
        self.base_url = "https://www.linkedin.com/in/"

    def scrape_profile(self, profile_url: str):
        """Scrape posts from a LinkedIn profile"""
        profile_data = self.get_profile_data(profile_url)
        posts = self.scrape_posts(profile_url)
        return {
            "profile": profile_data,
            "posts": posts
        }

    def get_profile_data(self, profile_url: str):
        """Get basic profile data from LinkedIn"""
        response = requests.get(f"{self.base_url}{profile_url}")
        soup = BeautifulSoup(response.content, 'html.parser')
        profile_data = {
            "first_name": soup.find('h1').text.split()[0],
            "last_name": soup.find('h1').text.split()[-1],
            "headline": soup.find('h2').text,
            "profile_url": profile_url
        }
        return profile_data

    def scrape_posts(self, profile_url: str):
        """Scrape posts from the LinkedIn profile"""
        posts = []
        response = requests.get(f"{self.base_url}{profile_url}/recent-activity/")
        soup = BeautifulSoup(response.content, 'html.parser')
        post_elements = soup.find_all('div', {'class': 'feed-shared-update-v2'})
        for post in post_elements:
            post_data = {
                "posted_at": post.find('span', {'class': 'visually-hidden'}).text.strip(),
                "text": post.find('span', {'class': 'break-words'}).text.strip(),
                "url": f"{self.base_url}{profile_url}/detail/recent-activity/",
                "author": self.get_profile_data(profile_url),
                "stats": self.extract_reactions(post),
                "media": self.extract_media(post)
            }
            posts.append(post_data)
        return posts

    def extract_reactions(self, post):
        """Extract reactions from a post"""
        stats = {
            "total_reactions": 0,
            "likes": 0,
            "comments": 0
        }
        # Example: Extract reactions count (likes, comments, etc.)
        reactions = post.find_all('span', {'class': 'social-details-social-counts__reactions'})
        for reaction in reactions:
            stats["likes"] += int(reaction.text)
        return stats

    def extract_media(self, post):
        """Extract media information from the post"""
        media = {}
        media_elements = post.find_all('img')
        if media_elements:
            media = {
                "type": "image",
                "url": media_elements[0]['src'],
                "thumbnail": media_elements[0]['src']
            }
        return media