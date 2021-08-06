# msa-project-order-prediction

Idea for the project:
We see in the world right now that hunger and malnutrition are one of the major issues faced by many developing countries. Though there are people around the world dying due to hunger we still see a lot of food wasted in large restaurant chains and food joints where they order in bulk and throw away the materials if they dont get enough orders. I thought that AI might come in handy to predict the amount of raw materials that should be ordered by the food chains to ensure that no food is wasted. A number of factors like base rate of restaurant, frequeny of certain customers and other parameters can be used to predict the future food requirement. This will really help in preventing wastage of food and ensuring that food reaches to people who need it.

Approach for the problem:
The approach that I have choosen for this solution is to use Azure Machine learning studio and using the existing food order dataset from Kaggle. I have created a training dataset from the available dataset which can be used on test data and to predict future orders for the restaurant. Since, we have to predict a certain value I have used the Linear regression model from the different ones available on Azure. We can use the service created in Azure Machine Learning to get a prediction of what number of orders are supposed to be received for particular data provided as input to the service.

Implementation:
I have followed the learning path from Microsoft Learn modules to create a Pipeline to create a training model. This is then further used to create an inference pipeline which will help us test the predictions made by the service.Later the pipeline is deployed as a REST API on the Container instance and accessed using the python script to display prediction values. The server.py file contains the REST endpoint and key used to connect to the service.
