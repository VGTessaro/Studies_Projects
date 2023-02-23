in_english = input("What do you want to say in 'Piratian'? ")

piratian = {
	"sir":"matey", 
	"hotel":"fleabag inn",
	"student":"swabbie",
	"boy":"matey",
	"madam":"proud beauty",
	"professor":"foul blaggart",
	"restaurant":"galley",
	"your":"yer",
	"excuse":"arr",
	"students":"swabbies",
	"are":"be",
	"lawyer":"foul blaggart",
	"the":"th’",
	"restroom":"head",
	"my":"me",
	"hello":"avast",
	"is":"be",
	"man":"matey"
	}
textin = in_english.split()
textout = []
for word in textin:
    if word in piratian:
        textout.append(piratian[word])
    else:
        textout.append(word)
        
complete_txt = " ".join(textout)

print(complete_txt)