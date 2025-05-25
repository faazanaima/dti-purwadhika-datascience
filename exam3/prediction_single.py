import streamlit as st
import pandas as pd
import pickle
import numpy as np
import shap
import matplotlib.pyplot as plt
from conn import get_connection
import datetime
from custom_components import custom_cleaning, ThresholdClassifier, drop_unwanted_columns, get_transformed_dataframe

plt.rcParams['text.usetex'] = False


def tab2_shap_local(pipeline, transformed_input):
    model = pipeline.named_steps['model']
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(transformed_input)

    # Handle SHAP values for binary classification
    if isinstance(shap_values, list) and len(shap_values) == 2:
        sv = shap_values[1][0]  # first sample shap values for positive class
        base_value = explainer.expected_value[1]
    elif isinstance(shap_values, np.ndarray) and shap_values.ndim == 3:
        sv = shap_values[0, :, 1]
        base_value = explainer.expected_value[1]
    else:
        sv = shap_values[0]
        base_value = explainer.expected_value

    st.subheader("Top 10 Features Contributing to Prediction")
    shap_df = pd.DataFrame([sv], columns=transformed_input.columns)
    top_features = shap_df.T.abs().sort_values(by=0, ascending=False).head(10)

    fig_hbar, ax = plt.subplots()
    top_features[0].sort_values().plot.barh(ax=ax, color='skyblue')
    ax.set_xlabel("SHAP Value (absolute)")
    ax.set_ylabel("Feature")
    ax.set_title("Top 10 SHAP Features")
    fig_hbar.tight_layout()
    st.pyplot(fig_hbar)
    plt.close(fig_hbar)

    st.subheader("SHAP Waterfall Plot")
    shap.waterfall_plot(
        shap.Explanation(
            values=sv,
            base_values=base_value,
            data=transformed_input.iloc[0].values,
            feature_names=transformed_input.columns
        ),
        max_display=10
    )
    st.pyplot(plt.gcf())
    plt.close('all')

    st.subheader("SHAP Force Plot")
    fig_force = shap.force_plot(
        base_value,
        sv,
        transformed_input.iloc[0].values,
        feature_names=transformed_input.columns,
        matplotlib=True,
        show=False
    )
    st.pyplot(fig_force)
    plt.close(fig_force)


def app():
    tab1, tab2 = st.tabs(["Prediction", "Results"])

    with tab1:
        st.write("Predict whether a customer will subscribe to a term deposit.")

        # Load pipeline and label encoder once
        if "pipeline" not in st.session_state or "label_encoder" not in st.session_state:
            try:
                with open('final_pipeline.pkl', 'rb') as f:
                    saved = pickle.load(f)
                    st.session_state["pipeline"] = saved['pipeline']
                    st.session_state["label_encoder"] = saved['label_encoder']
                    st.session_state["feature_names"] = st.session_state["pipeline"].named_steps['preprocessor'].get_feature_names_out()
                    # st.success("✅ Model loaded successfully.")
            except Exception as e:
                # st.error(f"❌ Failed to load model: {e}")
                return

        pipeline = st.session_state["pipeline"]
        label_encoder = st.session_state["label_encoder"]
        feature_names = st.session_state.get("feature_names")

        # Input form
        age = st.slider("Age", 6, 100, 30)
        job_options = {
            "Admin": "admin.",
            "Self-Employed": "self-employed",
            "Services": "services",
            "Housemaid": "housemaid",
            "Technician": "technician",
            "Management": "management",
            "Student": "student",
            "Blue-Collar": "blue-collar",
            "Entrepreneur": "entrepreneur",
            "Retired": "retired",
            "Unemployed": "unemployed",
            "Unknown": "unknown"
        }
        housing_options = {"No": "no", "Yes": "yes"}
        loan_options = {"No": "no", "Yes": "yes"}
        contact_options = {"Cellular": "cellular", "Telephone": "telephone", "Unknown": "unknown"}
        month_options = {
            "January": "jan", "February": "feb", "March": "mar", "April": "apr",
            "May": "may", "June": "jun", "July": "jul", "August": "aug",
            "September": "sep", "October": "oct", "November": "nov", "December": "dec"
        }
        poutcome_options = {"Unknown": "unknown", "Other": "other", "Failure": "failure", "Success": "success"}

        job_display = st.selectbox("Job Type", list(job_options.keys()), index=0)
        job = job_options[job_display]

        balance = st.number_input("Account Balance", value=0.0, format="%.2f")

        housing_display = st.selectbox("Housing Loan", list(housing_options.keys()), index=1)
        housing = housing_options[housing_display]

        loan_display = st.selectbox("Personal Loan", list(loan_options.keys()), index=0)
        loan = loan_options[loan_display]

        contact_display = st.selectbox("Contact Type", list(contact_options.keys()), index=0)
        contact = contact_options[contact_display]

        month_display = st.selectbox("Last Contact Month", list(month_options.keys()), index=0)
        month = month_options[month_display]

        campaign = st.number_input("Number of Contacts During Campaign", min_value=0, max_value=50, value=1)
        pdays = st.number_input("Days Since Last Contact (pdays)", min_value=-1, max_value=999, value=-1)

        poutcome_display = st.selectbox("Outcome of Previous Campaign", list(poutcome_options.keys()), index=0)
        poutcome = poutcome_options[poutcome_display]

        if st.button("🔮 Predict"):
            input_df = pd.DataFrame([{
                'age': age,
                'job': job,
                'balance': balance,
                'housing': housing,
                'loan': loan,
                'contact': contact,
                'month': month,
                'campaign': campaign,
                'pdays': pdays,
                'poutcome': poutcome
            }])

            st.subheader("🔍 Input Summary")
            st.dataframe(input_df)

            try:
                transformed_input = get_transformed_dataframe(pipeline, input_df)
                model = pipeline.named_steps['model']
                y_pred = model.predict(transformed_input)
                y_pred_label = y_pred[0] if isinstance(y_pred, (list, np.ndarray)) else y_pred

                if hasattr(label_encoder, 'inverse_transform') and isinstance(y_pred_label, (int, np.integer)):
                    label = label_encoder.inverse_transform([y_pred_label])[0]
                else:
                    label = y_pred_label

                # st.write("Transformed shape:", transformed_input.shape)
                # st.write("Transformed data preview:")
                st.dataframe(transformed_input)

                st.subheader("🔎 Model Raw Prediction Probabilities")
                if hasattr(model, 'predict_proba'):
                    proba = model.predict_proba(transformed_input)
                    st.write(proba)
                else:
                    st.write("Model doesn't support predict_proba.")

                st.subheader("🎯 Prediction Result")
                st.success(f"Prediction: **{label.upper()}**")
                if label.lower() == 'yes':
                    st.info("This customer is **likely to subscribe** to a term deposit.")
                    st.balloons()
                else:
                    st.warning("This customer is **unlikely to subscribe**.")
                    st.snow()

                # Save session state for results tab
                st.session_state["input_df"] = input_df
                st.session_state["transformed_input"] = transformed_input
                st.session_state["prediction"] = y_pred_label

            except Exception as e:
                st.error(f"❌ An error occurred during prediction:\n{e}")

        # Save to history button
        if "prediction" in st.session_state and "input_df" in st.session_state:
            if st.button("💾 Save to History"):
                if not st.session_state.get("authenticated", False):
                    st.warning("⚠️ You need to login first to save prediction history.")
                else:
                    try:
                        conn = get_connection()
                        if conn is None:
                            st.error("⚠️ Could not connect to database.")
                        else:
                            cur = conn.cursor()
                            now = datetime.datetime.now()
                            username = st.session_state.get("username", None)

                            if username is None:
                                st.error("⚠️ Username not found in session.")
                                cur.close()
                                conn.close()
                            else:
                                # Query user_id from user_dex by username (which is 'name' in your table)
                                cur.execute("SELECT user_id FROM user_dex WHERE name = %s", (username,))
                                result = cur.fetchone()
                                if result is None:
                                    st.error(f"⚠️ User '{username}' not found in database.")
                                    cur.close()
                                    conn.close()
                                else:
                                    user_id = result[0]  # integer user_id

                                    input_df = st.session_state.get("input_df")
                                    prediction = st.session_state.get("prediction")

                                    if input_df is None or prediction is None:
                                        st.warning("Please make a prediction first before saving.")
                                    else:
                                        try:
                                            if label_encoder is not None and hasattr(label_encoder, 'inverse_transform'):
                                                # Pastikan prediction adalah int (misalnya hasil prediksi model)
                                                if isinstance(prediction, int) and prediction < len(label_encoder.classes_):
                                                    label = label_encoder.inverse_transform([prediction])[0]
                                                elif isinstance(prediction, str) and prediction in label_encoder.classes_:
                                                    label = prediction  # sudah berupa string label
                                                else:
                                                    raise ValueError("Prediction is not a valid class or index.")
                                            else:
                                                label = str(prediction)
                                        except Exception as e:
                                            st.warning(f"⚠️ Label decoding failed: {e}")
                                            label = str(prediction)


                                        values = (
                                            user_id,
                                            now.date(),
                                            int(input_df.at[0, 'age']),
                                            str(input_df.at[0, 'job']),
                                            float(input_df.at[0, 'balance']),
                                            str(input_df.at[0, 'housing']),
                                            str(input_df.at[0, 'loan']),
                                            str(input_df.at[0, 'contact']),
                                            str(input_df.at[0, 'month']),
                                            int(input_df.at[0, 'campaign']),
                                            int(input_df.at[0, 'pdays']),
                                            str(input_df.at[0, 'poutcome']),
                                            str(label)
                                        )

                                        insert_query = """
                                            INSERT INTO history_dex (
                                                user_id, date, age, job, balance, housing, loan, 
                                                contact, month, campaign, pdays, poutcome, prediction
                                            )
                                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                        """

                                        cur.execute(insert_query, values)
                                        conn.commit()
                                        cur.close()
                                        conn.close()
                                        st.success("✅ History saved successfully.")

                    except Exception as e:
                        st.error(f"❌ Failed to save history: {e}")

    with tab2:
        if "pipeline" not in st.session_state or "transformed_input" not in st.session_state:
            st.info("Please make a prediction first on the 'Prediction' tab.")
        else:
            tab2_shap_local(st.session_state["pipeline"], st.session_state["transformed_input"])


if __name__ == "__main__":
    app()
