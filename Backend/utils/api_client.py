from .utility import API_Verbs

class NBA_Client(API_Verbs): 
    def __init__(self):
        super().__init__()
    
    def get_team_id(self, team_param: str):
        response =  self.get(endpoint=f'teams?search={team_param}?')
        print(response)