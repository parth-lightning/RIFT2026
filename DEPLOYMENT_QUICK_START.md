# ⚡ PharmaGuard - Deployment Quick Start

Fast-track deployment in 3 steps. Choose your platforms and follow the relevant section.

---

## 🚀 FASTEST PATH: Netlify + Railway (15 minutes)

### **Pre-Requisites** (5 minutes)

```bash
# 1. Make sure everything is committed
git status

# 2. Install Netlify CLI
npm install -g netlify-cli

# 3. Have these ready:
# - GitHub account (repo pushed)
# - Railway account
# - Google Gemini API key
# - Text editor for copying URLs
```

### **Step 1: Deploy Frontend to Netlify** (5 minutes)

**Via GitHub Integration (Easiest):**

```bash
# Just push to GitHub
git add .
git commit -m "Ready for deployment"
git push origin main
```

Then:

1. Go to [app.netlify.com](https://app.netlify.com)
2. Click **"Add new site"** → **"Import an existing project"**
3. Select GitHub + authorize + select RIFT2026 repo
4. Settings:
   - **Base directory:** `frontend`
   - **Build command:** `npm install && npm run build`
   - **Publish directory:** `frontend/build`
5. Click **"Deploy"**
6. Wait 2-3 minutes
7. **Copy your Netlify URL:** `https://xxxxx.netlify.app`

💾 **Save this URL** - you'll need it for the backend!

### **Step 2: Deploy Backend to Railway** (5 minutes)

```bash
# Add deployment config files
# (If not already added)

git add Procfile runtime.txt requirements.txt
git commit -m "Add Railway config"
git push origin main
```

Then:

1. Go to [railway.app](https://railway.app)
2. Click **"New Project"** → **"GitHub Repo"**
3. Select RIFT2026 repo
4. Click **"Deploy Now"**
5. Wait for first deployment (~2-3 minutes)
6. Click service → **"Generate Domain"**
7. **Copy your Railway URL:** `https://xxxxx.up.railway.app`

### **Step 3: Connect Frontend ↔ Backend** (5 minutes)

**In Netlify Dashboard:**

1. Go to your site
2. Site Settings → **Build & deploy** → **Environment**
3. Click **"Edit variables"**
4. Add new variable:
   - **Key:** `VITE_API_URL`
   - **Value:** `https://xxxxx.up.railway.app/api` ← Your Railway URL
5. Click **"Deploy"** → **"Trigger deploy"**

**In Railway Dashboard:**

1. Go to your project
2. Click service settings
3. Add **Variable:**
   - **Key:** `CORS_ORIGINS`
   - **Value:** `["https://xxxxx.netlify.app"]` ← Your Netlify URL
4. Service auto-redeploys

### **Step 4: Test It!** ✅

```bash
# Test backend health
curl https://xxxxx.up.railway.app/api/health

# Should return:
# {"status":"ok","gemini_configured":true,...}
```

Then:

1. Open your Netlify URL in browser
2. Upload sample VCF file
3. Select drugs
4. Hit "Analyze"
5. See results! 🎉

---

## 🔧 Configuration Files Reference

### Create in root `RIFT2026/`:

**Procfile**

```
web: python -m uvicorn src.main:app --host 0.0.0.0 --port $PORT
```

**runtime.txt**

```
python-3.11.7
```

**railway.toml** (for Railway)

```toml
[build]
builder = "nixpacks"

[deploy]
startCommand = "python -m uvicorn src.main:app --host 0.0.0.0 --port $PORT"
healthcheckPath = "/api/health"
```

**frontend/.env.production** (in frontend folder)

```env
VITE_API_URL=https://your-backend-url/api
```

---

## 🆘 Quick Troubleshooting

### "Frontend shows 404"

```bash
# Verify build
cd frontend
npm run build
# Check that build/ folder has index.html
ls build/
```

### "API calls show CORS error"

1. Check backend URL in Netlify env variable exactly matches (no trailing slash)
2. Verify CORS_ORIGINS in Railway matches your Netlify URL
3. Redeploy backend after CORS change

### "Gemini API not working"

```bash
# Check Railway logs
# Click service → Logs
# Look for "GEMINI_API_KEY" errors
# Verify API key is set: Settings → Variables → Look for GEMINI_API_KEY
```

### "Build fails on Netlify"

```bash
# Check build logs
# Netlify Dashboard → Builds → Latest → Build log
# Common: missing npm install, wrong build command

# Fix: Ensure frontend/package.json has all dependencies:
cd frontend
npm install  # Run locally first
npm run build  # Should complete without errors
git add .
git push origin main  # Redeploy
```

---

## 📋 Deployment Checklist

**Before Deployment:**

- [ ] `git push origin main` completed
- [ ] No uncommitted changes (`git status` shows clean)
- [ ] All files added: Procfile, runtime.txt, requirements.txt

**After Frontend Deploy:**

- [ ] Netlify site loads without 404
- [ ] Browser console has no errors (F12)
- [ ] Netlify URL copied

**After Backend Deploy:**

- [ ] Railway shows "Running" status
- [ ] Health check passes (curl test)
- [ ] Railway URL copied

**After Connecting:**

- [ ] VITE_API_URL set in Netlify
- [ ] CORS_ORIGINS set in Railway
- [ ] Both services redeployed
- [ ] Frontend loads backend data

**Final Test:**

- [ ] Upload VCF file
- [ ] Analysis completes
- [ ] Results display
- [ ] Export works

---

## 💰 Cost Breakdown (Monthly)

| Item              | Free            | Paid            |
| ----------------- | --------------- | --------------- |
| Netlify Frontend  | ✅ $0           | -               |
| Railway Backend   | ✅ $0 (limited) | $5              |
| Google Gemini API | ✅ $0 (limited) | Variable        |
| Custom Domain     | ❌ $12/year     | -               |
| **TOTAL**         | **$0-1/month**  | **$5-10/month** |

---

## 🔐 Environment Variables Needed

### Backend (Railway/Render)

```
GEMINI_API_KEY=your-actual-key-here
CORS_ORIGINS=["https://yoursite.netlify.app"]
```

### Frontend (Netlify)

```
VITE_API_URL=https://your-backend-url.com/api
```

---

## 📊 Services at a Glance

| Service     | Cost  | Setup Time | Best For          |
| ----------- | ----- | ---------- | ----------------- |
| **Netlify** | Free  | 5 min      | Frontend React    |
| **Railway** | $5/mo | 5 min      | Backend Python    |
| **Render**  | Free  | 5 min      | Backend (no DB)   |
| **Heroku**  | Paid  | 5 min      | Advanced (legacy) |

**Recommendation: Netlify + Railway = Best value + easiest setup + best docs**

---

## 🚨 Emergency Contact Info

**Netlify:** https://support.netlify.com  
**Railway:** https://railway.app/support  
**FastAPI:** https://fastapi.tiangolo.com

**Logs Location:**

- **Netlify:** Dashboard → Deployments → Logs tab
- **Railway:** Dashboard → Service → Logs tab
- **Browser:** F12 → Console

---

## 📈 What to Do After Deployment

1. **Monitor** - Check logs daily first week
2. **Test** - Try all features on live site
3. **Share** - Post on LinkedIn! 🎉
4. **Improve** - Gather feedback, iterate
5. **Scale** - As users grow, upgrade plans

---

## ⏭️ Next Steps

1. **Deploy Now** - Follow the 4-step process above
2. **Test Everything** - Upload files, run analysis
3. **Add Custom Domain** - Optional but looks professional
4. **Setup Monitoring** - Get alerts for errors
5. **Share on LinkedIn** - Use LINKEDIN_CONTENT_GUIDE.md

---

**Version:** 1.0  
**Last Updated:** February 2026  
**Status:** Ready to Deploy

_Need more details? See DEPLOYMENT_GUIDE.md for comprehensive documentation._
