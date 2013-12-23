solutions = [
	{	"name"	:	"sub2",
		"url"	:	"https://github.com/StefanTischler/gerrit_sub2.git"
	},
]

hooks = [
	{	"pattern"	:	"*",
		"action"	:	["git", "checkout", "master", "HEAD"]
	},
]