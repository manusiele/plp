import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import sys

def load_data(file_path='metadata.csv', sample_size=None):
    """Load the CORD-19 metadata.csv file."""
    df = pd.read_csv(file_path, nrows=sample_size)
    print("Data loaded successfully.")
    return df

def explore_data(df):
    """Perform basic data exploration."""
    # Dimensions
    print("Dimensions (rows, columns):", df.shape)
    
    # Data types
    print("\nData types:\n", df.dtypes)
    
    # Missing values
    print("\nMissing values:\n", df.isnull().sum())
    
    # Basic statistics
    print("\nNumerical statistics:\n", df.describe())

def clean_data(df):
    """Handle missing data."""
    # Calculate missing value percentages
    missing_percent = df.isnull().mean() * 100
    print("\nMissing values (%):\n", missing_percent[missing_percent > 0].sort_values(ascending=False))
    
    # Drop columns with >80% missing values
    threshold = 0.8
    cols_to_drop = missing_percent[missing_percent > threshold * 100].index
    df = df.drop(columns=cols_to_drop)
    print("Dropped columns:", cols_to_drop)
    
    # Fill missing values for key columns
    df['title'] = df['title'].fillna('Unknown') if 'title' in df.columns else df
    df['abstract'] = df['abstract'].fillna('No abstract') if 'abstract' in df.columns else df
    df['publish_time'] = df['publish_time'].fillna('Unknown') if 'publish_time' in df.columns else df
    df['journal'] = df['journal'].fillna('Unknown') if 'journal' in df.columns else df
    
    print("\nMissing values after cleaning:\n", df.isnull().sum())
    return df

def create_visualizations(df):
    """Create visualizations for publications by year and top journals."""
    # Convert publish_time to datetime
    if 'publish_time' in df.columns:
        df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
        df['year'] = df['publish_time'].dt.year
    
    # Publications by year
    if 'year' in df.columns:
        plt.figure(figsize=(10, 6))
        sns.countplot(data=df, x='year')
        plt.title('Number of Publications by Year')
        plt.xlabel('Year')
        plt.ylabel('Number of Papers')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('publications_by_year.png')
        plt.show()
    
    # Top 10 journals
    if 'journal' in df.columns:
        top_journals = df['journal'].value_counts().head(10)
        plt.figure(figsize=(10, 6))
        sns.barplot(x=top_journals.values, y=top_journals.index)
        plt.title('Top 10 Journals by Publication Count')
        plt.xlabel('Number of Papers')
        plt.ylabel('Journal')
        plt.tight_layout()
        plt.savefig('top_journals.png')
        plt.show()

def run_streamlit_app(df):
    """Run Streamlit app to display findings."""
    st.title('CORD-19 Dataset Analysis')
    
    # Dataset overview
    st.header('Dataset Overview')
    st.write('First 5 rows of the dataset:')
    st.dataframe(df.head())
    
    # Dimensions
    st.write(f'Dataset Dimensions: {df.shape[0]} rows, {df.shape[1]} columns')
    
    # Missing values
    st.header('Missing Values')
    missing_percent = df.isnull().mean() * 100
    st.write('Percentage of missing values per column:')
    st.write(missing_percent[missing_percent > 0].sort_values(ascending=False))
    
    # Visualizations
    st.header('Visualizations')
    
    # Publications by year
    if 'publish_time' in df.columns:
        df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
        df['year'] = df['publish_time'].dt.year
        st.subheader('Publications by Year')
        plt.figure(figsize=(10, 6))
        sns.countplot(data=df, x='year')
        plt.title('Number of Publications by Year')
        plt.xlabel('Year')
        plt.ylabel('Number of Papers')
        plt.xticks(rotation=45)
        st.pyplot(plt)
    
    # Top journals
    if 'journal' in df.columns:
        st.subheader('Top 10 Journals')
        top_journals = df['journal'].value_counts().head(10)
        plt.figure(figsize=(10, 6))
        sns.barplot(x=top_journals.values, y=top_journals.index)
        plt.title('Top 10 Journals by Publication Count')
        plt.xlabel('Number of Papers')
        plt.ylabel('Journal')
        st.pyplot(plt)

def main():
    """Main function to run analysis or Streamlit app."""
    # Check if running as Streamlit app
    if 'streamlit' in sys.argv[0].lower():
        df = load_data('metadata.csv', sample_size=10000)  # Adjust path/sample size
        run_streamlit_app(df)
    else:
        # Run analysis
        df = load_data('metadata.csv', sample_size=10000)  # Adjust path/sample size
        explore_data(df)
        df = clean_data(df)
        create_visualizations(df)
        print("\nAnalysis complete. To run Streamlit app, use: streamlit run cord19_analysis.py")

if __name__ == "__main__":
    main()