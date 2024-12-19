from typing import List, Dict, Optional

class Book:
    books = []
    next_id = 1

    @classmethod
    def add_book(cls, title, author):
        book = {"id": cls.next_id, "title": title, "author": author}
        cls.books.append(book)
        cls.next_id += 1
        return book

    @classmethod
    def get_book(cls, book_id):
        return next((book for book in cls.books if book["id"] == book_id), None)

    @classmethod
    def update_book(cls, book_id, title, author):
        book = cls.get_book(book_id)
        if book:
            book["title"] = title
            book["author"] = author
        return book

    @classmethod
    def delete_book(cls, book_id):
        book = cls.get_book(book_id)
        if book:
            cls.books.remove(book)
        return book


class Member:
    members = []
    next_id = 1

    @classmethod
    def add_member(cls, name):
        member = {"id": cls.next_id, "name": name}
        cls.members.append(member)
        cls.next_id += 1
        return member

    @classmethod
    def get_all_members(cls):
        return cls.members
