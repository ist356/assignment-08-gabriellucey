import pandas as pd
import streamlit as st 


def top_locations(violations_df : pd.DataFrame, threshold=1000) -> pd.DataFrame:
    '''
    Return a dataframe of the locations of parking tickets with $1,000 or more in total aggregate violation amounts.  
    This dataframe is keyed on location (1 row per location) and has two columns: location and amount.  
    There should be 135 rows in this dataframe.
    '''
    pivot = violations_df.pivot_table(index='location', values='amount', aggfunc='sum')
    top_df = pivot[pivot['amount'] >= threshold].sort_values('amount', ascending=False)
    top_df['location'] = top_df.index
    top_df = top_df.reset_index(drop=True)
    return top_df


def top_locations_mappable(violations_df : pd.DataFrame, threshold=1000) -> pd.DataFrame:
    '''
    get top locations then add lat and long from the original dataframe.  
    Again this dataframe is keyed on location (1 row per location) and 4 columns: location, lat, lon, amount  
    Make sure you have the same number of rows as the top_locations dataframe
    '''
    top_df = top_locations(violations_df, threshold)
    combined = top_df.merge(violations_df[['location', 'lat', 'lon']], on='location', how='left').drop_duplicates(subset='location').reset_index(drop=True)
    return combined


def tickets_in_top_locations(violations_df : pd.DataFrame, threshold=1000) -> pd.DataFrame:
    '''
    Return a dataframe of the parking tickets that were issued in the top locations.  
    This dataframe is keyed on ticket number and has the same columns as the original dataframe.  
    It should just be a subset of the original dataframe where the location one of the top locations.  
    There should be 8,109 rows in this dataframe.
    '''
    top_df = top_locations(violations_df, threshold)
    del top_df['amount']
    combined = violations_df.merge(top_df, on='location', how='inner').reset_index(drop=True)
    return combined

if __name__ == '__main__':
    '''
    Main ETL job. 
    '''
    import streamlit as st
    import pandas as pd

    df = pd.read_csv('./cache/final_cuse_parking_violations.csv')
    top = top_locations(df)
    top.to_csv('./cache/top_locations.csv', index=False)
    locations = top_locations_mappable(df)
    locations.to_csv('./cache/top_locations_mappable.csv', index=False)
    top_tickets = tickets_in_top_locations(df)
    top_tickets.to_csv('./cache/tickets_in_top_locations.csv', index=False)
    st.write(top)
    st.write(locations)
    st.write(top_tickets)