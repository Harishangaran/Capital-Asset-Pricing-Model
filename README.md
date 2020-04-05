# Capital-Asset-Pricing-Model
Run linear regression between your benchmark and preferred stock.

CAPITAL ASSET PRICING MODEL USING LINEAR REGRESSION

E(Ri)=Rf+βi[E(Rm)−Rf)]

where

E(Ri)  -  is the expected returnn of the asset.
Rf  - is the risk-free asset, typically a US government bond. #assumed zero
βi  - is the sensitivity of the expected excess asset returns 
    to the expected market returns.
E(Rm)−Rf -  is the considered the risk premium.


The following script allows you to run regression
between a benchamrk index such as S&P500 and a stock.

#Call the capm class as follows:

    capm(benckmark ticker,stock ticker, period)
        eg: capm('^GSPC','MSFT','500d')
        
    #Output
        Regression graph and the regression statistics summary
            beta, alpha, R value, p value and the standard error

#Additionally you can call the cummReturnPlot() method
to plot cummulative return graph.

    eg: capm('^GSPC','MSFT','500d).cummReturnPlot()
