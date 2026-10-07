# Session 5: Git and GitHub

`git commit -m "message"` commits staged changes only. `git commit -a -m "message"` first stages modified and deleted *tracked* files, but it does not add new untracked files. A new file still needs `git add`.

This repository's history demonstrates cherry-pick. I created commits on `main`, then a `git-practice` branch with two commits. I selected one commit from that branch and applied it to `main` with `git cherry-pick <hash>`. The selected change is the Git command note in this folder. The history can be checked with:

```bash
git log --oneline --all --graph --decorate -12
git show --stat HEAD
git branch -a
```

[`git-output.md`](git-output.md) records the actual commit IDs and command output after the exercise.
