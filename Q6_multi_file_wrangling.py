import pandas as pd

def wrangle_data():
    df_student = pd.read_csv('student_personal.csv')
    df_exam = pd.read_csv('exam_scores.csv')
    
    # Merge both files on StudentID
    merged_df = pd.merge(df_student, df_exam, on='StudentID', how='inner')
    
    # Calculate the average marks per Department for each Subject
    avg_marks = merged_df.groupby(['Department', 'Subject'])['Marks'].mean().reset_index()
    
    # Reshape the result so that each Subject becomes a column
    pivoted_df = avg_marks.pivot(index='Department', columns='Subject', values='Marks')
    
    print("Final Pivoted Table (Average Marks):")
    print(pivoted_df)

if __name__ == "__main__":
    wrangle_data()
