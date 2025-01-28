from analysis import calculate_average_vitals, detect_trends, identify_abnormal_readings


def generate_report(data):
    """
    Generate a comprehensive report including:
    1. Average vitals.
    2. Abnormal readings.
    3. Trends over time.
    """
    print("\nGenerating report...")
    
    # Calculate average vitals
    avg_systolic_bp, avg_diastolic_bp, avg_bmi = calculate_average_vitals(data)
    
    # Identify abnormal readings
    high_bp, abnormal_bmi = identify_abnormal_readings(data)
    
    # Detect trends
    age_bp_trend = detect_trends(data)
    
    # Compile report
    report = {
        'Average Vitals': {
            'Average Systolic BP': avg_systolic_bp,
            'Average Diastolic BP': avg_diastolic_bp,
            'Average BMI': avg_bmi
        },
        'Abnormal Readings': {
            'High Blood Pressure': high_bp[['age', 'ap_hi', 'ap_lo']].head(),  # Show first 5 rows
            'Abnormal BMI': abnormal_bmi[['age', 'bmi']].head()  # Show first 5 rows
        },
        'Trends Over Time': {
            'Blood Pressure Trend by Age': age_bp_trend.head()  # Show first 5 rows
        }
    }
    
    print("Report generated successfully!")
    return report, age_bp_trend
