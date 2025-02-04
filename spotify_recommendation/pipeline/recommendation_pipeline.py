from spotify_recommendation.config.configuration import ConfigurationManager
from spotify_recommendation.components.recommend import RecommendSongs
from spotify_recommendation.logging import logger

STAGE_NAME = "Recommendation System"

class RecommendationPipeline:
    def __init__(self):
        pass

    def initiate_recommendation(self, song_name, num_recommendations=5):
        """Runs the recommendation pipeline."""
        try:
            config = ConfigurationManager()
            recommendation_config = config.get_recommendation_config()
            recommender = RecommendSongs(config=recommendation_config)

            # Get recommendations
            recommendations = recommender.get_recommendations(song_name, num_recommendations)

            logger.info(f"Recommendations for '{song_name}':\n{recommendations}")
            return recommendations
        except Exception as e:
            logger.exception(f"Error in Recommendation System: {str(e)}")
            raise e


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        obj = RecommendationPipeline()
        song_name = "Angie"  # Example song name
        recommendations = obj.initiate_recommendation(song_name, num_recommendations=5)
        logger.info(f"Recommendation System completed successfully!")
    except Exception as e:
        logger.exception(e)
        raise e
