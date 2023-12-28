import argparse
import requests
import json

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_posts():
    url = f"{BASE_URL}/posts"
    response = requests.get(url)
    print_response(response)

def get_post(post_id):
    url = f"{BASE_URL}/posts/{post_id}"
    response = requests.get(url)
    print_response(response)

def create_post(title, body, user_id):
    url = f"{BASE_URL}/posts"
    data = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    headers = {"Content-type": "application/json; charset=UTF-8"}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    print_response(response)

def print_response(response):
    print(f"Status Code: {response.status_code}")
    if response.text:
        print("Response:")
        print(json.dumps(response.json(), indent=2))
    else:
        print("No content in the response.")

def main():
    parser = argparse.ArgumentParser(description="Simple command-line REST client for JSONPlaceholder.")
    parser.add_argument("action", choices=["get_posts", "get_post", "create_post"], help="Action to perform")
    parser.add_argument("--post_id", type=int, help="Post ID for 'get_post' action")
    parser.add_argument("--title", help="Title for 'create_post' action")
    parser.add_argument("--body", help="Body for 'create_post' action")
    parser.add_argument("--user_id", type=int, help="User ID for 'create_post' action")

    args = parser.parse_args()

    if args.action == "get_posts":
        get_posts()
    elif args.action == "get_post":
        if not args.post_id:
            print("Error: --post_id is required for 'get_post' action.")
        else:
            get_post(args.post_id)
    elif args.action == "create_post":
        if not all([args.title, args.body, args.user_id]):
            print("Error: --title, --body, and --user_id are required for 'create_post' action.")
        else:
            create_post(args.title, args.body, args.user_id)

if __name__ == "__main__":
    main()