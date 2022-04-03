# Action: Check For New Commits

Check for new commits in public repositories periodically. Built using [GhApi](https://ghapi.fast.ai/) and [fastcore](https://fastcore.fast.ai/)

### Usage

```
Arguments:
  ref_datetime: (str) The datetime to check the latest commit 
      datetime against. Must follow the ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`, 
      e.g. "2022-01-01T00:00:00Z" (https://en.wikipedia.org/wiki/ISO_8601) (default: ``)
  owner: (str) The owner of the public repository
  repo: (str) The name of the public repository
  file_path: (str, optional) Check for commits only on a particular filepath (default: `None`)

Returns:
  A tuple of:
      (boolean whether there are new commits, datetime of new commits or None, Commit message or None)
```


You can test this workflow like this with `gh` in the root of this repo

```
gh workflow run action.yml  \\ 
      -f repo="pytorch-image-models"  \\
      -f owner="rwightman"  \\
      -f ref_datetime="2022-04-01T00:00:00Z"
```
