import string

spam_corpus = [["I", "am", "spam", "spam", "I", "am"], ["I", "do", "not", "like", "that", "spamiam"]]
ham_corpus = [["do", "i", "like", "green", "eggs", "and", "ham"], ["i", "do"]]

THRESHOLD = 1
PROB_LIST_SIZE = 15
BASE_PROB = 0.5

class BayesSpam:

    def __init__(self, ham, spam):

        self.threshold = THRESHOLD
        self.unknown_probability_value = BASE_PROB
        self.ngood = len(ham)
        self.nbad = len(spam)

        self.ham_hash = self.hash_occurances(ham)
        self.spam_hash = self.hash_occurances(spam)

        self.score_hash = {}
        for word in self.ham_hash:
            self.score_hash[word.upper()] = self.spam_score(word)

        for word in self.spam_hash:
            self.score_hash[word.upper()] = self.spam_score(word)

        print("Scores:")
        print(self.score_hash, "\t")

    @staticmethod
    def hash_occurances(corpus):
        new_hash = {}
        for i in corpus:
            for v in i:
                if v.upper() in new_hash:
                    new_hash[v.upper()] += 1
                else:
                    new_hash[v.upper()] = 1
        return new_hash

    def spam_score(self, word):
        # Ternary operation to assign good value
        g = (2 * self.ham_hash[word.upper()] if word.upper() in self.ham_hash else self.unknown_probability_value)
        # Ternary operation to assign bad value
        b = (self.spam_hash[word.upper()] if word.upper() in self.spam_hash else self.unknown_probability_value)

        if g + b > self.threshold:
            return max(0.01, min(0.99, min(1.0, b/self.nbad) /
                                 (min(1.0, g/self.ngood) + min(1.0, b/self.nbad))))
        else:
            return 0

    def filter_spam(self, mail):
        mail = mail.translate(str.maketrans('', '', string.punctuation))  # remove punctuation
        words = mail.split()
        list_product = 1
        list_compliment = 1

        for word in words:
            if word.upper() in self.score_hash:
                prob = self.score_hash[word.upper()]
            else:
                prob = self.unknown_probability_value

            list_product *= prob
            list_compliment *= (1 - prob)

            print(words, list_product / (list_product + list_compliment))
            return list_product / (list_product + list_compliment)


if __name__ == '__main__':
    spam_filter = BayesSpam(ham_corpus, spam_corpus)
    print(spam_filter.filter_spam("i"))
    print(spam_filter.filter_spam("I am sam, sam I am, do you like green eggs and ham?"))
    print(spam_filter.filter_spam("SpamIam"))
    # print(filter_spam("I am sam, sam I am, do you like green eggs and ham?", ham_hash, spam_hash))
