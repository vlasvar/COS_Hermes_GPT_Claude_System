# Chief of Staff System

A user-owned, model-agnostic operating system for working with an AI Chief of Staff.

The system combines:

- **Google Sheets** for structured operational state
- **Google Drive** for source documents and evidence
- **Markdown** for policies, context, workflows, and reviews
- **Agent adapters** for Hermes, ChatGPT Projects, and Claude Projects
- An optional, separate **GPT Sites dashboard concept** as a replaceable presentation layer

> This repository contains only generic templates, schemas, instructions, and fictional examples. Never commit a real user's data, credentials, private documents, sheet exports, or conversation history.

## What this is

This is not a prompt collection. It is a small operating kernel with a consistent data model, permission rules, workflow, and audit trail. The AI model can change without forcing the user to rebuild the system.

```text
Experience       Chat / optional dashboard
Agent adapter    Hermes | ChatGPT Project | Claude Project
Kernel           Context | policy | permissions | workflows
User-owned data  Google Sheets | Drive | Markdown
```

## Core operating loop

```text
Capture → Interpret → Classify → Propose → Approve → Execute → Record → Review
```

## Beginner setup guide — no coding required

If you can download a folder and copy and paste text, you can set this up. Take it one step at a time. Nothing in this guide sends messages, spends money, or publishes anything.

### Before you start

You need:

- A Google account
- One AI assistant: **ChatGPT**, **Claude**, or **Hermes**
- About 20 minutes

For the easiest first setup, use a **ChatGPT Project** or **Claude Project**. Hermes gives you more control but requires installing the Hermes application and copying a few commands.

### Part 1 — Download the kit

1. At the top of this GitHub page, click the green **Code** button.
2. Click **Download ZIP**.
3. Open your Downloads folder.
4. Double-click the downloaded ZIP file to unzip it.
5. You should now see a folder named `COS_Hermes_GPT_Claude_System`.

Keep this downloaded folder as the clean template. Your personal information should go into your private AI Project and Google Sheet, not back into this GitHub repository.

### Part 2 — Create your Google Sheet

The Sheet is the system's notebook. It holds projects, actions, commitments, decisions, reviews, and the agent activity log.

1. Open [Google Sheets](https://sheets.google.com).
2. Create a **Blank spreadsheet**.
3. Rename it to **My Chief of Staff**.
4. In the top menu, click **Extensions**, then **Apps Script**.
5. A new Apps Script page will open. Delete the small example function already shown there.
6. In the downloaded kit, open `templates`, then `google-sheets`, then `Code.gs`. If your computer asks which app to use, choose Notepad on Windows or TextEdit on macOS.
7. Select everything in `Code.gs` and copy it.
8. Paste it into the Apps Script editor.
9. Click the **Save** icon.
10. Near the top, choose `provisionChiefOfStaffSystem` from the function menu.
11. Click **Run**.
12. Google may ask you to choose your account and approve access. Read the request before accepting it. The included script declares `@OnlyCurrentDoc` so it is limited to the current spreadsheet. Stop if the permission screen asks for something unrelated.
13. Return to your Google Sheet.

You should now see these tabs:

`Inbox`, `Projects`, `Actions`, `Commitments`, `Decisions`, `Contacts`, `Reviews`, and `Agent Log`.

If you see those eight tabs, the Sheet is ready. The script creates headers and formatting only; it does not add personal information or send data anywhere.

Now create the evidence folder:

1. Open [Google Drive](https://drive.google.com).
2. Click **New**, then **New folder**.
3. Name it **Chief of Staff Evidence**.
4. Leave its access set to **Restricted**. Do not make it public.

This folder is where you can later keep documents that support a project, commitment, or decision. You do not need to put anything in it yet.

### Part 3 — Choose your AI assistant

Pick **one** option for your first setup. You can add another assistant later without rebuilding the Sheet.

<details>
<summary><strong>Option A: ChatGPT Project — easiest for most people</strong></summary>

1. Open ChatGPT.
2. Create a new **Project**.
3. Name it **My Chief of Staff**.
4. Open `adapters/chatgpt/PROJECT_INSTRUCTIONS.md` from the downloaded kit.
5. Copy all its text and paste it into the Project's instruction field.
6. Upload these six files to the Project:
   - `kernel/SYSTEM.md`
   - `kernel/CONTEXT.md`
   - `kernel/PERMISSIONS.md`
   - `kernel/WORKFLOWS.md`
   - `templates/profile/USER_PROFILE.md`
   - `config/system.example.yaml`
7. Also upload `examples/demo-inputs.md` so you can test the system safely.

Do not upload passwords, API keys, bank documents, identity documents, or other secrets.

</details>

<details>
<summary><strong>Option B: Claude Project</strong></summary>

1. Open Claude.
2. Create a new **Project**.
3. Name it **My Chief of Staff**.
4. Open `adapters/claude/CLAUDE.md` from the downloaded kit.
5. Copy all its text into the Project instructions.
6. Add these six files to the Project Knowledge:
   - `kernel/SYSTEM.md`
   - `kernel/CONTEXT.md`
   - `kernel/PERMISSIONS.md`
   - `kernel/WORKFLOWS.md`
   - `templates/profile/USER_PROFILE.md`
   - `config/system.example.yaml`
7. Also add `examples/demo-inputs.md` for the safe test.

Do not upload passwords, API keys, bank documents, identity documents, or other secrets.

</details>

<details>
<summary><strong>Option C: Hermes profile — more control</strong></summary>

First install and configure [Hermes Agent](https://hermes-agent.nousresearch.com/docs). Then open a terminal in the downloaded repository and run:

```bash
python scripts/create_instance.py ../my-private-cos --adapter hermes
hermes profile create chief-of-staff --description "Maintains my private Chief of Staff system."
hermes profile use chief-of-staff
hermes --in ../my-private-cos
```

The first command creates a separate private workspace. The next commands create and start an isolated Hermes profile. Full details are in the [Hermes adapter guide](adapters/hermes/README.md).

</details>

### Part 4 — Let the assistant set up your private profile

Open your new AI Project or Hermes profile and send this message:

```text
Help me set up this Chief of Staff System. Read the uploaded kernel, profile template, configuration template, and permission rules first.

Interview me one question at a time. Use my answers to prepare a completed USER_PROFILE.md and system.yaml. Do not ask for or store passwords, API keys, bank details, identity numbers, or other secrets. Keep the permission level at 1 (Suggest). Do not send messages, publish anything, delete anything, or spend money.
```

Answer one question at a time. When the interview is finished:

1. Ask the assistant to give you the completed `USER_PROFILE.md` and `system.yaml` files.
2. Download those two files.
3. In ChatGPT or Claude, remove the blank `USER_PROFILE.md` and `system.example.yaml` files, then upload the completed `USER_PROFILE.md` and `system.yaml`. In Hermes, save the completed files in the private workspace created earlier.
4. Keep these completed files private. Never add them to this public template repository.

When the assistant asks about storage, give it the links to your private Google Sheet and restricted evidence folder. These links identify the correct private resources; they do not make those resources public. If your AI plan does not support a Google Sheets connection, that is okay: the assistant can operate in **Suggest** mode and tell you exactly which rows to add manually.

### Part 5 — Run a safe test

Do not begin with important personal information. Start with the fictional examples included in the kit.

Send this message:

```text
Process the first fictional item in demo-inputs.md. Stay at permission level 1. Show me the classification, proposed Sheet changes, approval requirement, evidence, and Agent Log entry. Do not perform any external action.
```

A correct result should:

- Classify the information
- Propose one or more Sheet records
- Use stable record IDs
- Tell you whether approval is required
- Avoid sending or publishing anything
- Record the proposed operation in `Agent Log`

Repeat the test with all five fictional inputs. When the results look correct, your basic system is ready.

### Part 6 — Start using it carefully

Give the system one real item at a time, such as:

- A project you want to organize
- A commitment you need to remember
- A decision and the reason behind it
- A task with a due date

Keep permission level 1 until you trust the classifications and proposed changes. Connecting a tool does not automatically give the assistant permission to use it.

### The four rules to remember

1. **The Google Sheet is the operational source of truth.**
2. **Google Drive holds source documents and evidence.**
3. **Your AI Project or Hermes profile provides the intelligence and conversation.**
4. **The optional dashboard is only a view, never another database.**

> Stuck? Do not guess. Tell your assistant which numbered step you reached and copy the exact error message. Do not include passwords or secret keys.

After the core system works, you can explore the optional [GPT Sites dashboard concept](docs/dashboard-gpt-sites.md). The dashboard is a bonus, not a setup requirement.

## Technical quick start

1. Read [Privacy and public-repository rules](docs/privacy.md).
2. Generate a private workspace outside this repository:

   ```bash
   python scripts/create_instance.py /path/to/private-cos --adapter hermes
   ```

   Replace `hermes` with `chatgpt` or `claude` when appropriate.
3. Create the Google Sheet with [`templates/google-sheets/Code.gs`](templates/google-sheets/Code.gs), or reproduce the schema in [`schema/sheets.json`](schema/sheets.json).
4. Complete `USER_PROFILE.md` and `system.yaml` in the generated private workspace.
5. Configure the selected agent environment using [Agent profiles and projects](docs/profiles.md):
   - [Hermes profile](adapters/hermes/README.md)
   - [ChatGPT Project](adapters/chatgpt/README.md)
   - [Claude Project](adapters/claude/README.md)
6. Process the fictional inputs in [`examples/demo-inputs.md`](examples/demo-inputs.md).
7. Run the first review using [`templates/reviews/WEEKLY_REVIEW.md`](templates/reviews/WEEKLY_REVIEW.md).

Full instructions: [Onboarding](docs/onboarding.md).

## Repository map

```text
kernel/       Canonical terminology, rules, permissions, and workflows
schema/       Machine-readable data contracts
adapters/     Thin setup layers for each supported agent environment
templates/    Google Sheets, private profile, and review templates
docs/         Architecture, privacy, onboarding, and dashboard concept
examples/     Fictional test inputs only
scripts/      Private-instance generation and repository validation
```

## Core vs optional

The mandatory core is deliberately small: Inbox, Projects, Actions, Commitments, Decisions, Contacts, Reviews, and Agent Log. Finance, CRM, content, health, and household workflows should be optional modules rather than additions to the kernel.

## Validate the repository

```bash
python scripts/validate.py
python -m unittest discover -s tests -v
```

## Status

Early private build. The repository is being developed as if it were already public: generic examples only, no personal case study, and no private instance data.

## License

[MIT](LICENSE)
