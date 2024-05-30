#!/usr/bin/python3

import requests
import csv


def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        post = response.json()
        print(f"Status code: {response.status_code}")
    
        for title in post:
            print(title['title'])

def fetch_and_save_posts():
     
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        posts = response.json()
        data = [{'id': post['id'], 'title': post['title'],
                 'body': post['body']} for post in posts]

        with open('posts.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(data)