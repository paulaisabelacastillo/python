meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "GG EZ": "Respuesta usada para decir que la partida de un juego estaba fácil",
            "CHAD": "Palabra empleada para referirse a alguien bienhechor o sereno",
            "COPO DE NIEVE": "Termino usado para referirse a alguien que se ofende facilmente",
            "BAIT": "Palabra usada para referirse a un comentario hecho a proposito para enfurecer",
            "CHAMBEAR": "Sinonímo de forma coloquial a trabajar o laborar",
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print ("La palabra", {word}, "significa:", {meme_dict[word]})
    
else:
    print("lo sentimos, pero esta palabra no esta disponible :´(")
