Esta es una breve explicación del proyecto.

En primer lugar y para que pueda funcionar el proyecto, se debe de contar con 
unos complementos de software adecuados, estos se pueden encontrar en el archivo
"requeriments.txt". En caso de que necesite instalar alguno de ellos y/o actualizar
los que ya tenga, la siguiente instrucción cumplirá tal cometido:

        pip install -r requeriments.txt´

Vale la pena mencionar que esta instalación debería llevarse a cabo en un entorno
virtual, una de las formas para hacerlo se muestra a continuación:
    
         python3 -m venv venv
         source venv/bin/activate
         
Una vez que ya se tiene todo lo necesario para ejecutar el proyecto, esto es,
el entorno virtual y el software que le da soporte, se debe ejecutar la siguiente 
línea de código

        uvicorn main:app --reload
        
Con esa línea se tiene entonces acceso al proyecto, es decir, se puede interactuar
por medio del navegador con la implementación del parqueadero propuesta por nosotros.

Información que complementa la presentada aquí, junto con una pequeña guía de uso,
puede ser encontrada en el archivo 
        
        Parqueadero - Guía de uso.pdf