## Movie Recommendation System

This Streamlit application provides a user-friendly interface to explore movie recommendations based on collaborative filtering techniques.

### Features:

Movie Selection: Users can easily choose a movie from a dropdown menu populated with all available titles.<br>
Recommendation Generation: Upon clicking the "Recommend" button, the system suggests ten similar movies based on user selection.<br>
Collaborative Filtering: Recommendations are generated using pre-computed similarity scores between movies, indicating how closely related they are in terms of user ratings.<br>
Requirements:

Python: Ensure you have Python installed (version 3.x recommended) along with the necessary libraries.<br>
Streamlit (https://streamlit.io/)<br>
Pandas (https://pandas.pydata.org/)<br>
Pickle (https://python.readthedocs.io/en/latest/library/pickle.html)<br>
Data Files: The application relies on three pre-processed data files:<br>
  1.movies.pkl: Contains information about the movies, likely including title, genre, and other relevant attributes.<br>
  2.similarity.pkl: Stores the pre-computed similarity matrix used for recommendations.<br>
  3.ratings_cleaned_df.csv: A cleaned DataFrame containing user ratings for various movies.<br>
  
### Usage:

Clone this repository or download the code files.<br>
Install the required Python libraries (pip install streamlit pandas pickle).<br>
Make sure the movies.pkl, similarity.pkl, and ratings_cleaned_df.csv files are located in the app/utils/artifacts directory (adjust the path if needed).<br>
Run the application using streamlit run app.py (replace app.py with your script name if different).<br>

### Expected Behavior:
The application launches in your web browser, displaying a title ("Movie Recommendation System") and a horizontal divider.<br>
A dropdown menu labeled "Choose a movie to get recommendations?" appears, listing all movie titles.<br>
Clicking a movie from the list and then pressing the "Recommended" button triggers the recommendation process.<br>
A list of ten recommended movies, similar to the chosen one, is displayed below.<br>
