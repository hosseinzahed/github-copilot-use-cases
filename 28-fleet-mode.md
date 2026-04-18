## Fleet Mode

Fleet Mode allows you to run multiple GitHub Copilot coding agents in parallel, each working on a separate task within the same repository. Instead of queuing tasks one after another, you can assign several issues or feature requests simultaneously, and each agent operates in its own isolated branch, writing code, running tests, and opening a pull request when done.

### How It Works

1. **Assign multiple tasks** — From the Copilot dashboard or by labeling issues, you kick off several coding agents at once.
2. **Isolated branches** — Each agent creates its own branch (e.g., `copilot/fix-123`, `copilot/feat-456`) so there are no merge conflicts while work is in progress.
3. **Parallel execution** — Agents run concurrently on GitHub-hosted infrastructure, each following its own plan: reading code, making changes, running CI, and iterating on failures.
4. **Pull requests** — When an agent finishes, it opens a PR with a summary of changes, test results, and a link back to the originating issue.
5. **Human review** — You review the PRs as they arrive, approve, request changes, or close them. Agents can respond to review comments and push follow-up commits.

### Example

Imagine you have a backlog with three independent issues:

| Issue | Description |
|-------|-------------|
| #101  | Fix the off-by-one error in pagination |
| #102  | Add a dark-mode toggle to the settings page |
| #103  | Write unit tests for the billing module |

With Fleet Mode you assign all three to Copilot at once:

```
Label issues #101, #102, and #103 with "copilot"
```

Copilot spins up three agents in parallel:

```
Agent A  ──▶  branch: copilot/fix-101   ──▶  PR #201 (pagination fix)
Agent B  ──▶  branch: copilot/feat-102  ──▶  PR #202 (dark-mode toggle)
Agent C  ──▶  branch: copilot/test-103  ──▶  PR #203 (billing tests)
```

Each agent works independently — reading the codebase, making changes, running CI — and opens a pull request when done. You review the three PRs as they come in, rather than waiting for each task to finish sequentially.

### When to Use Fleet Mode

- **Sprint cleanup** — Knock out a batch of small-to-medium issues at the start of a sprint.
- **Test coverage drives** — Generate tests across multiple modules simultaneously.
- **Multi-area refactors** — Apply similar changes to independent parts of the codebase in parallel.
- **Onboarding prep** — Fix documentation gaps, lint warnings, and starter bugs before a new team member joins.

### Considerations

- Each agent works in isolation, so tasks that depend on one another should still be handled sequentially.
- Monitor the PR queue — a burst of agent PRs can overwhelm reviewers if not planned for.
- Set up required CI checks so agents iterate on failures automatically before requesting review.

Learn more: [Using Copilot coding agent](https://docs.github.com/en/copilot/using-github-copilot/using-copilot-coding-agent)
