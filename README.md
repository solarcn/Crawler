# Novel Crawler

这是一个简单的小说爬虫脚本，基于 `requests` + `BeautifulSoup`，从小说章节页递归抓取内容并保存为本地 `txt`。

## 依赖

- Python 3.8+
- requests
- beautifulsoup4
- html5lib

## 安装依赖

建议使用虚拟环境：

```powershell
python -m venv .venv
& .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 运行步骤

1. 进入项目目录（改成你本地的路径）：
   ```powershell
   cd "<你的工程路径>"
   # 例如：cd "C:\Users\<你的用户名>\OneDrive\文档\Crawler"
   ```
2. 激活虚拟环境（如尚未激活）：
   ```powershell
   & .venv\Scripts\Activate.ps1
   ```
3. 运行脚本：
   ```powershell
   python novel.py
   ```
4. 按提示输入：
   - 网址（起始章节 URL）
   - 保存文件名（默认 `novel_temp.txt`）

5. 程序循环抓取当前页面内容并自动获取下一页（通过 `getGeneticNextPage.py` 函数），直到不再是有效的 `http` 链接或与当前页相同。

## 示例网址

- http://www.81xsw.com/0_169/10088024.html
- http://www.biquke.com/xxx

（请根据目标网站调整链接，建议只使用允许抓取的站点）

## 输出路径

默认保存在当前目录下，文件名由你输入或使用默认 `novel_temp.txt`。你可以用相对路径或绝对路径：

- `novel_temp.txt`
- `output\my_novel.txt`
- `C:\Users\Lei\OneDrive\文档\Crawler\result.txt`

## 注意

- 可能存在反爬机制。请遵守网站协议权利，适当加延迟（当前脚本已经 `time.sleep(1)`）。
- 若遇到 `ModuleNotFoundError: No module named 'bs4'`，请确认已安装 dependency。
