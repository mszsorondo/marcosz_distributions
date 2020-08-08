# marcosz_distributions  
Este paquete sirve para hacer cómputo de distribuciones y muestras.  
### Distribuciones disponibles:   
Binomial  
Normal (Gaussian)   
Geométrica   
### Instalación:
pip install marcosz_distributions  

### Métodos y atributos comunes:
.mean
.stdev
.calculate_mean()
.calculate_stdev()
### Ejemplos de uso:  
from marcosz_distributions import Binomial  
binom = Binomial(0.2, 20) #Binomial de 20 muestras con p(exito) = 0.2  
binom.calculate_mean()  

### En desarrollo:  
Manejo de datos  
Histogramas y gráficos de densidad




