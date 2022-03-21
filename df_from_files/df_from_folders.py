#Create df for all data
all_df = pd.DataFrame()

# Read data and concatinating to a general df
for current_path, dirs, files in os.walk(p):
    for file in files:
        #construct full path to file
        data_path =(current_path+'/'+file)
        
        #Getting data
        temp_df = pd.read_csv(data_path)
        
        #Getting date and time from folder names
        path_parts = current_path.split('/')
        date = path_parts[-2]
        name = path_parts[-1]
        
        #Adding date and time to df
        temp_df['date'] = date #current_path.split('/')[-2]
        temp_df['time'] = name #current_path.split('/')[-1]

        
        all_df = pd.concat((all_df, temp_df))