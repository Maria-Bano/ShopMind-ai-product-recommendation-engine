import google.generativeai as genai
from products.models import Product as ModelProduct,UserProductClick
import pandas as pd
from GenAI import first_order_logic 
import xgboost as xgb,shap
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MultiLabelBinarizer


genai.configure(api_key="AIzaSyAyv64aLWQw6wvugGGduj99XPoQl5-N33g")
model = genai.GenerativeModel("gemini-2.0-flash-exp")
def load_data():
    products = ModelProduct.objects.all()
    df = pd.DataFrame([{
    'id': product.id,
    'name': product.name,
    'min_price': product.min_price,
    'max_price': product.max_price,
    'description': product.description,
    'categories': product.categories.split(','),
    'tags': product.tags_list.split(',')
    } for product in products])
    return df

def load_user_clicks(user_id):
    user_clicks = UserProductClick.objects.filter(user__id = user_id)
    user_clicks_df = pd.DataFrame([{
        'user_id': click.user.id,
        'product_id':click.product.id
    } for click in user_clicks])
    return user_clicks_df

def get_recommendation(user_id):
    df = load_data()
    clicks = load_user_clicks(user_id)
    response = model.generate_content(f"Here is the list of products that are present in my data base {df} and here are the products clicked by the user{clicks} so recommend me the 10 best products that are same as clicked products note only give me the product id's in the form of a string where id's separated by commas don't give anything else in response")
    try:
        s = response.text[:-2]
        lst = [int(x.strip()) for x in s.split(',')]
        if len(clicks) != 0:
            print(lst)
            referred = df[df['id'].isin(lst)].copy()
            explain_recommendations(clicks, referred)
            return lst
        else:
            print("Returing None")
            return None
    except:
        print("Error occured in llm.")
        if clicks is not None and not clicks.empty:
            lst = first_order_logic.recommend_products(user_id)
            referred = df[df['id'].isin(lst)].copy()
            explain_recommendations(clicks, referred)
            return lst
        

def preprocess_tags(all_products):
    """
    Convert list-type 'tags' column into dummy variables.
    """
    # Convert 'tags' column (which contains lists) into dummy variables
    tag_dummies = all_products['tags'].apply(lambda x: pd.Series(1, index=x)).fillna(0)
    all_products = all_products.drop(columns=['tags'])  # Remove the original 'tags' column
    all_products = pd.concat([all_products, tag_dummies], axis=1)  # Add the dummy columns
    return all_products


def explain_recommendations(Clicked_Products, Recommended_Products):
    # Step 1: Prepare the data for feature extraction (categories and tags)
    
    # Initialize MultiLabelBinarizer to convert the list of categories and tags into a one-hot encoded form
    mlb_categories = MultiLabelBinarizer()
    mlb_tags = MultiLabelBinarizer()
    
    # Fit the encoder on the categories and tags from both Clicked_Products and Recommended_Products
    all_categories = Clicked_Products['categories'].tolist() + Recommended_Products['categories'].tolist()
    all_tags = Clicked_Products['tags'].tolist() + Recommended_Products['tags'].tolist()
    
    mlb_categories.fit(all_categories)
    mlb_tags.fit(all_tags)
    
    # Transform categories and tags into one-hot encoded vectors
    clicked_categories_encoded = mlb_categories.transform(Clicked_Products['categories'])
    clicked_tags_encoded = mlb_tags.transform(Clicked_Products['tags'])
    recommended_categories_encoded = mlb_categories.transform(Recommended_Products['categories'])
    recommended_tags_encoded = mlb_tags.transform(Recommended_Products['tags'])
    
    # Step 2: Combine the features into a single dataset for both Clicked and Recommended products
    # Here, we're simply concatenating the encoded categories and tags for each product
    clicked_features = pd.DataFrame(clicked_categories_encoded).join(pd.DataFrame(clicked_tags_encoded))
    recommended_features = pd.DataFrame(recommended_categories_encoded).join(pd.DataFrame(recommended_tags_encoded))
    
    # Step 3: Prepare the labels for the training (binary classification - clicked or not clicked)
    clicked_labels = [1] * len(Clicked_Products)  # Products that were clicked
    recommended_labels = [0] * len(Recommended_Products)  # Products that are recommended, but not yet clicked
    
    # Combine the Clicked_Products and Recommended_Products features and labels
    features = pd.concat([clicked_features, recommended_features], ignore_index=True)
    labels = clicked_labels + recommended_labels
    
    # Step 4: Train a RandomForestClassifier on the combined data
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(features, labels)
    
    # Step 5: Use SHAP to explain the recommendations
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(recommended_features)
    
    # Step 6: Generate a natural language explanation for why these products are recommended
    for i, product in recommended_features.iterrows():
        explanation = f"Recommendation for '{Recommended_Products.iloc[i]['name']}': This product is recommended because the following features are influential:"
        
        # Get the SHAP values for the product (only the second set, because we are explaining recommendations)
        feature_shap_values = shap_values[1][i]
        
        # Sort features by importance
        sorted_indices = feature_shap_values.argsort()
        
        # Explain which features had the most influence (categories or tags)
        for index in sorted_indices[-5:]:  # Show top 5 influential features
            feature_name = mlb_categories.classes_[index] if index < len(mlb_categories.classes_) else mlb_tags.classes_[index - len(mlb_categories.classes_)]
            explanation += f" {feature_name} had a significant influence on the recommendation."
        
        print(explanation)