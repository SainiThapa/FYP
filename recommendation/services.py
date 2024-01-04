from collections import defaultdict
from recommendation.algorithm import CosineSimilarity
from recommendation.models import Lawyer


class LawyerRecommendationService:
    def __init__(self, laywer_data) -> None:
        # (self, )
        self.lawyer_data = laywer_data
        self.cleaned_data = None
        self.preprocessed_documents = defaultdict()  # noqa: F821
        self.results = {}
        self.model = CosineSimilarity(self.preprocessed_documents)

    def preprocess(self):
        for lawyer in self.lawyers:
            id = lawyer.id
            expertise = lawyer.expertise
            data = f"{expertise}"

            self.preprocessed_documents[id] = data

    def get_similarity_scores(self, n=5):
        profile = self.profile
        self.preprocess()
        tf_idf_matrix = self.model.calculate_tfidf()
        profile_tf_idf_vector = self.model.fit_document(
            document=f"{profile.needed_expertise}"
        )

        for id, value in tf_idf_matrix:
            tf_idf_vector = value

            result = self.model.cosine_similarity(tf_idf_vector, profile_tf_idf_vector)
            if result > 0.4:  # please adjust values as your requirement
                self.results[id] = result
        return sorted(self.results.items(), key=lambda x: x[1], reverse=True)[:n]

    @classmethod
    def get_lawyer(self, Lawyer_id):
        laywer = Lawyer.objects.get(id=Lawyer_id)
        return laywer

    @classmethod
    def get_lawyer_recommendations(self):
        pass
