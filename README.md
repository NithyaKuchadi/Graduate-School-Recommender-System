# Graduate-School-Recommender-System
As competition for admission into higher education increases, it becomes even more important for applicants to find graduate schools that fit their requirements and expectation. Selecting appropriate schools to apply, however, is a time-consuming process, especially when looking for schools at graduate level due to the various factors in decision making imposed by the schools and applicants. This problem can be addressed by developing a recommender system for graduate admission seekers which can help them to choose graduate school matching their academic profile. 

Data is scraped from edulix.com. The required data is extracted from the HTML by using the python library ‘BeautifulSoup’.

Data Pre-processing Steps:
1. Missing values are replaced with 0
2. Old GRE Quant and Verbal Scores are converted to New Scores.
3. GPA is normalized


Implemented 2 models.
1. K Nearest Neighbors
2. CNN

KNN recommends n universities whereas CNN recommends only 1 university.

Sample Output of KNN:


![](Screenshots/1.png)

![](Screenshots/2.png)

Sample Output of CNN for the scores [159.5744681, 170.212766, 5.0, 3.83] is:

![](Screenshots/3_cnn.png)
