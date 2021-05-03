import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm
digits = datasets.load_digits()
print(digits.target)
print(digits.images[0])

clf = svm.SVC(gamma=0.001, C=100)
print(len(digits.data))
x = digits.data[:-1]
y = digits.target[:-1] 
clf.fit(x,y)
# print('Prediction:', clf.predict(digits.data[-1]))
# plt.imshow(digits.images[-1],cmap=plt.cm.gray_r, interpolation="nearest")
# plt.show()

images_and_labels = list(zip(digits.images, digits.target))
# for every element in the list
for index, (image, label) in enumerate(images_and_labels[:10]):
    # initialize a subplot of 2X4 at the i+1-th position
    plt.subplot(2, 5, index + 1)
    # Display images in all subplots
    plt.imshow(image, cmap=plt.cm.gray_r,interpolation='nearest')
    # Add a title to each subplot
    plt.title('Training: ' + str(label))
# Show the plot
plt.show()

