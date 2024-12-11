import os
from supabase import create_client, Client
from dotenv import load_dotenv
from nba_api.stats.endpoints import playercareerstats

load_dotenv()




url: str = os.environ.get("ON_ONE_PSQL_URL")
key: str = os.environ.get("ON_ONE_PSQL_KEY")
# print(url, key)
# supabase: Client = create_client(url, key)

# print(supabase)

# Nikola Jokić
career = playercareerstats.PlayerCareerStats(player_id='203999') 

# pandas data frames (optional: pip install pandas)
print(career.get_data_frames()[0])

# json
# career.get_json()

# dictionary
# print(career.get_dict())