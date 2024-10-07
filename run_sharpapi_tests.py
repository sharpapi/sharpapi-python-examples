import logging
import random
import string
import os

from dotenv import load_dotenv

from sharpapi.sharp_api_service import SharpApiService
from sharpapi.dto.job_description_parameters import JobDescriptionParameters
import questionary  # Use questionary instead of inquirer


def random_string(length=8):
    """Generate a random string of fixed length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def test_ping(sharp_api, logger):
    logger.info("Testing ping() method...")
    ping_response = sharp_api.ping()
    logger.info(f"Ping Response: {ping_response}")
    logger.info("-" * 50)


def test_quota(sharp_api, logger):
    logger.info("Testing quota() method...")
    quota_info = sharp_api.quota()
    if quota_info:
        logger.info("Quota Information:")
        logger.info(f"Timestamp: {quota_info.timestamp}")
        logger.info(f"On Trial: {quota_info.on_trial}")
        logger.info(f"Trial Ends: {quota_info.trial_ends}")
        logger.info(f"Subscribed: {quota_info.subscribed}")
        logger.info(f"Current Subscription Start: {quota_info.current_subscription_start}")
        logger.info(f"Current Subscription End: {quota_info.current_subscription_end}")
        logger.info(f"Subscription Words Quota: {quota_info.subscription_words_quota}")
        logger.info(f"Subscription Words Used: {quota_info.subscription_words_used}")
        logger.info(f"Subscription Words Used Percentage: {quota_info.subscription_words_used_percentage}%")
    else:
        logger.info("Failed to retrieve quota information.")
    logger.info("-" * 50)


def test_parse_resume(sharp_api, logger):
    logger.info("Testing parse_resume() method...")
    resume_file_path = 'sample_resume.pdf'  # Replace with your actual file path
    if os.path.exists(resume_file_path):
        status_url = sharp_api.parse_resume(resume_file_path, language='English')
        result_job = sharp_api.fetch_results(status_url)
        logger.info("Parsed Resume Result:")
        logger.info(result_job.get_result_json())
    else:
        logger.warning(f"Resume file '{resume_file_path}' not found. Skipping parse_resume test.")
    logger.info("-" * 50)


def test_generate_job_description(sharp_api, logger):
    logger.info("Testing generate_job_description() method...")
    job_description_params = JobDescriptionParameters(
        name=f"Software Engineer",
        company_name=f"Company {random_string(8)}",
        minimum_work_experience="3+ years",
        minimum_education="Bachelor's Degree in Computer Science",
        employment_type="Full-time",
        required_skills=[
            "Proficiency in Python",
            "Experience with RESTful APIs",
            f"Knowledge of {random_string(7)}"
        ],
        optional_skills=[
            "Familiarity with Docker",
            "Experience with cloud services"
        ],
        country="USA",
        remote=True,
        visa_sponsored=False,
        language='English',
        voice_tone='Professional',
        context=None
    )
    status_url = sharp_api.generate_job_description(job_description_params)
    result_job = sharp_api.fetch_results(status_url)
    logger.info("Generated Job Description Result:")
    logger.info(result_job.get_result_json())
    logger.info("-" * 50)


def test_related_skills(sharp_api, logger):
    logger.info("Testing related_skills() method...")
    skill_name = f"Coding"
    status_url = sharp_api.related_skills(skill_name, language='English', max_quantity=5)
    result_job = sharp_api.fetch_results(status_url)
    logger.info("Related Skills Result:")
    logger.info(result_job.get_result_json())
    logger.info("-" * 50)


def test_related_job_positions(sharp_api, logger):
    logger.info("Testing related_job_positions() method...")
    job_position_name = f"Flutter Developer"
    status_url = sharp_api.related_job_positions(job_position_name, language='English', max_quantity=5)
    result_job = sharp_api.fetch_results(status_url)
    logger.info("Related Job Positions Result:")
    logger.info(result_job.get_result_json())
    logger.info("-" * 50)


def test_product_review_sentiment(sharp_api, logger):
    logger.info("Testing product_review_sentiment() method...")
    review = f"This product is {random.choice(['great', 'terrible'])}! {random_string(10)}"
    status_url = sharp_api.product_review_sentiment(review)
    result_job = sharp_api.fetch_results(status_url)
    logger.info("Product Review Sentiment Result:")
    logger.info(result_job.get_result_json())
    logger.info("-" * 50)


def test_product_categories(sharp_api, logger):
    logger.info("Testing product_categories() method...")
    product_name = f"Apple Watch v.{random_string(2)}"
    status_url = sharp_api.product_categories(
        product_name,
        language='English',
        max_quantity=5,
        voice_tone='Neutral'
    )
    result_job = sharp_api.fetch_results(status_url)
    logger.info("Product Categories Result:")
    logger.info(result_job.get_result_json())
    logger.info("-" * 50)


def test_generate_product_intro(sharp_api, logger):
    logger.info("Testing generate_product_intro() method...")
    product_data = f"This is a new product called Apple Watch v.{random_string(2)}. It is designed to help with {random_string(15)}."
    status_url = sharp_api.generate_product_intro(
        product_data,
        language='English',
        max_length=100,
        voice_tone='Friendly'
    )
    result_job = sharp_api.fetch_results(status_url)
    logger.info("Generated Product Intro Result:")
    logger.info(result_job.get_result_json())
    logger.info("-" * 50)


def test_generate_thank_you_email(sharp_api, logger):
    logger.info("Testing generate_thank_you_email() method...")
    product_name = f"Apple Watch v.{random_string(2)}"
    status_url = sharp_api.generate_thank_you_email(
        product_name,
        language='English',
        max_length=200,
        voice_tone='Professional',
        context=None
    )
    result_job = sharp_api.fetch_results(status_url)
    logger.info("Generated Thank You Email Result:")
    logger.info(result_job.get_result_json())
    logger.info("-" * 50)


def test_detect_phones(sharp_api, logger):
    logger.info("Testing detect_phones() method...")
    text_with_phone = f"Contact me at {random.randint(100,999)}-555-{random.randint(1000,9999)} for more information."
    status_url = sharp_api.detect_phones(text_with_phone)
    result_job = sharp_api.fetch_results(status_url)
    logger.info("Detected Phones Result:")
    logger.info(result_job.get_result_json())
    logger.info("-" * 50)


def test_detect_emails(sharp_api, logger):
    logger.info("Testing detect_emails() method...")
    text_with_email = f"Please send an email to test_{random_string(5)}@example.com."
    status_url = sharp_api.detect_emails(text_with_email)
    result_job = sharp_api.fetch_results(status_url)
    logger.info("Detected Emails Result:")
    logger.info(result_job.get_result_json())
    logger.info("-" * 50)


def test_detect_spam(sharp_api, logger):
    logger.info("Testing detect_spam() method...")
    spam_text = f"Congratulations! You have won {random.randint(1000,5000)} dollars! Click here to claim your prize."
    status_url = sharp_api.detect_spam(spam_text)
    result_job = sharp_api.fetch_results(status_url)
    logger.info("Spam Detection Result:")
    logger.info(result_job.get_result_json())
    logger.info("-" * 50)


def test_summarize_text(sharp_api, logger):
    logger.info("Testing summarize_text() method...")
    long_text = (
        f"This is a long text that needs to be summarized. {random_string(50)} "
        "It contains multiple sentences and information."
    )
    status_url = sharp_api.summarize_text(
        long_text,
        language='English',
        max_length=50,
        voice_tone='Neutral',
        context=None
    )
    result_job = sharp_api.fetch_results(status_url)
    logger.info("Summarized Text Result:")
    logger.info(result_job.get_result_json())
    logger.info("-" * 50)


def test_generate_keywords(sharp_api, logger):
    logger.info("Testing generate_keywords() method...")
    content = f"This is some content about Apple Watch v.{random_string(1)} that needs keywords."
    status_url = sharp_api.generate_keywords(
        content,
        language='English',
        max_quantity=5,
        voice_tone='Neutral',
        context=None
    )
    result_job = sharp_api.fetch_results(status_url)
    logger.info("Generated Keywords Result:")
    logger.info(result_job.get_result_json())
    logger.info("-" * 50)


def test_translate(sharp_api, logger):
    logger.info("Testing translate() method...")
    text_to_translate = f"This is a text to translate. Let's see what comes out {random_string(3)}"
    target_language = 'Spanish'
    status_url = sharp_api.translate(
        text_to_translate,
        language=target_language,
        voice_tone='Neutral',
        context=None
    )
    result_job = sharp_api.fetch_results(status_url)
    logger.info("Translated Text Result:")
    logger.info(result_job.get_result_json())
    logger.info("-" * 50)


def test_paraphrase(sharp_api, logger):
    logger.info("Testing paraphrase() method...")
    text_to_paraphrase = f"This is a text that needs to be paraphrased. Lorem ipsum. Go. Now. {random_string(10)}"
    status_url = sharp_api.paraphrase(
        text_to_paraphrase,
        language='English',
        max_length=100,
        voice_tone='Neutral',
        context=None
    )
    result_job = sharp_api.fetch_results(status_url)
    logger.info("Paraphrased Text Result:")
    logger.info(result_job.get_result_json())
    logger.info("-" * 50)


def test_proofread(sharp_api, logger):
    logger.info("Testing proofread() method...")
    text_to_proofread = f"This is a txt with erors that need to be corected. {random_string(10)}"
    status_url = sharp_api.proofread(text_to_proofread)
    result_job = sharp_api.fetch_results(status_url)
    logger.info("Proofread Text Result:")
    logger.info(result_job.get_result_json())
    logger.info("-" * 50)


def test_generate_seo_tags(sharp_api, logger):
    logger.info("Testing generate_seo_tags() method...")
    content_for_seo = f"This is content about Apple Watch v.{random_string(2)} that needs SEO tags."
    status_url = sharp_api.generate_seo_tags(
        content_for_seo,
        language='English',
        voice_tone='Neutral'
    )
    result_job = sharp_api.fetch_results(status_url)
    logger.info("Generated SEO Tags Result:")
    logger.info(result_job.get_result_json())
    logger.info("-" * 50)


def test_travel_review_sentiment(sharp_api, logger):
    logger.info("Testing travel_review_sentiment() method...")
    travel_review = f"The trip was {random.choice(['amazing', 'disappointing'])}. {random_string(10)}"
    status_url = sharp_api.travel_review_sentiment(travel_review)
    result_job = sharp_api.fetch_results(status_url)
    logger.info("Travel Review Sentiment Result:")
    logger.info(result_job.get_result_json())
    logger.info("-" * 50)


def test_tours_and_activities_product_categories(sharp_api, logger):
    logger.info("Testing tours_and_activities_product_categories() method...")
    ta_product_name = f"Tour Universal Studios Singapore"
    status_url = sharp_api.tours_and_activities_product_categories(
        ta_product_name,
        city='Paris',
        country='France',
        language='English',
        max_quantity=5,
        voice_tone='Neutral',
        context=None
    )
    result_job = sharp_api.fetch_results(status_url)
    logger.info("Tours and Activities Product Categories Result:")
    logger.info(result_job.get_result_json())
    logger.info("-" * 50)


def test_hospitality_product_categories(sharp_api, logger):
    logger.info("Testing hospitality_product_categories() method...")
    hospitality_product_name = f"Hotel Hilton New York"
    status_url = sharp_api.hospitality_product_categories(
        hospitality_product_name,
        city='New York',
        country='USA',
        language='English',
        max_quantity=5,
        voice_tone='Neutral',
        context=None
    )
    result_job = sharp_api.fetch_results(status_url)
    logger.info("Hospitality Product Categories Result:")
    logger.info(result_job.get_result_json())
    logger.info("-" * 50)


def main():
    # Load environment variables from .env file
    load_dotenv()
    api_key = os.getenv('SHARP_API_KEY')

    if not api_key:
        raise ValueError("API key not found. Please set SHARP_API_KEY in your .env file.")

    # Initialize logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Initialize the SharpApiService
    sharp_api = SharpApiService(api_key)

    # Define the list of tests
    tests = [
        ("Ping", test_ping),
        ("Quota", test_quota),
        ("Parse Resume", test_parse_resume),
        ("Generate Job Description", test_generate_job_description),
        ("Related Skills", test_related_skills),
        ("Related Job Positions", test_related_job_positions),
        ("Product Review Sentiment", test_product_review_sentiment),
        ("Product Categories", test_product_categories),
        ("Generate Product Intro", test_generate_product_intro),
        ("Generate Thank You Email", test_generate_thank_you_email),
        ("Detect Phones", test_detect_phones),
        ("Detect Emails", test_detect_emails),
        ("Detect Spam", test_detect_spam),
        ("Summarize Text", test_summarize_text),
        ("Generate Keywords", test_generate_keywords),
        ("Translate", test_translate),
        ("Paraphrase", test_paraphrase),
        ("Proofread", test_proofread),
        ("Generate SEO Tags", test_generate_seo_tags),
        ("Travel Review Sentiment", test_travel_review_sentiment),
        ("Tours and Activities Product Categories", test_tours_and_activities_product_categories),
        ("Hospitality Product Categories", test_hospitality_product_categories),
    ]

    # Prepare the choices for questionary
    choices = [test_name for (test_name, _) in tests] + ["Exit"]

    while True:
        # Use questionary to ask which test to run
        choice = questionary.select(
            "Which test would you like to run?",
            choices=choices,
            use_arrow_keys=True
        ).ask()

        if choice == "Exit":
            print("Exiting the program.")
            break

        # Find the selected test function
        for test_name, test_func in tests:
            if choice == test_name:
                try:
                    test_func(sharp_api, logger)
                except Exception as e:
                    logger.error(f"An error occurred during {test_name}:")
                    logger.error(e)
                break


if __name__ == '__main__':
    main()
