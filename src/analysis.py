

def calculate_average_vitals(data):
    """
    Calculate average values for systolic BP, diastolic BP, and BMI.
    """
    avg_systolic_bp = data['ap_hi'].mean()
    avg_diastolic_bp = data['ap_lo'].mean()
    avg_bmi = data['bmi'].mean()
    return avg_systolic_bp, avg_diastolic_bp, avg_bmi


def identify_abnormal_readings(data):
    """
    Identify patients with abnormal readings:
    1. High blood pressure: Systolic > 140 or Diastolic > 90.
    2. Abnormal BMI: BMI < 18.5 (underweight) or BMI > 24.9 (overweight).
    """
    # Abnormal blood pressure
    high_bp = data[(data['ap_hi'] > 140) | (data['ap_lo'] > 90)]
    
    # Abnormal BMI
    abnormal_bmi = data[(data['bmi'] < 18.5) | (data['bmi'] > 24.9)]
    
    return high_bp, abnormal_bmi


def detect_trends(data):
    """
    Detect trends in blood pressure over age.
    """
    # Group by age and calculate average blood pressure
    age_bp_trend = data.groupby('age')[['ap_hi', 'ap_lo']].mean()
    return age_bp_trend
