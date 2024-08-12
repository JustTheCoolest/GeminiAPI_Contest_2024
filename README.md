# Star Cut AI

**Edit images in download speed**

Using the function calling features of Gemini to perform basic discrete image manipulation operations like cutting and rotating, using a prompt that is given in natural human language. The point is to prevent generative AI the power to spoil your images. By restricting Gemini to only be able to access hard coded functions (with flexibility) to manipulate the images in a safe manner, we ensure higher quality and trust. By being able to describe what we want in natural language, we get to do what we want faster and without the learning curve of traditional editing softwares.

# Setup Instructions:

Follow these steps to set up and run the application:

1. **Clone the repository**: Clone this repository to your local machine using `git clone <repository_url>`.

2. **Navigate to the repository folder**: Use the command `cd <repository_name>` to navigate into the cloned repository.

3. **Set up the environment variables**: Create a `.env` file in the root directory of the project. Add your Google API key to this file in the following format: `GOOGLE_API_KEY="<Your Key>"`.

4. **Install the required packages**: Run `pip install -r requirements.txt` to install the necessary packages listed in the `requirements.txt` file.

5. **Run the application**: Finally, start the application by running `streamlit run app.py` in your terminal.

Remember to replace `<repository_url>`, `<repository_name>`, and `<Your Key>` with the actual repository URL, the name of your local repository folder, and your actual Google API key, respectively.