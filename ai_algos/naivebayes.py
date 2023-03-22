
# Text classification
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

# Create the training data
texts = ["Welcome bro", "bye dude","get the fuck out", "hi dude","good bye","shutup fuck er","go fuck yourslef","fuck off"]
# labels = [2, -3, 0,0] # positive to negative emotions
    # or
labels = ["good","good","bad","good","neutral","bad","bad","bad"]

# feature extractor
vectorizer = CountVectorizer()

#  texts to a bag of words representation
X = vectorizer.fit_transform(texts)

# Naive Bayes model
clf = MultinomialNB()

# Train the model on the data
clf.fit(X, labels)

# Predict the class of a new text
text = "bye fuck"
X_new = vectorizer.transform([text])

prediction = clf.predict(X_new)
print(prediction)


# # Flower Classification
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
y = iris.target

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#  Naive Bayes model
clf = GaussianNB()

# Train the model on the training data
clf.fit(X_train, y_train)

# Model Accuracy
accuracy = clf.score(X_test, y_test)
print("Model Accuracy:", accuracy)

# Model Prediction
# input format [sepal length (cm), sepal width (cm), petal length (cm), petal width (cm)]
Flower_types = iris['target_names']

prediction = clf.predict([[2,3,4,5]])
print("Predicted Type:", Flower_types[prediction])
