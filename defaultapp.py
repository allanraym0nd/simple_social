# text_posts = {
#     1: {"title": "New Post", "content": "cool text post"},
#     2: {"title": "Morning Thoughts", "content": "Starting the day with some code ☕"},
#     3: {"title": "Debugging Life", "content": "Why does fixing one bug create three more?"},
#     4: {"title": "Late Night Coding", "content": "2am and still pushing commits 🚀"},
#     5: {"title": "Learning FastAPI", "content": "Building APIs is actually fun"},
#     6: {"title": "Coffee Break", "content": "Time for a quick recharge ☕"},
#     7: {"title": "Dev Struggles", "content": "It worked yesterday, why not today?"},
#     8: {"title": "Small Wins", "content": "Finally fixed that annoying bug 🎉"},
#     9: {"title": "Clean Code", "content": "Refactoring feels so satisfying"},
#     10: {"title": "Weekend Vibes", "content": "Coding and chilling 😎"}
# }


# @app.get("/posts")
# def get_all_posts(limit: int = None):
#     if limit:
#         # converts the dictionary to a list to provide slicing":limit"
#         return list(text_posts.values())[:limit]
#     return text_posts


# @app.get("/posts/{id}")
# def get_post(id: int) -> PostCreate:
#     if id not in text_posts:
#         raise HTTPException(status_code=404, detail="Post Not Found")

#     return text_posts.get(id)


# @app.post("/posts")
# def create_post(post: PostCreate) -> PostCreate:
#     new_post = {"title": post.title, "content": post.content}
#     text_posts[max(text_posts.keys()) + 1] = new_post

#     return new_post
