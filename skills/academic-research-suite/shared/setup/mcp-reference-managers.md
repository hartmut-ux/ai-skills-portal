# MCP Setup: Reference Managers & Academic Discovery

Connecting your reference manager and academic search tools to Claude Code via MCP (Model Context Protocol) lets Claude search your personal library, retrieve paper details, and cite directly from your collection — without copy-pasting.

---

## 1. Zotero MCP

**What it does**: Claude can search your Zotero library by author, title, or keyword; retrieve abstracts and metadata; and cite papers already in your collection.

**Setup**:
1. Get your Zotero API key: [zotero.org/settings/keys](https://www.zotero.org/settings/keys)
2. Get your Zotero user ID: shown on the same page
3. In Claude Code, open **Settings → Integrations → Add MCP** and paste:

```json
{
  "mcpServers": {
    "zotero": {
      "command": "npx",
      "args": ["-y", "zotero-mcp"],
      "env": {
        "ZOTERO_API_KEY": "your_api_key_here",
        "ZOTERO_USER_ID": "your_user_id_here"
      }
    }
  }
}
```

Or ask Claude Code directly:
```
Set up the Zotero MCP server. My API key is [key] and my user ID is [id].
Give me a step-by-step tutorial assuming I'm a complete novice.
```

**Once connected**, you can ask:
```
Search my Zotero library for papers by Venuti
Summarize the paper "The Translator's Invisibility" from my Zotero
Find all papers in my Zotero tagged "systematic review" and list their abstracts
```

---

## 2. Mendeley MCP

**What it does**: Same as Zotero — access your Mendeley library from within Claude Code.

**Setup**: Search for the current Mendeley MCP server:
```
Search GitHub for a Mendeley MCP server. Go to the link and give me a step-by-step tutorial on how to add it to Claude Code. Assume I'm a complete novice.
```

Claude will find the latest version and generate a tailored tutorial for your system.

---

## 3. Consensus MCP (AI-powered academic search)

**What it does**: Searches peer-reviewed literature using natural language questions. Returns papers with evidence ratings and consensus assessments. Better than a keyword search for "what does research say about X" questions.

**Setup**:
- Go to [consensus.app](https://consensus.app) → API → get your key
- Ask Claude Code:
```
Set up the Consensus MCP. My API key is [key].
```

**Example use**:
```
Use Consensus to find papers on the effect of sleep deprivation on academic performance
What does the research say about second-language acquisition in adult learners? Use Consensus.
```

---

## 4. Exa MCP (semantic web + academic search)

**What it does**: Semantic search across the web and academic sources. Useful for finding papers, grey literature, and recent preprints that aren't in your personal library yet.

**Setup**:
- Get API key at [exa.ai](https://exa.ai)
- Ask Claude Code:
```
Set up the Exa MCP. My API key is [key].
```

**Example use**:
```
Use Exa to find recent papers on Hans Christian Andersen in postcolonial literature
Find preprints on AI-assisted systematic review published in the last 6 months
```

---

## 5. Scheduled Literature Monitoring

Once Consensus or Exa is connected, you can set up a recurring search:

```
Schedule a daily task at 10am: search Consensus for new papers on [your topic], 
add title + DOI + abstract to literature/new-papers-log.md
```

This keeps your literature folder current without manual searching.

---

## Which Tool for Which Task?

| Need | Tool |
|------|------|
| Cite from papers you already have | Zotero or Mendeley |
| Find new papers on a topic | Consensus or Exa |
| Stay updated on new publications | Scheduled Consensus/Exa task |
| Search by author or your own tags | Zotero or Mendeley |

---

*Part of the academic-research-suite skill. Set up whichever tools match your workflow.*
