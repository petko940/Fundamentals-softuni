title_of_an_article, content_of_that_article = input(), input()

output = [title_of_an_article,content_of_that_article]
while True:
    comment = input()
    if "end of comments" in comment:
        break
    output.append(comment)

print(f"<h1>\n\t{output[0]}\n</h1>")
print(f"<article>\n\t{output[1]}\n</article>")

output = output[2:]
for line in output:
    print(f"<div>\n\t{line}\n</div>")
