from file_reader import open_and_tokenize
from feature_extraction import get_features
import os
import csv

def features_in_path(folder_path, sentiment):
    """Return features from the files in the give folder path and set sentiment"""
    all_features = []
    for filename in os.listdir(folder_path)[:1000]:
        path = folder_path + "/" + filename
        tokens = open_and_tokenize(path)
        features = get_features(tokens)
        features["filename"] = filename
        features["sentiment"] = sentiment
        all_features.append(features)
    return all_features

def get_all_features():
    """Get all the features from the train sets"""
    all_features = []

    # Negative path
    train_negative_path = "./../aclImdb/train/neg"
    negative_features = features_in_path(train_negative_path, "negative")
    all_features.extend(negative_features)

    # Positive path
    train_positive_path = "./../aclImdb/train/pos"
    positive_features = features_in_path(train_positive_path, "positive")
    all_features.extend(positive_features)

    return all_features

def write_csv():
    """Write all the features to a csv"""
    with open('features.csv', 'w') as csvfile:
        features = get_all_features()
        fieldnames = features[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for feature in features:
            writer.writerow(feature)

def main():
    write_csv()

main()
