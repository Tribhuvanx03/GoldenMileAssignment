# Prerequisites   
* Python 3.8   
* Hugging Face API Token (for Llama 3.1)   

# Installation & Run  

1. Clone the Repo
```bash
https://github.com/Tribhuvanx03/GoldenMilePlatform.git
cd GoldenMile
```   
2. Install Dependencies
``` bash
pip install -r requirements.txt
```
3. Run the App
```bash
streamlit run app.py
```

# Docker Deployment  
To run the app in a standardized, isolated environment (not tested completely). If it fails, run the app by vanilla methods.

1. Build the Image
```bash
docker build -t golden-mile-app -f docker/Dockerfile .
```
2. Launch the Container
```bash
docker run -p 8501:8501 golden-mile-app
```

# File Structure   
```plaintext
GoldenMile/
├── app.py                  # Streamlit UI Entry point
├── requirements.txt        # Project dependencies
├── docker/
│   └── Dockerfile          # Production container configuration
├── src/
│   ├── models/             # XGBoost inference & model artifacts
│   ├── rag/                # Vector store (ChromaDB) & retrieval logic
│   └── llm/                # Llama 3.1 Prompt engineering & reasoning engine
├── data/
│   ├── raw/                # Historical property listings
│   └── knowledge_base/     # RERA, News, and Locality PDFs
│   └── processed/          # Project ready dataset (after undergoing EDA and feature engineering)
```

# Methodology   
* The Estimator: We use a Gradient Boosting model (XGBoost) to handle non-linear relationships between square footage, location density, and amenity scores.
* The Context Retriever: Our RAG pipeline uses ChromaDB to index locality profiles, ensuring the AI "knows" about the latest infrastructure projects before making a recommendation.
* The Reasoner: Llama 3.1 8B acts as the investment analyst, synthesizing the numerical output from the model with the textual output from the retriever.
