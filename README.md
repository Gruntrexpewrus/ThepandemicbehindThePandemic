# ThepandemicbehindThePandemic
Final codes and Discoveries for final project of the course Statistical Learning 2019/2020 at La Sapienza. Group01
![](Screenshot.png)

You can see there are different folders each with specific content.<br>

## CovidDataCollection
Files to collect/analyze data for national and regional developing of Covid spread, data took from https://github.com/pcm-dpc/COVID-19 (La Protezione Civile data).<br>

## RedditDataCLassbyHand
handmade method to create a userfriendly compilation of a train data in which we classified the sentiment of 540 comments by hand. <br>

## SentimentAnalysis
Python notebooks for performing sentiment analysis, methods used in it are SVD, SVM, Nayve Bayes, BERT model. <br>

## Amazon-review-scrape-master 
A library that we borrowen from https://github.com/shreyas707/Amazon-Review-Scraper and modified a little to get the data we wanted about reviews (used to create train data for sentiment analysis) <br>

## <br>



# article_analysis

`data/` Your datasets for the analysis go here. 

`Articles_Dataset_Preprocessor.ipynb` Used to perform preprocessing (special character removal, stemming and more) on the original dataset of articles. Outputs the preprocessed dataset.

`Classifiers.ipynb` Here we did some testing on the classifiers relevant to our analysis. Contains LDA and NMF. Also used to add a column to the dataset - the "updated" dataset will not be stored locally nor overwrite the one used.

`Covid_Articles_Statistics.ipynb` Here is applied the *dummy classifier*, the one using arbitrary keywords. There are also some plots and metrics to see how it performed, comparing the number of flagged articles to the actual numbers of new cases. Test is performed on the national scale. 

`Predictions.ipynb` Actual prediction of different quantitative information from the Protezione Civile dataset. Classification is done through NMF while regression on said ProCiv data is done through a Random Forest Regressor.
Included are the plots to see how our method performed. 

`Predictions_Without_Timestamp.ipynb` Predictions, same as *Predictions.ipynb* but without considering the date (converted to a timestamp) that is included with the articles. Basically considers only words and their frequencies (Bag of Words).

`Region Analysis` Exploratory analysis aided by the NMF classificator to check news behaviour over time. Data is first explored by region, then by zone (North, Centre, South, Islands).

`plots.zip` The plots we got from our scripts.
