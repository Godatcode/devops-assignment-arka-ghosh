# Sessions 1 and 2: Linux fundamentals

## Soft links and hard links

A symbolic link stores a path. It can cross filesystems and point to a directory, but it becomes dangling if the target moves. A hard link is another directory entry for the same inode. It normally cannot cross filesystems or link directories. Removing one hard link leaves the file data available through the other until the last link is removed.

```bash
mkdir -p link-lab && cd link-lab
printf 'sample\n' > original.txt
ln -s original.txt soft.txt
ln original.txt hard.txt
ls -li original.txt soft.txt hard.txt
readlink soft.txt
rm original.txt
cat hard.txt
# soft.txt is now dangling
rm soft.txt hard.txt
```

Interview answer: a soft link points to a *name*; a hard link is another *name for the same inode*. `ls -li` makes the difference visible.

## adduser and useradd

On Ubuntu, `adduser` is the friendly Debian script: it prompts for a password and account details and usually creates the home directory. `useradd` is the lower-level utility; its behavior depends on flags and distribution defaults. For an interactive Ubuntu account I would use `sudo adduser teststudent`, then verify with `id teststudent` and `getent passwd teststudent`. Remove the test account with `sudo deluser --remove-home teststudent`. These commands require an Ubuntu host and administrator access; they were not run on this macOS machine.

## journalctl

`journalctl` queries the systemd journal. `journalctl -b` shows this boot, `journalctl -u ssh --since today` filters a service, and `journalctl -f` follows new entries. `sudo journalctl -u ssh -n 30 --no-pager` is a useful service check. macOS does not run systemd, so this part requires an Ubuntu VM or host.

## Command notes

`pwd` shows the current directory, `ls -la` lists hidden entries and permissions, `cd` changes directory, `cp` copies, `mv` moves, `rm` removes, `find` searches, `grep` filters text, `chmod` changes permissions, `ps` lists processes, `df -h` shows filesystem usage, and `du -sh` measures a directory. Use `man <command>` to check flags before a destructive operation.

## Link exercise output (local run, 7 October 2026)

```text
13678527 ... hard.txt
13678527 ... original.txt
13678528 ... soft.txt -> original.txt
original.txt
Hard link after deleting original: sample
Soft link is dangling
```

The two regular names had the same inode (`13678527`); the symbolic link had a different inode.
