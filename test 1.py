import pandas as pd

df = pd.read_csv("EducationDataset_2023-24 IP PROJECT.csv")

all_columns = ['District', 
                'No of Zone',
                'No of Schools - Primary', 
                'No of Schools - Middle', 
                'No of Schools - Sec', 
                'No of Schools - Sr. Sec', 
                'No of Schools - Total',
                'No of Students - Pre Primary',
                'No of Students - Primary',
                'No of Students - Middle',
                'No of Students - Secondary',
                'No of Students - Sr Secondary',
                'No of Students - Boys','No of Students - Girls',
                'No of Students - Total','Class X and XII Result - DISTRICT',
                'NUMBER OF STUDENTS APPEARED IN CLASS X (Before Compt.) - 2023-24',
                'TOTAL NUMBER OF STUDENTS PASSED IN CLASS X (Before Compt.) - 2023-24',
                ' PASS PERCENTAGE IN CLASS X - (Before Compt.) - 2023-24',
                ' QUALITY INDEX IN CLASS X - (Before Compt) - 2023-24',
                'TOTAL NUMBER OF STUDENTS APPEARED IN CLASS XII - (Before Compt.) - 2023-24',
                'TOTAL NUMBER OF STUDENTS PASSED IN CLASS XII - (Before Compt.) - 2023-24',
                'PASS PERCENTAGE IN CLASS XII - (Before Compt.) - 2023-24',
                'QUALITY INDEX IN CLASS XII - (Before Compt.) - 2023-24',]  

mark_columns=['No of Students - Pre Primary',
                'No of Students - Primary',
                'No of Students - Middle',
                'No of Students - Secondary',
                'No of Students - Sr Secondary']

passStu=['PASS PERCENTAGE IN CLASS X - (Before Compt.) - 2023-24',
         'PASS PERCENTAGE IN CLASS XII - (Before Compt.) - 2023-24']

school_types = ['No of Schools - Primary', 
                    'No of Schools - Middle', 
                    'No of Schools - Sec', 
                    'No of Schools - Sr. Sec']

def task1_show_data():
    print(df)

def task2_calculate_average():
    df['Average'] = (df[mark_columns].mean(axis=1))
    print("✅ Average number of Student of all states:\n", df[['Average']])

def task3_assign_grade():
    if 'Average' not in df.columns:
        df['Average'] = df[passStu[0]].mean(axis=1)
    
    def grade(avg):
        if avg >= 98: return 'A+'
        elif avg >= 95: return 'A'
        elif avg >= 93: return 'B'
        elif avg >= 90: return 'C'
        else: return 'D'

    df['GradeX'] = df['Average'].apply(grade)
    print("✅ Grades assigned:\n", df[['District', 'Average', 'GradeX']])

def task4_add_grade_column():
     if 'Average' not in df.columns:
        df['Average'] = df[passStu[1]].mean(axis=1)

        def grade(avg):
            if avg >= 98: return 'A+'
            elif avg >= 95: return 'A'
            elif avg >= 93: return 'B'
            elif avg >= 90: return 'C'
            else: return 'D'

        df['GradeXII'] = df['Average'].apply(grade)
        print("✅ Grade column added:\n", df[['District', 'Average', 'GradeXII']])

def task5_show_school_stats():
    
    print("✅ Max and Min number of schools by type and district:\n")
    for school in school_types:
        max_val = df[school].max()
        min_val = df[school].min()
        
        max_districts = df[df[school] == max_val]['District'].tolist()
        min_districts = df[df[school] == min_val]['District'].tolist()

        print(f"School Type: {school}")
        print(f"  Max ({max_val}) in: {', '.join(max_districts)}")
        print(f"  Min ({min_val}) in: {', '.join(min_districts)}\n")

def task6_save_all():
    df.to_csv("Modified_EducationDataset.csv", index=False)
    if 'Average' in df.columns and any(df['Average'] > 80):
        df[df['Average'] > 80].to_csv("Filtered_Above80.csv", index=False)
    print("✅ Files saved.")


# Menu
while True:
    print("\nMenu:")
    print("1. Show full data")
    print("2. Calculate average marks")
    print("3. Assign grades to Class 10")
    print("4. Assign grades to Class 12")
    print("5. Show max and min number of schools by type and district")
    print("6. Save modified data to CSV")
    
    print("0. Exit")

    choice = input("Enter your choice (0–6): ")

    if choice == '1':
        task1_show_data()
    elif choice == '2':
        task2_calculate_average()
    elif choice == '3':
        task3_assign_grade()
    elif choice == '4':
        task4_add_grade_column() 
    elif choice == '5':
        task5_show_school_stats()
    elif choice == '6':
        task6_save_all()
    
    elif choice == '0':
        print("Exiting......")
        break
    else:
        print("❌ Errorrrrrrrrrrrrrr ❌ ")


