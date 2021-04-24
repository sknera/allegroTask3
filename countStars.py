from github import Github


def count_stars_for_user(username):
    g = Github()
    user = g.get_user(username)
    repos = user.get_repos()
    num_of_stars = 0
    result = []
    for repo in repos:
        result.append({"repository:": repo.name, "stars": repo.stargazers_count})
        num_of_stars += repo.stargazers_count
    return result, num_of_stars
