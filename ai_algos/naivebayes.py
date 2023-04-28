
# Text classification
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

texts = ["Welcome bro", "bye dude","get the fuck out", "hi dude","good bye","shutup fuck er","go fuck yourslef","fuck off"]
# labels = [2, -3, 0,0] # positive to negative emotions
    # or
labels = ["good","good","bad","good","neutral","bad","bad","bad"]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

clf = MultinomialNB()
clf.fit(X, labels)

text = "bye fuck"
X_new = vectorizer.transform([text])

prediction = clf.predict(X_new)
print(prediction)


# Flower Classification
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = GaussianNB()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print("Model Accuracy:", accuracy)

Flower_types = iris['target_names']

prediction = clf.predict([[2,3,4,5]])
print("Predicted Type:", Flower_types[prediction])
