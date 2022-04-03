"""Checks whether a public repository has had any commits since a reference datetime.
"""

from ghapi.all import GhApi

def check_if_new_commits(ref_datetime, owner, repo, file_path=None):
    """Checks whether a public repository has had any commits since a reference datetime.
    
    This uses the repos.list_commits function from GhApi: https://ghapi.fast.ai/fullapi.html
    See the `list-commits` github rest api documentation for a full additional parameters:
    https://docs.github.com/en/rest/reference/commits#list-commits
    
    Arguments:
        ref_datetime: (str) The datetime to check the latest commit 
            datetime against. Must follow the ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`, 
            e.g. "2022-01-01T00:00:00Z" (https://en.wikipedia.org/wiki/ISO_8601) (default: ``)
        owner: (str) The owner of the public repository
        repo: (str) The name of the public repository
        file_path: (str, optional) Check for commits only on a particular filepath (default: `None`)
    
    Returns:
        A tuple of:
            (boolean whether there are new commits, datetime of new commits or None)
    """
    
    api = GhApi()
    commits = api.repos.list_commits(
        owner=owner, 
        repo=repo, 
        results=file_path,
        since=ref_datetime,
        per_page=1
    )
    
    if len(commits) > 0:
        new_commits_present = True
        last_commit_date = commits[0]['commit']["committer"]["date"]
        commit_message = commits[0]['commit']["message"]
        return(new_commits_present, last_commit_date, commit_message)
    else:
        new_commits_present = False
        last_commit_date = None
        commit_message = None
        return (new_commits_present, last_commit_date, commit_message)
      
if __name__ == '__main__':
  owner = "rwightman"
  repo = "pytorch-image-models"
  ref_date = "2022-04-01T00:00:00Z"
  f_path = "results/results-imagenet.csv"
  
  new_commits_present, last_commit_date, commit_message = check_if_new_commits(
    ref_datetime=ref_date, 
    owner=owner, 
    repo=repo, 
    file_path=f_path
  )
  
  print("new_commits_present")
  print("last_commit_date")
  print("commit_message")
#   print("changelog 1")
#   print("changelog 2")
#   print("changelog 3")
    
#   print(f'{new_commits_present} || {last_commit_date} || {commit_message}')



