import io
import streamlit as st
import pandas as pd
import pickle
import numpy as np
import csv
import shap
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from custom_components import custom_cleaning, ThresholdClassifier, drop_unwanted_columns, get_transformed_dataframe

def to_excel(df):
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Prediction')
    return output.getvalue()

def app():
    # st.title("📊 Term Deposit Subscription Prediction")

    tab1, tab2 = st.tabs(["📁 Prediction", "📈 Results"])

    # Load pipeline and label encoder
    try:
        with open('final_pipeline.pkl', 'rb') as f:
            saved = pickle.load(f)
            pipeline = saved['pipeline']
            label_encoder = saved['label_encoder']
            model = pipeline.named_steps['model']
    except Exception as e:
        st.error(f"❌ Failed to load model: {e}")
        return

    if "feature_names" not in st.session_state:
        try:
            st.session_state["feature_names"] = pipeline.named_steps['preprocessor'].get_feature_names_out()
        except:
            st.session_state["feature_names"] = None

    if "prediction_df" not in st.session_state:
        st.session_state["prediction_df"] = None
        st.session_state["proba_df"] = None
        st.session_state["transformed_input"] = None
        st.session_state["shap_values"] = None
    if "model" not in st.session_state:
        st.session_state["model"] = model

    with tab1:
        st.write("""
        Upload an Excel or CSV file with customer data to predict whether each customer will subscribe to a term deposit.
        Required columns:
        `age, job, balance, housing, loan, contact, month, campaign, pdays, poutcome`
        """)

        uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=['csv', 'xlsx'])

        if uploaded_file is not None:
            try:
                if uploaded_file.name.endswith('.csv'):
                    sample = uploaded_file.read(2048).decode('utf-8')
                    uploaded_file.seek(0)
                    sniffer = csv.Sniffer()
                    dialect = sniffer.sniff(sample)
                    df = pd.read_csv(uploaded_file, sep=dialect.delimiter)
                else:
                    df = pd.read_excel(uploaded_file)

                st.subheader("📄 Uploaded Data Preview")
                st.dataframe(df)

                required_cols = ['age', 'job', 'balance', 'housing', 'loan', 'contact', 'month', 'campaign', 'pdays', 'poutcome']
                missing_cols = [col for col in required_cols if col not in df.columns]
                if missing_cols:
                    st.error(f"❌ Missing required columns: {missing_cols}")
                    return

                if st.button("🔮 Predict"):
                    transformed_input = get_transformed_dataframe(pipeline, df)
                    y_pred = model.predict(transformed_input)

                    # Safe inverse transform
                    try:
                        labels = label_encoder.inverse_transform(y_pred)
                    except:
                        labels = y_pred

                    df['prediction'] = labels
                    st.session_state["prediction_df"] = df
                    st.session_state["transformed_input"] = transformed_input

                    # Probability
                    if hasattr(model, 'predict_proba'):
                        proba = model.predict_proba(transformed_input)
                        try:
                            proba_df = pd.DataFrame(proba, columns=[f"prob_{cls}" for cls in label_encoder.classes_])
                        except:
                            proba_df = pd.DataFrame(proba, columns=[f"prob_{i}" for i in range(proba.shape[1])])
                        st.session_state["proba_df"] = proba_df
                        
                    df = st.session_state["prediction_df"]
                    st.subheader("🎯 Prediction Results")
                    st.dataframe(df[['age', 'job', 'balance', 'housing', 'loan', 'contact', 'month', 'campaign', 'pdays', 'poutcome', 'prediction']])

                    if st.session_state["proba_df"] is not None:
                        st.subheader("🔎 Prediction Probabilities")
                        st.dataframe(st.session_state["proba_df"])
                
                    st.success("✅ Prediction complete! See 'Results' tab.")

                    # Download button after prediction
                    excel_data = to_excel(df)
                    st.download_button(
                        label="📥 Download Prediction as Excel",
                        data=excel_data,
                        file_name="prediction_results.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )

            except Exception as e:
                st.error(f"❌ Error processing file: {e}")

    with tab2:
        if st.session_state["prediction_df"] is None:
            st.info("Please make a prediction first on the 'Prediction' tab")
        else:
            # ============Sunburst Chart: Deposit Prediction Distribution by Age Group===========
            df = st.session_state["prediction_df"]
            age_bins = [18, 25, 40, 60, float('inf')]
            age_labels = ['Young Adults', 'Adults', 'Middle-Aged Adults', 'Seniors']
            df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels, right=False)
            sunburst_data = df.groupby(['prediction', 'age_group']).size().reset_index(name='count')
            fig = px.sunburst(
                sunburst_data,
                path=['prediction', 'age_group'],
                values='count',
                color='prediction',
                hover_data=['count'],
                branchvalues="total"
            )
            fig.update_traces(textinfo='label+percent parent')
            fig.update_layout(
                width=700,
                height=700,
                margin=dict(t=50, l=10, r=10, b=10)
            )

            st.subheader("Sunburst Chart: Deposit Prediction Distribution by Age Group")
            st.plotly_chart(fig, use_container_width=True)
            
            # ============Sunburst Chart: Deposit Prediction Distribution by Age Group===========
            st.subheader("Job Type vs Term Deposit Prediction")

            plt.figure(figsize=(14, 6))
            sns.set(style="whitegrid")
            sns.countplot(
                data=df,
                x='job',
                hue='prediction', 
                order=df['job'].value_counts().index,
                palette='Set2'
            )
            plt.xlabel("Job", fontsize=12)
            plt.ylabel("Number of Customers", fontsize=12)
            plt.xticks(rotation=45, ha='right')
            plt.legend(title='Deposit')
            plt.tight_layout()
            st.pyplot(plt.gcf())
            plt.clf()
            
            # ============Distribution of Customers by Contact Method and Their Term Deposit Subscription Status===========
            st.subheader("Distribution of Customers by Contact Method and Their Term Deposit Prediction Status")
            plt.figure(figsize=(10, 6))
            sns.set(style="whitegrid")
            sns.countplot(
                data=df,
                x='contact',
                hue='prediction', 
                order=df['contact'].value_counts().index,
                palette='Set2'
            )
            plt.title("Contact Method vs Term Deposit Subscription", fontsize=16, fontweight='bold')
            plt.xlabel("Contact Method", fontsize=12)
            plt.ylabel("Number of Customers", fontsize=12)
            plt.legend(title='Deposit')
            plt.tight_layout()
            st.pyplot(plt.gcf())
            plt.clf()

            
            # ============Housing and Personal Loan Status vs Term Deposit Subscription===========
            st.subheader("Housing and Personal Loan Status vs Term Deposit Prediction Prediction")

            fig, axs = plt.subplots(1, 2, figsize=(14, 6))
            sns.set(style="whitegrid")

            sns.countplot(data=df, x='housing', hue='prediction', ax=axs[0], palette='Set2')
            axs[0].set_title("Housing Loan vs Deposit")
            axs[0].set_xlabel("Housing Loan")
            axs[0].set_ylabel("Number of Customers")

            sns.countplot(data=df, x='loan', hue='prediction', ax=axs[1], palette='Set2')
            axs[1].set_title("Personal Loan vs Deposit")
            axs[1].set_xlabel("Personal Loan")
            axs[1].set_ylabel("Number of Customers")

            plt.tight_layout()
            st.pyplot(fig)
            plt.clf()
            
            # ============Customer Balance Distribution===========
            st.subheader("Customer Balance Distribution")
            df_temp = st.session_state["prediction_df"].copy()

            # Define balance bins and labels
            balance_bins = [-float('inf'), 0, 1000, 5000, float('inf')]
            balance_labels = ['Negative', 'Low', 'Medium', 'High']

            # Apply binning
            df_temp['balance_group'] = pd.cut(df_temp['balance'], bins=balance_bins, labels=balance_labels, right=False)

            # Count occurrences in each group
            balance_counts = df_temp['balance_group'].value_counts().sort_index()

            # Plot pie chart
            plt.figure(figsize=(7, 7))
            plt.pie(balance_counts, labels=balance_counts.index, autopct='%1.1f%%',
                    startangle=140, colors=sns.color_palette('pastel'))
            plt.title('Customer Balance Distribution')
            plt.axis('equal')  # Circle pie chart

            st.pyplot(plt.gcf())
            plt.clf()
            # ============Term Deposit Subscription by Balance Group===========
            st.subheader("Term Deposit Prediction Subscription by Balance Group")
            sunburst_data = df_temp.groupby(['prediction', 'balance_group']).size().reset_index(name='count')
            fig = px.sunburst(
                sunburst_data,
                path=['prediction', 'balance_group'],
                values='count',
                color='prediction',
                title='Deposit Status by Balance Group (Prediction)',
                hover_data=['count'],
                branchvalues="total"
            )
            fig.update_traces(textinfo='label+percent parent')
            fig.update_layout(
                width=800,
                height=800,
                margin=dict(t=50, l=10, r=10, b=10)
            )
            st.plotly_chart(fig, use_container_width=True)
            
            sunburst_data = df_temp.groupby(['balance_group','prediction']).size().reset_index(name='count')
            fig = px.sunburst(
                sunburst_data,
                path=['balance_group', 'prediction', ],
                values='count',
                color='prediction',
                title='Deposit Prediction Status by Balance Group (Balance Group)',
                hover_data=['count'],
                branchvalues="total"
            )
            fig.update_traces(textinfo='label+percent parent')
            fig.update_layout(
                width=800,
                height=800,
                margin=dict(t=50, l=10, r=10, b=10)
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # ============ Feature Importance (SHAP) ========
            st.subheader('Feature Importance')

            # Model step name in pipeline, adjust if different
            model_step_name = 'model'
            model = pipeline.named_steps.get(model_step_name, None)

            # Get the preprocessor
            preprocessor = pipeline.named_steps.get('preprocessor', None)

            def get_feature_names_from_preprocessor(preprocessor):
                features = []
                try:
                    # If the preprocessor is a ColumnTransformer
                    for name, transformer, columns in preprocessor.transformers_:
                        # If transformer is a pipeline, get the last step's feature names
                        if hasattr(transformer, 'named_steps'):
                            last_step = list(transformer.named_steps.values())[-1]
                            if hasattr(last_step, 'get_feature_names_out'):
                                names = last_step.get_feature_names_out(columns)
                            else:
                                names = columns
                        # If transformer has get_feature_names_out directly
                        elif hasattr(transformer, 'get_feature_names_out'):
                            names = transformer.get_feature_names_out(columns)
                        else:
                            names = columns
                        features.extend(names)
                except Exception as e:
                    print(f"Error getting feature names from preprocessor: {e}")
                return features

            if model is None:
                st.error(f"Model step '{model_step_name}' not found in pipeline.")
            else:
                if hasattr(model, 'feature_importances_'):
                    fi = model.feature_importances_

                    # Get features from session state if available, else get from preprocessor
                    features = st.session_state.get("feature_names", None)
                    if features is None and preprocessor is not None:
                        features = get_feature_names_from_preprocessor(preprocessor)

                    # If still None or empty, create dummy feature names
                    if features is None or len(features) == 0:
                        features = [f'feature_{i}' for i in range(len(fi))]

                    # Ensure features is a list, not a numpy array
                    if isinstance(features, np.ndarray):
                        features = features.tolist()

                    # Remove unwanted feature from features list only, do not remove from importances
                    unwanted_feature = 'multi_cat__poutcome_not_exist'
                    if unwanted_feature in features:
                        features.remove(unwanted_feature)  # remove from feature list only

                    # Now, if number of features > number of importances, truncate features to match
                    if len(features) > len(fi):
                        st.warning(f"More features ({len(features)}) than importances ({len(fi)}). Truncating features.")
                        features = features[:len(fi)]
                    elif len(features) < len(fi):
                        st.warning(f"More importances ({len(fi)}) than features ({len(features)}). Truncating importances.")
                        fi = fi[:len(features)]

                    fi_df = pd.DataFrame({
                        'feature': features,
                        'importance': fi
                    }).sort_values(by='importance', ascending=False)

                    fig_fi, ax_fi = plt.subplots(figsize=(8, 6))
                    sns.barplot(data=fi_df, x='importance', y='feature', ax=ax_fi)
                    ax_fi.set_title('Feature Importance')
                    ax_fi.set_xlabel('Importance')
                    ax_fi.set_ylabel('Feature')
                    plt.tight_layout()

                    st.pyplot(fig_fi)
                    plt.close(fig_fi)

                else:
                    st.info("Model does not have feature_importances_ attribute.")

            # ============ SHAP Analysis ============
            
            model = pipeline.named_steps['model']
            transformed_input = st.session_state["transformed_input"]

            explainer = shap.TreeExplainer(model, data=transformed_input)
            shap_values = explainer.shap_values(transformed_input)

            if isinstance(shap_values, list):
                shap_values_class1 = shap_values[1]
                shap_values_class0 = shap_values[0]
            else:
                shap_values_class1 = shap_values[:, :, 1]
                shap_values_class0 = shap_values[:, :, 0]

            # Plot untuk kelas "Yes" (class 1)
            fig1, ax1 = plt.subplots(figsize=(10, 6))
            shap.summary_plot(shap_values_class1, transformed_input, feature_names=transformed_input.columns, show=False)
            st.subheader("SHAP Summary Plot - Class YES (1)")
            st.pyplot(fig1)
            plt.close(fig1)

            # Plot untuk kelas "No" (class 0)
            fig0, ax0 = plt.subplots(figsize=(10, 6))
            shap.summary_plot(shap_values_class0, transformed_input, feature_names=transformed_input.columns, show=False)
            st.subheader("SHAP Summary Plot - Class NO (0)")
            st.pyplot(fig0)
            plt.close(fig0)
    

