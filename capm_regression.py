# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:21:41 2020

@author: harishangaran

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

"""

import yfinance as yf
import matplotlib.pyplot as plt

from scipy import stats


class capm:
    def __init__(self,benchmark,stock,period):
        self.benchmark = benchmark
        self.stock = stock
        self.period = period
        self.callPrices()
        self.calDailyReturn()
        self.runRegression()
        self.scatterPlot()
        
    def callPrices(self):
        
        # Calling the price from yahoo finance
        self.stockIndex = yf.Ticker(self.benchmark).history(self.period)
        self.asset = yf.Ticker(self.stock).history(self.period)
        
        # Return dataframes of the benchmark index and the stock
        return self.stockIndex,self.asset
    
    def calDailyReturn(self):
        
        # Calculate daily return of benchmark and stock
        self.asset['Daily return'] = self.asset['Close'].pct_change(1)
        self.stockIndex['Daily return'] = self.stockIndex['Close'].pct_change(1)
        
        return self.asset,self.stockIndex

    def runRegression(self):
        
        # Run linear regression
        self.beta,self.alpha,self.r_value,self.p_value,self.std_err = stats.linregress(
            self.asset['Daily return'].iloc[1:],self.stockIndex['Daily return'].iloc[1:])
        
    def scatterPlot(self):
        plt.figure(figsize=(12, 8), dpi=150)
        
        # Plotting scatter
        plt.scatter(self.asset['Daily return'],self.stockIndex['Daily return'],alpha=0.25)
        
        # Plotting fitted line
        # plt.plot(x, intercept + slope*x, 'r')
        plt.plot(self.asset['Daily return'],(self.alpha + (self.beta*self.asset['Daily return'])),c='r')
        plt.xlabel(self.stock)
        plt.ylabel(self.benchmark)
        plt.title('Linear regression of {} vs {}'.format(self.stock,self.benchmark))
        
        # Table of regression statistics
        plt.table(cellText=[[self.beta,self.alpha,self.r_value,self.p_value,
                             self.std_err]],cellLoc='center',colLabels=['BETA','ALPHA',
                            'R VALUE','P VALUE','STD ERROR'],loc='bottom',bbox=[0.0,-0.2,1,0.1])
    
    def cummReturnPlot(self):
        
        # Additional function to plot cummulative return
        # Calculating cummulative return
        self.asset['Cummulative'] = self.asset['Close']/self.asset['Close'].iloc[0]
        self.stockIndex['Cummulative'] = self.stockIndex['Close']/self.stockIndex['Close'].iloc[0]

        # Plotting cummulative return graph
        self.stockIndex['Cummulative'].plot(label=self.benchmark)
        self.asset['Cummulative'].plot(label=self.stock)
        plt.legend()

regress = capm('^GSPC','AAPL','1000d')
