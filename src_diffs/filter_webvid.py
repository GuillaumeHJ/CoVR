import pandas as pd
import json
from datasets import load_dataset
from pathlib import Path
import time
from tqdm import tqdm

# Enable tqdm for pandas
tqdm.pandas()

def load_cleanvid_metadata():
    """Load CleanVid-15M metadata and retain only necessary columns"""
    print("\n=== Loading CleanVid-15M Metadata ===")
    start_time = time.time()

    dataset = load_dataset("shinonomelab/cleanvid-15m_map", streaming=False)["train"]

    df = dataset.to_pandas()

    # Extract accountId from author column
    def extract_account_id(author_str):
        try:
            author_info = json.loads(author_str)
            return author_info.get("accountsId", None)
        except json.JSONDecodeError:
            return None

    df["author"] = df["author"].progress_apply(extract_account_id)

    # Extract categories as a list from string representation
    def extract_categories(categories_str):
        try:
            # Convert string representation of list to an actual list
            return json.loads(categories_str) if isinstance(categories_str, str) else []
        except json.JSONDecodeError:
            return []

    df["categories"] = df["categories"].progress_apply(extract_categories)

    # Drop unnecessary columns
    df = df[["id", "author", "categories"]]

    elapsed_time = time.time() - start_time
    print(f"\nMetadata loading completed:")
    print(f"- Total entries retained: {len(df):,}")
    print(f"- Time taken: {elapsed_time:.2f} seconds")

    return df

def extract_video_id(path):
    """Extract video ID from path string"""
    return path.split('/')[-1]

def filter_similar_pairs(covr_df, metadata_df):
    """Filter for similar pairs based on authors or categories"""
    print("\nFiltering similar pairs...")

    # Extract video IDs
    covr_df["vid1_id"] = covr_df["pth1"].progress_apply(extract_video_id).astype(str)
    covr_df["vid2_id"] = covr_df["pth2"].progress_apply(extract_video_id).astype(str)

    # Ensure metadata index is also a string
    metadata_df = metadata_df.set_index("id")
    metadata_df.index = metadata_df.index.astype(str)

    print(f"Metadata col {metadata_df.columns}")
    print(f"CoVR col {covr_df.columns}")

    # Merge metadata for both videos
    merged = covr_df.merge(metadata_df, left_on="vid1_id", right_index=True, how="left")
    merged = merged.rename(columns={"author": "author1", "categories": "categories1"})
    merged = merged.merge(metadata_df, left_on="vid2_id", right_index=True, how="left")
    merged = merged.rename(columns={"author": "author2", "categories": "categories2"})

    print(f"Merged col {merged.columns}")

    # Check for similarity
    author_similarity = (merged["author1"] == merged["author2"]) & merged["author1"].notna()
    author_similarity_df = merged[author_similarity]

    category_similarity = merged.progress_apply(
        lambda row: bool(
            set(row["categories1"] or []).intersection(row["categories2"] or [])
        ) if isinstance(row["categories1"], list) and isinstance(row["categories2"], list) else False,
        axis=1,
    )
    category_similarity_df = merged[category_similarity]

    print(f"Author Similar pairs found : {len(author_similarity_df):,}")
    print(f"Category Similar pairs found: {len(category_similarity_df):,}")

    similar_pairs = merged[author_similarity | category_similarity]
    print(f"Similar pairs found: {len(similar_pairs):,}")
    return author_similarity, category_similarity, similar_pairs

def main():
    print("\n=== Starting WebVid-CoVR Similar Pairs Filtering ===")
    start_time = time.time()

    # Create annotation directory if it doesn't exist
    Path("annotation/webvid-covr").mkdir(parents=True, exist_ok=True)

    # Load CleanVid metadata
    metadata_df = load_cleanvid_metadata()

    # Process each split
    splits = ['train', 'val'] # , 'test']

    for split in splits:
        print(f"\n=== Processing {split} split ===")
        split_start_time = time.time()

        # Load annotations
        if split == 'train':
            input_path = f"annotation/webvid-covr/webvid2m-covr_{split}.csv"
        else:
            input_path = f"annotation/webvid-covr/webvid8m-covr_{split}.csv"
        print(f"Loading annotations from: {input_path}")
        covr_df = pd.read_csv(input_path)
        print(f"Loaded {len(covr_df):,} pairs")

        # Filter for similar pairs
        split_similar_author_df, split_similar_category_df, split_similar_df = filter_similar_pairs(covr_df, metadata_df)
        
        # Ensure columns are in the correct order
        columns = ['txt1', 'txt2', 'sim_txt', 'pth1', 'pth2', 'edit', 'scores']
        print("AUTOR SIML COL",split_similar_author_df.columns)
        print("CAT SIML COL",split_similar_category_df.columns)
        print("ALL SIML COL",split_similar_df.columns)

        print("\n=== Saving Results ===")
        if split == 'train':
            split_similar_author_df[columns].to_csv(f"annotation/webvid-covr/webvid2m-covr_{split}_similar_author.csv", index=False)
            split_similar_category_df[columns].to_csv(f"annotation/webvid-covr/webvid2m-covr_{split}_similar_category.csv", index=False)
            split_similar_df[columns].to_csv(f"annotation/webvid-covr/webvid2m-covr_{split}_similar.csv", index=False)

        else:
            split_similar_author_df[columns].to_csv(f"annotation/webvid-covr/webvid8m-covr_{split}_similar_author.csv", index=False)
            split_similar_category_df[columns].to_csv(f"annotation/webvid-covr/webvid8m-covr_{split}_similar_category.csv", index=False)
            split_similar_df[columns].to_csv(f"annotation/webvid-covr/webvid8m-covr_{split}_similar.csv", index=False)

        total_time = time.time() - split_start_time

        print(f"\n{split} split completed:")
        print(f"- Similar pairs found: {len(split_similar_df):,}")
        print(f"- Time taken: {total_time:.2f} seconds")


if __name__ == "__main__":
    main()
