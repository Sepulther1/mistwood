# Onboarding (Humans & Assistants)

## Humans
- Use `grcd` to work in the repo, and `python3 -m http.server 8000` to view the dashboard.
- Keep private keys in your password manager. Optionally put your **public** Age key in `.mistwood/age.pub`.
- Expect the assistant to ask you to authorize the GitHub connector (orgs may require admin approval).
- For new/private repos, force indexing with a GitHub search: `repo:<owner/repo> import`.

## Assistants
- Treat “GitHub connection verified” as a blocking requirement for a successful handoff.
- Always root file paths at `$GR`. Use batch-safe scripts and skip ACTIVE WFB in mass updates.
- Record any failure with an explicit next action and re-run probes after each action.
