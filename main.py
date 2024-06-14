from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from third_parties.linkedin import scrape_linkedin_profile


def main():
    load_dotenv()
    print("Hello")

    summary_template = """
    Given the LinkedIn information {information} about a person, create:
    1. A short summary
    2. Work experience
    3. Technologies they have worked with
    4. Two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=['information'],
        template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    try:
        linkedin_data = scrape_linkedin_profile(
            linkedin_profile_url='https://www.linkedin.com/in/adikal25')

        if linkedin_data:
            # Ensure the linkedin_data is a dictionary, not a plain string
            if isinstance(linkedin_data, str):
                linkedin_data = linkedin_data.strip()  # Remove any leading/trailing whitespace
                if linkedin_data.startswith('{') and linkedin_data.endswith('}'):
                    import json
                    linkedin_data = json.loads(linkedin_data)
                else:
                    raise ValueError(
                        "The retrieved LinkedIn data is not in JSON format.")

            res = chain.invoke(input={"information": linkedin_data})
            print(res)
        else:
            print("Failed to retrieve LinkedIn data")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
