# Heart Disease Prediction
Heart disease lead to cause death in most of European countries and it can affect anyone with no regards of the age. We are going to build tools for doctors that accelerates heart diagnosis based on few attributes. The dataset used to train the model is from the “UCI Machine Learning Repository”. 
#### References: 
  Dataset: UCI Machine Learning Repository
#### Research papers: 
* Detrano, R., Janosi, A., Steinbrunn, W., Pfisterer, M., Schmid, J., Sandhu, S., Guppy, K., Lee, S., & Froelicher, V. (1989). International application of a new probability algorithm for the diagnosis of coronary artery disease. American Journal of Cardiology,64,304--310.    [link](http://rexa.info/paper/b884ce2f4aff7ed95ce7bfa7adabaef46b88c60c)
* David W. Aha & Dennis Kibler. "Instance-based prediction of heart-disease presence with the Cleveland database."    [link](http://rexa.info/paper/0519d1408b992b21964af4bfe97675987c0caefc)
* Gennari, J.H., Langley, P, & Fisher, D. (1989). Models of incremental concept formation. Artificial Intelligence, 40, 11--61.  [link](sciencedirect.com/science/article/abs/pii/0004370289900465)
#### Requirements:
* Python 3.8
* Scikit-Learn 0.22 or above
* Pandas
* Numpy
* Flask


## Exploratory data analysis:
Most of the time, EDA comes after data cleaning but the data is already prepared for analysis. So, this is the first step to understand the data through some descriptive statistics. These are the summary of the distribution of each numerical variable.
![8477684a-3568-4ca6-886c-0884da36c811](https://user-images.githubusercontent.com/105801284/204309100-30ce72db-e078-498c-945f-266dd12fe2fa.png)
![79190f5f-176a-4615-9899-7dee6a34d860](https://user-images.githubusercontent.com/105801284/204309178-9e1c86cc-07b4-4597-9689-78c48e90508b.png)

## Model Building:
The data is preprocessed with:
-	“RobustScaler” to rescale the numerical features
-	“ OneHotEncoder” to encode the categories to a vector of 0 and 1
-	“SelectFromModel” to select the best parameters from the Stochastic Gradient Descent Classifier model.
When it comes to model building, we will pick the best that brings more value to the problem. For this kind of projects, our metrics for model evaluation are the “recall” and the “F1” score. Recall presents how much we reduced the “False Positive” and “F1” are the harmonic average of the “Precision” and “Recall”.
The model has F1 = 0.9 and Recall = 0.9 on the test set and F1 = 0.9 and Recall = 0.86 on the validation set.
This is the abstract view of the model pipeline.
![heart_disease_pipeline](https://user-images.githubusercontent.com/105801284/204309616-315f975e-38d3-462b-a119-cb6fe130b1de.jpg)
## Flask Web App : 
For this part, we are going to use Flask. The user will enter the diagnostic data as a request and get the probability of heart disease as response.
![Untitled](https://user-images.githubusercontent.com/105801284/204310076-51a3f0af-286d-4d28-b5c2-d26da27cd93c.png)
