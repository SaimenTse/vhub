import web

render = web.template.render('templates/')

urls = (
    '/', 'index'
)

email_file = open('mbox-short.txt')

plain_text = email_file.read()

class index:
    def GET(self):
        i = plain_text
        return render.index(i)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
