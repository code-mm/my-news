# 每日热门新闻页面

这是一个纯静态 HTML 新闻页面，配合 GitHub Actions 每天自动抓取热门分类前 30 条新闻，并发布到 GitHub Pages。

## 功能

- `index.html`：在浏览器中展示新闻。
- `scripts/fetch_news.py`：抓取 Google News RSS 的多分类新闻，每类前 30 条，生成 `data/news.json`。
- `.github/workflows/update-news.yml`：每日定时更新新闻数据。
- `.github/workflows/deploy-pages.yml`：推送到 `main` 分支后自动部署到 GitHub Pages。

## 使用步骤

1. 将仓库推送到 GitHub。
2. 进入仓库设置：
   - **Settings → Pages → Build and deployment**
   - Source 选择 **GitHub Actions**。
3. 在 **Actions** 中手动运行一次：
   - `Update News Data`（生成最新 `data/news.json`）
   - `Deploy to GitHub Pages`（首次部署）
4. 部署完成后，通过 `https://<你的用户名>.github.io/<仓库名>/` 访问。

## 本地预览

```bash
python3 scripts/fetch_news.py
python3 -m http.server 8080
# 浏览器打开 http://localhost:8080
```
