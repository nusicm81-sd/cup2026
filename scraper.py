import requests, json, os

def update_standings():
    # هذا الكود يستخرج البيانات ويضمن تسميتها بشكل ثابت
    url = "https://api.football-data.org/v4/competitions/WC/standings"
    headers = {'X-Auth-Token': os.getenv('API_KEY')}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        formatted_data = []
        for table in data['standings']:
            teams = [{"name": t['team']['name'], "pts": t['points'], "played": t['playedGames'], 
                      "won": t['won'], "drawn": t['draw'], "lost": t['lost'], 
                      "goalDifference": t['goalDifference']} for t in table['table']]
            formatted_data.append({"group": table['group'].replace('_', ' '), "teams": teams})
        with open('groups.json', 'w', encoding='utf-8') as f:
            json.dump(formatted_data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__": update_standings()
