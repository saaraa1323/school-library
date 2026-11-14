
from flask import Flask, render_template, send_from_directory, abort
import os

app = Flask(__name__)

FILES_FOLDER = os.path.join("static", "files")

categories = {
    "podcasts": {
        "title": "پادکست‌ها",
        "icon": "🎧",
        "description": "شنیدنی‌هایی برای یادگیری و تجربه‌های تازه",
        "folder": "podcasts",
        "files": [
            {"name": "podcast1.mp4", "title": "پادکست شماره یک"},
            {"name": "podcast2.mp4", "title": "پادکست شماره دو"},
            {"name": "podcast3.mp4", "title": "پادکست شماره سه"},
            {"name": "podcast4.mp4", "title": "پادکست شماره چهار"},
            {"name": "podcast5.mp4", "title": "پادکست شماره پنج"}
        ]
    },

    "videos": {
        "title": "ویدیوهای آموزشی",
        "icon": "🎬",
        "description": "تماشای آموزش‌ها و مطالب جذاب",
        "folder": "videos",
        "files": [
            {"name": "video1.mp4", "title": "ویدیوی آموزشی اول"},
            {"name": "video2.mp4", "title": "ویدیوی آموزشی دوم"},
            {"name": "video3.mp4", "title": "ویدیوی آموزشی سوم"}
        ]
    },

    "presentations": {
        "title": "پاورپوینت‌ها",
        "icon": "📊",
        "description": "ارائه‌های دیدنی و مطالب آموزشی",
        "folder": "presentations",
        "files": [
            {"name": "presentation1.pdf", "title": "ارائه شماره یک"},
            {"name": "presentation2.pdf", "title": "ارائه شماره دو"}
        ]
    },

    "books": {
    "title": "کتاب‌های دیجیتال",
    "icon": "📚",
    "description": "گشتی در دنیای کتاب‌ها و داستان‌ها",
    "folder": "books",
    "files": [
        {"name": "book1.pdf", "title": "کتاب شماره یک"},
        {"name": "book2.pdf", "title": "کتاب شماره دو"},
        {"name": "audio1.mp3", "title": "کتاب صوتی شماره یک"},
        {"name": "audio2.mp3", "title": "کتاب صوتی شماره دو"}
    ]
},

    "comics": {
        "title": "کمیک‌ها",
        "icon": "📖",
        "description": "داستان‌هایی جذاب در قالب تصویر",
        "folder": "comics",
        "files": [
            {"name": "comic1.pdf", "title": "کمیک شماره یک"},
            {"name": "comic2.pdf", "title": "کمیک شماره دو"}
        ]
    }
}


@app.route("/")
def home():
    return render_template("index.html", categories=categories)


@app.route("/category/<category_id>")
def show_category(category_id):

    if category_id not in categories:
        abort(404)

    category = categories[category_id]

    available_files = []

    for item in category["files"]:
        path = os.path.join(
            FILES_FOLDER,
            category["folder"],
            item["name"]
        )

        if os.path.isfile(path):
            available_files.append(item)

    return render_template(
        "category.html",
        category=category,
        category_id=category_id,
        files=available_files
    )


@app.route("/file/<category_id>/<filename>")
def open_file(category_id, filename):

    if category_id not in categories:
        abort(404)

    category = categories[category_id]

    # فقط فایل‌هایی که در فهرست مجاز تعریف شده‌اند
    allowed_files = [
        item["name"] for item in category["files"]
    ]

    if filename not in allowed_files:
        abort(404)

    return send_from_directory(
        os.path.join(FILES_FOLDER, category["folder"]),
        filename
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
