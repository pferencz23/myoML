import matplotlib.pyplot as plt

def corr_heatmap_plot(mixed_demographics_df):

    # Compute the correlation matrix
    corr_columns = mixed_demographics_df.columns.drop('MI')
    corr = mixed_demographics_df[corr_columns].corr()

    # Create the plot
    plt.figure(figsize=(8, 6))
    plt.matshow(corr, cmap='coolwarm', fignum=1)  # fignum=1 keeps it on the same figure
    plt.colorbar()

    # Add ticks and labels
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)

    # Annotate each cell with the correlation coefficient
    for i in range(len(corr.columns)):
        for j in range(len(corr.columns)):
            value = corr.iloc[i, j]
            plt.text(j, i, f"{value:.2f}", ha='center', va='center', color='black')

    plt.title("Correlation Matrix with Values", pad=20)
    plt.tight_layout()
    plt.show()