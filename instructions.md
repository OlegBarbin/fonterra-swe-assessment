# Fonterra SWE Assessment

## Background
Manufacturing cream cheese is a complex process that requires a high level of precision and control. The process involves multiple steps, including mixing, heating, cooling, and fermentation. To ensure the quality and consistency of the final product, it is essential to monitor and control various parameters throughout the process.

To assist this, the team has developed a series of Ordinary Differential Equations (ODEs) that describe the acidity during the cream cheese manufacturing process. There are four key inputs that we are interested in controlling:

* The bacterial concentration growth rate (mu) - typically ranges between 0.1 and 0.2
* log10 of lactic acid concentration production rate (q) - typically ranges between -20 and -10
* The initial bacterial  concentration (x0) - typically ranges between 10^4 to 10^8
* The initial lactic acid concentration (p0) - typically ranges between 10^-8 to 10^-4

Based on these inputs, the ODEs can be solved to determine the acidity profile over time. The acidity profile is a critical parameter that affects the taste, texture, and shelf life of the cream cheese.

The function that solves the ODEs is called `run_model` provided in `model.py`. `example_usage.py` shows how this function can be used to solve the ODEs and generate a plot for a given set of inputs.

## Task
The team wants to use this set of ODEs and build a tool that lets process technicians explore the impact of different input parameters on the acidity profile.

Your task is to develop a simple prototype application that leverages the model and presents an intuitive user interface that lets users interrogate the underlying ODEs. Bonus points for creative visual and interactive elements that create a more engaging user experience - how exactly this works is completely up to you (it doesn't have to be 100% practical!). The intended scope of this exercise is around 3 hours - use this to guide the level of polish in the application.

Submit your results into a private GitHub repository and share it with me at least a day prior to the second interview. It would be greatly appreciated if you could include a gif or video showing the application in action in the readme or the repo files.

Please reach out to clarify any questions you may have. We are looking forward to seeing your solution!
