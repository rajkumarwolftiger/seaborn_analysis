import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data Generation: Create realistic synthetic data for the business context
np.random.seed(42)
data = []
channels = ['Phone', 'Email', 'Chat', 'Social Media']
for channel in channels:
    # Generate different response time distributions for each channel
    if channel == 'Chat':
        response_times = np.random.normal(loc=5, scale=2, size=200)
    elif channel == 'Phone':
        response_times = np.random.normal(loc=8, scale=3, size=150)
    elif channel == 'Email':
        response_times = np.random.normal(loc=20, scale=8, size=100)
    else: # Social Media
        response_times = np.random.normal(loc=15, scale=5, size=120)

    # Ensure no negative response times
    response_times = [max(0, rt) for rt in response_times]
    
    for rt in response_times:
        data.append({'Channel': channel, 'Response Time (min)': rt})

df = pd.DataFrame(data)

# Professional Styling: Apply appropriate Seaborn styling
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=0.8)

# Set figure size for 512x512 output
plt.figure(figsize=(8, 8))

# Create violinplot: Use sns.violinplot() with appropriate parameters
# --- THIS IS THE UPDATED LINE ---
ax = sns.violinplot(
    x='Channel',
    y='Response Time (min)',
    data=df,
    palette='viridis',
    hue='Channel',      # Assign x-variable to hue
    legend=False,       # Disable the legend
    inner='quartile',
    linewidth=1.5
)

# Style the chart: Set appropriate titles, labels, and styling
ax.set_title('Customer Support Response Time Distribution', fontsize=16, weight='bold')
ax.set_xlabel('Support Channel', fontsize=12)
ax.set_ylabel('Response Time (Minutes)', fontsize=12)

# Save chart: Use plt.savefig() with exactly 512x512 pixel dimensions
plt.savefig('chart.png', dpi=64, bbox_inches='tight')
