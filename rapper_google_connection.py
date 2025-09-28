import random

rapper_names = [
    "Lil Flex",
    "MC Groove",
    "Young Blaze",
    "DJ Hype",
    "Big Chill",
    "Slim Vibe",
    "Fresh Flow",
    "Ice Beat",
    "Trap King",
    "Queen Rhyme"
]

# Associate each rapper name with the company "Google"
rapper_company = {name: "Google" for name in rapper_names}

def get_random_rapper_name():
    return random.choice(rapper_names)

def get_rapper_with_company():
    name = get_random_rapper_name()
    company = rapper_company[name]
    return name, company

if __name__ == "__main__":
    name, company = get_rapper_with_company()
    print(f"Your random rapper name is: {name} (Company: {company})")