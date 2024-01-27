import pandas as pd 
import numpy as np 
from scipy.stats import ttest_ind, f_oneway


during_hammas = pd.read_csv('during_hamas.csv')
after_hammas = pd.read_csv('post_hamas.csv')
during_jenin = pd.read_csv('during_jenin.csv')
after_jenin = pd.read_csv('after_jenin.csv')


#With spaces 
# Assuming you have two groups of sentences with spaces
group1_sentence_lengths = [len(sentence) for sentence in list(during_hammas['comment'])]
group2_sentence_lengths = [len(sentence) for sentence in list(after_hammas['comment'])]

group3_sentence_lengths = [len(sentence) for sentence in list(during_jenin['comment'])]
group4_sentence_lengths = [len(sentence) for sentence in list(after_jenin['comment'])]

# Perform T-test
t_statistic, p_value_ttest = ttest_ind(group1_sentence_lengths, group2_sentence_lengths)
print(t_statistic, p_value_ttest)

t_statistic, p_value_ttest = ttest_ind(group3_sentence_lengths, group4_sentence_lengths)
print(t_statistic, p_value_ttest)

#Without spaces (char count)
def sentence_length_without_spaces(sentence):
    # Remove spaces from the sentence
    sentence_without_spaces = sentence.replace(" ", "")
    
    # Count the length of the sentence without spaces
    length_without_spaces = len(sentence_without_spaces)
    
    return length_without_spaces


# Assuming you have two groups of sentences without spaces
group1_sentence_lengths_w = [sentence_length_without_spaces(sentence) for sentence in list(during_hammas['comment'])]
group2_sentence_lengths_w = [sentence_length_without_spaces(sentence) for sentence in list(after_hammas['comment'])]


group3_sentence_lengths_w = [sentence_length_without_spaces(sentence) for sentence in list(during_jenin['comment'])]
group4_sentence_lengths_w = [sentence_length_without_spaces(sentence) for sentence in list(after_jenin['comment'])]
# Perform T-test
t_statistic, p_value_ttest = ttest_ind(group1_sentence_lengths_w, group2_sentence_lengths_w)
print(t_statistic, p_value_ttest)


t_statistic, p_value_ttest = ttest_ind(group3_sentence_lengths_w, group4_sentence_lengths_w)
print(t_statistic, p_value_ttest)

#based on word counts 

def get_word_count(text):
    words = text.split()
    return len(words)

group1_words = [get_word_count(sentence) for sentence in list(during_hammas['comment'])]
group2_words = [get_word_count(sentence) for sentence in list(after_hammas['comment'])]
group3_words = [get_word_count(sentence) for sentence in list(during_jenin['comment'])]
group4_words = [get_word_count(sentence) for sentence in list(after_jenin['comment'])]

t_statistic, p_value_ttest = ttest_ind(group1_words, group2_words)
print(t_statistic, p_value_ttest)

t_statistic, p_value_ttest = ttest_ind(group3_words, group4_words)
print(t_statistic, p_value_ttest)


import nltk
from nltk import pos_tag, word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

def calculate_lexical_density(text):
    # Tokenize the text into words
    words = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words]

    # Get part-of-speech tags for each word
    pos_tags = pos_tag(filtered_words)

    # Define content word POS tags (Nouns, Verbs, Adjectives, Adverbs)
    content_word_pos_tags = {'NN', 'NNS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS'}

    # Count content words
    content_words = [word for word, pos_tag in pos_tags if pos_tag in content_word_pos_tags]

    # Calculate lexical density
    lexical_density = (len(content_words) / len(words)) * 100

    return lexical_density



# Example usage
group1_ld = [calculate_lexical_density(sentence) for sentence in list(during_hammas['comment'])]
group2_ld = [calculate_lexical_density(sentence) for sentence in list(after_hammas['comment'])]
group3_ld = [calculate_lexical_density(sentence) for sentence in list(during_jenin['comment'])]
group4_ld = [calculate_lexical_density(sentence) for sentence in list(after_jenin['comment'])]

t_statistic, p_value_ttest = ttest_ind(group1_ld, group2_ld)
print(t_statistic, p_value_ttest)

t_statistic, p_value_ttest = ttest_ind(group3_ld, group4_ld)
print(t_statistic, p_value_ttest)

import textstat

group1_r = [textstat.flesch_kincaid_grade(sentence) for sentence in list(during_hammas['comment'])]
group2_r = [textstat.flesch_kincaid_grade(sentence) for sentence in list(after_hammas['comment'])]
group3_r = [textstat.flesch_kincaid_grade(sentence) for sentence in list(during_jenin['comment'])]
group4_r = [textstat.flesch_kincaid_grade(sentence) for sentence in list(after_jenin['comment'])]

t_statistic, p_value_ttest = ttest_ind(group1_r, group2_r)
print(t_statistic, p_value_ttest)

t_statistic, p_value_ttest = ttest_ind(group3_r, group4_r)
print(t_statistic, p_value_ttest)