# PDF Table Extractor

### 📝 功能描述
这是一个基于浏览器的纯前端工具，用于从 PDF 文件中提取表格数据并转换为 Excel 格式。

### 核心技术
* **Tailwind CSS**: 用于快速构建美观的响应式 UI 界面。
* **PDF.js**: Google 维护的开源库，用于在浏览器中解析和渲染 PDF。
* **SheetJS (XLSX)**: 强大的 JavaScript 库，负责将提取的数据生成并下载为 Excel 文件。

### 如何使用
1. 在浏览器中打开 `index.html`。
2. 点击 "Choose a PDF File" 上传你的 PDF 文件。
3. 点击 "Open Editor" 进入数据处理界面。
4. 点击 "Extract Tables" 自动识别表格。
5. 确认数据无误后，点击 "Save Excel" 下载结果。
