import pandas as pd
import numpy as np

log_transcriptomics_data = pd.read_csv('data/log2FC_transcriptomics.csv')
proteomics = pd.read_csv('data/proteomics.csv')  

min_nonzero = log_transcriptomics_data["padj"][log_transcriptomics_data["padj"] > 0].min()
log_transcriptomics_data["padj"] = log_transcriptomics_data["padj"].replace(0, min_nonzero / 2)

FC_THRESHOLD   = 1.0
PADJ_THRESHOLD = 0.05

sig_sorted = log_transcriptomics_data[
    (log_transcriptomics_data["padj"] < PADJ_THRESHOLD) &
    (log_transcriptomics_data["log2FoldChange"].abs() > FC_THRESHOLD)].copy()

sig_sorted["direction"] = sig_sorted["log2FoldChange"].apply(
    lambda x: "Upregulated" if x > 0 else "Downregulated")
sig_sorted = sig_sorted.sort_values("padj")

proteomics = proteomics.rename(columns={"protein": "uniprot_id"})


merged = sig_sorted.merge(
    proteomics[["uniprot_id", "description", "avg_ratio", "ratio_count"]],
    on="uniprot_id",
    how="left"  
)
merged["description_clean"] = merged["description"].str.split(" OS=").str[0]


merged[["uniprot_id", "gene_name", "log2FoldChange", "padj", "direction",
        "avg_ratio", "ratio_count", "description_clean"]].to_csv("significant_genes_with_descriptions.csv", index=False)


up_descriptions   = merged[merged["direction"] == "Upregulated"]["description_clean"].dropna().unique().tolist()
down_descriptions = merged[merged["direction"] == "Downregulated"]["description_clean"].dropna().unique().tolist()

print(f"\nUnique descriptions for upregulated genes {up_descriptions}")
print(f"Unique descriptions for downregulated genes {down_descriptions}")
