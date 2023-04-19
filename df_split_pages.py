import pandas as pd
import matplotlib.pyplot as plt
import textwrap
from matplotlib.backends.backend_pdf import PdfPages

# Create a sample DataFrame with 44 columns
data = {f"Col {i}": range(100, 103) for i in range(1, 45)}
df = pd.DataFrame(data)

# Custom column labels
custom_labels = [f"Column {i}" for i in range(1, 45)]

# Wrap column labels
wrapped_labels = [textwrap.fill(label, width=8) for label in custom_labels]

def create_table_page(ax, df, col_labels):
    ax.axis('off')
    table = ax.table(cellText=df.values, colLabels=col_labels, loc='center')

    font_size = 8
    table.auto_set_font_size(False)
    table.set_fontsize(font_size)

    cell_width = font_size * 0.01
    for key, cell in table.get_celld().items():
        if key[1] >= 0:  # skip header cells
            cell.set_width(cell_width)

    table.scale(1, 1.5)

with PdfPages("table_44_columns_split_pages_with_common_cols.pdf") as pdf:
    # Create first page with first four columns + 20 columns
    fig, ax = plt.subplots(figsize=(11.69, 8.27))
    df_page1 = pd.concat([df.iloc[:, :4], df.iloc[:, 4:24]], axis=1)
    labels_page1 = wrapped_labels[:4] + wrapped_labels[4:24]
    create_table_page(ax, df_page1, labels_page1)
    pdf.savefig(fig, bbox_inches='tight')
    plt.close(fig)

    # Create second page with first four columns + remaining 20 columns
    fig, ax = plt.subplots(figsize=(11.69, 8.27))
    df_page2 = pd.concat([df.iloc[:, :4], df.iloc[:, 24:]], axis=1)
    labels_page2 = wrapped_labels[:4] + wrapped_labels[24:]
    create_table_page(ax, df_page2, labels_page2)
    pdf.savefig(fig, bbox_inches='tight')
    plt.close(fig)
