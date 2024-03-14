learn = load_learner('collab_model2.pkl')
# get dataloaders, before using the learner for inference as the learner is empty after loading
dls = CollabDataLoaders.from_df(df_ratings, item_name='movie_name')
# after loading we must add the data back in the learner
learn.dls = dls