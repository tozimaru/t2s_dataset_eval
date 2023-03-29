import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--phoneme_pairs_path', type=str, default='./phoneme_pairs.json')
parser.add_argument('--bigrams_outname', type=str, required=True)
parser.add_argument('--trigrams_outname', type=str)
args = parser.parse_args()

def generate_bigrams(consonants, vowels, impossible_combinations=None):
    """
    Create all possible bigrams from a given set of consonants and vowels, ensuring that each bigram contains at least one vowel.
    Exclude any bigrams or trigrams in the impossible_combinations list.
    
    Args:
    consonants (list): List of consonants to use for creating bigrams
    vowels (list): List of vowels to use for creating bigrams
    impossible_combinations (list): List of bigrams or trigrams to exclude from the final list of combinations. Default is None.
    
    Returns:
    list: List of all possible bigrams, with each bigram containing at least one vowel and excluding any impossible combinations
    """
    if impossible_combinations is None:
        impossible_combinations = []
        
    bigrams = []
    for c in consonants:
        for v in vowels:
            bigram = c + v
            if bigram not in impossible_combinations:
                bigrams.append(bigram)
            bigram = v + c
            if bigram not in impossible_combinations:
                bigrams.append(bigram)
    for v1 in vowels:
        for v2 in vowels:
            bigram = v1 + v2
            if bigram not in impossible_combinations:
                bigrams.append(bigram)
    return [b for b in bigrams if any(v in b for v in vowels)] 

def create_trigrams(consonants, vowels, impossible_combinations=None):
    """
    Create all possible trigrams from a given set of consonants and vowels, ensuring that each trigram contains at least one vowel.
    Exclude any bigrams or trigrams in the impossible_combinations list.
    
    Args:
    consonants (list): List of consonants to use for creating trigrams
    vowels (list): List of vowels to use for creating trigrams
    impossible_combinations (list): List of bigrams or trigrams to exclude from the final list of combinations. Default is None.
    
    Returns:
    list: List of all possible trigrams, with each trigram containing at least one vowel and excluding any impossible combinations
    """
    if impossible_combinations is None:
        impossible_combinations = []
        
    trigrams = []
    for c in consonants:
        for v1 in vowels:
            for v2 in vowels:
                trigram = c + v1 + v2
                if trigram not in impossible_combinations:
                    trigrams.append(trigram)
                trigram = v1 + c + v2
                if trigram not in impossible_combinations:
                    trigrams.append(trigram)
                trigram = v1 + v2 + c
                if trigram not in impossible_combinations:
                    trigrams.append(trigram)
    return [t for t in trigrams if any(v in t for v in vowels)]


