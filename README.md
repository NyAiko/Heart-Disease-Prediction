# Heart Disease Prediction

Heart disease is a leading cause of death in many countries and can affect individuals regardless of their age. This project aims to develop tools that accelerate heart disease diagnosis based on a few attributes. The dataset used to train the model is sourced from the "UCI Machine Learning Repository".

#### References:
- Dataset: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Heart+Disease)
#### Research papers:
- Detrano, R., Janosi, A., Steinbrunn, W., Pfisterer, M., Schmid, J., Sandhu, S., Guppy, K., Lee, S., & Froelicher, V. (1989). [International application of a new probability algorithm for the diagnosis of coronary artery disease.](http://rexa.info/paper/b884ce2f4aff7ed95ce7bfa7adabaef46b88c60c)
- David W. Aha & Dennis Kibler. "[Instance-based prediction of heart-disease presence with the Cleveland database.](http://rexa.info/paper/0519d1408b992b21964af4bfe97675987c0caefc)"
- Gennari, J.H., Langley, P, & Fisher, D. (1989). [Models of incremental concept formation.](https://www.sciencedirect.com/science/article/abs/pii/0004370289900465)


## Exploratory Data Analysis:
To understand the data, we performed exploratory data analysis (EDA). This included descriptive statistics and visualization of the distribution of each numerical variable. Additionally, we examined the correlations between features to gain insights into the relationships within the dataset.

![Distribution of Numerical Variables](https://user-images.githubusercontent.com/105801284/204309100-30ce72db-e078-498c-945f-266dd12fe2fa.png)
![Correlation Heatmap](https://user-images.githubusercontent.com/105801284/204309178-9e1c86cc-07b4-4597-9689-78c48e90508b.png)

## Model Building:
The data was preprocessed using the following steps:
- "RobustScaler" to rescale the numerical features based on their median and interquartile range.
- "OneHotEncoder" to encode categorical variables into binary vectors.
- "SelectFromModel" to select the most relevant input variables by training a Stochastic Gradient Descent Classifier model.

For model selection, we focused on maximizing the "recall" and "F1" score. The chosen model achieved an F1 score of 0.86 and a recall of 0.87 on the test set, and an F1 score of 0.87 and a recall of 0.86 on the validation set. The model pipeline can be summarized as follows:

![Model Pipeline](https://user-images.githubusercontent.com/105801284/204309616-315f975e-38d3-462b-a119-cb6fe130b1de.jpg)

## Streamlit Web App:
We have developed a user-friendly Streamlit web application that utilizes the trained machine learning models. The app enables users to make accurate heart disease diagnoses through a graphical user interface. Please follow the link below to access the application.


## Conclusion and Future Work:
In this project, we have successfully developed a heart disease prediction system using machine learning techniques. The trained model demonstrates promising results, achieving high accuracy, recall, and F1 scores. 

Future work may involve expanding the dataset, exploring advanced feature engineering techniques, or incorporating additional machine learning algorithms for comparison. We also aim to continuously improve the web application by incorporating user feedback and adding more interactive features.

Your feedback and contributions to this project are highly appreciated!
