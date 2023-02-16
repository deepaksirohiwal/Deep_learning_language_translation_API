# Language Translation API Documentation
This documentation describes how to use the Language Translation API, which provides translation capabilities for multiple languages.
## API Description
The Language Translation API is built using Python's <a href="https://fastapi.tiangolo.com/">FAST-API</a> framework and provides the following capabilities:
* Translation from one language to another, with support for multiple languages
## Running the API Locally
To run the Language Translation API locally, follow the steps below:
* Clone the repository from Github: git clone `https://github.com/deepaksirohiwal/Deep_learning_language_translation_API.git`
* Install the required dependencies by running `pip install -r requirements.txt`
* Run the API using Uvicorn by running `uvicorn main:app --reload`
* The API will now be available at `http://localhost:8000/`

## Docker Image
To run the Langauge Translation API locally using Docker image, follow the steps below:
* Build the docker image `docker buildx build --platform linux/amd64 -t dlapi .`
* Runt the API inside the docker container `docker run -d --name dlapi -p 80:80 dlapi`
* The API will now be available at `http://localhost:80`
## API Usage
To use the Language Translation API, send a POST request to the endpoint `/translate` and a `task_id` will be return. The request body should be in JSON format and contain the following parameters:
* `text` : The text to be translated.
* `base_lang`: The source language of the text (e.g., English).
* `final_language`: The target language for the translation (e.g., French).
Use the returned `task_id` to send a  GET request to the endpoint `/results`

**Here's an example request:**

![Animation](https://user-images.githubusercontent.com/38135521/219305634-30f986b5-4c24-4e73-a54e-780f0cb42400.gif)


**The API will respond with a JSON object containing the translated text:**

![request_responsejpg](https://user-images.githubusercontent.com/38135521/219305353-ec3c6210-bdc3-43f8-999d-8ce695546ac6.jpg)

## Supported Languages and Models
The Language Translation API supports multiple languages and trained on <a href="https://huggingface.co/t5-small">`t5-small`</a> model. This model can be replaced by more powerfull <a href="https://huggingface.co/google/flan-t5-xxl">t5-base</a> and <a href="https://huggingface.co/t5-large">t5-large</a>. Here's a list of currently supported languages and their corresponding language codes:
* English
* French
* German
* Romanian

# Conclusion
That's it! You now know how to run and use the Language Translation API. If you have any questions or feedback, please feel free to contact me.
* <a href="https://www.linkedin.com/in/deepak-sirohiwal-22330613a/">Linkedin<a>
