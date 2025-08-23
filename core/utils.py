redes = ('instagram', ('twitter', 'x'), 'facebook', 'flickr', 'linkedin')
def obtener_red_social(link: str):
    for red in redes:
        if red in link:
            return red[0]