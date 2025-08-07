import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Create DataFrame
a = pd.DataFrame()
a['A'] = [1, 2, 3]
a['B'] = [4, 5, 6]
a['C'] = [7, 8, 9]
a['D'] = np.random.rand(len(a))
a['E'] = np.random.randint(1, 10, size=len(a))

# Start saving plots into one PDF
with PdfPages('dataframe_plots.pdf') as pdf:

    # Bar Plot
    a.plot(kind='bar', x='A', y='B')
    plt.title('Bar Plot of B by A')
    plt.xlabel('A')
    plt.ylabel('B')
    pdf.savefig()
    plt.close()

    # Line Plot
    a.plot(kind='line', x='A', y='C')
    plt.title('Line Plot of C by A')
    plt.xlabel('A')
    plt.ylabel('C')
    pdf.savefig()
    plt.close()

    # Scatter Plot
    a.plot(kind='scatter', x='A', y='B')
    plt.title('Scatter Plot of B by A')
    plt.xlabel('A')
    plt.ylabel('B')
    pdf.savefig()
    plt.close()

    # Histogram
    a.plot(kind='hist', y='C', bins=5)
    plt.title('Histogram of C')
    plt.xlabel('C')
    plt.ylabel('Frequency')
    pdf.savefig()
    plt.close()

    # Box Plot
    a.plot(kind='box')
    plt.title('Box Plot of DataFrame')
    pdf.savefig()
    plt.close()

    # Area Plot
    a.plot(kind='area', x='A', y='B')
    plt.title('Area Plot of B by A')
    plt.xlabel('A')
    plt.ylabel('B')
    pdf.savefig()
    plt.close()

    # Pie Chart
    a.plot(kind='pie', y='C', labels=a['A'], autopct='%1.1f%%')
    plt.title('Pie Chart of C by A')
    plt.ylabel('')
    pdf.savefig()
    plt.close()

    # Correlation Matrix as a Heatmap using only Matplotlib
    corr = a.corr()
    fig, ax = plt.subplots()
    cax = ax.matshow(corr, cmap='coolwarm')
    plt.title('Correlation Matrix Heatmap', pad=20)
    plt.xticks(range(len(corr.columns)), corr.columns)
    plt.yticks(range(len(corr.columns)), corr.columns)
    fig.colorbar(cax)
    pdf.savefig()
    plt.close()
