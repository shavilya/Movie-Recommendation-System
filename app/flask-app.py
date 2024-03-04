from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load the stored models
movies = pd.read_pickle('artifacts/pickle/movies.pkl')
similarity = pickle.load(open('artifacts/pickle/similarity.pkl', 'rb'))

@app.route('/')
def index():
  # Convert movie titles to a list for select box options
  movie_options = movies['Title'].tolist()
  return render_template('index.html', movie_options=movie_options)

@app.route('/recommend', methods=['POST'])
def recommend():  
  selected_movie = request.form['movie_title']
  
  recommendation_list = []
  movie_index = movies[movies['Title'] == selected_movie].index[0] 
  distance = similarity[movie_index]
    
  recommended = sorted(list(enumerate(distance)) , reverse = True , key = lambda x : x[0])[1:11]
    
  for mov in recommended : 
    recommendation_list.append(movies.iloc[mov[0]].Title)
        
  return recommendation_list 

  
  #return render_template('recommendations.html', recommendations=recommended)

if __name__ == '__main__':
  app.run(debug=True)
