import os
import requests
import json

def update_standings():
    api_key = os.getenv('API_KEY')
    # السطر التالي يجب أن يكون داخل الدالة ومزاحاً بـ 4 مسافات فقط
    url = "https://api.football-data.org/v4/competitions/WC/standings"
    headers = {'X-Auth-Token': api_key}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            formatted_data = []
            
            for table in data['standings']:
                group_name = table['group'].replace('_', ' ')
                teams = []
                for t in table['table']:
                    teams.append({
                        "name": t['team']['name'],
                        "pts": t['points'],
                        "played": t['playedGames'],
                        "won": t['won'],
                        "drawn": t['draw'],
                        "lost": t['lost'],
                        "goalDifference": t['goalDifference']
                    })
                formatted_data.append({"group": group_name, "teams": teams})
            
            with open('groups.json', 'w', encoding='utf-8') as f:
                json.dump(formatted_data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_standings()
