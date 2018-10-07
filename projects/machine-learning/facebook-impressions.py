'''Supervised machine learning classifier that predicts whether the impression of Facebook posts will be > 1000
   Adapted from: https://www.tensorflow.org/hub/tutorials/text_classification_with_tf_hub'''

import tensorflow as tf
import tensorflow_hub as hub
import os
import pandas as pd
import pprint as pp
import numpy as np


# Load all files from a directory in a DataFrame.
def createDataset():
    df = pd.read_excel('data/SocialMediaInsightsforMachineLearning.xlsm', sheet_name='Key metrics')

    data = {}
    data['postMessage'] = list(df['Post Message'])
    #data['type'] = list(df['Type'])
    #data['postedTime'] = list(df['Posted'])
    #data['weather'] = list(df['Weather'])
    #data['weekend'] = list(df['Weekend'])
    data['impressions'] = [1 if x > 1000 else 0 for x in list(df['Impressions'])]

    #pp.pprint(data)

    pos_df = pd.DataFrame.from_dict(data)
    neg_df = pd.DataFrame.from_dict(data)

    return pd.concat([pos_df, neg_df]).sample(frac=1).reset_index(drop=True)



# Merge positive and negative examples, add an impressions column and shuffle.
'''def load_dataset(fileName):
    print os.path.join(fileName, "pos")
    pos_df = readDataFromFile(os.path.join(fileName, "pos"))
    neg_df = readDataFromFile(os.path.join(fileName, "neg"))
    pos_df['impressions'] = 1
    neg_df['impressions'] = 0
    return pd.concat([pos_df, neg_df]).sample(frac=1).reset_index(drop=True)'''


# Download and process the dataset files.
def getTrainTest():
    train_df = createDataset()
    test_df = createDataset()

    return train_df, test_df



# Reduce logging output.
tf.logging.set_verbosity(tf.logging.ERROR)

train_df, test_df = getTrainTest()
print train_df.head()

# Training input on the whole training set with no limit on training epochs.
train_input_fn = tf.estimator.inputs.pandas_input_fn(
    train_df, train_df["impressions"], num_epochs=None, shuffle=True)

# Prediction on the whole training set.
predict_train_input_fn = tf.estimator.inputs.pandas_input_fn(
    train_df, train_df["impressions"], shuffle=False)
# Prediction on the test set.
predict_test_input_fn = tf.estimator.inputs.pandas_input_fn(
    test_df, test_df["impressions"], shuffle=False)

embedded_text_feature_column = hub.text_embedding_column(
    key='postMessage',
    module_spec='https://tfhub.dev/google/nnlm-en-dim128/1')


df = pd.read_excel('data/SocialMediaInsightsforMachineLearning.xlsm', sheet_name='Key metrics')


'''estimator = tf.estimator.DNNClassifier(
    hidden_units=[500, 100],
    feature_columns=[embedded_text_feature_column],
    n_classes=2,
    optimizer=tf.train.AdagradOptimizer(learning_rate=0.003))'''


comment = hub.text_embedding_column("postMessage", "https://tfhub.dev/google/nnlm-en-dim128/1")
feature_columns = [comment]
features = {
    "postMessage": np.array(["wow, much amazing", "so easy"])
}
labels = np.array([[1], [0]])
input_fn = tf.estimator.inputs.numpy_input_fn(features, labels, shuffle=True)


estimator = tf.estimator.DNNClassifier([500, 100], feature_columns)
estimator.train(input_fn, max_steps=100)








# Training for 1,000 steps means 128,000 training examples with the default
# batch size. This is roughly equivalent to 5 epochs since the training dataset
# contains 25,000 examples.
estimator.train(input_fn=train_input_fn, steps=1000);


train_eval_result = estimator.evaluate(input_fn=predict_train_input_fn)
test_eval_result = estimator.evaluate(input_fn=predict_test_input_fn)

print("Training set accuracy: {accuracy}".format(**train_eval_result))
print("Test set accuracy: {accuracy}".format(**test_eval_result))



'''def main():
    fileName = 'data/key-metrics-table-1.csv'
    download_and_load_datasets(fileName)

main()'''