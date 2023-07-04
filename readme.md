# Dungeons and Dragons Transcription Script

This Python script uses OpenAI's GPT4 model to convert raw transcriptions of Dungeons and Dragons (D&D) games recorded over teleconferencing into a lively and engaging narrative.

If you do not have access to GPT4 you can of course use any model available, but in tests GPT 3.5 turbo did not produce good results as disambiguating between utterances of players VS what their characters are doing is a complex task for a large language model.

## Requirements 

This script requires the below Python packages:

- openai
- PyPDF2
- textwrap
- json
- os

These can be installed with pip:

```bash
pip install -r requirements.txt
```

## Authentication

You should replace `openai.api_key = "OPENAI_API_KEY"` with your own OpenAI API key which you can get from the [OpenAI platform](https://beta.openai.com/).

## Instructions 

1. Save your D&D game transcript PDF as `any_name.pdf` in the same directory as this script.

2. Run the python script with:

    ```bash
    python dnd_transcription.py
    ```
3. The script breaks down the original transcript into manageable chunks and processes each chunk to create an engaging narrative.

4. The processed text is written out to `parsed_story.txt`.

5. The script maintains a progress file `progress.json` to keep track of already processed chunks in case of interruptions. Running the script again will continue from the last unprocessed chunk. 

## Notes 

This tool is designed specifically for transcribing D&D games, and takes the persona of Samgine weaving the tale of the characters: Illion, Feng, Klagnut, and Althea. 

The narrative focuses solely on the actions and interactions of the characters, with disregard for sections that don't advance the story and dialogues that don't contribute to its progression.

## Contact

This tool is maintained by GitHub user [Your username].

Any bugs, issues, or feature requests can be made by opening an issue or pull request on the GitHub repository.