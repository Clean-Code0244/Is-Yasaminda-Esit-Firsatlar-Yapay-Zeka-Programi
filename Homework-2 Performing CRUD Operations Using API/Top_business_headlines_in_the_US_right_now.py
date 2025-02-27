from requests import get
from pprint import pprint
from uuid import uuid4

endpoint = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=ea138aa89bb64498977010fc9039e36d'
response = get(url=endpoint)
data = response.json() # Now data in dictionary format
#pprint(data)

def create_data(source_name: str, author: str, title: str, description: str, publishedAt: str, content: str) -> dict:
    new_article = {
        "source": {"name": source_name, "id": str(uuid4())},
        "author": author,
        "title": title,
        "description": description,
        "publishedAt": publishedAt,
        "url": "https://apnews.com/article/stocks-markets-rates-tariffs-nvidia-79a76b267cd9565896d798e7bc6e82dd",
        "urlToImage": "https://apnews.com/article/stocks-markets-rates-tariffs-nvidia-79a76b267cd9565896d798e7bc6e82dd",
        "content": content
    }
    

    data["articles"].append(new_article)


    return data

def update_data(author: str) -> dict:
    for article in data.get("articles", []):
        if article.get("author") == author:
            print("You will now update the article by the author of your choice !!!")
            source_name = input("Please enter source name  to update: ")
            title = input("Please enter the title  to update: ")
            description = input("Please enter the Description  to update: ") 
            publishedAt = input("Please enter the date  to update: ")
            content = input("Please enter content  to update: ")

            article["title"] = title
            article["description"] = description
            article["publishedAt"] = publishedAt
            article["content"] = content
            article["source"]["name"] = source_name

    return data

def delete_data(author: str) -> dict:
    
    updated_articles = []
    for article in data["articles"]:
        if article.get("author") != author:
            updated_articles.append(article)  
    data["articles"] = updated_articles  
    
    return data

def read_data(author: str) -> str:
    output = ""
    if "articles" in data:
        for article in data["articles"]:
            if article.get("author") == author:
                output += f"Source: {article.get('source', {}).get('name', 'Unknown')}\n"
                output += f"Title: {article.get('title', 'N/A')}\n"
                output += f"Description: {article.get('description', 'N/A')}\n"
                output += f"Published At: {article.get('publishedAt', 'N/A')}\n"
                output += f"Content: {article.get('content', 'N/A')}\n"
                output += "-" * 40 + "\n"
        if output == "":
            output = f"No articles found for author: {author}"
    else:
        output = "No articles data available."
    return output

def read_all_data(data:dict) -> str:
    result = ""
    if "articles" in data and data["articles"]:
        for article in data["articles"]:
            result += (
                f"Title: {article.get('title', 'N/A')}\n"
                f"Author: {article.get('author', 'N/A')}\n"
                f"Source: {article.get('source', {}).get('name', 'N/A')}\n"
                f"Description: {article.get('description', 'N/A')}\n"
                f"Published At: {article.get('publishedAt', 'N/A')}\n"
                f"URL: {article.get('url', 'N/A')}\n"
                f"Content: {article.get('content', 'N/A')}\n"
                f"{'-' * 50}\n"
            )
    else:
        result = "No articles available."

    return result


while True:
    print("Press 0 for exiting the while loop ")
    process = input('Type a process name: ')

    match process:
        case 'create':
            create_data(source_name= input("Please enter source_name :"), author= input("Please enter Author name :"),title = input("Please enter the title :"),description= input("Please enter the Description :") ,publishedAt = input("Please enter the date :"),content = input("Please enter content :"))
            print("Please enter the 'list' keyword to see the content of the data that I extracted from API")
            
        case 'list':
            print(read_all_data(data))
        case 'update':
            author = input("Please enter the Author that you want to update : ")
            
            update_data(author=author)
            print("Please enter the 'list' keyword to see the content of the data that I extracted from API")
            
        case 'delete':
             author = input("Please enter the Author that you want to delete : ")
            
             delete_data(author=author)
        case 'read':
            author = input("Please write the name of the author whose article you would like to see : ")
            print(read_data(author=author))
            
        case "_":
            print('Please type a vaid process..!')

        case "0":
            print('Have a nice day :) ')
            break;

