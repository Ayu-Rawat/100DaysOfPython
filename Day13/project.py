import random

instagram_data = [
    {"name": "Cristiano Ronaldo", "followers": 622, "description": "Footballer, Al Nassr & Portugal.", "country": "Portugal"},
    {"name": "Lionel Messi", "followers": 495, "description": "Footballer, Inter Miami & Argentina.", "country": "Argentina"},
    {"name": "Selena Gomez", "followers": 430, "description": "Singer, actress, and businesswoman.", "country": "USA"},
    {"name": "Kylie Jenner", "followers": 400, "description": "Entrepreneur, media personality.", "country": "USA"},
    {"name": "Dwayne 'The Rock' Johnson", "followers": 395, "description": "Actor and former wrestler.", "country": "USA"},
    {"name": "Ariana Grande", "followers": 380, "description": "Singer and songwriter.", "country": "USA"},
    {"name": "Kim Kardashian", "followers": 365, "description": "Entrepreneur & TV personality.", "country": "USA"},
    {"name": "Beyoncé", "followers": 320, "description": "Singer & businesswoman.", "country": "USA"},
    {"name": "Justin Bieber", "followers": 290, "description": "Singer and songwriter.", "country": "Canada"},
    {"name": "Virat Kohli", "followers": 265, "description": "Cricketer, former India captain.", "country": "India"},
    {"name": "Taylor Swift", "followers": 270, "description": "Singer-songwriter.", "country": "USA"},
    {"name": "Jennifer Lopez", "followers": 252, "description": "Singer, actress, and dancer.", "country": "USA"},
    {"name": "Kendall Jenner", "followers": 290, "description": "Model and media personality.", "country": "USA"},
    {"name": "Neymar Jr", "followers": 210, "description": "Footballer, Al Hilal & Brazil.", "country": "Brazil"},
    {"name": "Nicki Minaj", "followers": 215, "description": "Rapper and singer.", "country": "USA"},
    {"name": "Khloé Kardashian", "followers": 215, "description": "TV personality & entrepreneur.", "country": "USA"},
    {"name": "Miley Cyrus", "followers": 205, "description": "Singer and actress.", "country": "USA"},
    {"name": "Shakira", "followers": 190, "description": "Singer and philanthropist.", "country": "Colombia"},
    {"name": "Kourtney Kardashian", "followers": 190, "description": "Entrepreneur & TV personality.", "country": "USA"},
    {"name": "LeBron James", "followers": 180, "description": "Basketball player, Lakers.", "country": "USA"},
    {"name": "Billie Eilish", "followers": 155, "description": "Singer and songwriter.", "country": "USA"},
    {"name": "Kevin Hart", "followers": 165, "description": "Comedian and actor.", "country": "USA"},
    {"name": "Drake", "followers": 150, "description": "Rapper and songwriter.", "country": "Canada"},
    {"name": "Zendaya", "followers": 160, "description": "Actress and singer.", "country": "USA"},
    {"name": "Gigi Hadid", "followers": 150, "description": "Model and influencer.", "country": "USA"},
    {"name": "Chris Hemsworth", "followers": 125, "description": "Actor, known for Thor.", "country": "Australia"},
    {"name": "Emma Watson", "followers": 130, "description": "Actress & activist.", "country": "UK"},
    {"name": "Huda Kattan", "followers": 115, "description": "Beauty influencer & entrepreneur.", "country": "USA"},
    {"name": "Shawn Mendes", "followers": 105, "description": "Singer-songwriter.", "country": "Canada"},
    {"name": "Vin Diesel", "followers": 100, "description": "Actor, Fast & Furious star.", "country": "USA"},
    {"name": "David Beckham", "followers": 80, "description": "Former footballer.", "country": "UK"},
    {"name": "Robert Downey Jr.", "followers": 90, "description": "Actor, Iron Man.", "country": "USA"},
    {"name": "Will Smith", "followers": 95, "description": "Actor and rapper.", "country": "USA"},
    {"name": "Priyanka Chopra", "followers": 90, "description": "Actress & producer.", "country": "India"},
    {"name": "Dua Lipa", "followers": 95, "description": "Singer and songwriter.", "country": "UK"},
    {"name": "Rihanna", "followers": 160, "description": "Singer & entrepreneur.", "country": "Barbados"},
    {"name": "Cardi B", "followers": 140, "description": "Rapper and songwriter.", "country": "USA"},
    {"name": "Camila Cabello", "followers": 80, "description": "Singer and songwriter.", "country": "Cuba"},
    {"name": "Zayn Malik", "followers": 75, "description": "Singer & former One Direction.", "country": "UK"},
    {"name": "Anushka Sharma", "followers": 65, "description": "Actress & producer.", "country": "India"},
    {"name": "Chris Evans", "followers": 60, "description": "Actor, Captain America.", "country": "USA"},
    {"name": "Tom Holland", "followers": 70, "description": "Actor, Spider-Man.", "country": "UK"},
    {"name": "Gal Gadot", "followers": 85, "description": "Actress, Wonder Woman.", "country": "Israel"},
    {"name": "Shane Dawson", "followers": 50, "description": "YouTuber & filmmaker.", "country": "USA"},
    {"name": "PewDiePie", "followers": 45, "description": "YouTuber & gamer.", "country": "Sweden"},
    {"name": "Liza Koshy", "followers": 40, "description": "Comedian & actress.", "country": "USA"},
    {"name": "MrBeast", "followers": 55, "description": "YouTuber & philanthropist.", "country": "USA"},
    {"name": "James Charles", "followers": 30, "description": "Makeup artist & influencer.", "country": "USA"},
    {"name": "NikkieTutorials", "followers": 25, "description": "Makeup artist & influencer.", "country": "Netherlands"},
    {"name": "David Dobrik", "followers": 40, "description": "YouTuber & vlogger.", "country": "USA"},
    {"name": "Dixie D'Amelio", "followers": 50, "description": "TikTok star & singer.", "country": "USA"},
    {"name": "Charli D'Amelio", "followers": 55, "description": "TikTok star & dancer.", "country": "USA"},
    {"name": "Addison Rae", "followers": 45, "description": "TikTok star & actress.", "country": "USA"},
    {"name": "Sundar Pichai", "followers": 20, "description": "CEO of Google & Alphabet.", "country": "India"},
    {"name": "Mark Zuckerberg", "followers": 15, "description": "Co-founder of Facebook.", "country": "USA"},
    {"name": "Elon Musk", "followers": 30, "description": "CEO of Tesla & SpaceX.", "country": "USA"},
    {"name": "Jeff Bezos", "followers": 10, "description": "Founder of Amazon.", "country": "USA"},
    {"name": "Narendra Modi", "followers": 90, "description": "Prime Minister of India.", "country": "India"}
]

print('''
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ '/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/  
''')

def game_over():
    global game_active
    global game_over_flag
    game_active = False
    game_over_flag = True

def get_next_person():
    global current_person
    global next_person
    global score
    current_person = next_person
    score += 1
    next_person = random.choice(instagram_data)

game_active = True
score = 0
game_over_flag = False

while game_active:
    current_person = random.choice(instagram_data)
    next_person = random.choice(instagram_data)
    while not game_over_flag:
        print(f"Compare A: {current_person['name']}, {current_person['description']}, from {current_person['country']}")
        print('''
         _    __    
        | |  / /____
        | | / / ___/
        | |/ (__  ) 
        |___/____(_)
        ''')
        print(f"Compare B: {next_person['name']}, {next_person['description']}, from {next_person['country']}")
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        if choice == "a":
            if current_person["followers"] >= next_person["followers"]:
                get_next_person()
            else:
                print(f"Wrong guess! You got a score of {score}")
                game_over()
        elif choice == "b":
            if current_person["followers"] <= next_person["followers"]:
                get_next_person()
            else:
                print(f"Wrong guess! You got a score of {score}")
                game_over()
        else:
            print(f"Invalid input! You got a score of {score}")
            game_over()


