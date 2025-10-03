# Telco Customer Churn Prediction 📊  

Proyek ini bertujuan untuk memprediksi **churn pelanggan** pada perusahaan telekomunikasi menggunakan dataset **Telco Customer Churn**. Analisis dilakukan melalui tahapan eksplorasi data, preprocessing, pemodelan machine learning, hingga visualisasi interaktif.  

---

## 🔍 Tujuan Proyek
- Mengidentifikasi faktor-faktor utama yang memengaruhi churn pelanggan.
- Membandingkan beberapa pendekatan preprocessing seperti **tuning hyperparameter**, **binning**, dan **feature selection**.
- Membangun model machine learning (Logistic Regression) untuk prediksi churn.
- Menyajikan hasil model dalam bentuk **dashboard interaktif** (Streamlit & Tableau).

---

## 📂 Struktur Notebook
Notebook utama: **`Notebook.ipynb`**

Tahapan analisis yang dilakukan:
1. **Exploratory Data Analysis (EDA)**  
   - Analisis distribusi churn.  
   - Visualisasi demografi pelanggan (gender, usia, senior citizen).  
   - Analisis perilaku layanan (Internet, Contract, Payment Method).  

2. **Data Preprocessing**  
   - Handling missing values.  
   - Encoding categorical features.  
   - Scaling numerical features.  
   - Feature selection untuk memilih variabel paling berpengaruh.  

3. **Modeling**  
   - Model utama: **Logistic Regression**.  
   - Eksperimen dengan:  
     - Benchmark  
     - Hyperparameter Tuning  
     - Binning  
     - Feature Selection  

   - **Hasil (Akurasi / ROC-AUC)**  
     - Train Set: Feature Selection menghasilkan skor tertinggi (0.7733).  
     - Test Set: Feature Selection juga memberikan performa terbaik (0.7681).  

4. **Interpretasi Model**  
   - Koefisien regresi dan odds ratio.  
   - Faktor yang meningkatkan risiko churn: `SeniorCitizen`, `MultipleLines`, `StreamingMovies`, `Electronic Check`, `PaperlessBilling`.  
   - Faktor yang menurunkan risiko churn: `Dependents`, `OnlineSecurity`, `TechSupport`, `Contract One/Two Years`.  

5. **Deployment**  
   - Model disimpan menggunakan **Joblib**.  
   - Aplikasi interaktif dibuat dengan **Streamlit**.  
   - Visualisasi tambahan menggunakan **Tableau Dashboard**.  

---

## 🚀 Deployment
- **Streamlit App**: [Klik di sini](https://telco-company-churn-prediction.streamlit.app/)  
- **Tableau Dashboard**: [Klik di sini](https://public.tableau.com/app/profile/lie.benedict.yahliel/viz/TelcoCompany_17595010148000/Dashboard1)  

---

## 🛠️ Tools & Library
- **Python**: Pandas, Numpy, Scikit-learn, Matplotlib, Seaborn, Joblib  
- **Deployment**: Streamlit  
- **Visualization**: Tableau  
