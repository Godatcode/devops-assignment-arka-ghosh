# Session 3: System information script

[`system_info.sh`](system_info.sh) prints the date, hostname, username, disk usage, and process list. It uses variables, asks for a folder name with `read`, creates the folder with `mkdir -p`, creates the output file with `touch`, and writes the complete process list using `>`.

```bash
./system_info.sh
# Enter a name for the output folder: system-report
cat system-report/processes.txt | head
```

The folder name is checked before it becomes a path. That prevents a response such as `../another-folder` from writing outside the working directory. The script works with Bash on Linux and macOS; The script uses Bash's `read -p` prompt as requested.

## Local check

On 7 October 2026 the script printed the date, hostname, username and disk table, created `system-report/processes.txt`, and `wc -l` reported 721 lines in that process file. The generated process listing was not committed because it can contain private command arguments.
