# Select variables
cols = ['JobSatisfaction', 'JobRole', 'JobInvolvement',
        'MonthlyIncome', 'YearsAtCompany', 'EnvironmentSatisfaction']

data = df[cols]

# ==============================
# 1. Descriptive Stats
# ==============================
print(data.describe())

# ==============================
# 2. JobSatisfaction by JobRole
# ==============================
import matplotlib.pyplot as plt

plt.figure()
data.boxplot(column='JobSatisfaction', by='JobRole')
plt.title("Job Satisfaction by Job Role")
plt.suptitle("")
plt.xticks(rotation=45)
plt.show()

# ==============================
# 3. Correlation (Spearman)
# ==============================
corr = data.corr(method='spearman')
print(corr)

plt.figure()
plt.imshow(corr)
plt.colorbar()
plt.title("Spearman Correlation")
plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.show()

# ==============================
# 4. ANOVA (JobRole impact)
# ==============================
from scipy.stats import f_oneway

groups = [group['JobSatisfaction'].values for name, group in data.groupby('JobRole')]
f_stat, p_value = f_oneway(*groups)

print("ANOVA result:")
print("F-statistic:", f_stat)
print("P-value:", p_value)

# ==============================
# 5. Scatter: Income vs Satisfaction
# ==============================
plt.figure()
plt.scatter(data['MonthlyIncome'], data['JobSatisfaction'])
plt.xlabel("Monthly Income")
plt.ylabel("Job Satisfaction")
plt.title("Income vs Job Satisfaction")
plt.show()