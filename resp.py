import requests

def repos_with_most_stars():
    gh_api_repo_search_url = "https://api.github.com/search/repositories"
    parameters = {"q": "stars:>5000"}
    response = requests.get(gh_api_repo_search_url, params=parameters)
    response_json = response.json()
    return response_json["items"]
    
if __name__ == "__main__":
    results = repos_with_most_stars()
    for result in results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]
        
    print(f"-> {name} is a {language} repo with {stars} stars.")