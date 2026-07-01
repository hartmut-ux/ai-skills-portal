# Pre-Edit Backup Hook

A **hook** fires automatically whenever a specified event occurs in Claude Code — no need to invoke it manually. This hook creates a timestamped backup of any manuscript or draft file *before* Claude edits it, so you can always recover the original version.

This is especially useful when:
- Incorporating peer reviewer comments (you may want the original annotated draft back)
- Making large-scale revisions (easy to restore if the revision goes wrong)
- Experimenting with structural changes to a draft

---

## Setup (one-time, ~2 minutes)

Open Claude Code in your project folder and paste this prompt:

```
Create a pre-edit hook that automatically backs up any file in the drafts/ folder before editing it. Save the backup to drafts/backups/ with a timestamp in the filename. Format: [originalname]_backup_YYYYMMDD_HHMMSS.[ext]
```

Claude Code will create a `.claude/hooks/` configuration file. Once created, the hook runs automatically — you do not need to think about it again.

---

## What the Hook Does

Before Claude edits `drafts/chapter2.docx`, it:
1. Creates `drafts/backups/chapter2_backup_20260607_143022.docx`
2. Proceeds with the edit

You can ask for backups at any time:
```
Show me the backups of chapter2
Restore chapter2 to the version from yesterday
```

---

## Recovering a Backup

```
Restore drafts/chapter2.docx from its most recent backup
```
or
```
Show me what changed between the current chapter2 and its backup from [date]
```

---

## Customizing the Scope

You can restrict the hook to specific file types or folders:
```
Only back up .docx and .md files in the drafts/ folder, not the literature/ folder
```

---

## Why Not Just Use Git?

Git is ideal for code. For non-technical researchers, a timestamped backup folder is simpler and more accessible — no terminal commands needed to browse or restore versions.

---

*Part of the academic-research-suite skill. Set up once per project.*
