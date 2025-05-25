import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
import pickle
import streamlit as st

def custom_cleaning(df):
    # Handle 'poutcome'
    if 'poutcome' in df.columns:
        df['poutcome'] = df['poutcome'].replace('unknown', 'not_exist')
    else:
        df['poutcome'] = 'not_exist'

    # Handle 'contact'
    if 'contact' in df.columns:
        df['contact'] = df['contact'].replace('unknown', 'other')
    else:
        df['contact'] = 'other'

    # Handle 'job'
    if 'job' in df.columns:
        df['job'] = df['job'].replace('unknown', 'management')
    else:
        df['job'] = 'management'

    # Handle 'housing'
    if 'housing' in df.columns:
        if df['housing'].isin(['unknown']).any():
            mode_housing = df.loc[df['housing'] != 'unknown', 'housing'].mode()
            if not mode_housing.empty:
                mode_housing_val = mode_housing[0]
            else:
                mode_housing_val = 'no'  # default fallback
            df['housing'] = df['housing'].replace('unknown', mode_housing_val)
    else:
        df['housing'] = 'no'  # default fallback if column missing

    # Handle 'loan'
    if 'loan' in df.columns:
        if df['loan'].isin(['unknown']).any():
            mode_loan = df.loc[df['loan'] != 'unknown', 'loan'].mode()
            if not mode_loan.empty:
                mode_loan_val = mode_loan[0]
            else:
                mode_loan_val = 'no'
            df['loan'] = df['loan'].replace('unknown', mode_loan_val)
    else:
        df['loan'] = 'no'

    # Handle 'month'
    if 'month' in df.columns:
        if df['month'].isin(['unknown']).any():
            mode_month = df.loc[df['month'] != 'unknown', 'month'].mode()
            if not mode_month.empty:
                mode_month_val = mode_month[0]
            else:
                mode_month_val = 'may'  # default fallback
            df['month'] = df['month'].replace('unknown', mode_month_val)
    else:
        df['month'] = 'may'

    # Other features
    df['is_firstcontact'] = df['pdays'] == -1
    campaign_median = df['campaign'].median()
    df['campaign'] = df['campaign'].apply(lambda x: campaign_median if x > 6 else x)

    return df

class ThresholdClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, base_model=None, threshold=0.53):
        self.base_model = base_model
        self.threshold = threshold
        self.classes_ = None

    def fit(self, X, y):
        self.classes_ = np.unique(y)
        self.base_model.fit(X, y)
        return self

    def predict(self, X):
        probas = self.base_model.predict_proba(X)[:, 1]
        preds = (probas >= self.threshold).astype(int)
        return np.array([self.classes_[i] for i in preds])

    def predict_proba(self, X):
        return self.base_model.predict_proba(X)

    def score(self, X, y):
        return self.base_model.score(X, y)

def drop_unwanted_columns(X, preprocessor=None):
    import streamlit as st

    # st.write("📥 Input to drop_unwanted_columns:", X.shape)

    feature_names = None

    # Try to get feature names from preprocessor if provided
    if preprocessor is not None:
        try:
            feature_names = preprocessor.get_feature_names_out()
            # st.write("ℹ️ Got feature names from preprocessor argument.")
        except Exception:
            st.write("⚠️ Failed to get feature names from preprocessor argument.")

    # If feature names not found, try from Streamlit session_state
    if feature_names is None and "feature_names" in st.session_state:
        feature_names = st.session_state["feature_names"]
        # st.write("ℹ️ Got feature names from Streamlit session_state.")

    # Convert to DataFrame with feature names if possible
    if not isinstance(X, pd.DataFrame):
        if feature_names is not None and isinstance(X, np.ndarray) and X.shape[1] == len(feature_names):
            X = pd.DataFrame(X, columns=feature_names)
            # st.write("✅ Created DataFrame using feature names.")
        else:
            X = pd.DataFrame(X)
            # st.write("⚠️ Created DataFrame WITHOUT feature names.")

    # Drop unwanted column if it exists
    to_drop = 'multi_cat__poutcome_not_exist'
    if to_drop in X.columns:
        X = X.drop(columns=[to_drop])
        # st.write(f"🗑 Column '{to_drop}' successfully dropped.")
    else:
        st.write(f"🚫 Column '{to_drop}' not found. Available columns:")
        # st.write(X.columns.tolist())

    # st.write("📤 Output from drop_unwanted_columns:", X.shape)
    return X


def get_transformed_dataframe(pipeline, input_df):
    # Step 1: Cleaning
    cleaned = pipeline.named_steps['cleaner'].transform(input_df)
    # st.write("🧽 Cleaned Data")
    # st.dataframe(cleaned)

    # Step 2: Preprocessing
    preprocessed = pipeline.named_steps['preprocessor'].transform(cleaned)
    # st.write("🔧 Preprocessed Data")
    # st.write("Shape:", preprocessed.shape)

    # Step 3: Feature names
    feat_names = list(pipeline.named_steps['preprocessor'].get_feature_names_out())
    # st.write("🔠 Feature Names Out")
    # st.write(feat_names)

    # # Tampilkan contoh nilai fitur (misalnya baris pertama)
    # if preprocessed.shape[0] > 0:
    #     example_row = pd.DataFrame(preprocessed[0:1], columns=feat_names)
    #     st.write("📊 Example feature values (first row):")
    #     st.dataframe(example_row)
    # else:
    #     st.write("No rows available to show feature values.")

    # Step 4: Drop unwanted columns using the drop_columns step (if exists)
    dropped = pipeline.named_steps['drop_columns'].transform(preprocessed)
    # st.write("🗑 Dropped Output")
    # st.write("Shape:", dropped.shape)

    # Step 6: Create final DataFrame after dropping
    feat_names_dropped = [f for f in feat_names if f != 'multi_cat__poutcome_not_exist']
    df_final = pd.DataFrame(dropped, columns=feat_names_dropped)
    # st.write("✅ Final Transformed Data")
    # st.dataframe(df_final)

    return df_final


