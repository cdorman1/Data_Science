import csv
from nltk.tokenize import word_tokenize
from nltk import NaiveBayesClassifier as nbc
from itertools import chain

training_data = set()

keywords = ['*trading halted', 'reports results', 'social velocity alert']
seen = set()
with open('/Users/chrisdorman/PycharmProjects/Thinkful/git/Data_Science/bloomberg_analytics_20161109.csv') as fn:
    reader = csv.DictReader(fn)
    count = 0
    for row in reader:
        if count < 2000:
            count += 1
        else:
            break
        desc = str.lower(row['DESCRIPTION'])
        for keyword in keywords:
            if desc in seen:
                continue
            elif desc == '':
                continue
            else:
                pass
            if keyword in desc:
                training_data.add((desc, 'pos'))
            else:
                training_data.add((desc, 'neg'))

            seen.add(desc)

vocabulary = set(chain(*[word_tokenize(t[0].lower()) for t in training_data]))

feature_set = [({i: (i in word_tokenize(keywords.lower())) for i in vocabulary}, tag) for keywords, tag in
               training_data]

classifier = nbc.train(feature_set)

test_phrase = '*TRADING HALTED'

featurized_test_phrase = {i: (i in word_tokenize(test_phrase.lower())) for i in vocabulary}

print "test_sent:", test_phrase
print "tag:", classifier.classify(featurized_test_phrase)
