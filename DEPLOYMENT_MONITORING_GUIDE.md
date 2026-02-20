# 📊 PharmaGuard - Post-Deployment Monitoring & Maintenance

Complete guide to keep your live application healthy, secure, and performant.

---

## Table of Contents

1. [Daily Monitoring](#daily-monitoring)
2. [Weekly Maintenance](#weekly-maintenance)
3. [Monthly Tasks](#monthly-tasks)
4. [Quarterly Reviews](#quarterly-reviews)
5. [Error Handling & Logs](#error-handling--logs)
6. [Performance Optimization](#performance-optimization)
7. [Security Checklist](#security-checklist)
8. [Scaling Guide](#scaling-guide)

---

## Daily Monitoring

### Morning Check (5 minutes)

```bash
# Check if services are running:

# Frontend health:
curl https://yoursite.netlify.app

# Backend health:
curl https://your-backend-url/api/health
```

**Should return:**

- Frontend: HTML page loads (status 200)
- Backend: JSON with `"status": "ok"`

### Netlify Dashboard Check

1. Go to **https://app.netlify.com**
2. Click your site
3. Check:
   - ✅ **Deployments:** Latest shows "Published"
   - ✅ **Analytics:** Traffic is normal (no sudden drops)
   - ✅ **Build:** No recent failed builds
   - ✅ **Performance:** No errors reported

### Railway Dashboard Check

1. Go to **https://railway.app**
2. Click your project
3. Check:
   - ✅ **Status:** Service says "Running" (green)
   - ✅ **CPU:** Below 50%
   - ✅ **Memory:** Below 70%
   - ✅ **No recent errors** in Logs

### Quick Test

1. **Open your site:** https://yoursite.netlify.app
2. **Test upload:** Select sample VCF file
3. **Test analysis:** Pick 1-2 drugs
4. **Verify:** Results appear within 30 seconds
5. **Check console:** F12 → Console tab → No red errors

**If anything looks wrong:** See [Error Handling & Logs](#error-handling--logs)

---

## Weekly Maintenance

### Every Monday (30 minutes)

#### 1. Review Logs

**Railway Logs:**

1. Dashboard → Service → **Logs**
2. Filter by **Last 7 days**
3. Look for RED entries
4. If found: Click to see full error message
5. Check if repeated (error pattern = problem)

**Netlify Logs:**

1. Dashboard → Site → **Deploys**
2. Click each deploy from past week
3. See "Build log"
4. Look for YELLOW/RED warnings

**Document any issues found:**

```
Date: YYYY-MM-DD
Issue: [Description]
Frequency: [Once / Multiple times / Recurring daily]
Impact: [None / Minor / Blocking]
Action: [Ignore / Investigate / Fix]
```

#### 2. Performance Check

**Netlify Analytics:**

1. Click **"Analytics"** tab
2. Review metrics:
   - Total requests (should be consistent)
   - Bandwidth used
   - Error rate (should be <1%)
   - Average response time

**Railway Metrics:**

1. Click **"Metrics"** tab
2. Review past 7 days:
   - CPU usage (trend)
   - Memory usage (trend)
   - Network in/out
   - Status uptime (should be 99%+)

#### 3. Update Dependency Status

```bash
# Check for outdated packages locally:

# Frontend
cd frontend
npm outdated

# Backend
pip list --outdated

# Document findings:
# Can update if patch version only (e.g., 1.0.0 → 1.0.5)
# Test before deploying to production
```

#### 4. Security Check

- [ ] Check if any security bulletins for:
  - React (https://github.com/facebook/react/security/advisories)
  - FastAPI (https://github.com/tiangolo/fastapi/security/advisories)
  - Google Gemini API (check Google Cloud console)

- [ ] Verify API keys have not been exposed
  - Check GitHub commit history for accidental key pushes
  - If exposed: Immediately rotate in Cloud Console

#### 5. User Feedback Review (if applicable)

- [ ] Check email for complaints
- [ ] Review GitHub issues (if public)
- [ ] Monitor social media mentions
- [ ] Document patterns for next release

---

## Monthly Maintenance

### First Day of Month (1 hour)

#### 1. Full System Health Check

**Netlify:**

```
[ ] Last 30 deployments all successful
[ ] No error rate spike
[ ] Bandwidth still within limits
[ ] Build time consistent (~3 minutes)
```

**Railway:**

```
[ ] Uptime = 99%+
[ ] No OOM (Out of Memory) errors
[ ] CPU never exceeds 80%
[ ] No repeated timeout errors
```

#### 2. Dependency Updates (Safe Version)

Only update PATCH versions (x.y.Z changes) on production:

```bash
# Frontend
cd frontend
npm update  # Updates patch versions only

# Test locally
npm run build
# Verify no build errors

# If OK, commit and push
git add package-lock.json
git commit -m "Update dependencies - patch versions"
git push origin main
```

**Wait 5 minutes for Netlify to redeploy**

```bash
# Test after deploy
curl https://yoursite.netlify.app
```

```bash
# Backend
pip install --upgrade $(pip list --outdated | awk '{print $1}' | grep -v Django)

# OR safer: manually update one at a time
pip install --upgrade requests  # example
pip install --upgrade fastapi
# etc.

# Test
python -m uvicorn src.main:app --reload
# Try some test requests

# If OK:
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update dependencies - patch versions"
git push origin main
```

**Wait for Railway to redeploy**

#### 3. Cost Analysis

| Service    | Expected | Alert if > |
| ---------- | -------- | ---------- |
| Netlify    | $0       | N/A        |
| Railway    | $5       | $15        |
| Gemini API | $0-5     | $20        |

**Check:**

1. **Netlify:** Dashboard → **Plan** section
2. **Railway:** Dashboard → **Billing** → **Statements**
3. **Google Cloud:** Console → **Billing**

If costs increasing unexpectedly:

- Contact support
- Check for bots hitting API
- Review if traffic increased

#### 4. Backup Check (if using database)

```bash
# If you add database later:
# Ensure automatic backups are enabled
# For Railway PostgreSQL: enabled by default
# For Render: check backup settings

# Test restore procedure once per month
# (Don't actually restore, just verify you CAN)
```

#### 5. Documentation Update

- [ ] Update README with latest API examples
- [ ] Update deployment guide if procedures changed
- [ ] Update feature list if new features added
- [ ] Update known issues section

---

## Quarterly Reviews

### Every 3 Months (2-3 hours)

#### 1. Full Load Testing

```bash
# Create script to simulate traffic:

#!/bin/bash
# test_load.sh

for i in {1..100}; do
  curl https://yoursite.netlify.app &
done
wait

# Run this and monitor:
# - Railway CPU/Memory during test
# - Response times
# - Any errors in logs
```

#### 2. Feature & Performance Report

Create a summary document:

```markdown
## Quarter Q1 2026 Performance Report

### Traffic

- Total requests: X million
- Peak daily users: Y
- Average response time: Z ms

### Uptime

- Netlify: 99.9%
- Railway: 99.97%
- API: 99.95%

### Issues

- [Issue 1]: Impact - Resolution
- [Issue 2]: Impact - Resolution

### Changes Made

- [Update 1]: Date and impact
- [Update 2]: Date and impact

### Next Steps

- [ ] Implement feature X
- [ ] Optimize feature Y
- [ ] Scale infrastructure
```

#### 3. Major Dependency Updates

Review what can be updated to MINOR or MAJOR versions:

```bash
# Frontend (test on separate branch first)
git checkout -b update/dependencies
cd frontend
npm install react@latest
npm install fastapi-equivalent-libs-latest  # if any
npm run build
# Test thoroughly
# Push to GitHub
# Create Pull Request
# After testing: merge to main
```

#### 4. Infrastructure Review

**Questions to ask:**

- [ ] Is Railway's free tier enough or should we upgrade?
- [ ] Do we need database integration?
- [ ] Should we add caching?
- [ ] Should we migrate to containerized setup (Docker)?
- [ ] Is there unused code to clean up?
- [ ] Are there performance bottlenecks?

#### 5. Security Audit

```bash
# Check for known vulnerabilities:

# Frontend
cd frontend
npm audit

# Backend
pip-audit  # pip install pip-audit first

# Fix any issues found
npm audit fix
```

#### 6. User Analytics (if applicable)

- [ ] Review most used features
- [ ] Check VCF file sizes (optimize parsing if huge)
- [ ] Monitor drug selection frequency
- [ ] Identify confused users (support requests)
- [ ] Plan next version improvements

---

## Error Handling & Logs

### Where to Find Logs

**Frontend Errors (Browser):**

1. Open site at https://yoursite.netlify.app
2. Press **F12** → **Console** tab
3. Red entries = errors
4. Click on error to see details
5. Common errors:
   - `CORS error` → Backend URL wrong
   - `404 /api/analyze` → Backend down
   - `SyntaxError` → Build issue

**Frontend Build Errors (Netlify):**

1. Dashboard → **Deploys**
2. Click failed deploy
3. Click **"Logs"** at bottom
4. Shows build-time errors
5. Usually: missing dependency, wrong build command

**Backend Errors (Railway):**

1. Dashboard → Service → **Logs**
2. Recent logs at top
3. Red entries = errors
4. Common errors:
   - `ModuleNotFoundError` → Missing dependency
   - `GEMINI_API_KEY not found` → Env var not set
   - `Port already in use` → Conflict
   - `CORS blocked` → Origin not allowed

**Backend Errors (Python):**

```bash
# Run locally to test:
python -m uvicorn src.main:app --reload

# Watch for errors in terminal
# Press Ctrl+C to stop

# Common issues:
# - SyntaxError: something in Python file
# - ImportError: missing package
# - ConnectionError: database/API unreachable
```

### How to Debug

**Step 1: Identify the Error**

- What service? (Frontend or Backend)
- What file? (specific endpoint or feature)
- When? (specific action that caused it)

**Step 2: Check Logs**

- Go to appropriate logs (see above)
- Look for timestamp matching when error occurred
- Read full error message (may span multiple lines)

**Step 3: Common Quick Fixes**

| Error                          | Usual Cause               | Fix                              |
| ------------------------------ | ------------------------- | -------------------------------- |
| `Cannot connect to server`     | Backend URL wrong         | Update VITE_API_URL in Netlify   |
| `CORS error`                   | Backend rejecting request | Update CORS_ORIGINS in Railway   |
| `GEMINI_API_KEY undefined`     | Not set in Railway        | Add to Variables, redeploy       |
| `TypeError: data is undefined` | API returned wrong format | Check backend response structure |
| `Failed to upload file`        | File too large            | VCF files should be <50MB        |
| `Analysis timeout`             | Server taking too long    | Increase timeout or upgrade plan |

**Step 4: Escalate if Needed**

- Check status pages: https://www.netlify.com/status, https://railway.app/status
- Contact support if service is down
- Check GitHub issues if it's a library issue

---

## Performance Optimization

### Monitor Page Speed

**Use Netlify Analytics:**

1. Dashboard → **Analytics**
2. Look at **Performance** metrics
3. Track over time

**Use External Tools:**

```bash
# Test from command line:
curl -w "@curl_format.txt" -o /dev/null -s https://yoursite.netlify.app

# Or use online tools:
# - https://pagespeed.web.dev/
# - https://www.webpagetest.org/
```

### Common Performance Issues & Fixes

| Issue         | Symptom                            | Solution                                                   |
| ------------- | ---------------------------------- | ---------------------------------------------------------- |
| Slow API      | Analysis takes >30s                | Check Railway CPU usage; upgrade if needed                 |
| Large bundle  | Frontend loads slowly              | Remove unused dependencies: `npm audit`                    |
| Memory leak   | Browser uses more memory over time | Check for console errors; look for setInterval not cleared |
| Database slow | Queries take long                  | Not used in v1.0, but prepare for v2.0                     |

### Optimization Tips

```javascript
// Frontend optimization
// 1. Code splitting (already in Vite)
// 2. Lazy loading for components
// 3. Image optimization (if added)
// 4. CSS optimization (Tailwind already minimal)

// 4. Cache API responses
const cache = new Map();
async function analyzeWithCache(data) {
  const key = JSON.stringify(data);
  if (cache.has(key)) return cache.get(key);

  const result = await fetch("/api/analyze", {
    method: "POST",
    body: JSON.stringify(data),
  });
  cache.set(key, result);
  return result;
}
```

```python
# Backend optimization
# 1. Use caching decorators
from functools import lru_cache

@lru_cache(maxsize=100)
def parse_vcf_file(file_path):
    # Only compute once per unique file
    ...

# 2. Async operations
import asyncio

async def analyze_concurrent(drugs):
    # Process multiple drugs in parallel
    ...

# 3. Connection pooling
# (automatic in FastAPI + SQLAlchemy if DB added)
```

---

## Security Checklist

### Monthly Security Review

- [ ] **API Keys**
  - GEMINI_API_KEY securely stored in Railway variables (not in code)
  - No keys in git history
  - Rotate keys quarter-annually
  - Monitor key usage in Google Cloud Console

- [ ] **CORS Configuration**
  - Only allowing your Netlify domain
  - No wildcard `*` origins in production
  - Review if expanding to other domains

- [ ] **Dependencies**

  ```bash
  npm audit
  pip-audit
  ```

  - Update if vulnerabilities found
  - Review changelogs before updating

- [ ] **Environment Variables**
  - Never commit `.env` files
  - All production variables in Railway, never in code
  - Review what variables are actually needed

- [ ] **Database** (when added in v2.0)
  - Use SSL connections
  - Never commit database credentials
  - Enable backups and test restore

### Quarterly Security Audit

1. **Review Access**
   - Who has Railway dashboard access
   - Who has Netlify dashboard access
   - Revoke unnecessary access

2. **Check for Data Leaks**
   - GitHub history: `git log --all --full-history --source -- <file>`
   - Netlify logs: Any sensitive data in build logs
   - Railway logs: Any secrets exposed

3. **SSL/TLS Status**

   ```bash
   # Check certificate
   openssl s_client -connect yoursite.netlify.app:443 | grep -A 2 "Certificate"
   ```

4. **Rate Limiting**
   - Consider adding rate limits if API gets abused
   - Monitor for suspicious patterns
   - Block if detected

### Security Best Practices

```python
# Backend examples:

# 1. Input validation (already done with Pydantic)
from pydantic import BaseModel, validator

class AnalysisRequest(BaseModel):
    patient_history: dict
    selected_drugs: list[str]

    @validator('selected_drugs')
    def validate_drugs(cls, v):
        allowed = ['Warfarin', 'Clopidogrel', ...]
        if not all(drug in allowed for drug in v):
            raise ValueError('Invalid drug')
        return v

# 2. Auth (for v2.0 with user accounts)
from fastapi.security import HTTPBearer

security = HTTPBearer()

@app.post("/api/analyze")
async def analyze(data, credentials = Depends(security)):
    # Verify user
    # Log request
    # Rate limit per user
    ...

# 3. Logging important events
import logging
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

logger.warning(f"Invalid VCF uploaded from {ip_address}")
```

---

## Scaling Guide

### Know When to Scale

**Scale when:**

- Railway CPU consistently >80%
- Response time increasing
- Getting 404 errors on upload
- Users complaining about slowness
- Traffic increasing month-over-month

**Monitor these metrics:**

```
Daily active users: [Current: __]
API requests per day: [Current: __]
Avg response time: [Current: __ ms]
Error rate: [Current: __%]
Uptime: [Current: ___%]
```

### Scaling Steps

**Step 1: Increase Railway Plan**

```bash
# Current: Free $5/month tier
# Options:
# - Starter: $5/month (current)
# - Pro: $12/month (2x resources)
# - Business: Custom pricing

# To upgrade:
1. Railway Dashboard → Logs
2. Click "..." menu → Billing
3. Click current plan
4. Select new plan
5. Click "Upgrade"
```

**Step 2: Add Caching Layer** (if data repeated)

```python
# Add Redis caching
# pip install redis-py
# Railway automatically provides Redis

import redis
cache = redis.Redis(host='localhost', port=6379)

@app.post("/api/analyze")
async def analyze(data):
    cache_key = hash(json.dumps(data))

    # Check cache first
    cached = cache.get(cache_key)
    if cached:
        return json.loads(cached)

    # Compute if not cached
    result = compute_analysis(data)
    cache.set(cache_key, json.dumps(result), ex=3600)  # 1 hour expiry
    return result
```

**Step 3: Database Integration** (when data persistence needed)

```python
# Add PostgreSQL
# Railway provides free PostgreSQL in Starter plan

# pip install sqlalchemy psycopg2-binary

from sqlalchemy import create_engine

DATABASE_URL = "postgresql://user:password@host/dbname"
engine = create_engine(DATABASE_URL)

# Now you can store results
class AnalysisResult(Base):
    user_id: int
    analysis_date: datetime
    results: json
```

**Step 4: CDN for Frontend** (if images/media added)

Already using Netlify CDN for free, but can add:

```bash
# CloudFlare CDN (free tier)
# For custom domain, add CloudFlare nameservers
# Enables edge caching globally
```

**Step 5: Load Balancing** (if traffic very high)

```bash
# Not needed until thousands of concurrent users
# Railway handles auto-scaling for you
# No action needed until critical scale
```

---

## Maintenance Schedule Template

Print and use this weekly:

```
WEEK BEGINNING: ________________

☐ DAILY CHECKS
  ☐ Frontend loads (curl test)
  ☐ Backend health check (curl test)
  ☐ Netlify dashboard - no errors
  ☐ Railway dashboard - running status
  ☐ Test file upload and analysis
  ☐ Check browser console for errors

☐ WEEKLY CHECKS (Monday)
  ☐ Review Netlify build logs
  ☐ Review Railway service logs
  ☐ Check for errors/warnings
  ☐ Verify performance metrics
  ☐ Document any issues found
  ☐ Email to self if issues: [NOTES]

ISSUES FOUND:
_________________________________
_________________________________
_________________________________

ACTIONS TAKEN:
_________________________________
_________________________________
_________________________________

NEXT WEEK FOLLOW-UP:
_________________________________
_________________________________
```

---

## Support Contacts & Resources

**Service Dashboards:**

- Netlify: https://app.netlify.com
- Railway: https://railway.app
- Google Cloud: https://console.cloud.google.com

**Documentation:**

- Netlify Docs: https://docs.netlify.com
- Railway Docs: https://docs.railway.app
- FastAPI Docs: https://fastapi.tiangolo.com

**Getting Help:**

- Netlify Support: https://support.netlify.com
- Railway Community: https://discord.gg/railway
- FastAPI Discussions: https://github.com/tiangolo/fastapi/discussions

---

**Version:** 1.0  
**Last Updated:** February 2026  
**Review Schedule:** Weekly check-ins, monthly deep-dive

_This guide ensures your production application stays healthy and performant._
