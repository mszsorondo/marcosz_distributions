# marcosz_distributions
Installation: >> pip install marcosz_distributions  
This libyary computes and displays graphs of probability distributions.  

#Current available distributions:  
Binomial(prob,size)  
Gaussian/Normal (mu,sigma) 
General
###Attributes:
mean  
stdev
###Methods:
.read_data_file(filename) #para leer muestras dentro de archivos de texto  
.calculate_mean()  
.calculate_stdev(sample=True)  
.plot_histogram()  
.pdf(x)  
.plot_histogram_pdf()  
####Distribution operators:
For now, addition between distributions is the only available operation.  
Addition can be performed simply by using the common addition ("+") sign.  

#Under development
Geometric  
Negative Binomial