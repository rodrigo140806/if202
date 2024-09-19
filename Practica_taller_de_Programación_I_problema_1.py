class Persona:
    def _init_ (self, nombre):
        self.Rodrigo_Huamaní = nombre
    def caminar(self,distancia_de_Rodrigo_Huamaní):
        print(f"{self.Rodrigo_Huamaní} ha caminado {distancia_de_Rodrigo_Huamaní} km")

class Atleta(Persona):
    def entrada (self, distancia_de_Rodrigo_Huamaní):
        if distancia_de_Rodrigo_Huamaní <= 20:
         calorias_de_Rodrigo_Huamaní = distancia_de_Rodrigo_Huamaní *500
         self.calorias_consumidas_Rodrigo_Huamaní += calorias_de_Rodrigo_Huamaní
         print(f"{self.Rodrigo_Huamaní} ha entrenado {distancia_de_Rodrigo_Huamaní} kms y consumido {calorias_de_Rodrigo_Huamaní} cal")
    
        else:
         print("La distancia de entrenamiento debe ser menos o igual a 20 kms")
    def competir(self, distancia_de_Rodrigo_Huamaní):
       if distancia_de_Rodrigo_Huamaní > 20 and distancia_de_Rodrigo_Huamaní <= 30:
          calorias_de_Rodrigo_Huamaní = distancia_de_Rodrigo_Huamaní *750
          self.calorias_consumidas_Rodrigo_Huamaní += calorias_de_Rodrigo_Huamaní
          print(f"{self.Rodrigo_Huamaní} ha competido en {distancia_de_Rodrigo_Huamaní} kms y consumio {calorias_de_Rodrigo_Huamaní} cal")
       else:
          print("La distancia de competencia debe estar entre 20 y 30 kms")
        

atleta = Atleta("Rodrigo Huamani")
atleta.caminar (2)
atleta.entrada(15)
atleta.competir(25)






    
