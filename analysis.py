"""
学生成绩数据分析
运行：python analysis.py
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "data.csv"
OUTPUT_DIR = ROOT / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


def load_data(path=DATA_FILE):
    """读取成绩数据。"""
    return pd.read_csv(path)


def add_statistics(df):
    """计算总分、平均分和等级。"""
    subject_cols = ["数学", "英语", "Python"]
    result = df.copy()
    result["总分"] = result[subject_cols].sum(axis=1)
    result["平均分"] = result[subject_cols].mean(axis=1).round(2)

    def level(score):
        if score >= 90:
            return "A"
        if score >= 80:
            return "B"
        if score >= 70:
            return "C"
        return "D"

    result["等级"] = result["平均分"].apply(level)
    return result


def subject_summary(df):
    """生成各科统计信息。"""
    subjects = ["数学", "英语", "Python"]
    summary = df[subjects].agg(["mean", "max", "min"]).T
    summary.columns = ["平均分", "最高分", "最低分"]
    return summary.round(2)


def save_bar_chart(df):
    """保存各科平均分柱状图。"""
    subjects = ["数学", "英语", "Python"]
    means = df[subjects].mean()
    ax = means.plot(kind="bar", figsize=(7, 4), title="各科平均成绩")
    ax.set_xlabel("科目")
    ax.set_ylabel("平均分")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "subject_means.png", dpi=150)
    plt.close()


def save_distribution(df):
    """保存平均分分布图。"""
    ax = df["平均分"].plot(
        kind="hist", bins=5, figsize=(7, 4), title="学生平均分分布"
    )
    ax.set_xlabel("平均分")
    ax.set_ylabel("人数")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "score_distribution.png", dpi=150)
    plt.close()


def main():
    """运行完整分析流程。"""
    df = load_data()
    result = add_statistics(df)

    print("=== 数据预览 ===")
    print(result.to_string(index=False))
    print("\n=== 各科统计 ===")
    print(subject_summary(result).to_string())
    print("\n=== 班级平均分 ===")
    print(round(result["平均分"].mean(), 2))
    print("\n=== 最高分学生 ===")
    top = result.loc[result["平均分"].idxmax()]
    print(f"{top['姓名']}：{top['平均分']:.2f}")
    print("\n=== 等级人数 ===")
    print(result["等级"].value_counts().sort_index().to_string())

    result.to_csv(OUTPUT_DIR / "result.csv", index=False, encoding="utf-8-sig")
    save_bar_chart(result)
    save_distribution(result)
    print(f"\n结果已保存到：{OUTPUT_DIR}")


if __name__ == "__main__":
    main()
