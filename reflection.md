# Reflection

Student Name:  Gabriel Lucey
Sudent Email:  gplucey@syr.edu

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

**Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 

**Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`

Doing this assignment in class was a great way to explore mapping with a UI like Streamlit. I struggled most with etl.py as I had some trouble in class trying to scrape the correct elements. etl.py, however, was a great way to reflect on past concepts such as pivot tables in the top_locations function and merging dataframes in the top_locations_mappable function. I was originally confused because I was used to merging tables using left_on or right_on, but since the column names were identical, I found that I could use the on parameter instead.

This assignment was important as it helped me work on my mapping skills using GeoPandas. By mapping the tickets on Streamlit, I found that folium_static from streamlit_folium must be used to visualize maps on Streamlit. This assignment helped me explore new parameters such as the marker_kwds, which helped map specific points on the map, and vmin and vmax, which helped control the zoom.

Finally, I was able to learn how to map visualizations using Seaborn and Streamlit. I found that if you wanted to visualize two plots side by side, you set each of them up in a column and use with loops to actively change the visualizations when input is changed. Overall, this assignment was very useful for refreshing myself on old topics and further developing my visualization skills.