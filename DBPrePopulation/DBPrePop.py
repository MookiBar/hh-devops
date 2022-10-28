import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text

# DEFINE THE DATABASE CREDENTIALS
# CHANGE THESE FOR YOUR LOCAL ENVIRONMENT
user = 'root'
password = 'secretrootpassword'
host = '11.100.10.100'
port = 3306
database = 'hh_db'

# Import CSV
users = pd.read_csv ("testusers.csv", skipinitialspace=True)
users.index+=1
forums = pd.read_csv ("testforum.csv", skipinitialspace=True)
forums.index+=1
localities = pd.read_csv ("testlocality.csv", skipinitialspace=True)
localities.index+=1
metrics = pd.read_csv ("testmetrics.csv", skipinitialspace=True)
metrics.index+=1
organizations = pd.read_csv ("testorganization.csv", skipinitialspace=True)
organizations.index+=1
pages = pd.read_csv ("testpage.csv", skipinitialspace=True)
pages.index+=1
programs = pd.read_csv ("testprogram.csv", skipinitialspace=True)
programs.index+=1
ratings = pd.read_csv ("testratings.csv", skipinitialspace=True)
ratings.index+=1
representatives = pd.read_csv ("testrepresentative.csv", skipinitialspace=True)
representatives.index += 1
status = pd.read_csv ("teststatus.csv", skipinitialspace=True)
status.index+=1


#for now we're just going to populate all of the tables, then later we'll work on a menu
if __name__ == '__main__':
    # create sqlalchemy engine (if you're not using mariadb, this will need to be slightly different)
    engine = create_engine("mariadb+pymysql://{0}:{1}@{2}:{3}/{4}".format(
                user, password, host, port, database
            ))

    users.to_sql('USER', con=engine, if_exists='append', index_label='UserID')
    organizations.to_sql('ORGANIZATION', con=engine, if_exists='append', index_label='OrganizationID')
    representatives.to_sql('REPRESENTATIVE', con=engine, if_exists='append', index=False)
    programs.to_sql('PROGRAM', con=engine, if_exists='append', index_label='ProgramID')
    localities.to_sql('LOCALITY', con=engine, if_exists='append', index_label='LocalityID')
    pages.to_sql('PAGE', con=engine, if_exists='append', index_label='PageID')
    forums.to_sql('FORUM', con=engine, if_exists='append', index_label='ForumID')
    ratings.to_sql('RATINGS', con=engine, if_exists='append', index_label='RatingID')
    status.to_sql('STATUS', con=engine, if_exists='append', index_label='StatusID')
    metrics.to_sql('USAGE_METRICS', con=engine, if_exists='append', index_label='MetricID')






