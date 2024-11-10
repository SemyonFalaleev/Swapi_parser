from models import SwapiPeople

def serializer(json_data):
    
    json_data['films'] = ", ".join(json_data.get('films', []))
    json_data['species'] = ", ".join(json_data.get('species', []))
    json_data['starships'] = ", ".join(json_data.get('starships', []))
    json_data['vehicles'] = ", ".join(json_data.get('vehicles', []))

    swapi_person = SwapiPeople(
        id=json_data.get('id'),
        name=json_data.get('name'),
        films=json_data.get('films'),
        height=json_data.get('height'),
        mass=json_data.get('mass'),
        hair_color=json_data.get('hair_color'),
        skin_color=json_data.get('skin_color'),
        eye_color=json_data.get('eye_color'),
        birth_year=json_data.get('birth_year'),
        gender=json_data.get('gender'),
        homeworld=json_data.get('homeworld'),
        species=json_data['species'], 
        starships=json_data['starships'],  
        vehicles=json_data['vehicles'], 
        url=json_data.get('url'),
        created=json_data.get('created'),
        edited=json_data.get('edited')
    )
    
    return swapi_person