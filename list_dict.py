#user index
user_db = {
    'sandcastle':{'name':'ALAN M JOSE',
                  'age':50,
                  "role":'AUTHOR'
                  },
    'spiderman':{'name':'PETER PARKER',
                  'age':45,
                  "role":'RESEARCH SCIENTIST'
                  },
    'sophi54':{'name':'SOPHIA TESLA',
                  'age':39,
                  "role":'AI ARCHITECT'
                  },
    'tr4acy':{'name':'TRACY SERAPH',
                  'age':40,
                  "role":'DOCTER'
                  },
    'ANUCREM34@':{'name':'KINGLIA',
                  'age':31,
                  "role":'TEACHER'
                  }
}
#SOCIAL GRAPH 
social_graph = {
    'sandcastle':{ 'followers':{'spiderman',"sophi54","tr4acy"},
                  'following':{'sophi54','tr4acy','spiderman'}
                  },
    'spiderman':{
                 'followers':{'sandcastle',"sophi54","tr4acy"},
                'following':{'sophi54','assmika','sandcastle','tr4acy'}
                  },
    'sophi54':{'followers':{'sandcastle','spiderman','tr4acy'},
                'following':{'sandcastle','spiderman','asmika34@'}
                  },
    'tr4acy':{'followers':{'sandcastle','spiderman',},
                'following':{'sandcastle','spiderman','sophi54'}
                  },
    'asmika34@':{'followers':{'sophi54','spierman'},
                'following':{}
                  }
}
print(user_db['sandcastle']['name'])