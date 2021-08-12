from DataBaseSync.models import Member

# class for save data to db
class dbSaver:

    # A function that initially writes 
    # the name and data parameters
    def __init__(self, name: str, username: str, description: str,
                followers: str, following: str, stars: str, 
                location: str, repositories: str, contributions: str,
                profile_link: str):

        self.name = name
        self.username = username
        self.description = description
        self.followers = followers
        self.following = following
        self.stars = stars
        self.location = location
        self.repositories = repositories
        self.contributions = contributions
        self.profile_link = profile_link

    # A function that takes parameters from __init__
    # and save data to db
    def save(self) -> None:
        m = Member(
                name=self.name,
                username=self.username,
                description=self.description,
                followers=self.followers,
                following=self.following,
                stars=self.stars,
                location=self.location,
                repositories=self.repositories,
                contributions=self.contributions,
                profile_link=self.profile_link
            )

        m.save()
