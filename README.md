# ThepandemicbehindThePandemic
Final codes and Discoveries for final project of the course Statistical Learning 2019/2020 at La Sapienza, first Year course in Data Science Master's degree. Group01 (5 people)

## NO Data except some little exception are here on the repository for reasons of IP. Anyone interested can send an email to leonardoplacidi@gmail.com
![](Screenshot.png)

You can see there are different folders each with specific content.<br>

## CovidDataCollection
Files to collect/analyze data for national and regional developing of Covid spread, data took from https://github.com/pcm-dpc/COVID-19 (La Protezione Civile data).<br>
`GenerationDsetsRegioniCovid.ipynb` Here we collected the data region by region (24feb-end of jun, but didn't use it all) and added some features.<br>
`GenerationUniqueDBNazionaleCovid.ipynb` Here we collected the data for all Italy (24feb-end of jun, but used only until end of May period) and added some features.<br>

## RedditDataCLassbyHand
handmade method to create a userfriendly compilation of a train data in which we classified the sentiment of 540 comments by hand. <br>
`DATAREDDITAMANO.ipynb` code to create an interactive way of filling a train data in which we were classifying by hand the sentiment. <br>
`AMANOREDDIT.csv` Is the actual dataset, only data we uploaded here for IP reasons.

## SentimentAnalysis
Python notebooks for performing sentiment analysis, methods used in it are SVD, SVM, Nayve Bayes, BERT model.<br>
`finalSVD123RedditPolarityMethod1.ipynb` methods used in it are SVD, SVM, Nayve Bayes, BERT model, all to find that BERT is the best model.<br>
`LittleProcessingONRedditDataAndMegathreads.ipynb` Here we just did some formatting on the data because we needed it to later be able to create the train set and plot some analysis of the sentiment by date.


## Amazon-review-scraper-master 
A library that we borrowen from https://github.com/shreyas707/Amazon-Review-Scraper and modified a little to get the data we wanted about reviews (used to create train data for sentiment analysis) <br>

## <br>



## article_analysis/

`data/` Your datasets for the analysis go here. 

`Articles_Dataset_Preprocessor.ipynb` Used to perform preprocessing (special character removal, stemming and more) on the original dataset of articles. Outputs the preprocessed dataset.

`Classifiers.ipynb` Here we did some testing on the classifiers relevant to our analysis. Contains LDA and NMF. Also used to add a column to the dataset - the "updated" dataset will not be stored locally nor overwrite the one used.

`Covid_Articles_Statistics.ipynb` Here is applied the *dummy classifier*, the one using arbitrary keywords. There are also some plots and metrics to see how it performed, comparing the number of flagged articles to the actual numbers of new cases. Test is performed on the national scale. 

`Predictions.ipynb` Actual prediction of different quantitative information from the Protezione Civile dataset. Classification is done through NMF while regression on said ProCiv data is done through a Random Forest Regressor.
Included are the plots to see how our method performed. 

`Predictions_Without_Timestamp.ipynb` Predictions, same as *Predictions.ipynb* but without considering the date (converted to a timestamp) that is included with the articles. Basically considers only words and their frequencies (Bag of Words).

`Region Analysis.ipynb` Exploratory analysis aided by the NMF classificator to check news behaviour over time. Data is first explored by region, then by zone (North, Centre, South, Islands).

`plots.zip` The plots we got from our scripts.

## creating-article-dataset/

The scripts here are just for demonstrating purposes.

This folder contains downloaders and parsers useful for downloading data from webpages. 

`multithread_update_all_content.py` This files contains the calls to the news parsers, where each parser has a thread to run independently from the others. 

`singlethread_update_all_content.py` Same as previous file, though no implementation for multithreading is provided. It was useful as a testbench for the parsers.

`scraping_quotidiani.py` Scraping of the new outlets URLS and info from the quotidiani.net website.

`downloaders/page_parsers/*.py` Here are all the scripts to parse web pages and extract partial article information from them. 

`page_downloaders/*.py` Specific downloaders for web pages. Might seem incomplete, though sometimes it's just a matter of changing the target URL.

`newsparsers/*.py` Here are all the news outlets website parsers able to extract all the information from an article. 

`newsparsers/parser_template.py` This is the template for writing a news parser. 



