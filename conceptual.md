### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
	- In python you don't have to declare what type of variable you are creating. 
	- Javascript is a language for the internet, python has many uses such as on servers and data science.
	
- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you 
  can try to get a missing key (like "c") *without* your programming 
  crashing.
	- dict.get("c", false)
	- if "c" in dict:  
		c_value = dict["c]

- What is a unit test?
	- a test to see if an individual component of an app  	works

- What is an integration test?
	- To see if individual components work together

- What is the role of web application framework, like Flask?	
	- To simplify and help create responses for the request on the front end.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
	- The former would be more of like an existing place somewhere on the website.
	- The latter would be more of when you have selected an option on a page and you are now gathering that selection.

- How do you collect data from a URL placeholder parameter using Flask?
	- request.args["key"]  
- How do you collect data from the query string using Flask?
	- request.args["key"]  
  
- How do you collect data from the body of the request using Flask?
	- request.form["key"]  
	  
- What is a cookie and what kinds of things are they commonly used for?
	- a piece of data that is stored in browser to log information about your interactions with the website 

- What is the session object in Flask?
	- A object where one can set information on the back-end and then store this information on the front end as a cookie.

- What does Flask's `jsonify()` do?
	- creates an object that is nested into your overall response

- What was the hardest part of this past week for you?
  What was the most interesting?
	- Just determining if I should use the solution manual at all when I am doing an exercise, even though I have been stuck for a while on a problem. It's all interesting. Well, testing is kind of boring.
