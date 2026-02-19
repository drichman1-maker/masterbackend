# Workflow Orchestration

## 1. Plan Mode Default
- Enter plan mode for ANY non-trivial task (3+ steps or architectural decisions)
- If something goes sideways, STOP and re-plan immediately — don't keep pushing
- Use plan mode for verification steps, not just building
- Write detailed specs upfront to reduce ambiguity

## 2. Subagent Strategy
- Use subagents liberally to keep main context window clean
- Offload research, exploration, and parallel analysis to subagents
- For complex problems, throw more compute at it via subagents
- One task per subagent for focused execution

## 3. Self-Improvement Loop
- After ANY correction from the user: update `tasks/lessons.md` with the pattern
- Write rules for yourself that prevent the same mistake
- Ruthlessly iterate on these lessons until mistake rate drops
- Review lessons at session start for relevant project

## 4. Verification Before Done
- Never mark a task complete without proving it works
- Diff behavior between main and your changes when relevant
- Ask yourself: "Would a staff engineer approve this?"
- Run tests, check logs, demonstrate correctness

## 5. Demand Elegance (Balanced)
- For non-trivial changes: pause and ask "is there a more elegant way?"
- If a fix feels hacky: "Knowing everything I know now, implement the elegant solution"
- Skip this for simple, obvious fixes — don't over-engineer
- Challenge your own work before presenting it

## 6. Autonomous Bug Fixing
- When given a bug report: just fix it. Don't ask for hand-holding
- Point at logs, errors, failing tests — then resolve them
- Zero context switching required from the user
- Go fix failing CI tests without being told how

---

## Task Management

1. **++Plan First++:** Write plan to `tasks/todo.md` with checkable items
2. **++Verify Plans++:** Check in before starting implementation
3. **++Track Progress++:** Mark items complete as you go
4. **++Explain Changes++:** High-level summary at each step
5. **++Document Results++:** Add review section to `tasks/todo.md`
6. **++Capture Lessons++:** Update `tasks/lessons.md` after corrections

---

## Core Principles

- **++Simplicity First++:** Make every change as simple as possible. Impact minimal code.
- **++No Laziness++:** Find root causes. No temporary fixes. Senior developer standards.
- **++Minimal Impact++:** Changes should only touch what's necessary. Avoid introducing bugs.

---

## Deployment Patterns (Feb 19, 2026)

### Before Deploying a New Service

1. **Check existing services** — don't create duplicate databases
2. **Verify plan compatibility** — free/starter/individual matter
3. **Prepare environment variables** — DATABASE_URL, API keys
4. **Test locally first** — catch errors before deployment

### Railway Deployment Checklist

- [ ] Create GitHub repo with code
- [ ] Add railway.json or Dockerfile
- [ ] Create service in Railway dashboard
- [ ] Add PostgreSQL if needed
- [ ] **Manually set DATABASE_URL in Variables**
- [ ] Deploy and check logs
- [ ] Verify health endpoint

### Common Issues

| Issue | Cause | Fix |
|-------|-------|-----|
| Healthcheck fails | DATABASE_URL not set | Set in Variables tab |
| Connection to localhost | Default fallback triggered | DATABASE_URL empty or wrong |
| Cron fails | Free tier doesn't support cron | Upgrade to starter+ |
| Blueprint fails | Legacy plan names | Use "individual" for PostgreSQL |

### Post-Deployment Verification

```bash
curl https://<service>.up.railway.app/health
curl https://<service>.up.railway.app/api/products
```

Both should return 200 OK with expected data.

---

## Local Git → GitHub → Deployment Pattern

### When You Have Code But No GitHub Remote

**Problem:** Code lives in `/Users/douglasrichman/.openclaw/workspace/unified-backend/price-aggregator-api/` but no GitHub remote configured.

**Solution:**

1. **Create GitHub repo manually** (if CLI token lacks scopes):
   - Go to github.com/new
   - Repository name: `price-aggregator-api`
   - Public repo, no README

2. **Connect local code to GitHub:**
   ```bash
   cd /Users/douglasrichman/.openclaw/workspace/unified-backend/price-aggregator-api
   git remote add origin https://github.com/drichman1-maker/price-aggregator-api.git
   git branch -M master
   git push -u origin master
   ```

3. **Verify Railway/Render auto-deploy:**
   ```bash
   curl https://price-aggregator-api-production.up.railway.app/api/products
   ```

### Key Commands

| Task | Command |
|------|---------|
| Check current remotes | `git remote -v` |
| Add GitHub remote | `git remote add origin https://github.com/user/repo.git` |
| Push and link | `git push -u origin master` |
| Force push (careful!) | `git push -f origin master` |

### Common Issues

| Issue | Cause | Fix |
|-------|-------|-----|
| "origin does not exist" | No remote configured | `git remote add origin <url>` |
| Token lacks scopes | CLI token missing `public_repo` | Create repo manually in browser |
| No auto-deploy | Service not connected to GitHub | Connect in Railway/Render dashboard |
