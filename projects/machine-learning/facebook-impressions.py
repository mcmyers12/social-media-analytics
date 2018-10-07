'''Supervised machine learning classifier that predicts whether the impression of Facebook posts will be > 1000
   Adapted from: https://www.tensorflow.org/hub/tutorials/text_classification_with_tf_hub'''

import tensorflow as tf
import tensorflow_hub as hub
import pandas as pd
import pprint as pp
import numpy as np

tf.logging.set_verbosity(tf.logging.ERROR)


def getTrainTest(fileName):
    df = pd.read_excel(fileName, sheet_name='Key metrics')
    msk = np.random.rand(len(df)) < 0.7
    train_df = df[msk]
    test_df = df[~msk]

    return train_df, test_df


def getFeatures(df):
    return {
        'postMessage': np.array(list(df['Post Message'])),
        'type': np.array(list(df['Type'])),
        'weather': np.array(list(df['Weather'])),
        'weekend': np.array(list(df['Weekend']))
    }


def getLabels(df):
    return np.array([1 if x > 1000 else 0 for x in list(df['Impressions'])])


def runClassifier(fileName):
    train_df, test_df = getTrainTest(fileName)

    train_features = getFeatures(train_df)
    train_labels = getLabels(train_df)
    test_features = getFeatures(test_df)
    test_labels = getLabels(test_df)

    # Training input on the whole training set with no limit on training epochs.
    train_input_fn = tf.estimator.inputs.numpy_input_fn(train_features, train_labels, num_epochs=None, shuffle=True)

    # Prediction on the whole training set.
    predict_train_input_fn = tf.estimator.inputs.numpy_input_fn(
        train_features, train_labels, shuffle=False)
    # Prediction on the test set.
    predict_test_input_fn = tf.estimator.inputs.numpy_input_fn(
        test_features, test_labels, shuffle=False)


    '''vocabulary_feature_column =
        tf.feature_column.categorical_column_with_vocabulary_list(
            key='type',
            vocabulary_list=["kitchenware", "electronics", "sports"])'''

    embedded_text_feature_column = hub.text_embedding_column("postMessage", "https://tfhub.dev/google/nnlm-en-dim128/1")
    feature_columns = [embedded_text_feature_column]

    estimator = tf.estimator.DNNClassifier(
        hidden_units=[500, 100],
        feature_columns=feature_columns,
        n_classes=2,
        optimizer=tf.train.AdagradOptimizer(learning_rate=0.003))


    estimator.train(input_fn=train_input_fn, steps=1000);


    train_eval_result = estimator.evaluate(input_fn=predict_train_input_fn)
    test_eval_result = estimator.evaluate(input_fn=predict_test_input_fn)

    print("Training set accuracy: {accuracy}".format(**train_eval_result))
    print("Test set accuracy: {accuracy}".format(**test_eval_result))



runClassifier('data/SocialMediaInsightsforMachineLearning.xlsm')