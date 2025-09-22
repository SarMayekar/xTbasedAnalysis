import pandas as pd
import glob
import os

def combine_split_files():
    """Combine split CSV files into complete dataset"""
    
    # Find all part files
    csv_files = sorted(glob.glob('data/raw/wsl_events_all_part*.csv'))
    
    if not csv_files:
        print("No split files found")
        return
    
    # Combine files
    df_combined = pd.concat([pd.read_csv(f) for f in csv_files], ignore_index=True)
    
    # Save combined file
    output_path = 'data/processed/wsl_events_all_combined.csv'
    df_combined.to_csv(output_path, index=False)
    
    print(f"Combined {len(csv_files)} files into {output_path}")
    print(f"Total rows: {len(df_combined)}")

if __name__ == "__main__":
    combine_split_files()
