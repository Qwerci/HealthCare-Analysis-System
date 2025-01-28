
from cleanining import clean_and_preprocess, load_data
from report import generate_report
from visualization import addditional_visualizations, visualize_trends


def main():
    
    file_path = '..\data\cardio_train.csv'  
    
    # Load the dataset
    print("Loading dataset...")
    data = load_data(file_path)
    if data is None:
        return
    
    # Clean and preprocess the data
    data = clean_and_preprocess(data)
    
    # Generate report
    report, age_bp_trend = generate_report(data)
    
    # Print report
    print("\nCardiovascular Disease Data Analysis Report")
    print("==========================================")
    
    print("\nAverage Vitals:")
    print(f"Average Systolic BP: {report['Average Vitals']['Average Systolic BP']:.2f} mmHg")
    print(f"Average Diastolic BP: {report['Average Vitals']['Average Diastolic BP']:.2f} mmHg")
    print(f"Average BMI: {report['Average Vitals']['Average BMI']:.2f}")
    
    print("\nAbnormal Readings:")
    print("Patients with High Blood Pressure:")
    print(report['Abnormal Readings']['High Blood Pressure'])
    print("\nPatients with Abnormal BMI:")
    print(report['Abnormal Readings']['Abnormal BMI'])
    
    print("\nTrends Over Time:")
    print("Blood Pressure Trend by Age:")
    print(report['Trends Over Time']['Blood Pressure Trend by Age'])
    
    # Visualize trends
    print("\nVisualizing blood pressure trends over age...")
    visualize_trends(age_bp_trend)
    addditional_visualizations(data)

if __name__ == "__main__":
    main()
