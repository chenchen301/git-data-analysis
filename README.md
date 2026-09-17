# Git 数据分析项目：学生成绩分析

这是一个用于演示 Git、Jupyter Notebook 和可复现数据分析流程的示例项目。

## 项目目标

- 使用 Git 进行版本管理。
- 使用 Jupyter Notebook 展示分析过程和结果。
- 使用 Python 对学生成绩数据进行统计分析。
- 生成可保存、可复现的分析结果和图表。

## 项目结构

```text
git-data-analysis/
├── README.md
├── requirements.txt
├── data.csv
├── analysis.py
├── analysis.ipynb
├── .gitignore
└── output/
```

## 环境要求

建议使用 Python 3.10 或更高版本。

## 安装依赖

```bash
python -m venv .venv
```

Windows：

```bash
.venv\\Scripts\\activate
```

macOS/Linux：

```bash
source .venv/bin/activate
```

安装依赖：

```bash
pip install -r requirements.txt
```

## 运行 Python 分析

```bash
python analysis.py
```

脚本会生成：

- `output/result.csv`
- `output/subject_means.png`
- `output/score_distribution.png`

## 运行 Jupyter Notebook

```bash
jupyter notebook
```

打开 `analysis.ipynb`，依次运行所有单元格即可看到数据表、统计结果和图表。

## 可复现性

数据文件固定为项目中的 `data.csv`，分析逻辑固定在 `analysis.py` 和 `analysis.ipynb` 中，依赖版本范围记录在 `requirements.txt` 中。因此其他用户克隆仓库后，可以按照上述步骤重新运行分析。

## Git 版本管理

本项目包含 Git 提交历史，并创建了发布标签：

```bash
git log --oneline
git tag
```

标签：

```text
v1.0.0
```

## 项目结果

Notebook 会展示：

1. 原始成绩数据。
2. 每名学生的总分和平均分。
3. 各科平均分、最高分和最低分。
4. 班级整体平均分。
5. 平均分最高的学生。
6. 成绩等级人数统计。
7. 各科平均成绩柱状图。
8. 学生平均分分布图。

## License

仅用于课程学习和 Git/Jupyter 实践。
