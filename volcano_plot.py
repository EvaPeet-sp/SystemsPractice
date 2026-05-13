import pandas as pd
import matplotlib
import dash_bio
import numpy as np

log_transcriptomics_data = pd.read_csv('data/log2FC_transcriptomics.csv')

# fix dividing by zero error (with the log transformation) by replacing zero p-values
#  with the smallest non-zero p-value in the dataset divided by 2  
min_nonzero = log_transcriptomics_data["padj"][log_transcriptomics_data["padj"] > 0].min()
log_transcriptomics_data["padj"] = log_transcriptomics_data["padj"].replace(0, min_nonzero / 2)

FC_THRESHOLD   = 1.0 
PADJ_THRESHOLD = 0.05

# print the genes
points_of_interest = log_transcriptomics_data[(log_transcriptomics_data["padj"] < PADJ_THRESHOLD)
                                       &(log_transcriptomics_data["log2FoldChange"].abs() > FC_THRESHOLD)
].copy()

points_of_interest["direction"] = points_of_interest["log2FoldChange"].apply(
    lambda x: "Upregulated" if x > 0 else "Downregulated"
)

# print list of upregualted 
upregulated_genes = points_of_interest[points_of_interest["direction"] == "Upregulated"]["gene_name"].tolist()
print(f"Upregulated Genes: {upregulated_genes}")


# print list of downregulated
downregulated_genes = points_of_interest[points_of_interest["direction"] == "Downregulated"]["gene_name"].tolist()
print(f"Downregulated Genes: {downregulated_genes}")

sig_sorted = points_of_interest.sort_values("padj")

print(f"Total significant genes: {len(sig_sorted)}")
print(f"  Upregulated:   {(sig_sorted['direction'] == 'Upregulated').sum()}")
print(f"  Downregulated: {(sig_sorted['direction'] == 'Downregulated').sum()}")
print()
print(sig_sorted[["ncbi_id", "gene_name", "log2FoldChange", "padj", "direction", "uniprot_id"]].to_string(index=False))

fig = dash_bio.VolcanoPlot(
    dataframe=log_transcriptomics_data,
    effect_size="log2FoldChange",
    p="padj",
    snp="ncbi_id",
    gene="gene_name",
    logp=True,
    genomewideline_value=-np.log10(PADJ_THRESHOLD),
    point_size=5,
    effect_size_line_width=4,
    genomewideline_width=2
)

fig.update_layout(
    xaxis=dict(
        title="log₂ Fold Change",
        range=[-5, 5],
        tickfont=dict(size=12)
    ),
    yaxis=dict(
        title="−log₁₀(padj)",
        range=[0, 30],
        tickfont=dict(size=12)
    ),
    width=850,
    height=550,
)

fig.show()