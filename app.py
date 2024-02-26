import pickle as p 
import streamlit as st 

def recommend(selected_movie) :
    recommendation_list = []
    movie_index = movies[movies['Title'] == selected_movie].index[0] 
    distance = similarity[movie_index]
    
    recommended = sorted(list(enumerate(distance)) , reverse = True , key = lambda x : x[0])[1:11]
    
    for mov in recommended : 
        recommendation_list.append(movies.iloc[mov[0]].Title)
        
    return recommendation_list 

movies = p.load(open('artifacts\pickle\movies.pkl' , 'rb'))
similarity = p.load(open('artifacts\pickle\similarity.pkl' , 'rb'))


st.header('Movie Recommendation System')

selected_movie = st.selectbox("Select a movie to recommend" , movies['Title'])

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    for i in recommendations: 
        st.write(i)
        
        
        
st.divider()
st.write("Github Repo: https://github.com/shavilya/Movie-Recommendation-System")
st.write("Kaggle : https://www.kaggle.com/shavilyarajput")
st.write("Linkedin : https://www.kaggle.com/shavilyarajput")