import matplotlib.pyplot as plt
import seaborn as sns

def visualize_trends(age_bp_trend):
    """
    Visualize blood pressure trend over age
    """
    plt.figure(figsize=(10,6))
    plt.plot(age_bp_trend.index, age_bp_trend['ap_hi'], label='Systolic BP')
    plt.plot(age_bp_trend.index, age_bp_trend['ap_lo'], label='Diastolic BP')
    plt.title('Blood Pressure Trends by Age')
    plt.xlabel('Age (Years)')
    plt.ylabel('Blood Pressure (mmHg)')
    plt.legend()
    plt.grid()
    plt.show()

def addditional_visualizations(data):
    """
    Create additional visualizations for deeper insights:
    1. Distribution of Blood Pressure (Histogram and KDE Plot).
    2. BMI Distribution (Histogram and KDE Plot).
    3. Correlation Heatmap.
    4. Count Plots for categorical features.
    5. Box Plots for blood pressure and BMI.
    """
    print("\nGenerating additional visualizations...")

    sns.set_theme(style="whitegrid")

    # 1. Distribution of Blood Pressure (Histogram and KDE Plot)
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    sns.histplot(data['ap_hi'], bins=30, kde=True, color='blue')
    plt.title('Distribution of Systolic BP')
    plt.xlabel('Systolic BP (mmHg)')
    
    plt.subplot(1, 2, 2)
    sns.histplot(data['ap_lo'], bins=30, kde=True, color='green')
    plt.title('Distribution of Diastolic BP')
    plt.xlabel('Diastolic BP (mmHg)')
    plt.show()

    # 2. BMI Distribution (Histogram and KDE Plot)
    plt.figure(figsize=(8, 6))
    sns.histplot(data['bmi'], bins=30, kde=True, color='purple')
    plt.title('Distribution of BMI')
    plt.xlabel('BMI')
    plt.show()
    
    # 3. Correlation Heatmap
    plt.figure(figsize=(10, 8))
    correlation_matrix = data.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap')
    plt.show()
    
    # 4. Count Plots for Categorical Features
    categorical_features = ['cholesterol', 'gluc', 'smoke', 'alco', 'active']
    plt.figure(figsize=(15, 10))
    for i, feature in enumerate(categorical_features, 1):
        plt.subplot(2, 3, i)
        sns.countplot(x=feature, data=data, palette='Set2')
        plt.title(f'Count Plot of {feature.capitalize()}')
    plt.tight_layout()
    plt.show()
    
    # 5. Box Plots for Blood Pressure and BMI
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    sns.boxplot(x=data['ap_hi'], color='blue')
    plt.title('Box Plot of Systolic BP')
    
    plt.subplot(1, 2, 2)
    sns.boxplot(x=data['ap_lo'], color='green')
    plt.title('Box Plot of Diastolic BP')
    plt.show()
    
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=data['bmi'], color='purple')
    plt.title('Box Plot of BMI')
    plt.show()
    