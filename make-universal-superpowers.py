import os
import urllib.request
import zipfile
import shutil

print("🚀 Building FULL Universal Superpowers ZIP with UPDATED ACTIVATE.md...")

REPO_NAME = "universal-superpowers"
TEMP_DIR = "temp_superpowers"
ORIGINAL_ZIP_URL = "https://github.com/obra/superpowers/archive/refs/heads/main.zip"

# Clean previous runs
for path in [REPO_NAME, TEMP_DIR]:
    if os.path.exists(path):
        shutil.rmtree(path)

# Download full original repo
print("📥 Downloading complete original repo...")
urllib.request.urlretrieve(ORIGINAL_ZIP_URL, "original.zip")

with zipfile.ZipFile("original.zip", 'r') as zip_ref:
    zip_ref.extractall(TEMP_DIR)

# Copy EVERYTHING
shutil.copytree(os.path.join(TEMP_DIR, "superpowers-main"), REPO_NAME, dirs_exist_ok=True)

shutil.rmtree(TEMP_DIR)
os.remove("original.zip")

# === UPDATED README.md ===
with open(f"{REPO_NAME}/README.md", "w", encoding="utf-8") as f:
    f.write('''# Universal Superpowers — for Grok & Every AI Chat Platform

**100% complete mirror of obra/superpowers** + universal activation.

Works on **Grok • Claude • ChatGPT • Gemini • LM Arena • yupp.ai • Cursor • Codex • OpenCode** — any LLM chat.

**No plugins • No uploads • One prompt.**

## How to use (20 seconds)
1. Paste the entire content of `ACTIVATE.md` as your first message.
2. Give the AI your task.

The AI will instantly load every skill from GitHub and follow the original framework with zero deviation.

## What's inside (everything from original)
- All 14 skills with exact SKILL.md, flowcharts, checklists
- All plugins, agents, commands, docs, hooks, lib, tests, etc.
- Updated ACTIVATE.md (v2.0 — much stronger)

Superpowers everywhere. Enjoy!
''')

# === NEW & IMPROVED ACTIVATE.md (this is the big update) ===
with open(f"{REPO_NAME}/ACTIVATE.md", "w", encoding="utf-8") as f:
    f.write('''**SUPERPOWERS FULLY ACTIVATED — UNIVERSAL EDITION v2.0**

You are now running the complete **Universal Superpowers** framework.

**Main Repo:** https://github.com/YOUR_GITHUB_USERNAME/universal-superpowers

**All skills live here (raw):**
https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/universal-superpowers/main/skills/[skill-name]/SKILL.md

**EXTREMELY IMPORTANT — READ THIS FIRST**
If you think there is even a 1% chance a skill might apply to what you are doing, you ABSOLUTELY MUST invoke/load the skill.

IF A SKILL APPLIES TO YOUR TASK, YOU DO NOT HAVE A CHOICE. YOU MUST USE IT.

This is not negotiable. This is not optional. You cannot rationalize your way out of this.

**MANDATORY STARTUP SEQUENCE**
1. Immediately load and follow: https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/universal-superpowers/main/skills/using-superpowers/SKILL.md
2. For every single user message from now on:
   - Check if ANY skill applies (even 1%)
   - If yes → fetch the full SKILL.md using your browse/web tool
   - Announce at the top of your reply: **Active skill: [name]**
   - Follow every checklist, flowchart, gate, and anti-pattern rule EXACTLY

**HOW TO FETCH SKILLS (platform specific)**
- **Grok**: Use your `browse_page` tool with the exact raw URL above.
- **Claude / Cursor / ChatGPT / Gemini / others**: Use your web browse / fetch / search tool to load the raw GitHub URL.
- Always prefer fresh fetch over memory.

**RED FLAGS — IF YOU THINK ANY OF THESE, STOP AND LOAD A SKILL**
- "This is just a simple question"
- "I need more context first"
- "Let me explore the codebase first"
- "I can check git/files quickly"
- "This doesn’t need a formal skill"
- "I remember this skill"
- "This doesn’t count as a task"
- "The skill is overkill"
- "I’ll just do this one thing first"

**Skill Priority Order**
1. Process skills first (brainstorming, systematic-debugging, writing-plans, using-superpowers)
2. Implementation skills second (TDD, subagent-driven-development, etc.)

**Permanent Rules for the entire conversation**
- Begin every response with **Active skill: ...**
- Never write code, plan, debug, or answer without first loading the correct skill.
- Strict RED-GREEN-REFACTOR when test-driven-development applies.
- Use all your tools perfectly (code_execution for TDD, browse_page for research, etc.).
- Zero deviation from the original Superpowers discipline.

Superpowers are now active for the rest of this chat.
Reply with: "**Superpowers v2.0 activated. Ready.**" and wait for my first task.
''')

# === Create ZIP ===
print("📦 Creating universal-superpowers.zip with updated ACTIVATE.md...")
shutil.make_archive(REPO_NAME, 'zip', REPO_NAME)

print("✅ DONE! ACTIVATE.md has been massively upgraded.")
print(f"   File: {REPO_NAME}.zip")
print("")
print("Next steps:")
print("1. Run the script → get the new zip")
print("2. Upload to your GitHub repo 'universal-superpowers'")
print("3. Replace YOUR_GITHUB_USERNAME in ACTIVATE.md")
print("4. Done!")
print("")
print("The new ACTIVATE.md is now 3× stronger and forces perfect Superpowers behavior on every platform, especially Grok.")
print("Enjoy the upgraded version! 🚀")