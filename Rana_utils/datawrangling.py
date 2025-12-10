print("Hello from test.py")

# fix_column_names function to fix column names in a dataframe
def fix_column_names(df,df_cols):
    
    #Lower Case the Columns
    df.columns = df.columns.map(str.casefold)
    #Column's naming convention as Title 
    df.columns = df.columns.str.title()
    # remove all the leading (spaces at the beginning) and trailing (spaces at the end)
    df.columns = df.columns.str.strip()
    # remove non-word characters
    df.columns = df.columns.str.replace('\W', '', regex=True)

    df.columns = ["Column_"+str(a) if a.isnumeric()  else a for i, a in enumerate(df.columns)]

    df.columns = ["Column_"+str(i) if 'Unnamed' in a  else a for i, a in enumerate(df.columns)]

    # col_after_Fix=df.columns
    df_cols['Columns_After']=df.columns

     
    return df,df_cols   


# custom pie chart function to be used in EDA notebook
def make_pie_chart(matplot_plt,data_frame,pie_chart_labels,pie_chart_values,colors,title,image_path,image_name):
    matplot_plt.figure(figsize=(6, 6))
    matplot_plt.pie(data_frame[pie_chart_values], labels = data_frame[pie_chart_labels], colors = colors, autopct='%.0f%%')
    matplot_plt.title(title, bbox={'facecolor':'0.8', 'pad':5})
    matplot_plt.savefig(image_path+image_name, format='png', bbox_inches='tight')
    matplot_plt.show()
