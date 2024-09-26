Questions = [
	{	"prompt" : "What is my name?",
 		"Options" : ["A. Darshan","B. Ayush","C. Chaitanya","D. Divyansh"],
		"Answer" : "A"	
	},
	{	"prompt" : "What am i Studying?",
 		"Options" : ["A. B-Tech AIML","B. B-Tech C&IT","C. B-Tech CSSE","D. CSE"],
		"Answer" : "A"	
	},
	{	"prompt" : "Where do i live?",
 		"Options" : ["A. Dharwad","B. Banglore","C. Davangere","D. Pune"],
		"Answer" : "C"	
	},
	{	"prompt" : "What is my favorite food?",
 		"Options" : ["A. Pani Pori","B. Dosa","C. Vada Pav","D. Sev puri"],
		"Answer" : "B"	
	},
	{	"prompt" : "What phone do i use?",
 		"Options" : ["A. I phone","B. Oneplus","C. MI","D. Real me"],
		"Answer" : "B"	
	}
]

def QA(Questions):
  score = 0
  for  Question in Questions:
    print(Question["prompt"])
    for opi in Question["Options"]:
      print(opi)
    ans = input("Enter your answer: ")

QA(Questions)