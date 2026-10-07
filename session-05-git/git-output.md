# Git command output

Captured on 7 October 2026 in this repository.

## `git commit -m` with an untracked file

```text
On branch git-practice
Untracked files:
  session-05-git/cherry-picked-command.md
nothing added to commit but untracked files present
```

After `git add session-05-git/cherry-picked-command.md`, `git commit -m` created commit `330172b`. In contrast, editing the already tracked `tracked-note.txt` and running `git commit -a -m` created `2912d67` without a separate `git add`.

## Cherry-pick

```text
$ git log --oneline --all --graph --decorate -8
* 10a1b85 (main) Add command note for cherry-pick
| * 330172b (git-practice) Add command note for cherry-pick
| * 2912d67 Update tracked note with commit -a
|/
* 60ef102 Add tracked file for Git practice
* 6153e1d Add Kubernetes, Terraform, CI, and final project
* 7433331 Add Docker applications and network labs
* e22f017 Document Linux, shell, networking, and Git exercises
```

I selected branch commit `330172b` and ran `git cherry-pick 330172b` on `main`. It created `10a1b85` on main with the same file change; the different hash is expected because a cherry-pick creates a new commit. The separate tracked-note change stayed only on `git-practice`.
