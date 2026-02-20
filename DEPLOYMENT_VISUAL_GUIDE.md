# 🖼️ PharmaGuard - Visual Deployment Step-by-Step Guide

Complete walkthrough with exact clicks, buttons, and field values.

---

## PART 1: Prepare Your Code (10 minutes)

### Step 1.1: Clean Up and Commit

```bash
# Terminal at RIFT2026 root

# See what's not committed
git status

# Add everything
git add .

# Commit with message
git commit -m "Deployment ready: PharmaGuard v1.0"

# Push to GitHub
git push origin main

# Verify on GitHub - open https://github.com/YOUR-USERNAME/RIFT2026
# Should see all files there
```

### Step 1.2: Create Procfile

**Create new file: `RIFT2026/Procfile` (NO EXTENSION)**

```
web: python -m uvicorn src.main:app --host 0.0.0.0 --port $PORT
```

```bash
# Add to git
git add Procfile
git commit -m "Add Procfile for Railway deployment"
git push origin main
```

### Step 1.3: Create runtime.txt

**Create new file: `RIFT2026/runtime.txt`**

```
python-3.11.7
```

```bash
git add runtime.txt
git commit -m "Add Python version specification"
git push origin main
```

### Step 1.4: Create railway.toml

**Create new file: `RIFT2026/railway.toml`**

```toml
[build]
builder = "nixpacks"

[deploy]
startCommand = "python -m uvicorn src.main:app --host 0.0.0.0 --port $PORT"
healthcheckPath = "/api/health"
healthcheckTimeout = 30
```

```bash
git add railway.toml
git commit -m "Add Railway configuration"
git push origin main
```

### Step 1.5: Create Frontend Environment

**Create new file: `RIFT2026/frontend/.env.production`**

```env
VITE_API_URL=https://PLACEHOLDER-REPLACE-LATER.com/api
VITE_APP_NAME=PharmaGuard
```

```bash
git add frontend/.env.production
git commit -m "Add production environment config"
git push origin main
```

✅ **All config files pushed to GitHub**

---

## PART 2: Deploy Frontend to Netlify (10-15 minutes)

### Step 2.1: Open Netlify

1. Open browser → Go to **https://app.netlify.com**
2. See options:
   - If new account: **"Sign up"** with GitHub
   - If existing account: **"Log in"** with GitHub

### Step 2.2: Authorize GitHub

1. Click **"Authorize Netlify by Netlify"**
2. GitHub popup appears
3. Click **"Authorize"** in popup
4. You're logged in to Netlify

### Step 2.3: Create New Site

1. See **"Start from Git"** button or **"Add new site"**
2. Click it
3. Select **"Import an existing project"**
4. Click **"GitHub"** option

### Step 2.4: Select Repository

1. See list of your GitHub repos
2. Find **"RIFT2026"** in the list
3. Click it
4. See confirmation

### Step 2.5: Configure Build Settings

**You see screen with build settings:**

```
┌─────────────────────────────────────┐
│ Basic build settings                │
├─────────────────────────────────────┤
│ Owner: [your-username]              │
│ Repository: RIFT2026                │
│ Branch to deploy: main              │
│                                     │
│ BASE DIRECTORY: [_____frontend____] │
│ BUILD COMMAND: [npm install && npm  │
│                npm run build______] │
│ PUBLISH DIRECTORY: [frontend/build] │
│                                     │
│ ☐ Show advanced                    │
└─────────────────────────────────────┘
```

**Fill in exactly:**

- **Base directory:** `frontend`
- **Build command:** `npm install && npm run build`
- **Publish directory:** `frontend/build`

### Step 2.6: Click "Show Advanced"

Check this box ☑ **"Show advanced"**

Scroll down and find **"Add environment variables"**

### Step 2.7: Add Environment Variables

For each variable, click **"+ Add variable"**:

**Variable 1:**

- **Key:** `VITE_API_URL`
- **Value:** `https://PLACEHOLDER.com/api` (we'll update this later)

**Variable 2:**

- **Key:** `NODE_VERSION`
- **Value:** `18.0.0`

**Variable 3:**

- **Key:** `NODE_ENV`
- **Value:** `production`

### Step 2.8: Deploy

1. Click big **"Deploy site"** button
2. See screen: **"Building and deploying..."**
3. Wait 2-3 minutes
4. See "Site is live!" ✅

### Step 2.9: Get Your URL

1. You see section:
   ```
   Production deploys
   ├─ Status: Published ✅
   └─ Domain: https://xxxxx.netlify.app
   ```
2. Click on the domain → Opens your live site
3. **COPY THIS URL** (without https://)
   ```
   Example: yourproject.netlify.app
   ```

📌 **SAVE THIS URL - YOU NEED IT SOON!**

### Step 2.10: Test Frontend

1. Your site should load
2. You see: Upload form, empty for now
3. Press F12 (Developer Tools)
4. See errors about `/api/analyze` → That's OK, backend not live yet
5. Close F12

✅ **Frontend is LIVE!**

---

## PART 3: Deploy Backend to Railway (10-15 minutes)

### Step 3.1: Open Railway

1. Open browser → Go to **https://railway.app**
2. Click **"Dashboard"** or **"Start"**

### Step 3.2: Login with GitHub

1. Click **"Login with GitHub"**
2. GitHub popup appears
3. Click **"Authorize railway-app"**
4. Redirects to Railway dashboard

### Step 3.3: Create New Project

1. See dashboard with:
   - **"New Project"** button
   - **"Templates"** section
2. Click **"New Project"**

### Step 3.4: Choose Deployment Method

You see options:

- **"GitHub Repo"** ← Choose this
- "Deploy from Repo"

Click **"GitHub Repo"**

### Step 3.5: Select Your Repository

1. Railway asks: **"Which repo do you want to deploy?"**
2. See list of your GitHub repos
3. Find **"RIFT2026"** (or search)
4. Click it to select
5. Click **"Deploy Now"**

### Step 3.6: Wait for Deployment

You see:

```
Status: Building...
  % Complete: ████░░░░░░ 40%
  Building from Procfile...
```

Wait 2-3 minutes until it says:

```
Status: Running ✅
Service is healthy
```

### Step 3.7: Get Backend URL

1. See service details on left
2. Click service name (probably "RIFT2026" or main service)
3. See **"Generate Domain"** or **"Public URL"** button
4. Click it
5. You get URL like: `https://xxxxx.up.railway.app`

**COPY THIS URL**

### Step 3.8: Set Environment Variables

1. In Railway service details
2. Click **"Variables"** tab
3. See empty table with **"Add"** button
4. Click **"Add"** and fill:

| Key              | Value                              |
| ---------------- | ---------------------------------- |
| `GEMINI_API_KEY` | `your-actual-key-from-google`      |
| `CORS_ORIGINS`   | `["https://yoursite.netlify.app"]` |
| `APP_NAME`       | `PharmaGuard`                      |

**For CORS_ORIGINS:** Use the Netlify URL you saved in Step 2.9

After each variable, press Enter or click Add

5. Service auto-redeploys (~2 minutes)
6. Wait until status shows **"Running"** ✅

### Step 3.9: Test Backend

```bash
# In terminal, run:
curl https://YOUR-RAILWAY-URL/api/health

# Should see response like:
# {"status":"ok","gemini_configured":true,"supported_drugs":[...]}
```

If you see that ✅ → Backend is working!

📌 **SAVE THIS URL - YOU NEED IT NEXT!**

✅ **Backend is LIVE!**

---

## PART 4: Connect Frontend to Backend (5 minutes)

### Step 4.1: Update Netlify Environment Variable

You set `VITE_API_URL` to placeholder earlier. Now update it:

**In Netlify Dashboard:**

1. Click your site name at top
2. Left menu → Click **"Site settings"**
3. See sections
4. Find **"Build & deploy"** → Click **"Environment"**
5. See your variables:

   ```
   VITE_API_URL = https://PLACEHOLDER.com/api
   CORS_ORIGINS = [...]
   NODE_VERSION = 18.0.0
   ```

6. Click on `VITE_API_URL` variable
7. Click **"Edit"** icon (pencil)
8. Replace value with your Railway URL:
   ```
   https://xxxxx.up.railway.app/api
   ```
9. Click **"Save"**

### Step 4.2: Trigger Netlify Redeploy

1. Go back to main site dashboard
2. Click **"Builds"** on left menu
3. Click **"Trigger deploy"** button
4. Select **"Deploy site"**
5. Wait for green checkmark ✅

### Step 4.3: Test the Connection

**Open your Netlify site URL in browser**

1. You see the PharmaGuard app
2. Open F12 (Developer Tools)
3. Console tab
4. Should see NO CORS errors
5. Upload a test VCF file
6. Select drugs (like Warfarin)
7. Click **"Analyze"**
8. Wait ~10 seconds
9. See results!

If you see results ✅ → **Everything works!**

💾 **Save these URLs for later:**

- Frontend: `https://yoursite.netlify.app`
- Backend: `https://xxxxx.up.railway.app`

---

## PART 5: Final Verification (5 minutes)

### Checklist - Mark each as you verify ✅

**Frontend (Netlify):**

- [ ] Site loads at https://yoursite.netlify.app
- [ ] No 404 errors
- [ ] UI looks correct
- [ ] Upload button visible
- [ ] F12 console shows no CORS errors

**Backend (Railway):**

- [ ] Health check returns 200 status
- [ ] Running status in Railway dashboard
- [ ] All environment variables set
- [ ] No error messages in logs

**Integration:**

- [ ] Upload VCF file in frontend
- [ ] Analysis processes successfully
- [ ] Results display on screen
- [ ] No loading errors
- [ ] Export button works

**Production Ready:**

- [ ] Both services marked "Running"
- [ ] No bandwidth warnings
- [ ] Error logs clear
- [ ] At least one successful analysis test

If all ✅ → **You're live!**

---

## Common Issues & Fixes

### Issue: Frontend shows "Cannot connect to server"

**Fix:**

1. Netlify Dashboard → Site settings → Build & deploy → Environment
2. Check `VITE_API_URL` value
3. Should be: `https://xxxxx.up.railway.app/api` (with /api)
4. No trailing slash
5. Click **"Trigger deploy"** → **"Deploy site"**
6. Wait 2 minutes
7. Try again

### Issue: "CORS error" in browser console (F12)

**Fix:**

1. Railway dashboard → Service settings → Variables
2. Find `CORS_ORIGINS`
3. Should be: `["https://yoursite.netlify.app"]` (exact domain)
4. No trailing slash
5. Click Save (auto-redeploys)
6. Wait 2 minutes
7. Refresh browser (Ctrl+Shift+R for hard refresh)
8. Try upload again

### Issue: Analysis button clicks but nothing happens

**Fix:**

1. Railway dashboard → Click service → Logs tab
2. Look for red errors
3. Common: `"GEMINI_API_KEY not set"`
   - Go to Variables
   - Add it properly
   - Click Save
4. Or: `"API timeout"`
   - Contact Railway support
   - Upgrade plan

### Issue: "Cannot POST /api/analyze"

**Fix:**

1. Backend might not be running
2. Railway dashboard → Check status
3. Should say "Running"
4. If says "Deploying": wait
5. If says "Error": click service → Logs → see error
6. Common: Python version mismatch
   - Check runtime.txt = python-3.11.7
   - Rebuild with **"Force redeploy"**

### Issue: Frontend build fails on Netlify

**Fix:**

1. Netlify Builds tab → Click failed build → Show details
2. Look for error message
3. Common: `"npm ERR! 404"`
   - Missing dependency
   - Solution: `cd frontend && npm install` locally
   - Verify it builds: `npm run build`
   - `git add .` and `git push origin main`
   - Trigger deploy again

---

## 🎯 You're Done!

You now have:

- ✅ Frontend live at https://yoursite.netlify.app
- ✅ Backend live at https://xxxxx.up.railway.app
- ✅ Both connected and working
- ✅ Production-ready app

### Next Steps:

1. **Test thoroughly**
   - Try different VCF files
   - Test all drug combinations
   - Verify analysis accuracy

2. **Share on LinkedIn**
   - See LINKEDIN_CONTENT_GUIDE.md
   - Use deployment URL in post
   - Tag the live app

3. **Monitor**
   - Railway dashboard daily
   - Check for errors
   - Review logs weekly

4. **Scale** (if getting traffic)
   - Upgrade Railway plan
   - Add custom domain
   - Enable monitoring

---

**Version:** 1.0  
**Last Updated:** February 2026  
**Difficulty:** Beginner Friendly  
**Time to Complete:** ~1 hour

_Questions? See DEPLOYMENT_GUIDE.md for detailed explanations._
