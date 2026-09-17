from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).parent
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)
SUBJECTS = ["数学", "英语", "Python"]


df = pd.read_csv(ROOT / "data.csv")
df["总分"] = df[SUBJECTS].sum(axis=1)
df["平均分"] = df[SUBJECTS].mean(axis=1).round(2)
df["等级"] = pd.cut(
    df["平均分"], [0, 70, 80, 90, 100], labels=["D", "C", "B", "A"], right=False
)

print("=== 数据 ===")
print(df.to_string(index=False))
print("\n=== 各科统计 ===")
print(df[SUBJECTS].agg(["mean", "max", "min"]).T.round(2))
print("\n班级平均分：", round(df["平均分"].mean(), 2))
print("最高分：", df.loc[df["平均分"].idxmax(), ["姓名", "平均分"]].to_dict())
print("\n=== 等级人数 ===")
print(df["等级"].value_counts().sort_index())

# 保存分析结果

df.to_csv(OUT / "result.csv", index=False, encoding="utf-8-sig")

df[SUBJECTS].mean().plot(kind="bar", title="各科平均成绩")
plt.tight_layout()
plt.savefig(OUT / "subject_means.png", dpi=150)
plt.close()

df["平均分"].plot(kind="hist", bins=5, title="学生平均分分布")
plt.tight_layout()
plt.savefig(OUT / "score_distribution.png", dpi=150)
plt.close()

print("\n结果已保存到 output/")
