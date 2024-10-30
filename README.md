# Coffee Exploration and Recommendations Model
From the first sip to the perfect brew, this tool is designed to guide every coffee enthusiast—whether novice or expert—toward discovering their ideal coffee match, making selection simple, enjoyable, and personalized to your taste preferences.

![cf](https://github.com/user-attachments/assets/eb983823-832f-4eaf-b781-d4a402125598)

*Image credit: [istockphoto.com](https://www.istockphoto.com/photos/coffee)*

## *Description:*

This project leverages a comprehensive dataset of coffee, encompassing various categories such as type, cost, origin, flavor profile, and more, to build an interactive recommendation model. The model is designed to analyze consumer preferences entered into the system—such as desired taste, budget, and preferred coffee origin—and output personalized coffee recommendations. By utilizing advanced data analysis and machine learning techniques, the model helps consumers discover new coffee varieties that align with their tastes and preferences, offering a unique, customized coffee-buying experience. 

## *Technologies Used:*

### Project Flow Chart:

  Our [Project flow chart](https://github.com/lotzamotza/coffee-recommendations/blob/main/Project%20Flowchart.jpg) was created as a visual tool to assist with project management, ensuring that each stage of our project is clearly defined and efficiently executed. The chart outlines the key phases of the project, from problem definition and data collection to model deployment and reporting. By assigning specific tasks to team members and visually representing the workflow, the chart helps us track progress, manage tasks effectively, and maintain clear communication within the team. This structured approach ensures that all project elements are aligned and contributes to a successful outcome.

### - Data Collection and Processing:

We began by scraping data from [The Coffee Review.com](https://www.coffeereview.com/), ensuring compliance with legal guidelines for data usage. This initial step involved gathering comprehensive data on various coffee varieties, including reviews and ratings. After extraction, we focused on processing the raw data, which involved normalizing pricing formats and handling missing values. This ensured that the dataset was consistent and reliable, setting a solid foundation for further analysis.

### - Data Cleaning and Analysis:

After the initial data collection, we conducted a detailed cleaning and analysis phase. We scraped individual links from 100 pages of reviews on CoffeeReviews.com using Selenium WebDriver. From each link, we extracted review data and converted it into a readable data frame. To standardize the dataset, we converted the cost of each coffee to a uniform US dollar amount per 12 ounces, removing any rows that could not be converted. Additional cleanup included converting various currencies and normalizing weights from grams to ounces to ensure consistency across all data points.

In this step, we also used Geoapify to add the latitude and longitude for each coffee's origin and roaster site. This geolocation data allowed us to create a mapping visualization in Tableau, providing a geographic context to the coffee varieties and enhancing the overall analysis.

### - Machine Learning:
  
    - Feature Engineering
      
We preprocessed the text descriptions to enhance model performance by converting text to lowercase, removing punctuation and stopwords, and applying stemming. The ratings for Aroma, Acid, Body, Flavor, and Aftertaste were doubled from a 0-10 scale to a 0-20 scale to increase prediction granularity.
 
    - Initial Model Development
    
The dataset was split into an 80% training set and a 20% testing set. We built a machine learning pipeline that includes scaling, text transformation, and encoding steps, with a RandomForestRegressor used to predict the quality ratings across multiple targets.

    - User Input and Prediction
    
The final model allows users to input coffee details (cost, origin, roast level, description) and receive predictions for the quality ratings based on the trained model.

### - Dashboard/ Data Visualization:

We imported the data into [TableauPublic](https://public.tableau.com/app/profile/julie.ramsey/viz/TheCoffeeProject_17300372249670/CoffeeExploration) ensuring all value types were set correctly to support precise analysis. To enhance interactivity, we created custom parameters, enabling users to filter and explore specific data points. Using latitude and longitude values, we built an interactive map visualization. Calculated fields were also developed to dynamically display points on the map based on user selections. For an improved user experience, we customized tooltips, color schemes, and marker sizes to enhance clarity and visual appeal. Additionally, we used Seaborn and Matplotlib in Python for complementary visualizations, allowing us to explore and validate patterns revealed in Tableau.



### - Word Cloud:

 We created the [word cloud](https://github.com/lotzamotza/coffee-recommendations/blob/main/Word%20Count/WordcloudIMAGE.png) by first selecting relevant text data column and then cleaning it by removing common stopwords, punctuation, and converting everything to lowercase for consistency. We then calculated the frequency of each word to determine its prominence in the word cloud. Using a word cloud generator, we input the processed text, adjusting the shape and colors to highlight key themes. The result visually represents the most frequent terms, allowing for a quick grasp of the main ideas within the dataset



# *How to use the Machine Learning program:*

 ### How to Run the Program:

#### **Make Sure Python is Installed:**

Ensure that Python is installed on your computer. You'll also need Python packages, like pandas, numpy, and sklearn, as these are required for the program to run.

 #### Run the Program:

- Open your terminal or command prompt.

- Navigate to the folder where your program file is saved.

- Run the program by typing python your_program_name.py and pressing Enter. Replace your_program_name.py with the actual name of your Python file.

### What Happens When You Run the Program:

#### User Inputs:

- The program will ask you to input some details about a coffee:

- Cost per 12 ounces: _You’ll need to enter the price of the coffee for 12 ounces._

- Origin: _You’ll be asked to type where the coffee comes from (e.g., Ethiopia, Colombia)._

- Roast Level: _You’ll input the roast level of the coffee, like Light, Medium, or Dark._

- Description: _You’ll type a brief description of the coffee, highlighting its flavors or any other notable characteristics._

#### Program Outputs:

After you provide the inputs, the program will use the information to predict how the coffee will be rated across five categories: Aroma, Acid, Body, Flavor, and Aftertaste.
It will display each of these predicted ratings.
The program will then calculate an Overall Rating by adding up these five ratings.
It will also calculate a Website Rating by taking the overall rating, dividing it by 2, adding 50, and rounding it to the nearest whole number.

#### Result Display:

- Predicted Ratings: _You’ll see the predicted ratings for Aroma, Acid, Body, Flavor, and Aftertaste._
  
- Overall Rating: _The sum of the predicted ratings will be displayed as the "Overall Rating."_
  
- Website Rating: _Finally, the program will show the "Website Rating," which is a simpler, standardized score for easier interpretation._

#### Example:

If you enter:

**Cost:** $22

**Origin:** Guji Zone, Oromia Region, southern Ethiopia

**Roast Level:** Light

**Description:** "Balanced, high-toned, multi-layered. Dried plum, genmaicha tea, lemon balm, candied violet, cocoa nib in aroma and cup. Sparkling acidity; crisp, satiny mouthfeel. Notes of dried plum and genmaicha tea are foregrounded in the pleasing finish."

**The program might display something like:**

**Aroma:** 18.02

**Acid:** 17.82

**Body:** 16.14

**Flavor:** 18.00

**Aftertaste:** 16.06

**Overall Rating:** 86.04

**Website Rating:** 93

This gives you a complete picture of how the coffee might be rated, both on the website and in a simple overall score.

![Black-Coffee-easy-Recipe1](https://github.com/user-attachments/assets/36bb2b9b-a10b-4b0b-bd71-b637c2a50385)

*Image credit: [herzindagi.com](https://www.herzindagi.com/recipe-tips/how-to-make-black-coffee-at-home-article-183761)*

## *Looking Ahead:*

### Possible Improvements: 
To further refine our predictive model, we propose an increased focus on lower-rated coffees, which have been underrepresented in the current dataset. By incorporating additional data sources that specifically address lower-end ratings, we aim to gain deeper insights into the factors that contribute to these assessments. This effort will include integrating diverse review types and perspectives from a broader array of reviewers, thereby capturing a more comprehensive spectrum of opinions and experiences. Such an approach will significantly enhance the robustness of our dataset, ultimately leading to more accurate and nuanced predictions across the full range of coffee ratings.

### Ideas for Development:

### Project Expansion:
Looking ahead, after the coffee exploartion project, we see an opportunity to expand our research into the impacts of climate change on coffee production. By studying how changing climates affect coffee-growing regions, we could explore ways to predict and mitigate these effects, contributing valuable insights to both the coffee industry and broader environmental discussions.


![mario-ibrahimi-2RrAct0Rf8E-unsplash1](https://github.com/user-attachments/assets/3306afb3-10d5-4ba9-9895-e7e850834b6d)


## *Citations*

**Coffee Terminology**  
   Retrieved from [hermanoscoffeeroasters.com](https://www.hermanoscoffeeroasters.com)

**Data Source**  
   Retrieved from [Coffee Review](https://www.coffeereview.com/review/)

**Inspiration and Partial Code**  
   Retrieved from [Kaggle - Coffee Scraping](https://www.kaggle.com/code/hanifalirsyad/coffee-scraping/output)

**Geoapify Geocoding and Mapping API**  
   Geoapify. (2024). Retrieved from [Geoapify](https://www.geoapify.com/)

**ChatGPT**  
   OpenAI. (2024). *ChatGPT (Version GPT-4)*. Retrieved from [ChatGPT](https://chat.openai.com/)
