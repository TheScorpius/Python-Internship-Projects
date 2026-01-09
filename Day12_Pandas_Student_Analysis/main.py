import pandas as pd

def main():
    df = pd.read_csv("Day12_Pandas_Student_Analysis\students.csv")

    print("Student Data\n")
    print(df)

    print("\nBasic Analysis")
    print("Average Marks:", df["Marks"].mean())
    print("Highest Marks:", df["Marks"].max())
    print("Lowest Marks:", df["Marks"].min())

    print("\nStudents with Marks >= 80")
    print(df[df["Marks"] >= 80])

    print("\nAverage Attendance:", df["Attendance"].mean())

if __name__ == "__main__":
    main()