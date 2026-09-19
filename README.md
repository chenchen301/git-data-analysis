# FXI（凝血因子XI）数据分析项目

## 1. 项目简介

本项目以凝血因子 XI（Factor XI，FXI）为主题，使用 Python、Pandas、Matplotlib 和 Jupyter Notebook 对整理后的教学数据进行简单分析。

项目主要介绍 FXI 的结构、凝血功能、FXI 缺乏以及相关研究方向，并通过统计图展示不同主题资料的数量。

> 注意：项目中的 data.csv 是为了完成数据分析作业而整理的教学数据，不代表真实患者数据，也不能用于临床诊断。

## 2. 学习目标

- 了解 FXI 的基本生物学信息。
- 学习使用 Pandas 读取 CSV 数据。
- 学习进行简单的数据分组和统计。
- 使用 Matplotlib 绘制柱状图。
- 使用 Jupyter Notebook 展示分析过程。
- 使用 Git 进行版本管理。

## 3. 项目结构

```text
fxi-analysis/
├── README.md
├── analysis.ipynb
├── analysis.py
├── data.csv
├── requirements.txt
└── .gitignore
```

## 4. 环境安装

建议使用 Python 3.10 或更高版本。

```bash
pip install -r requirements.txt
```

## 5. 运行 Python 程序

在项目目录中运行：

```bash
python analysis.py
```

程序会读取 data.csv，并在 output 文件夹生成统计结果和图片。

## 6. 使用 Jupyter Notebook

运行：

```bash
jupyter notebook
```

打开 `analysis.ipynb`，依次运行代码单元即可看到数据表、统计结果和柱状图。

## 7. 数据内容

数据按照 Structure、Function、Disease 和 Research 四个主题进行整理。

其中包含 FXI 的蛋白结构、激活方式、在凝血过程中的作用、FXI 缺乏以及 FXI 抑制研究等信息。

## 8. 科学背景

FXI 是血浆中的凝血因子，以同源二聚体形式存在。每个亚基包含四个 apple domains 和一个催化结构域。FXI 被激活后形成 FXIa，可激活凝血因子 IX，从而参与凝血过程。

FXI 缺乏通常被称为血友病 C。已有研究指出，FXI 缺乏患者的出血表现存在较大差异，单纯根据 FXI 水平并不能完全预测出血情况。

FXI 也是近年来抗血栓研究关注的靶点之一。研究人员希望进一步理解 FXI 在血栓形成和正常止血之间的作用。

## 9. 可复现性

项目不依赖网络数据。运行项目时，只需要安装 requirements.txt 中列出的 Python 包，并使用项目自带的 data.csv。

因此其他用户可以下载项目后重新运行 Python 文件或 Jupyter Notebook，得到相同的分析流程和图表。

## 10. Git 版本管理

本项目使用 Git 管理代码版本。

示例命令：

```bash
git init
git add .
git commit -m "Initial FXI analysis project"
git tag -a v1.0.0 -m "FXI analysis version 1.0.0"
```

## 11. 项目结论

通过本项目可以看到，FXI 相关资料可以按照结构、功能、疾病和研究方向进行整理。数据分析部分虽然比较简单，但能够完整展示 CSV 数据读取、分组统计、可视化和 Jupyter 展示的基本流程。

## 12. 参考资料

1. NCBI Gene: F11 coagulation factor XI。
2. Biology of factor XI, Research and Practice in Thrombosis and Haemostasis, 2024。
3. Structure and function of factor XI。
4. Why Factor XI Deficiency is a Clinical Concern。

## 13. 许可证

本项目仅用于学习和课程作业，不用于医学诊断或临床决策。
