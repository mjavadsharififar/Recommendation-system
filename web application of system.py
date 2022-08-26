import pandas as pd
import streamlit as st

final = pd.read_csv('movies_final.csv',index_col = [0])
movie_sim = pd.read_csv('movie_sim.csv',index_col = [0])

st.title('Welcome to the Movie recommender!')
st.markdown('### Here you can find which movies go with your interests!') #st.header() st.subheader()
st.text('Please select your favourite genre from below drop down list:') #st.write()

genre_list = ['اجتماعی','انیمیشن','اکشن', 'بیوگرافی','تاریخی', 'ترسناک', 'تلویزیونی', 'جنایی'
              , 'جنگی', 'خانوادگی', 'درام', 'رمانتیک', 'فانتزی', 'ماجراجویی', 'موزیکال', 'کمدی', 'کودک', 'راز آلود', 'ورزشی']
genre = st.selectbox("Choose your favorite genre...",['انتخاب کنید'] + genre_list)

if genre == 'انتخاب کنید':
  st.write('You have not selected any genre yet...')
else:
  st.write('so your favorite is {}, Now please select one the movies you have liked from this genre...'.format(genre))
  
  genre_frame = final[final[genre]==1]
  movie = st.selectbox('Select one these movies:',['انتخاب کنید']+list(genre_frame.index))

  try:
    movie_by_genre = movie_sim.loc[list(genre_frame.index),list(genre_frame.index)]
    similar_movies = movie_by_genre[movie].sort_values(ascending = False)
    st.write('According to our Analysis, you might like these movies:')
    if len(similar_movies)>5: #it shows us the 5 best mathc to user selection
        for i in range(1,6):
            st.write(similar_movies.index[i])
    else:
        for i in range (1,len(similar_movies)):
            st.write(similar_movies.index[i])
  except:
    st.write('You have not chosen any movie yet...')
