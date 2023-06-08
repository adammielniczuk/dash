import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# Sample data
df = pd.read_csv("data\companies_late.csv", sep = ";")

# Sort the DataFrame by 'Late_Percent' column in descending order
df_sorted = df.sort_values('Late_Percent', ascending=True)

colors = df_sorted['colors']

# Plotting the bar chart
f_size = 8
fig, ax = plt.subplots(figsize=(8, 2))
bars = ax.barh(df_sorted['Company'], df_sorted['Late_Percent'], color = colors)



# Add icons next to the bars
for i, bar in enumerate(bars):
    company = df_sorted['Company'].iloc[i]
    logo_path = df_sorted['Logo_Path'].iloc[i]
    img = plt.imread(logo_path)
    imagebox = OffsetImage(img, zoom=1.5 * f_size * bar.get_height() / img.shape[0])  # Scale the zoom value based on the image width
    imagebox.image.axes = ax
    ab = AnnotationBbox(imagebox, (df_sorted['Late_Percent'].iloc[i], i),
                        xybox=(2 * f_size * bar.get_height() / img.shape[0] * img.shape[1], 0),  # Adjust the xybox offsets as needed
                        xycoords='data',
                        boxcoords="offset points",
                        frameon=False)
    ax.add_artist(ab)

ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.xlabel('Late Percent')
plt.ylabel('Company')
plt.title('Late Percent by Company')
plt.yticks(rotation=45)

company_late_fig = fig