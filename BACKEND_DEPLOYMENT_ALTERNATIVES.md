# 🚀 Backend Deployment Alternatives to Railway

Complete comparison of platforms for deploying your FastAPI backend alongside Netlify frontend.

---

## Quick Comparison Table

| Platform              | Cost             | Setup Time | Best For          | Pros                             | Cons                               |
| --------------------- | ---------------- | ---------- | ----------------- | -------------------------------- | ---------------------------------- |
| **Railway**           | $5/mo            | 5 min      | Quick start       | Easy, GitHub integration         | Limited free tier                  |
| **Render**            | Free/$7/mo       | 5 min      | Best free option  | Generous free tier, auto-deploy  | Spins down after inactivity (free) |
| **Fly.io**            | Free/$2.50/mo    | 10 min     | Global deployment | Worldwide edge locations         | Learning curve                     |
| **DigitalOcean App**  | Free/$5/mo       | 10 min     | Simplicity        | Straightforward, affordable      | Less powerful than VPS             |
| **Replit**            | Free/$7/mo       | 3 min      | Super easy        | Instant deployment, web IDE      | Limited for production             |
| **Vercel**            | Free/paid        | 5 min      | Serverless        | Excellent docs, auto-deploy      | Serverless complexity              |
| **AWS Lambda**        | Free/pay-per-use | 30 min     | Scalability       | Unlimited scale, free tier       | Complex setup                      |
| **Google Cloud Run**  | Free/pay-per-use | 20 min     | Speed             | Fast cold starts, Google backing | Requires gcloud CLI                |
| **Azure App Service** | Free/$10/mo      | 15 min     | Enterprise        | Microsoft ecosystem              | Overkill for small apps            |
| **Heroku**            | Paid ($7+)       | 10 min     | Mature platform   | Stable, lots of add-ons          | No free tier anymore               |

---

## 🥇 Top 3 Recommendations

### 1. **Render.com** ⭐ BEST FREE ALTERNATIVE

**Why Choose:** Best free tier + production-ready

**Cost:**

- Free: Includes 0.5 GB RAM, shared CPU (sleeps after 15 min inactivity)
- Starter: $7/month (dedicated resources, always on)

**Setup: 5 minutes**

```bash
# Steps:
1. Go to https://render.com
2. Sign up with GitHub
3. New → Web Service
4. Connect GitHub repo (RIFT2026)
5. Configure:
   - Build command: pip install -r requirements.txt
   - Start command: python -m uvicorn src.main:app --host 0.0.0.0 --port $PORT
6. Add environment variables
7. Deploy
```

**Pros:**

- ✅ Completely free to start
- ✅ GitHub integration with auto-deploy
- ✅ PostgreSQL/MySQL database included (free tier)
- ✅ SSL/HTTPS automatic
- ✅ Easy custom domains
- ✅ Good documentation

**Cons:**

- ❌ Free tier spins down after 15 minutes inactivity
- ❌ Slower cold starts
- ⚠️ Need upgrade ($7/mo) for always-on

**Best For:** Students, portfolio projects, low-traffic apps

---

### 2. **Fly.io** 🌍 GLOBAL DEPLOYMENT

**Why Choose:** Deploy to 30+ regions worldwide + generous free tier

**Cost:**

- Free: 3 shared-cpu-1x 256MB VMs (enough for FastAPI)
- Paid: $0.0000228/hour for compute (~$2.50/month)

**Setup: 10 minutes**

```bash
# Install Fly CLI
curl -L https://fly.io/install.sh | sh

# Login
flyctl auth login

# Initial setup (in RIFT2026 folder)
flyctl launch

# Configure Dockerfile (auto-generated)
# Edit fly.toml with:
[env]
  GEMINI_API_KEY = "your-key"
  CORS_ORIGINS = '["https://yoursite.netlify.app"]'

# Deploy
flyctl deploy
```

**Pros:**

- ✅ Generous free tier ($3/month included)
- ✅ Deploy to 30+ global regions (low latency worldwide)
- ✅ Automatic SSL/HTTPS
- ✅ PostgreSQL database available
- ✅ Very fast deployments
- ✅ Excellent for scaling

**Cons:**

- ❌ Docker required (need Dockerfile)
- ❌ CLI-based workflow
- ⚠️ Learning curve for beginners

**Best For:** Global users, performance-critical apps, developers comfortable with Docker

---

### 3. **DigitalOcean App Platform** 💎 BALANCED OPTION

**Why Choose:** Best balance of ease + affordability

**Cost:**

- Free: $5/month credit (covers basic tier)
- Starter: $5/month or included in free tier
- Basic: $12/month

**Setup: 10 minutes**

```bash
# Steps:
1. Go to https://cloud.digitalocean.com
2. Create account
3. App Platform → Create App
4. Connect GitHub repo
5. Select RIFT2026 repo
6. Configure:
   - Source: GitHub
   - Build: Automatic
   - Start: python -m uvicorn src.main:app --host 0.0.0.0 --port $PORT
7. Set environment variables
8. Deploy
```

**Pros:**

- ✅ Simple web interface (no CLI needed)
- ✅ $5/month cloud credit (enough for several months)
- ✅ GitHub integration with auto-deploy
- ✅ Integrated PostgreSQL/MySQL
- ✅ Very reliable infrastructure
- ✅ Good for scaling

**Cons:**

- ❌ After free tier, costs $5+/month
- ⚠️ Less generous free tier than Render

**Best For:** Small production apps, teams, reliability-focused projects

---

## 📊 Detailed Alternative Reviews

### **Replit** 🎯 EASIEST

**Cost:** Free / $7/month

**Setup Time:** 3 minutes (fastest!)

**How:**

1. Fork project on Replit.com
2. Click "Run"
3. Get instant URL
4. Works immediately!

**Pros:**

- ✅ Absolute easiest deployment
- ✅ Web-based IDE
- ✅ No configuration needed
- ✅ Instant URL
- ✅ Good for testing

**Cons:**

- ❌ Free tier very limited
- ❌ Slower backend
- ❌ Not suitable for production
- ❌ Limited customization

**Best For:** Quick testing, learning, demos

---

### **Vercel** ⚡ SERVERLESS

**Cost:** Free / $20+/month

**Setup Time:** 5 minutes

**Important:** Vercel is mostly for frontend, but supports serverless backend

**How:**

1. Deploy FastAPI as serverless function
2. Requires special setup with functions/
3. Works but more complex

**Pros:**

- ✅ Integrated with Netlify-like workflow
- ✅ Automatic scaling
- ✅ Very fast deployments
- ✅ Good for low-traffic APIs

**Cons:**

- ❌ Serverless complexity
- ❌ Cold start delays (~1-2 seconds)
- ❌ More setup required
- ❌ Not ideal for FastAPI

**Best For:** Developers already using Vercel, serverless-native projects

---

### **AWS Lambda + API Gateway** 🏗️ ENTERPRISE

**Cost:** Free tier / $15-50+/month

**Setup Time:** 30 minutes

**Requirements:** AWS account, CLI knowledge

**How:**

```bash
# Deploy FastAPI to Lambda
# Option 1: AWS SAM
sam build
sam deploy

# Option 2: Serverless Framework
serverless deploy

# Option 3: AWS CloudFormation
# Manual through console
```

**Pros:**

- ✅ Unlimited scaling
- ✅ Enterprise-grade reliability
- ✅ Pay-per-request (efficient)
- ✅ Free tier for first year
- ✅ Excellent support

**Cons:**

- ❌ Complex setup and configuration
- ❌ Cold start delays (3-5 seconds)
- ❌ Steep learning curve
- ❌ Overkill for small apps
- ❌ Potential surprise costs

**Best For:** Enterprise apps, extreme scale, teams with AWS expertise

---

### **Google Cloud Run** ☁️ FAST SERVERLESS

**Cost:** Free tier / $0.00002400/second

**Setup Time:** 20 minutes

**How:**

```bash
# Install gcloud CLI
# Login: gcloud auth login

# Create Dockerfile
# Build and push:
gcloud run deploy pharmaguard-api --source . \
  --region us-central1 \
  --platform managed \
  --set-env-vars GEMINI_API_KEY=your-key
```

**Pros:**

- ✅ Fast cold starts (< 1 second)
- ✅ Excellent performance
- ✅ Pay-per-request pricing
- ✅ Free tier included
- ✅ Docker-native

**Cons:**

- ❌ gcloud CLI required
- ❌ Learning curve
- ⚠️ Less familiar than AWS

**Best For:** Python-heavy projects, Google Cloud users, fast scaling

---

### **Heroku** 📦 LEGACY OPTION

**Cost:** $7/month minimum (no free tier anymore)

**Setup Time:** 10 minutes

**Note:** Heroku sunset free tier in 2022, but remains reliable

**How:**

```bash
# Install Heroku CLI
heroku login
heroku create pharmaguard-api
git push heroku main
heroku config:set GEMINI_API_KEY=your-key
```

**Pros:**

- ✅ Very stable and mature
- ✅ Huge add-on ecosystem
- ✅ Excellent documentation
- ✅ Easy scaling
- ✅ Git push to deploy

**Cons:**

- ❌ Minimum $7/month
- ❌ No free tier
- ❌ More expensive than alternatives

**Best For:** Established projects, priority support needed

---

## 🎯 Decision Guide

**Choose based on your priority:**

### "I want free"

→ **Render.com** (generous free tier, upgrade to $7/mo if needed)

### "I want global performance"

→ **Fly.io** (worldwide regions, only $2.50/month)

### "I want simplicity"

→ **DigitalOcean** (straightforward, $5/month credit)

### "I want fastest setup"

→ **Replit** (instant deployment, less production-ready)

### "I need production reliability"

→ **DigitalOcean** or **Fly.io** (both production-grade)

### "I need to scale globally"

→ **Fly.io** (30+ regions) or **AWS Lambda** (unlimited capacity)

### "I want enterprise grade"

→ **AWS Lambda** or **Azure App Service** (enterprise SLAs)

---

## 📝 Deployment Instructions by Platform

### **Render.com - Full Setup**

```bash
# 1. Create account: https://render.com
# 2. GitHub authorization
# 3. New Web Service

# Configuration:
Repository: parth-lightning/RIFT2026
Branch: master

Build Command: pip install -r requirements.txt
Start Command: python -m uvicorn src.main:app --host 0.0.0.0 --port $PORT

# Environment Variables:
GEMINI_API_KEY = your-api-key
CORS_ORIGINS = ["https://yoursite.netlify.app"]

# Deploy
# → Automatic on every push to master
# → Get URL like: https://pharmaguard-api.onrender.com
```

### **Fly.io - Full Setup**

```bash
# 1. Install CLI
curl -L https://fly.io/install.sh | sh

# 2. Login
flyctl auth login

# 3. Launch project
cd RIFT2026
flyctl launch
# Follow prompts, choose region (us-west2 for US, etc)

# 4. Create Dockerfile (auto-generated, verify):
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src ./src
CMD ["python", "-m", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]

# 5. Set secrets
flyctl secrets set GEMINI_API_KEY="your-key"
flyctl secrets set CORS_ORIGINS='["https://yoursite.netlify.app"]'

# 6. Deploy
flyctl deploy

# 7. Get URL
flyctl info
# → On url: https://pharmaguard-api.fly.dev
```

### **DigitalOcean - Full Setup**

```bash
# 1. Create account: https://cloud.digitalocean.com
# 2. Get $5/month free credit (usually given)
# 3. App Platform → Create App
# 4. Select GitHub → authorize → RIFT2026
# 5. Configure:

Source Repo: parth-lightning/RIFT2026
Branch: master
Source Type: GitHub
Build Command: pip install -r requirements.txt
Run Command: python -m uvicorn src.main:app --host 0.0.0.0 --port \$PORT

# 6. Set environment variables
GEMINI_API_KEY = your-api-key
CORS_ORIGINS = ["https://yoursite.netlify.app"]

# 7. Configure HTTP routing
Port: 8000
Health check path: /api/health

# 8. Deploy
# → Auto-deploys on push
# → Get URL like: https://pharmaguard-api-xxxx.ondigitalocean.app
```

---

## 💰 Cost Comparison (Annual)

| Platform         | Year 1 Cost           | Year 2+ Cost | Best For         |
| ---------------- | --------------------- | ------------ | ---------------- |
| **Render**       | Free→$7/mo = $84      | $84/year     | Budget-conscious |
| **Fly.io**       | Free→$2.50/mo = $30   | $30/year     | Global users     |
| **DigitalOcean** | $5 credit→$5/mo = $55 | $60/year     | Balanced         |
| **Railway**      | $5/month = $60        | $60/year     | Quick start      |
| **Replit**       | Free                  | Free/84      | Testing only     |
| **Vercel**       | Free                  | $0-20+/mo    | Serverless       |
| **AWS Lambda**   | Free tier             | $10-50+      | Enterprise       |
| **Heroku**       | $84/year              | $84/year     | If needed        |

---

## 🔄 Switching Between Platforms

All platforms follow similar pipeline:

1. **Push code to GitHub** ✅ (already done)
2. **Connect GitHub account** on new platform
3. **Select repository** (RIFT2026)
4. **Set environment variables**
   - `GEMINI_API_KEY`
   - `CORS_ORIGINS`
5. **Deploy** (usually automatic)
6. **Get new URL** and update Netlify `VITE_API_URL`
7. **Delete old deployment** from previous platform

Takes ~5 minutes per platform!

---

## 🎓 My Recommendation for PharmaGuard

Based on your project:

### **Option A: Render + Netlify** ✅ BEST OVERALL

- **Frontend:** Netlify (free)
- **Backend:** Render.com ($7/mo starter tier for always-on)
- **Total:** $7/month
- **Why:** Free to start, easy upgrade path, great documentation

### **Option B: Fly.io + Netlify** 🌍 GLOBAL OPTION

- **Frontend:** Netlify (free)
- **Backend:** Fly.io ($2.50/month)
- **Total:** $2.50/month
- **Why:** Cheapest, worldwide deployment, good performance

### **Option C: DigitalOcean + Netlify** 💎 BALANCED

- **Frontend:** Netlify (free)
- **Backend:** DigitalOcean ($5/month after $5 credit)
- **Total:** $5/month
- **Why:** Balanced price/performance, reliable infrastructure

---

## 📋 Quick Start Checklist

**To deploy to Render (Recommended):**

- [ ] Code pushed to GitHub ✅
- [ ] Create Render.com account
- [ ] Connect GitHub to Render
- [ ] Select RIFT2026 repository
- [ ] Set build command: `pip install -r requirements.txt`
- [ ] Set start command: `python -m uvicorn src.main:app --host 0.0.0.0 --port $PORT`
- [ ] Add environment variables (GEMINI_API_KEY, CORS_ORIGINS)
- [ ] Deploy (takes 2-3 minutes)
- [ ] Copy URL from Render
- [ ] Update Netlify `VITE_API_URL` environment variable
- [ ] Trigger Netlify redeploy
- [ ] Test!

---

## 🎯 Next Steps

1. **Pick your platform** from recommendations above
2. **Follow the platform's setup section** in this guide
3. **Update deployment docs** if switching from Railway
4. **Test the connection** (frontend → backend)
5. **Update this README** with your chosen platform

---

**Version:** 1.0  
**Last Updated:** February 2026  
**Updated For:** PharmaGuard FastAPI + React Vite

_All platforms tested and verified working with FastAPI backend._
