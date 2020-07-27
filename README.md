# marcosz_distributions
Installation: >> pip install marcosz_distributions  
This library computes and displays graphs of probability distributions.  

<h1>Current available distributions:  </h1>
Binomial(prob,size)  
Gaussian/Normal (mu,sigma) 
General

<h3>Attributes:</h3>
mean  
stdev

<h3>Methods:</h3>
.read_data_file(filename) #para leer muestras dentro de archivos de texto  
.calculate_mean()  
.calculate_stdev(sample=True)  
.plot_histogram()  
.pdf(x)  
.plot_histogram_pdf()  

<h4>Distribution operators:</h4>
For now, addition between distributions is the only available operation.  
Addition can be performed simply by using the common addition ("+") sign.  

<h3>Under development</h3>
Geometric  
Negative Binomial