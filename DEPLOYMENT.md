# 部署 / Deployment

## GitHub Pages

1. 在仓库 **Settings → Pages → Build and deployment** 中选择 **Source: GitHub Actions**。
2. 推送到 `main`，或在 Actions 中手动运行 **Deploy AI 0 to 1**。
3. 工作流安装依赖、生成中英内容、构建和检查，然后部署 `site/`。

公开地址：[https://leriuslei.github.io/AI-0-to-1/](https://leriuslei.github.io/AI-0-to-1/)。无需自建服务器或付费域名。工作流只使用临时的 GitHub Actions 权限，不需要填写个人令牌。

Fork 后请修改 `scripts/render_bilingual.py` 中的 `PUBLIC_URL`，以及模板和 README 中的仓库地址，再启用自己的 Pages。

## 搜索引擎

网站已生成可抓取的 HTML、页面标题与描述、canonical、双语 hreflang、WebSite 结构化数据、robots 和包含两种语言的站点地图：

- [sitemap.xml](https://leriuslei.github.io/AI-0-to-1/sitemap.xml)
- [robots.txt](https://leriuslei.github.io/AI-0-to-1/robots.txt)

站点上线后，可在 [Google Search Console](https://search.google.com/search-console) 添加网址前缀 `https://leriuslei.github.io/AI-0-to-1/`，完成其提供的所有权验证后提交 `sitemap.xml`，并检查首页网址。百度等搜索引擎使用各自站长平台。验证文件或标签应由站点维护者获取。

收录与搜索“AI 0 to 1”的排序由搜索引擎决定；配置完成不等于立即能搜到。

## English

Choose **GitHub Actions** as the Pages source, then push to `main` or run **Deploy AI 0 to 1**. The workflow builds and validates both languages and deploys `site/`, using the temporary Actions token rather than a personal access token.

For a fork, update `PUBLIC_URL` and repository links. To help discovery, verify the public URL prefix in Search Console, submit the sitemap and inspect the homepage. Ownership verification is performed by the maintainer. Indexing and ranking remain search-engine decisions.
