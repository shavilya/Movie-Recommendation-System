import streamlit as st 
import pandas as pd 
import pickle 

movies = pickle.load(open('artifacts/pickle/movies.pkl' , 'rb'))
similarity = pickle.load(open('artifacts/pickle/similarity.pkl' ,'rb'))

def recommend(movie_title) : 
    recommendations = []
    movie_index = movies[movies['Title'] == movie_title].index[0]
    distance  = similarity[movie_index]
    
    movie_list = sorted(list(enumerate(distance)) , reverse = True , key = lambda x : x[1])[1:11]

    for i in movie_list : 
        
        recommendations.append(movies.iloc[i[0]].Title)
        
    return recommendations 

st.header('Movie Recommendation System')
st.divider()


selected_movie = st.selectbox("Choose a movie to get recommendations?" , options= movies['Title'])

if st.button("Recommeded") : 
    recommended_movies = recommend(selected_movie)
    st.write(recommended_movies)

    