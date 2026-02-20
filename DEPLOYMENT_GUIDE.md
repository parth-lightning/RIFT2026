# 🚀 PharmaGuard - Complete Deployment Guide

## Table of Contents

1. [Overall Architecture](#overall-architecture)
2. [Creating Necessary Files](#creating-necessary-files)
3. [Frontend Deployment to Netlify](#frontend-deployment-to-netlify)
4. [Backend Deployment Options](#backend-deployment-options)
5. [Connecting Frontend & Backend](#connecting-frontend--backend)
6. [Domain & SSL Setup](#domain--ssl-setup)
7. [Monitoring & Maintenance](#monitoring--maintenance)

---

## Overall Architecture

```
┌─────────────────────────────────────────┐
│  Netlify (Frontend)                     │
│  - React/Vite static site               │
│  - CDN delivery                         │
│  - URL: yoursite.netlify.app            │
└──────────────────┬──────────────────────┘
                   │ HTTPS Request
                   ▼
┌─────────────────────────────────────────┐
│  Backend Server (Railway/Render)        │
│  - FastAPI Python application           │
│  - Database ready                       │
│  - URL: yourapi.railway.app             │
│  - Google Gemini API integration        │
└─────────────────────────────────────────┘
```

---

## Creating Necessary Files for Deployment

### 1. Create `.netlify.toml` (Frontend Configuration)

Location: `RIFT2026/.netlify.toml`

```toml
[build]
  command = "cd frontend && npm install && npm run build"
  publish = "frontend/build"
  functions = "netlify/functions"

[build.environment]
  NODE_VERSION = "18.0.0"
  NODE_ENV = "production"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200

[[headers]]
  for = "/*"
  [headers.values]
    Cache-Control = "public, max-age=0, must-revalidate"
    X-Content-Type-Options = "nosniff"
    X-Frame-Options = "DENY"
    X-XSS-Protection = "1; mode=block"

[context.production]
  environment = { NODE_ENV = "production" }
```

### 2. Create `Procfile` (Backend Configuration)

Location: `RIFT2026/Procfile`

```
web: python -m uvicorn src.main:app --host 0.0.0.0 --port $PORT
```

### 3. Create `runtime.txt` (Python Version)

Location: `RIFT2026/runtime.txt`

```
python-3.11.7
```

### 4. Create `railway.toml` (For Railway Deployment)

Location: `RIFT2026/railway.toml`

```toml
[build]
builder = "nixpacks"

[deploy]
startCommand = "python -m uvicorn src.main:app --host 0.0.0.0 --port $PORT"
healthcheckPath = "/api/health"
healthcheckTimeout = 30
```

### 5. Create `frontend/.env.production`

Location: `RIFT2026/frontend/.env.production`

```env
VITE_API_URL=https://your-backend-url.com/api
VITE_APP_NAME=PharmaGuard
```

### 6. Update `.gitignore`

Location: `RIFT2026/.gitignore`

```
# Environment files
.env
.env.local
.env.*.local

# Node
node_modules/
npm-debug.log
yarn-error.log
build/
dist/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
.venv

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Local development
.netlify/
.cache/
```

---

## Frontend Deployment to Netlify

### Method 1: GitHub Integration (Recommended)

#### Step 1: Prepare Your Repository

```bash
# Initialize git if not already done
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: PharmaGuard full-stack app"

# Add remote
git remote add origin https://github.com/YOUR-USERNAME/RIFT2026.git

# Push to GitHub
git branch -M main
git push -u origin main
```

#### Step 2: Connect to Netlify

1. **Visit [netlify.com](https://app.netlify.com/)**

2. **Sign up/Log in** with GitHub

3. **Click "Add new site"** → **"Import an existing project"**

4. **Select GitHub** and authorize Netlify

5. **Choose your RIFT2026 repository**

#### Step 3: Configure Build Settings

On Netlify's build configuration page:

```
Base directory: frontend
Build command: npm install && npm run build
Publish directory: frontend/build
```

#### Step 4: Set Environment Variables

1. Click **"Show advanced"** during deployment setup
2. Click **"New variable"** and add:

| Key            | Value                              |
| -------------- | ---------------------------------- |
| `VITE_API_URL` | `https://your-backend-url.com/api` |
| `NODE_VERSION` | `18.0.0`                           |

#### Step 5: Deploy

1. Click **"Deploy"**
2. Wait for build to complete (usually 2-3 minutes)
3. Get your Netlify URL: `https://yoursite.netlify.app`

### Method 2: Manual Upload via Netlify CLI

```bash
# Install Netlify CLI
npm install -g netlify-cli

# Login to Netlify
netlify login

# Build frontend
cd frontend
npm run build

# Deploy
cd build
netlify deploy --prod
```

### Method 3: Drag & Drop

1. Build your frontend: `cd frontend && npm run build`
2. Go to [netlify.com/drop](https://app.netlify.com/drop)
3. Drag the `frontend/build` folder
4. Wait for deployment

---

## Backend Deployment Options

### Option 1: Railway.app (Recommended ⭐)

#### Advantages:

- ✅ Easiest setup
- ✅ GitHub integration
- ✅ Free tier: $5/month PostgreSQL database included
- ✅ Auto-deploys on push
- ✅ Great Python support

#### Step-by-Step Guide:

**1. Create Railway Account**

- Visit [railway.app](https://railway.app/)
- Sign up with GitHub
- Authorize Railway to access repositories

**2. Configure GitHub for Deployment**

```bash
git add .netlify.toml Procfile runtime.txt requirements.txt
git commit -m "Add deployment configuration"
git push origin main
```

**3. Create Railway Project**

1. Go to Railway Dashboard
2. Click **"New Project"**
3. Select **"GitHub Repo"**
4. Choose your RIFT2026 repository
5. Select **"Deploy Now"**

**4. Set Environment Variables**

In Railway Dashboard → Project Settings → Variables:

```
GEMINI_API_KEY=your-actual-gemini-api-key
CORS_ORIGINS=["https://yoursite.netlify.app","http://localhost:3000"]
APP_NAME=PharmaGuard
APP_VERSION=1.0.0
SUPPORTED_DRUGS=Warfarin,Clopidogrel,Metoprolol,Simvastatin,Sertraline,Codeine
```

**5. Generate Domain**

1. In Railway, click **"Generate domain"**
2. Copy the URL (e.g., `https://pharmaguard-production.up.railway.app`)
3. Update your Netlify environment variable

**6. Test Backend**

```bash
curl https://your-railway-url/api/health
```

Should return:

```json
{
  "status": "ok",
  "gemini_configured": true,
  "supported_drugs": [...]
}
```

---

### Option 2: Render.com

#### Advantages:

- ✅ Free tier available
- ✅ Github integration
- ✅ Good uptime
- ✅ PostgreSQL database support

#### Steps:

1. **Create Render Account**
   - Visit [render.com](https://render.com/)
   - Sign up with GitHub

2. **Create Web Service**
   - Click **"New +"** → **"Web Service"**
   - Connect GitHub repository
   - Select RIFT2026 repo

3. **Configure**
   - **Name:** `pharmaguard-api`
   - **Environment:** `Python 3.11`
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `python -m uvicorn src.main:app --host 0.0.0.0 --port $PORT`

4. **Set Environment Variables**
   - Click **"Environment"** → **"Add Environment Variable"**
   - Add all variables from the Railway section above

5. **Deploy**
   - Click **"Create Web Service"**
   - Wait for deployment
   - Get your URL (e.g., `https://pharmaguard-api.onrender.com`)

---

### Option 3: Heroku (Legacy - Requires Credit Card)

Heroku no longer offers free tier, but here's how if you have credits:

```bash
# Install Heroku CLI
# macOS: brew install heroku
# Windows: Download from heroku.com/cli

# Login
heroku login

# Create app
heroku create pharmaguard-api

# Add buildpack for Python
heroku buildpacks:add heroku/python

# Set environment variables
heroku config:set GEMINI_API_KEY=your-key
heroku config:set CORS_ORIGINS='["https://yoursite.netlify.app"]'

# Deploy
git push heroku main

# View logs
heroku logs --tail

# Get URL
heroku open
```

---

### Option 4: AWS Lambda with Zappa

Most scalable but requires AWS knowledge:

```bash
pip install zappa

# Initialize Zappa
zappa init

# Deploy
zappa deploy production

# Update after changes
zappa update production

# Get URL from CloudFormation
```

---

## Connecting Frontend & Backend

### Step 1: Update Netlify Environment

1. Go to **Netlify Dashboard**
2. Select your site
3. Go to **Site Settings** → **Build & Deploy** → **Environment**
4. Add variable:

```
VITE_API_URL = https://your-backend-url/api
```

5. Trigger redeploy: **Builds** → **Trigger deploy**

### Step 2: Update Backend CORS

In your backend deployment (Railway/Render):

Set environment variable:

```
CORS_ORIGINS=["https://yoursite.netlify.app","https://www.yoursite.netlify.app"]
```

### Step 3: Test Connection

**Test 1: Health Check**

```bash
curl https://your-backend-url/api/health
```

**Test 2: Frontend Test**

1. Open your Netlify site
2. Open browser console (F12)
3. Check for CORS errors
4. Try uploading a VCF file

**Test 3: Full Analysis**

1. Upload sample VCF
2. Select drugs
3. Submit analysis
4. Verify results display

---

## Domain & SSL Setup

### Using Netlify Custom Domain

1. **Register Domain**
   - GoDaddy, Namecheap, Google Domains, etc.
   - Cost: ~$10-15/year

2. **Add to Netlify**
   - Netlify Dashboard → **Domain Settings**
   - Click **"Add custom domain"**
   - Enter your domain (e.g., `pharmaguard.io`)
   - Netlify provides DNS records

3. **Update DNS Provider**
   - Go to your domain registrar
   - Add Netlify's nameservers
   - Wait 24 hours for propagation

4. **Enable SSL**
   - Automatic on Netlify
   - Free via Let's Encrypt
   - Check **Domain Settings** → **SSL**

### Backend Custom Domain

For Railway/Render:

1. **Create CNAME record** with your DNS provider:

   ```
   Name: api
   Type: CNAME
   Value: your-railway-url
   ```

2. **Add custom domain** in Railway/Render settings
3. **Enable HTTPS** (automatic)
4. **Update frontend** with new backend URL

---

## Monitoring & Maintenance

### Frontend Monitoring (Netlify)

1. **Analytics**
   - Dashboard → **Analytics**
   - View traffic, deployment history

2. **Build Notifications**
   - Settings → **Build & deploy** → **Deploy notifications**
   - Get notified on deploy success/failure

3. **Environment Variables**
   - Regularly rotate API keys
   - Update CORS origins if backend changes

### Backend Monitoring

**Railway:**

- Dashboard → **Deployments** → View logs
- Set up monitoring alerts

**Render:**

- Logs section → Filter by date/level
- Metrics tab → CPU, memory usage

### Regular Maintenance

**Weekly:**

- Check deployment logs for errors
- Monitor API response times
- Review error messages

**Monthly:**

- Update dependencies
  ```bash
  npm update --all  # Frontend
  pip install --upgrade -r requirements.txt  # Backend
  ```
- Review usage metrics
- Test VCF file uploads

**Quarterly:**

- Update Python/Node versions
- Security audit of dependencies
- Performance optimization review

### Troubleshooting Deployments

**Problem: Frontend builds but shows 404**

- Check Netlify Publish directory: `frontend/build`
- Verify `_redirects` file exists

**Problem: API calls fail with CORS errors**

- Check backend `CORS_ORIGINS` environment variable
- Ensure frontend URL matches exactly
- Redeploy backend after CORS update

**Problem: Large VCF files cause timeout**

- Increase Railway/Render timeout settings
- Consider increasing plan for more resources
- Optimize VCF parsing in backend

**Problem: LLM explanations not generating**

- Verify `GEMINI_API_KEY` is set correctly
- Check Google Gemini API quota
- Review backend logs for API errors

---

## Cost Analysis

### Recommended Setup (Netlify + Railway)

| Service           | Cost            | Notes                           |
| ----------------- | --------------- | ------------------------------- |
| Netlify           | Free            | Frontend, 100GB/month bandwidth |
| Railway           | ~$5/month       | Backend, includes PostgreSQL    |
| Google Gemini API | Free            | Up to rate limit                |
| Custom Domain     | ~$12/year       | Optional                        |
| **Total**         | **~$5-6/month** | Or free with free tiers         |

### Alternative: Netlify + Render

| Service           | Cost          | Notes                |
| ----------------- | ------------- | -------------------- |
| Netlify           | Free          | Frontend             |
| Render            | Free          | Limited backend tier |
| Google Gemini API | Free          | Up to rate limit     |
| **Total**         | **~$0/month** | Limited features     |

---

## Deployment Checklist

Before going live:

**Frontend:**

- [ ] Build completes without errors
- [ ] All assets load correctly
- [ ] Responsive design works on mobile
- [ ] API URL is correct in environment variables
- [ ] No console errors in browser

**Backend:**

- [ ] Health check endpoint responds
- [ ] All environment variables are set
- [ ] CORS origins include frontend URL
- [ ] Google Gemini API is configured
- [ ] Log output shows healthy startup

**Integration:**

- [ ] Frontend loads successfully
- [ ] File upload shows no CORS errors
- [ ] VCF analysis completes
- [ ] Results display correctly
- [ ] Export functionality works

**Production:**

- [ ] Custom domain configured (if applicable)
- [ ] SSL/HTTPS working
- [ ] Analytics enabled
- [ ] Error notifications configured
- [ ] Monitoring set up

---

## Quick Reference Commands

```bash
# Build frontend locally
cd frontend && npm run build

# Build and deploy via Netlify CLI
npm install -g netlify-cli
netlify deploy --prod --dir frontend/build

# Test backend locally
python -m uvicorn src.main:app --reload

# Deploy backend to Railway
git push heroku main  # if using Heroku
git push origin main  # Railway auto-deploys from GitHub

# View logs
netlify logs  # Netlify logs
heroku logs --tail  # Heroku
railway logs  # Railway in dashboard
```

---

## Support & Resources

- **Netlify Docs:** https://docs.netlify.com/
- **Railway Docs:** https://docs.railway.app/
- **FastAPI Docs:** https://fastapi.tiangolo.com/deployment/
- **GitHub Actions CI/CD:** https://github.com/features/actions

---

**Last Updated:** February 2026  
**Version:** 1.0.0  
**Status:** Production Ready

_For questions or issues, refer to the main README.md and SRS_Report.md_
