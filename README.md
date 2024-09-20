# Wiki

Wiki is a simple web-based encyclopedia application where users can browse, search, create, and edit entries. This project is a part of the CS50 Web Programming with Python and JavaScript course, demonstrating the use of Django, Python, and Markdown to HTML conversion.

## Features

1. **Index Page**: 
    - Displays a list of all encyclopedia entries that users can read through.

2. **Search**:
    - Users can search for encyclopedia entries by typing a query into the search bar.

3. **Create New Page**:
    - Users can create a new encyclopedia entry.

5. **Edit Page**:
    - Users can edit an existing encyclopedia entry.

6. **Random Page**:
    - Users can click on "Random Page" to be taken to a random encyclopedia entry.

7. **Markdown to HTML Conversion**:
    - The project uses the `markdown2` package to convert Markdown content into HTML.
    - Using Markdown for content ensures simplicity, readability, consistency, and easy HTML conversion, allowing users to focus on writing without complex formatting.

## Installation

1. **Clone the repository**:
    ```
    git clone https://github.com/JayShukla8/Wiki.git
    cd Wiki/
    ```

2. **Install dependencies**:
    - Make sure you have Python installed.
    - Install Django and markdown2 by running:
    ```
    pip install django markdown2
    ```

3. **Run the server**:
    ```
    python manage.py runserver
    ```

4. **Access the app**:
    - Open your browser and go to `http://127.0.0.1:8000/wiki/` to view the Wiki Home Page.

## Project Structure

- `encyclopedia/`: Contains the main Django app files.
    - `templates/encyclopedia/`: HTML templates for the project.
    - `static/encyclopedia/`: Static files like CSS.
    - `urls.py`: URL routing for the app.
    - `views.py`: Contains the logic for rendering the encyclopedia.
    - `forms.py`: Contains form definition for new page.
    - `util.py`: Helper functions for retrieving and saving encyclopedia entries.

- `entries/`: Directory where all the Markdown files for encyclopedia entries are stored.

## Demo

- For a live demonstration of the project, watch this [video](https://youtu.be/BSn7r_ihxUw).
- Also, here's what the home page looks like-
     ![image](https://github.com/user-attachments/assets/b506e55b-e7b3-4a2b-8d30-2f492e966ae5)

  
## Future Improvements

- Implement user authentication to restrict editing and page creation to logged-in users.
- Improve styling with a more modern design.
- Comments Section: Enable users to comment on entries for discussions and feedback.
- Mobile Responsiveness: Enhance the design for better usability on mobile devices.
- Deployment to Production: Make the project go live by deploying it on a suitable web hosting platform, ensuring accessibility to users online.

## Acknowledgements

- **Mr. Brian Yu** for the inspiration and guidance and being an awesome teacher.

---

