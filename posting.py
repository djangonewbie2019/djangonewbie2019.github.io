#!/usr/bin/env python3
from slugify import slugify
import sys
import time

layout = "post"

now = time.localtime()

if len(sys.argv) > 1:
    title = " ".join(sys.argv[1:])
else:
    title = "Title"

slug = slugify(title)

filename = "%s-%s.md" % (time.strftime("%Y-%m-%d", now), slug)

with open("_posts/%s" % filename, "w", encoding="utf-8") as f:
    f.write("---\n")
    f.write("layout: %s\n" % layout)
    f.write("date: %s\n" % time.strftime("%Y-%m-%d %H:%M:%S %z", now))
    f.write("title: %s\n" % title)
    f.write("slug: %s\n" % slug)
    f.write("categories: \n")
    f.write("tags: \n")
    f.write("---\n")

